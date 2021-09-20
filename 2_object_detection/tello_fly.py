import time
from pathlib import Path
from typing import Tuple

import cv2
from djitellopy import Tello
from loguru import logger

import keyboard
from controller import TelloController


class TelloFly:
    def __init__(self, tello: Tello, controller: TelloController) -> None:
        self.tello = tello
        self.controller = controller

    def fly(self, window: Tuple[int, int] = (360, 240), battery: bool = False) -> None:
        self.tello.streamon()
        while True:
            self.control()

            image = self.tello.get_frame_read().frame
            image = cv2.resize(image, window)

            cv2.imshow("Image", image)
            cv2.waitKey(1)

            if keyboard.get_key("z"):
                self.save_image(image)

            if battery:
                logger.info(f"[INFO] Remaining battery: {self.tello.get_battery()}")

    @staticmethod
    def save_image(image, images_dir: str = "data/images") -> None:
        images_dir.mkdir(parents=True, exist_ok=True)
        image_savepath = Path(images_dir, f"{time.time()}.jpg")
        cv2.imwrite(image_savepath, image)
        logger.info(f"Image saved to {image_savepath}")

    def control(self) -> None:
        values = self.controller.get_key_control(self.tello)
        self.tello.send_rc_control(values[0], values[1], values[2], values[3])
        time.sleep(0.05)
