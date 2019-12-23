#!/bin/python3
from shared import Pactl, Dunst

Pactl.setSink("Mute", 0, "toggle")
Dunst.sendMuteState()