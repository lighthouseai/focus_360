import os

cmd = "libcamera-vid -t 0 -n  --width 1920 --height 1080 --codec mjpeg  --inline --listen -o tcp://0.0.0.0:5000"
cmdToKill = "sudo killall -9 libcamera-vid"

while True: 
    os.system(cmdToKill)
    os.system(cmd)