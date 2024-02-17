import os
import sys

import pygame

from src.utilities.config import BLACK, SPLASH_DURATION


# Function to display the splash screen
def show_splash_screen(screen):
    # Get the root directory of the project
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate to the assets folder and construct the path to the splash image
    splash_image_path = os.path.join("..", "assets", "images", "splash_image.png")

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
