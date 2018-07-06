from pytube import YouTube
from pprint import pprint

def run(url):
    yt =YouTube(url)
    print(yt.title)
    a = input('Do you want to download the video or audio? (V/A) ')
    if a == 'V' or a == 'v' :
        pprint(yt.streams.all())
        pprint('Enter itag to download video')
        itag = int(input())
        stream = yt.streams.get_by_itag(itag)
        print('wait..downloading...')
        stream.download()
        pprint('Video downloaded. ')
    elif a == 'A' or a == 'a' :
        pprint(yt.streams.filter(only_audio=True).all())
        pprint('Enter itag to download audio')
        itag = int(input())
        stream = yt.streams.get_by_itag(itag)
        print('wait..downloading...')
        stream.download()
        print('Audio downloaded.')
    else:
        pprint('Invalid input')
        quit()


def do_youtube():
    url = input('Paste url and press enter to download video : \n')
    str(url)
    run(url)