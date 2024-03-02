import sys

import pygame

from src.scenes.menu import show_menu
from src.scenes.splash_screen import show_splash_screen
from src.utilities.config import *

"""
Module Name: main.py
Author: Nino Ross
Date: February 14, 2024
Description: Guardian's Ascension is a captivating Diablo-style RPG built with Pygame. 
Dive into a thrilling adventure where you embark on a journey to defend the realm against 
dark forces, conquer treacherous dungeons, and unlock powerful abilities. With immersive 
graphics and dynamic gameplay mechanics, Guardian's Ascension promises an epic gaming 
experience. Join the ranks of legendary guardians and ascend to greatness in this 
action-packed RPG.
"""


# Main function
def main():
    pygame.init()  # Initialize Pygame

    # Set up the display
    screen = pygame.display.set_mode((INITIAL_WIDTH, INITIAL_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Guardians Ascension")
    show_splash_screen(screen)  # Show splash screen
    show_menu(screen)  # Show menu
    clock = pygame.time.Clock()  # Clock for controlling the frame rate

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        screen.fill(BLACK)  # Render
        pygame.display.flip()  # Flip the display
        clock.tick(60)  # Cap the frame rate

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
