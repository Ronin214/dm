from sys import argv
from pathlib import Path

import os
import configparser

#paths
programmPaht = Path(__file__).resolve().parent
configPath = programmPaht / "configDm.ini"

#configurate file varibls
config = configparser.ConfigParser()
config.read(configPath)

#help command
if argv[1] == "-h" or argv[1] == "-help" :
    print("dm -d {url} -dm || -dowloadMusic = dowload audio file")

    print("\n-dv || -dowloadVideo = dowload video")
    print("exemple = dm -d {url} -dv = dowload video file")

    print("\n----------------------------------------------")

    print("\n -h || -help = viwe commands")
    print(" -v || -version = viwe version")

    print("\n made by zag ^_^")

#version prefix
elif argv[1] == "-v" or argv[1] == "-version" :
    print("dm version - 0.2.1")
    print("made in 29.03.2025")

#download prefix
elif argv[1] == "-d" :

    #download music
    if argv[2] == "-dm" :

        ytDlpPrefix = config["Prefix"]["DmPrefix"]
    #download video
    elif argv[2] == "-dv" :
        
        ytDlpPrefix = config["Prefix"]["DvPrefix"]
        
    url = argv[3]

    os.system(f"yt-dlp {ytDlpPrefix} {url}")
