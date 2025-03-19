import os

userCountMusic =  int(input('count dowload music : '))
setProp = " -x --audio-format mp3 --embed-thumbnail --embed-metadata "

while userCountMusic > 0 :
    url = input("input url: ")

    os.system(f"yt-dlp -x {setProp}  {url}")

    userCountMusic = userCountMusic - 1
