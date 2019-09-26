import pytube
try:
    link = input('Enter the video link here-->')
    link = link.strip()
    yt = pytube.YouTube(link)
except:
    print("The link you have provided is not correct.")
    exit()

lis = []
vderaud = input("Want to download as a video or audio file??")
if vderaud == 'video' or vderaud == 'Video':
    stream = yt.streams.filter(adaptive=True).filter(file_extension='mp4').all()

    for i in stream:
        lis.append(i.resolution)
    print("Available resolution")
    print('Select one from here', lis, '\n')
    x = input("Enter your selected Resolution").strip()

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

elif vderaud == 'audio' or vderaud == 'Audio':

    stream = yt.streams.filter(only_audio=True).filter(mime_type="audio/webm").all()
    for i in stream:
        lis.append(i.abr)
    print("Available Average bitrate")
    print('Select one from here', lis, '\n')
    x = input("Enter your selected Average bitrate").strip()

    for j in lis:
        if x in j:
            # print("Resolution is available")
            break
    else:
        print("Sorry,selected Average bitrate is not available")
        exit()

    confirm = input("Do you want to download this Audio file?Y/N")
    try:
        path = input('Enter the path where you want to save this file')
        path = path.strip()

        if confirm == 'Y' or confirm == 'y':

            print("Audio file is downloading,Please wait\n")
            if x == '128kbps' or x == '128':
                stream = yt.streams.get_by_itag(140)
                stream.download(path)
            elif x == '50kbps' or x == '50':
                stream = yt.streams.get_by_itag(249)
                stream.download(path)
            elif x == '70kbps' or x == '70':
                stream = yt.streams.get_by_itag(250)
                stream.download(path)
            elif x == '160kbps' or x == '160':
                stream = yt.streams.get_by_itag(251)
                stream.download(path)
            else:
                print("Resolution not found")

        else:
            exit()
        print("Audio file Downloaded successfully")

    except:
        print("The path you have provided seems not correct")

