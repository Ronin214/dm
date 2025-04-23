from sys import argv
from pathlib import Path

import os
import configparser
import time

#configurate file varibls
config = configparser.ConfigParser()
config.read(Path(__file__).resolve().parent/"configDm.ini")

#help command
def helpCommand() :
    print("\n--------------- EXEMPLES -----------------")

    print("\ndm -d {url} -dm || -dowloadMusic = dowload audio file")

    print("\n-dv || -dowloadVideo = dowload video")
    print("exemple = dm -d -dv {url} = dowload video file")

    print("\n-p || -proxy = dowload video || music but use you proxy server")
    print("exemple = dm -p -dm || -dv {url} = dowload file but use proxy")

    print("\nсonfigured in path_to_dm/configDm.ini")

    print("\n----------- COMANDS || PREFIXS -----------")


    print("\n -h || -help = viwe commands")
    print(" -v || -version = viwe version")

    print("\n made by zag ^_^")

if argv[1] == "-h" or argv[1] == "-help" :
    helpCommand()

#version prefix
elif argv[1] == "-v" or argv[1] == "-version" :
    print("dm version B-3.2")
    print("made in 10.04.2025")

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

elif argv[1] == "-p" or "-proxy" :

    if argv[2] == "-dm" :
        ytDlpPrefix = config["ProxyPrefix"]["DmProxyPrefix"]

    elif argv[2] == "-dv" :
        ytDlpPrefix = config["ProxyPrefix"]["DvProxyPrefix"]
    
    url = argv[3]

    os.system(f"yt-dlp {ytDlpPrefix} {url}")
    

else :
    helpCommand()
