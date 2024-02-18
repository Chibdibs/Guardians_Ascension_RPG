import os
import sys
import pygame
from src.utilities.config import INITIAL_WIDTH, INITIAL_HEIGHT, BLACK
from src.utilities.game_functions import check_save_file

# Constants
TEXT_DEFAULT_COLOR = (234, 178, 160)
TEXT_HIGHLIGHTED_COLOR = (167, 111, 111)


# Render the menu items and ensure that it's centered upon resize
def render_menu(screen, font, options, background_image):
    screen.fill(BLACK)  # Clear the screen or fill it with a background color
    screen.blit(background_image, (0, 0))  # Redraw the background

    # Calculate total height of the menu for centering
    total_height = len(options) * (font.get_height() + 75) - 75
    start_y = (screen.get_height() - total_height) // 2

    text_surfaces_and_rects = []
    for option in options:
        text_surface = font.render(option, True, TEXT_DEFAULT_COLOR)
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, start_y))
        screen.blit(text_surface, text_rect)
        text_surfaces_and_rects.append((option, text_surface, text_rect))
        start_y += font.get_height() + 50  # Increase for the next option

    pygame.display.flip()  # Update the display to show the menu
    return text_surfaces_and_rects


# Optimizes the mouse hovering to decrease unnecessary resource load/use
def get_hovered_option(mouse_pos, text_surfaces_and_rects):
    for option, _, text_rect in text_surfaces_and_rects:
        if text_rect.collidepoint(mouse_pos):
            return option
    return None


# Displays the game main menu scene
def show_menu(screen):
    # Load background image
    background_image_path = os.path.join("..", "assets", "images", "menu_image.png")
    original_background_image = pygame.image.load(background_image_path).convert()

    # Initial scaling to fit the initial window size
    background_image = pygame.transform.scale(original_background_image, (INITIAL_WIDTH, INITIAL_HEIGHT))

    font = pygame.font.Font(None, 72)
    options = ["New Game", "Load Game", "Settings", "Quit"]
    if check_save_file():
        options.insert(0, "Resume")

    # Initial render
    text_surfaces_and_rects = render_menu(screen, font, options, background_image)
    hovered_option = None

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # Update the display surface to the new size
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                # Scale the original background image to fit the new dimensions
                background_image = pygame.transform.scale(original_background_image, (event.w, event.h))

                # Re-render the menu with updated screen dimensions
                text_surfaces_and_rects = render_menu(screen, font, options, background_image)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for option, _, text_rect in text_surfaces_and_rects:
                    if text_rect.collidepoint(event.pos):
                        if option == "Quit":
                            pygame.quit()
                            sys.exit()
                        else:
                            print(f"Selected option: {option}")
                            # Implement option selection logic here (e.g., start game, open settings, etc.)
                            waiting = False  # Break the loop if necessary

            elif event.type == pygame.MOUSEMOTION:
                current_hover = get_hovered_option(event.pos, text_surfaces_and_rects)

                if current_hover != hovered_option:  # Only update if the hover state changes
                    hovered_option = current_hover
                    # Re-render menu to clear previous highlights
                    render_menu(screen, font, options, background_image)
                    for option, text_surface, text_rect in text_surfaces_and_rects:
                        if option == hovered_option:
                            highlighted_text_surface = font.render(option, True, TEXT_HIGHLIGHTED_COLOR)
                            screen.blit(highlighted_text_surface, text_rect)
                        else:
                            screen.blit(text_surface, text_rect)

                    pygame.display.flip()  # Update the display with hover effects
