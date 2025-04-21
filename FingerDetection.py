
import cv2
import mediapipe as mp
from opcua import Client, ua
import logging
import time

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# OPC-UA Configuration
PLC_ENDPOINT = "opc.tcp://192.168.0.1:4840"  # Replace with your PLC's IP and port
LAMP_NODES = {
    1: 'ns=3;s="OPC-UA_Tags"."LAMP_1"',
    2: 'ns=3;s="OPC-UA_Tags"."LAMP_2"',
    3: 'ns=3;s="OPC-UA_Tags"."LAMP_3"',
    4: 'ns=3;s="OPC-UA_Tags"."LAMP_4"',
    5: 'ns=3;s="OPC-UA_Tags"."LAMP_5"'
}



# MediaPipe Hand Tracking Setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

class PLCController:
    def __init__(self):
        self.client = Client(PLC_ENDPOINT)
        # Remove security for debugging; add back if needed
        # self.client.set_security_string("Basic256Sha256,SignAndEncrypt")
        self.lamp_nodes = {}
        
    def connect(self):
        try:
            self.client.connect()
            logging.info("Connected to PLC successfully")
            for lamp_id, node_id in LAMP_NODES.items():
                self.lamp_nodes[lamp_id] = self.client.get_node(node_id)
            return True
        except Exception as e:
            logging.error(f"PLC connection failed: {e}")
            return False

    def control_lamp(self, lamp_id, state):
        if lamp_id not in self.lamp_nodes:
            logging.warning(f"Invalid lamp_id: {lamp_id}")
            return False
        try:
            variant = ua.Variant(state, ua.VariantType.Boolean)
            dv = ua.DataValue(variant)
            self.lamp_nodes[lamp_id].set_value(dv)
            logging.info(f"Wrote {state} to Lamp {lamp_id}")
            return True
        except Exception as e:
            logging.error(f"Failed to write to Lamp {lamp_id}: {e}")
            return False

    def read_lamp_state(self, lamp_id):
        if lamp_id not in self.lamp_nodes:
            logging.warning(f"Invalid lamp_id for reading: {lamp_id}")
            return None
        try:
            value = self.lamp_nodes[lamp_id].get_value()
            return value
        except Exception as e:
            logging.error(f"Failed to read Lamp {lamp_id}: {e}")
            return None

class GestureController:
    def __init__(self):
        self.hands = mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.prev_fingers = [False] * 5

    def detect_gesture(self, image):
        results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        fingers = [False] * 5
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            self.draw_landmarks(image, hand_landmarks)
            fingers = self.check_fingers(hand_landmarks)
        return fingers

    def check_fingers(self, landmarks):
        fingers = []
        # Thumb
        thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
        fingers.append(thumb_tip.x < thumb_ip.x)
        # Other fingers
        for tip, pip in [(mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.INDEX_FINGER_PIP),
                         (mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP),
                         (mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_PIP),
                         (mp_hands.HandLandmark.PINKY_TIP, mp_hands.HandLandmark.PINKY_PIP)]:
            tip_landmark = landmarks.landmark[tip]
            pip_landmark = landmarks.landmark[pip]
            fingers.append(tip_landmark.y < pip_landmark.y)
        return fingers

    def draw_landmarks(self, image, landmarks):
        mp_drawing.draw_landmarks(
            image,
            landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0,0,255), thickness=2)
        )

def main():
    plc = PLCController()
    if not plc.connect():
        logging.error("Exiting due to PLC connection failure")
        return

    gesture = GestureController()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logging.error("Failed to open camera")
        return

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            logging.warning("Failed to read frame from camera")
            continue

        image = cv2.flip(image, 1)
        current_fingers = gesture.detect_gesture(image)

        # Check for state changes and control lamps
        state_changed = False
        for i, finger_state in enumerate(current_fingers):
            if finger_state != gesture.prev_fingers[i]:
                state_changed = True
                break

        if state_changed:
            logging.info("State change detected, processing updates")
            for i, finger_state in enumerate(current_fingers, 1):
                if finger_state != gesture.prev_fingers[i-1]:
                    if plc.control_lamp(i, finger_state):
                        logging.info(f"Controlled Lamp {i} to {finger_state}")
                    gesture.prev_fingers[i-1] = finger_state

        # Read and display actual lamp states from PLC
        lamp_statuses = []
        for lamp_id in range(1, 6):
            state = plc.read_lamp_state(lamp_id)
            if state is not None:
                lamp_statuses.append(state)
            else:
                lamp_statuses.append(False)  # Default to OFF if read fails

        # Update display with actual PLC states
        status = [f"LAMP {i+1}: {'ON' if state else 'OFF'}" 
                 for i, state in enumerate(lamp_statuses)]
        y_pos = 30
        image_with_text = image.copy()
        for text in status:
            cv2.putText(image_with_text, text, (10, y_pos), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            y_pos += 30

        cv2.imshow('Gesture Control', image_with_text)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
            break

        # Small delay to reduce CPU usage
        time.sleep(0.01)

    cap.release()
    cv2.destroyAllWindows()
    plc.client.disconnect()
    logging.info("Disconnected from PLC")

if __name__ == "__main__":
    main()