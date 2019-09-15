#!/usr/bin/python3
from subprocess import Popen, PIPE
from sys import exit
from os import path
from time import sleep
import psutil
from playsound import playsound

# CONFIG #
current_path = path.dirname(path.realpath(__file__)) + "/"
alert_audio = file_loc = current_path + "alert.mp3" # https://freesound.org/people/SomeAudioGuy/sounds/43866/
high_level = 10
low_level = 5
check_every = 10 # in seconds
selected_susbend_commend_index = 0
# END CONFIG #

suspend_commands = ["systemctl suspend", "pm-suspend", "pm-hibernate", "pm-suspend-hybrid"]
# for more info visit -> https://www.cyberciti.biz/faq/linux-command-to-suspend-hibernate-laptop-netbook-pc/

notified = False 
debug = True 


def call(cmd):
    Popen(cmd, stdout=PIPE, stderr=PIPE)

def showMSG(msg = "Connect The Charger, Low Battery Level!!"):
    call(["i3-nagbar",  "-m",  msg, "-t", "error"])

def suspend():
    call(suspend_commands[selected_susbend_commend_index].split(" "))

while(True):
    try:
        battery = psutil.sensors_battery()
        
        if debug: print("=" * 30)
        if debug: print(f"High Level: {high_level}%, Low Level: {low_level}%, Check Every: {check_every}sec")
        if debug: print(f"Percent: {round(battery.percent, 1)}%")
        if debug: print(f"Is Charging: {battery.power_plugged}")
        if debug: print(f"Next Action Suspend: {notified}")

        if battery.power_plugged:
            notified = False
        elif battery.percent <= high_level and not notified:
            if debug: print(f"Event: Low Level")
            showMSG()
            playsound(alert_audio)
            notified = True
        elif battery.percent <= low_level:
            if debug:
                print("Event: Suspend [after 5secs]")
                sleep(5)
            notified = False
            suspend()
        
        sleep(check_every)
    except KeyboardInterrupt:
        if debug: print("Script Stopped!!")
        exit()
    except Exception as err:
        if debug: print(str(err))
        exit(1)
