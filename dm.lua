
local ytDlpPrefix
local url

function helpCommand()
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
    
end

if arg[1] == "-h" or arg[1] == "-help" then
    helpCommand()

elseif arg[1] == "-v" or arg[1] == "-version" then

    print("vresion ID-1 lua")
    print("mada in hui poimi")

elseif arg[1] == "-d" then

    if arg[2] == "-dm" then
        ytDlpPrefix = nil
    elseif arg[2] == "-dv" then
        ytDlpPrefix = nil
    end

    url = arg[3]

end