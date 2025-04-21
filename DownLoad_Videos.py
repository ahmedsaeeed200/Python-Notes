import yt_dlp

def download_mp3(url):
    """
    Download the audio from a YouTube video and save it as an MP3 file.
    
    Parameters:
        url (str): The YouTube URL provided by the user.
    """
    # Options for yt-dlp to extract audio and convert to MP3
    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',      # Convert to MP3 format
            'preferredquality': '192',    # Set audio quality (192 kbps)
        }],
        'outtmpl': '%(title)s.%(ext)s',   # Save file as "[video title].mp3"
    }
    
    # Download the audio using the specified options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Prompt the user to enter the YouTube URL
    url = input("Enter YouTube URL: ")
    print("Downloading audio from:", url)
    download_mp3(url)
    print("Download complete!")