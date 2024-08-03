import pygame

from core.config import Config


def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption("Fuzzy Broccoli 2")
    clock = pygame.time.Clock()
    return screen, clock
