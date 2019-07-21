# DoDucMinh-Python-C-T
print("Welcomo to MP3")
#Version1
print("Pick one of a options: ")
chon = ['Show ALL songs','Show detail of a song','Play a song','Search and download songs','Exit']
for i in range(len(chon)):
    print(i + 1,". ",chon[i])
n = int(input(">>>"))
#IF
while True:
    o = True
    if n == 1 or 2 or 3:
        print("Empty")
    if n == 5:
        thoat = ['Co', 'Khong']
        print("Are you sure?")
        for i in range(len(thoat)):
            print(i + 1,". ",thoat[i])
        a = input(">>>")
        if a == 1:
            print("Ok")
            o == True
            break
        if a == 2:
            print("Lol, just kidding, BYE!")
            o == False
            break
    if n == 4:
        m = input("Enter the URL of song that you want to search: ")
        from youtube_dl import YoutubeDL
        options = {}
        ydl = YoutubeDL(options)
        info = ydl.extract_info(m)
        import json
        with open('info.json', 'w',encoding="utf8") as json_file:
           json.dump(info, json_file)
    print(*extract.info)
