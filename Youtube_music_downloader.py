from pytube import YouTube
from moviepy.editor import *

print("Welcome to Xeltyck's YouTube downloader. \n\nEvery option downloads in the highest Audio/Video available resolution (720p 30fps max output).\n")
while True:
    print("Options:\n\n1.Download Audio (mp3)\n2.Download Video (mp4)\n3.Exit\n")
    option = str(input("Enter your option: \n"))
    
    if option == "1":
        #Download stage
        yt = YouTube(str(input("Enter the link: \n")))
        print(f"Title: {yt.title}\n ")
        stream = yt.streams.get_audio_only() #Selects audio on its maximum available resolution (.mp4 format)
        stream.download(filename=yt.title+".mp4") #If not set, there could be some filename errors when converting the file to mp3.
        song = yt.title + ".mp4"
        
        #Conversion stage: 
        clip = AudioFileClip(song)# Selects the audio file
        clip.write_audiofile(yt.title+".mp3")
        clip.close()
        
        #Elimination of the original video file:
        os.remove(yt.title+".mp4")
    
    elif option == "2":
        #Download stage
        yt = YouTube(str(input("Enter the link: \n")))
        print(f"Title: {yt.title}\n ")
        stream = yt.streams.get_highest_resolution() #Selects video on its maximum available resolution (.mp4 format)
        stream.download()
    
    elif option == "3":
        break

    else:
        print("Not a valid option, try again.")
    
