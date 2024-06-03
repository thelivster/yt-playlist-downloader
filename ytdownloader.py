from pytube import YouTube, Playlist
from sys import argv #argv[n] takes the nth argument given by user in cli
from pick import pick

link = input('Insert the url of your playlist : ')



title = 'What do you want to do with this playlist?'

options = ['Download Playlist', 'Scrape URLs', 'Collect Titles', 'Collect Titles + Views']

option, index = pick(options, title, indicator='=>', default_index=0)

path='C:/Users/yourusername/Desktop/'

p = Playlist(link)

for video in p.videos:
    print(video.watch_url)

if index == 0 :
    for video in p.videos:
        print(f'Downloading : {video.title}, with {video.views} views.')
        video.streams.first().download(path)
elif option == 'collect URL':
    for url in p.videos:
        print(url.watch_url)
elif index == 2:
    for title in p.videos:
        print(title.title)
else:
    for title in p.videos:
        print(title.title+' with '+str(title.views)+' views.')


