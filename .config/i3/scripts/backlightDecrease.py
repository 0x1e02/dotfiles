#!/bin/python
from shared import Xbacklight, Dunst
if (Xbacklight.get()<=10):
    Xbacklight.set(1)
else:
    Xbacklight.set(round(Xbacklight.get()/10)*10 - 10)
Dunst.send("Brightness", f"{int(round(Xbacklight.get()/10)*10)}%", replace="11")