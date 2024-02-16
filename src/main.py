import pygame
import os
import time
import sys

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


# CONSTANTS
MIN_WIDTH, MIN_HEIGHT = 1280, 720
BLACK = (0, 0, 0)
SPLASH_DURATION = 3000  # 3000 milliseconds = 3 seconds


# Function to display the splash screen
def show_splash_screen(screen):
    # Get the root directory of the project
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate to the assets folder and construct the path to the splash image
    splash_image_path = os.path.join(root_dir, "..", "assets", "images", "splash_image.png")

    # Check if the splash image file exists
    if not os.path.exists(splash_image_path):
        print(f"Error: Splash image '{splash_image_path}' not found.")
        return

    # Load splash image
    splash_image = pygame.image.load(splash_image_path)
    # Display the splash image initially
    display_splash_image(screen, splash_image)

    # Record the time when the splash screen is displayed
    start_time = pygame.time.get_ticks()

    # Main loop for splash screen
    while pygame.time.get_ticks() - start_time < SPLASH_DURATION:
        # Process events during the waiting period
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle window resize event
            elif event.type == pygame.VIDEORESIZE:
                # Resize the window
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                # Display the splash image again after resizing
                display_splash_image(screen, splash_image)


def display_splash_image(screen, splash_image):
    # Get the dimensions of the splash image
    splash_width, splash_height = splash_image.get_size()

    # Calculate the scale factors to fit the splash image inside the window
    scale_x = screen.get_width() / splash_width
    scale_y = screen.get_height() / splash_height
    scale_factor = min(scale_x, scale_y)

    # Resize the splash image
    splash_image = pygame.transform.scale(splash_image, (int(splash_width * scale_factor),
                                                         int(splash_height * scale_factor)))

    # Display the splash image
    screen.fill(BLACK)
    screen.blit(splash_image, ((screen.get_width() - splash_image.get_width()) // 2,
                               (screen.get_height() - splash_image.get_height()) // 2))
    pygame.display.flip()


# Main function
def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Guardians Ascension RPG")

    # Show splash screen
    show_splash_screen(screen)

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state

        # Render
        screen.fill(BLACK)

        # Flip the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
