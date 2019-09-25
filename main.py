import pytube
try:
    link = input('Enter the video link here-->')
    link=link.strip()
    yt = pytube.YouTube(link)
except:
    print("The link you have provided is not correct.")
    exit()

lis = []
stream = stream = yt.streams.filter(adaptive=True).filter(file_extension='mp4').all()

for i in stream:
    lis.append(i.resolution)
print("Available resolution")
print('Select one from here', lis, '\n')
x = input("Enter your selected Resoution").strip()

for j in lis:
    if x in j:
        # print("Resolution is available")
        break
else:
    print("Sorry,selected resolution is not available")
    exit()

confirm = input("Do you want to download this video?Y/N")
try:
    path = input('Enter the path where you want to save this file')
    path = path.strip()

    if confirm == 'Y' or confirm == 'y':

        print("Video is downloading,Please wait\n")
        if x == '144p' or x == '144':
            stream = yt.streams.get_by_itag(160)
            stream.download(path)
        elif x == '240p' or x == '240':
            stream = yt.streams.get_by_itag(133)
            stream.download(path)
        elif x == '360p' or x == '360':
            stream = yt.streams.get_by_itag(18)
            stream.download(path)
        elif x == '480p' or x == '480':
            stream = yt.streams.get_by_itag(135)
            stream.download(path)
        elif x == '720p' or x == '720':
            stream = yt.streams.get_by_itag(22)
            stream.download(path)
        elif x == '1080p' or x == '1080':
            stream = yt.streams.get_by_itag(137)
            stream.download(path)
        else:
            print("Resolution not found")

    else:
        exit()
    print("Video Downloaded successfully")

except:
    print("The path you have provided seems not correct")