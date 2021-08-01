import keyboard
from loguru import logger
from djitellopy import Tello
from tello_fly import TelloFly
from tello_controller import TelloController


def main():
    logger.info("Initializing pygame...")

    keyboard.init()

    logger.info("Pygame initialized")
    logger.info("Connecting tello...")

    tello = Tello()
    tello.connect()

    logger.info("Tello connected")
    logger.info(f"Remaining battery: {tello.get_battery()}")

    controller = TelloController()
    fly = TelloFly(tello, controller)

    fly.fly(battery=True)


if __name__ == "__main__":
    main()
