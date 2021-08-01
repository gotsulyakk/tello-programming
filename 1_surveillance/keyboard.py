import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def get_key(key):
    ans = False
    for _ in pygame.event.get():
        pass

    key_input = pygame.key.get_pressed()
    my_key = getattr(pygame, f"K_{key}")

    if key_input[my_key]:
        ans = True
    pygame.display.update()

    return ans


if __name__ == "__main__":
    init()
