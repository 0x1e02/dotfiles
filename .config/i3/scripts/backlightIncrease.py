#!/bin/python3
from shared import Xbacklight, Dunst


Xbacklight.set(round(Xbacklight.get()/10)*10 + 10)
Dunst.send("Brightness", f"{int(round(Xbacklight.get()/10)*10)}%", replace="11")