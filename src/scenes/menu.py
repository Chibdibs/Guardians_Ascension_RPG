import os
import sys

import pygame

from src.utilities.config import MIN_WIDTH, MIN_HEIGHT, BLACK
from src.utilities.game_functions import check_save_file

# Constant
TEXT_DEFAULT_COLOR = (234, 178, 160)
TEXT_HIGHLIGHTED_COLOR = (167, 111, 111)


def show_menu(screen):
    # Load background image
    background_image_path = os.path.join("..", "assets", "images", "menu_image.png")
    background_image = pygame.image.load(background_image_path).convert()

    # Resize background image to fit the screen
    background_image = pygame.transform.scale(background_image, (MIN_WIDTH, MIN_HEIGHT))

    # Clear the screen
    screen.fill(BLACK)

    # Display background image
    screen.blit(background_image, (0, 0))

    # Display menu options based on save file status
    options = ["New Game", "Load Game", "Settings", "Quit"]
    if check_save_file():
        options.insert(0, "Resume")

    # Display menu text
    font = pygame.font.Font(None, 72)
    text_y = MIN_HEIGHT // 2 - 50  # Initial y-coordinate for the first option

    text_surfaces_and_rects = []  # Store (text_surface, text_rect) tuples

    # # Initialize text variable
    # text = None

    for option in options:
        text_surface = font.render(option, True, TEXT_DEFAULT_COLOR)
        text_rect = text_surface.get_rect(center=(MIN_WIDTH // 2, text_y))
        screen.blit(text_surface, text_rect)
        text_surfaces_and_rects.append((option, text_surface, text_rect))
        text_y += 75  # Increment y-coordinate distance for the next option

    pygame.display.flip()

    # Wait for user input to select an option
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the bounds of any option
                for option, text_surface, text_rect in text_surfaces_and_rects:
                    # Check if the mouse click is within the bounds of the option's rectangle
                    if text_rect.collidepoint(event.pos):
                        if option == "Quit":
                            pygame.quit()
                            sys.exit()
                        else:
                            print(f"Selected option: {option}")
                            return option  # Return the selected option
            elif event.type == pygame.MOUSEMOTION:
                # Redraw all menu options in their default state
                for option, _, text_rect in text_surfaces_and_rects:
                    text_surface = font.render(option, True, TEXT_DEFAULT_COLOR)  # Default color
                    screen.blit(text_surface, text_rect)

                # Apply hover effects to the currently hovered option
                for option, text_surface, text_rect in text_surfaces_and_rects:
                    if text_rect.collidepoint(event.pos):
                        highlighted_text_surface = font.render(option, True, TEXT_HIGHLIGHTED_COLOR)  # Hover color
                        screen.blit(highlighted_text_surface, text_rect)
                    else:
                        screen.blit(text_surface, text_rect)

                pygame.display.flip()  # Update the display

