from sys import argv
from pathlib import Path

import os
import configparser

#path
programmPaht = Path(__file__).resolve().parent

#configurate file varibls
config = configparser.ConfigParser()
config.read(programmPaht/"configDm.ini")

#help command
def helpCommand() :
    print("dm -d {url} -dm || -dowloadMusic = dowload audio file")

    print("\n-dv || -dowloadVideo = dowload video")
    print("exemple = dm -d {url} -dv = dowload video file")

    print("\n----------------------------------------------")

    print("\n -h || -help = viwe commands")
    print(" -v || -version = viwe version")

    print("\n made by zag ^_^")

if argv[1] == "-h" or argv[1] == "-help" :
    helpCommand()

#version prefix
elif argv[1] == "-v" or argv[1] == "-version" :
    print("dm version B-3.1")
    print("made in 31.03.2025")

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

else :
    helpCommand()
