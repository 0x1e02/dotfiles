#!/bin/python3
from shared import Pactl, Dunst

Pactl.setSink("Volume", 0, "-5%")
Dunst.sendVolume()