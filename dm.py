from sys import argv

import os
import configparser

#configurate file varibls
config = configparser.ConfigParser()
config.read("configDm.ini")

if argv[1] == "-h" or argv[1] == "-help" :
    print("dm -d {url} -dm || -dowloadMusic = dowload audio file")

    print("\n-dv || -dowloadVideo = dowload video")
    print("exemple = dm -d {url} -dv = dowload video file")

    print("\n----------------------------------------------")

    print("\n -h || -help = viwe commands")
    print(" -v || -version = viwe version")

    print("\n made by zag ^_^")


elif argv[1] == "-v" or argv[1] == "-version" :
    print("dm version - 0.2.1")
    print("made in 29.03.2025")

elif argv[1] == "-d" :

    if argv[3] == "-dm" :

        ytDlpPrefix = config["Prefix"]["DmPrefix"]
    
    elif argv[3] == "-dv" :
        
        ytDlpPrefix = config["Prefix"]["DvPrefix"]
        
    url = argv[2]

    os.system(f"yt-dlp {ytDlpPrefix} {url}")

