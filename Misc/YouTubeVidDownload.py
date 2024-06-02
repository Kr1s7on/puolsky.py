# pip install pytube
import pytube

link = input("Enter the link of the YouTube video you want to download: ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Downloaded successfully!")
