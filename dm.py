from sys import argv

import os


if argv[1] == "-h" or argv[1] == "-help" :
    print("dm {url} = dowload audio file")

    print("\n-dv || -dowloadVideo = dowload video")
    print("exemple = dm {url} -dv = dowload video file")

    print("\n----------------------------------------------")

    print("\n -h || -help = viwe commands")
    print(" -v || -version = viwe version")
    print(" -odm || -oldm = use old dm version")

    print("\n made by zag ^_^")


elif argv[1] == "-v" or argv[1] == "-version" :
    print("dm version - 0.2.1")
    print("made in 26.03.2025")

elif argv[1] == "-odm" or argv[1] == "-oldm" :
    
    userCountMusic =  int(input('count dowload music : '))
    setProp = " -x --audio-format mp3 --embed-thumbnail --embed-metadata "

    while userCountMusic > 0 :
        url = input("input url: ")

        os.system(f"yt-dlp {setProp}  {url}")

        userCountMusic = userCountMusic - 1


else :

    url = argv[1]

    if argv[2] == "-dv" or argv[2] == "-dowloadVideo" :
        ytDlpPrefix = "--embed-thumbnail --embed-metadata"
    
    else :
        ytDlpPrefix = "-x --audio-format mp3 --embed-thumbnail --embed-metadata"

    os.system(f"yt-dlp {ytDlpPrefix} {url}")
