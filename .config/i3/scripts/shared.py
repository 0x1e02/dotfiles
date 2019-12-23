#!/bin/python3
"""
This is a primitive wrapper for common Tasks using dunst and pactl
"""
import os

class Xbacklight:
    @staticmethod
    def set(value):
        os.system(f"xbacklight -set {value}")
    
    @staticmethod
    def get():
        return float(os.popen(f"xbacklight").read().strip())


class Dunst:
    @staticmethod
    def send(title, body, **kwargs):
        os.system(f"dunstify {title} {body} {' '.join(map(lambda x: '--' + ' '.join(x), kwargs.items()))}")

    @staticmethod
    def sendAudio(message):
        os.system(f"dunstify -i audio-volume-medium 'Audio' {message} -r 10 ")

    @staticmethod
    def sendVolume():
        Dunst.sendAudio(Pactl.getVolume())

    @staticmethod
    def sendMuteState():
        Dunst.sendAudio('Muted' if Pactl.isMuted() else 'Unmuted')

class Pactl:
    @staticmethod
    def getVolume():
        return list(filter(lambda x: "%" in x, os.popen("pactl list sinks | grep Volume").read().split("/")))[0].strip()
    
    @staticmethod
    def isMuted():
        return os.popen("pactl list sinks | grep Mute").read().strip().endswith("yes")
    
    @staticmethod
    def setSink(verb, *args):
        args = map(str, args)
        os.system(f"pactl set-sink-{verb.lower()} {' '.join(args)}")