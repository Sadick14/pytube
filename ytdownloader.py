from pytube import YouTube
from pytube.exceptions import PytubeError

video_url = input("Enter video url: ")

try:
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print(f'Downloaded: {yt.title}')
except PytubeError as e:
    print(f'An error occurred: {e}')
