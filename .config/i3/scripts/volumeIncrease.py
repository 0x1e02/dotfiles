#!/bin/python3
from shared import Pactl, Dunst

if Pactl.isMuted():
    Pactl.setSink("mute", 0, 0)
    Dunst.sendMuteState()
else:
    Pactl.setSink("volume", 0, "+5%")
    Dunst.sendVolume()
