print("Welcomo to MP3")

#Version1
print("Pick one of a options: ")
choice = ['Show ALL songs[]','Show detail of a song','Play a song','Search and download songs','Exit']

for i in range(len(choice)):
    print(i + 1,". ",choice[i])
n = int(input(">>>"))
#IF vo dung
if n == 1:
    songlist = []
if n == 2:
    print("Empty")
if n == 3:
    print("Empty")

#If chinh
while True:
    o = True
    if n == 5:
        thoat = ['Co', 'Khong']
        print("Are you sure?")
        for i in range(len(thoat)):
            print(i + 1,". ",thoat[i])
        a = input(">>>")
        if a == 1:
            print("Ok")
            break
        if a == 2:
            print("Lol, just kidding, BYE!")
    if n == 4:
        m = input("Enter the song that you want to search: ")
        print("Searching...")
        #Search

        from youtube_dl import YoutubeDL
        options = {
            'default_search': 'ytsearch3',
            'quiet': True,
        }

#Gap van de
        ydl = YoutubeDL(options)
        search_result = ydl.extract_info(m, download=False)
        import json
        with open('search.json', 'w',encoding="utf8") as json_file:
            json.dump(search_result, json_file)
            videos = search_result["entries"]

        for i,video in enumerate(videos):
            print(f"{i+1}. Tên: {video['title']}, Id của Video: {video['id']}, upload bởi: {video['uploader']}")

        print("Nhap bai hat ban muon tai: ")
        x = int(input(">>>"))
        print(videos[x-1]['webpage_url'])

        options = {
        'outtmpl': '%(id)s', # lấy tên file down về là id của video, lấy id làm tên file để tiện quản lí
        'postprocessors': [{
        'key': 'FFmpegExtractAudio', # Tách lấy audio
        'preferredcodec': 'mp3', # Format ưu tiên là mp3
        'preferredquality': '192', # Chất lượng bitrate
        }]}

        ydl = YoutubeDL(options)
        ydl.download([videos[x-1]['webpage_url']]) 

import json
with open('nhac.json',"r+",encoding="utf8") as json_file:  
    data = json.load(json_file)
    nhac = {'id' : video[x-1], "title" : [videos[x-1]['webpage_url']]}
    data.append(nhac)
    print(data)
    json_file.seek(0)
    json.dump(data, json_file)

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
mixer.init()
mixer.music.load(videos[x-1]["id"]+".mp3")
mixer.music.play()

while True:
    input("Press any key to stop")
    break
