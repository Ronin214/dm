from sys import argv

import os

if argv[1] == "-h" or argv[1] == "-help" :
    print("dm url = dowload file")
    print("\n -h / -help = viwe commands")
    print(" -v / -version = viwe version")
    print(" -odm / -oldm = use old dm version")
    print("\n made by zag ^_^")

elif argv[1] == "-v" or argv[1] == "-version" :
    print("dm version - 0.2")
    print("made in 25.03.2025")

elif argv[1] == "-odm" or argv[1] == "-oldm" :
    
    userCountMusic =  int(input('count dowload music : '))
    setProp = " -x --audio-format mp3 --embed-thumbnail --embed-metadata "

    while userCountMusic > 0 :
        url = input("input url: ")

        os.system(f"yt-dlp {setProp}  {url}")

        userCountMusic = userCountMusic - 1

else :

    url = argv[1]

    os.system(f"yt-dlp -x --audio-format mp3 --embed-thumbnail --embed-metadata  {url}")
