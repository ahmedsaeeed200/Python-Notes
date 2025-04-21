import numpy as np
import matplotlib.pyplot as plt
########### ---- Line Shapes ----###########

# '-'	Solid line
# ':'	Dotted line
# '--'	Dashed line
# '-.'	Dashed/dotted line


########### ---- Color Reference ----###########
# Color Syntax	Description
#   'r'	            Red
#   'g'	            Green
#   'b'	            Blue
#   'c'	            Cyan
#   'm'           	Magenta
#   'y'	            Yellow
#   'k'	            Black
#   'w'           	White

# -----------------------------> Example: <-----------------------------
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 'o:r',ms=20, mec='b', mfc='g')   #[ms: Marker Size | mec: border Color | mfc= Marker Face Color]

# plt.show()


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#

########### ---- Line Styles ----###########


# You can choose any of these styles:

# 'solid' (default)	'-'
# 'dotted'	':'
# 'dashed'	'--'
# 'dashdot'	'-.'
# 'None'	'' or ' '


# -----------------------------> Example: <-----------------------------

# import matplotlib.pyplot as plt
# import numpy as np


# x = np.array([0, 5, 6, 9, 8, 12])

"""plt.figure(figsize=(10, 5))"""  # To Adjust Figure Size

# plt.plot(x, ls='dotted', c='#8A2BE2', lw='1')  # [ls: 'Line Style' | c:'Color' | lw: 'lw']


# plt.legend()
# plt.show()

# ---->Note<----
"""To Draw Multiple Line On The Same Canvas, We Have Two Options"""

"""First_One"""  # You can plot as many lines as you like by simply adding more plt.plot() functions:

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

"""Second_One"""  # Draw two lines by specifiyng the x- and y-point values for both lines:

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#

########### ---- Labels and Title ----###########

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'blue','size':20}               # To Add Format To The Titles | Labels
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y, label = 'title of the element')
# plt.show()


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#

########### ----  Grid Lines ----###########

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# plt.show()

"""To Darw Grid For One Axis  ===>"""  # plt.grid(axis = 'x') | plt.grid(axis = 'y')


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#

########### ----  Display Multiple Plots ----###########

"""
suptitle() : Title For The Entire Page
title(): Title For Each Plot
"""

""" The "subplot()" function takes three arguments that describes the layout of the figure:"""

# 1) The layout is organized in rows and columns, which are represented by the first and second argument.

# 2) The third argument represents the index of the current plot.

# ---> Example <---

"""plt.subplot(1, 2, 1)"""
# the figure has 1 row, 2 columns, and this plot is the first plot.

"""plt.subplot(1, 2, 2)"""
# the figure has 1 row, 2 columns, and this plot is the second plot.


# ---> Example 1 <---
"""Draw 2 plots:"""
# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)

# plt.show()

# ---> Example 2 <---
"""Draw 2 plots on top of each other:"""
# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 1, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 1, 2)
# plt.plot(x,y)

# ---> Example 3 <---
"""
You can draw as many plots you like on one figure, just descibe the number of rows, columns, 
and the index of the plot.
"""
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show()


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#

########### ---- Scatter Plots ----###########

"""scatter()"""

# alpha: adjust the transparency of the dots

# ---> Example 1 <---

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#

########### ---- Bar Plots ----###########

# ---> Example 1 <---

# import matplotlib.pyplot as plt

# # Sample data
# categories = ['A', 'B', 'C']
# values = [10, 20, 15]
# colors = ['red', 'green', 'blue']

# # Plot 3 bars with different colors and labels
# plt.bar(categories, values, color=colors, label=categories, width = 0.1)

# plt.barh() : For Horizontal Bars

# # Add labels and title
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Graph with 3 Bars')

# # Add a legend
# plt.legend(title="Elements", loc='upper right')

# # Show the plot
# plt.show()


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#

########### ---- Histogram Plots ----###########

# import matplotlib.pyplot as plt
# import numpy as np

# # Simulate sensor data (e.g., temperature readings)
# np.random.seed(42)
# temperature_data = np.random.normal(150, 10, 1000)  # Normal distribution with mean=150, std=10

# # Create the histogram
# plt.hist(temperature_data, bins=20, color='orange', edgecolor='black', alpha=0.7)

# # Add labels and title
# plt.xlabel('Temperature (°C)')
# plt.ylabel('Frequency')
# plt.title('Temperature Distribution in Industrial Process')

# # Add vertical lines for control limits
# plt.axvline(np.mean(temperature_data), color='red', linestyle='dashed', linewidth=2, label=f"Mean: {np.mean(energy_consumption):.2f} kWh")
# plt.axvline(170, color='red', linestyle='--', label='Upper Control Limit')

# # Add a legend
# plt.legend()

# # Show the plot
# plt.show()


# ----------#----------#----------#----------#----------#----------#----------#----------#----------#


########### ---- Pie Charts ----###########

# ---- autopct="%1.1f%%" : To Add The Percent For Each Slice

# import matplotlib.pyplot as plt
# import numpy as np

# # Data
# y = np.array([35, 25, 25, 15]) # Each Item Means One Slice
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# colors = ["red", "yellow", "pink", "brown"]  # Custom colors
# explode = [0.05, 0, 0, 0.1]  # Slightly separate some slices

# # Create Pie Chart
# plt.figure(figsize=(7, 7))
# plt.pie(y, labels=mylabels, autopct="%1.1f%%", colors=colors, startangle=140,
#         explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})

# # Add legend
# plt.legend(title="Fruit Distribution", loc="best")

# # Display the chart
# plt.show()
