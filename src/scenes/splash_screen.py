import pygame
import os
import sys


def show_splash_screen(screen):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    splash_image_path = os.path.join(root_dir, "assets", "images", "splash_image.png")

    if not os.path.exists(splash_image_path):
        print(f"Error: Splash image '{splash_image_path}' not found.")
        return

    splash_image = pygame.image.load(splash_image_path)
    screen.blit(splash_image, (0, 0,))
    pygame.display.flip()
    pygame.time.delay(3000)
