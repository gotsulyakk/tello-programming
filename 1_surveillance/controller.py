from typing import Tuple

from djitellopy import Tello

import keyboard


class TelloController:
    @staticmethod
    def get_key_control(
        tello: Tello, speed: int = 50
    ) -> Tuple[float, float, float, float]:

        lr, fb, ud, yv = 0, 0, 0, 0

        if keyboard.get_key("a"):
            lr = -speed
        elif keyboard.get_key("d"):
            lr = speed

        if keyboard.get_key("w"):
            fb = speed
        elif keyboard.get_key("s"):
            fb = -speed

        if keyboard.get_key("SPACE"):
            ud = speed
        elif keyboard.get_key("LSHIFT"):
            ud = -speed

        if keyboard.get_key("q"):
            yv = speed
        elif keyboard.get_key("e"):
            yv = -speed

        if keyboard.get_key("TAB"):
            tello.takeoff()
        if keyboard.get_key("LCTRL"):
            tello.land()

        return lr, fb, ud, yv
