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
        options.insert(0, "Continue")

    # Initial render
    text_surfaces_and_rects = render_menu(screen, font, options, background_image)
    hovered_option = None
    current_screen = "Main Menu"

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
                        elif option == "Settings":
                            current_screen = "Settings"
                        elif option == "New Game":
                            current_screen = "First Level"
                        elif option == "Return to Main Menu":
                            current_screen = "Main Menu"
                        else:
                            print(f"Selected option: {option}")
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

        # Render the current screen based on the current screen state
        if current_screen == "Main Menu":
            render_menu(screen, font, options, background_image)
        elif current_screen == "Settings":
            render_settings(screen)
        elif current_screen == "First Level":
            render_first_level(screen)
        pygame.display.flip()  # Update the display


def render_settings(screen):
    # Placeholder function for settings scene
    screen.fill(BLACK)  # clear the screen
    font = pygame.font.Font(None, 36)
    settings_options = ["Return to Main Menu", "Sound", "Graphics", "Controls"]  # Options for settings
    text_y = screen.get_height() // 2 - 100  # Initial y-coordinate for the first option

    for option in settings_options:
        text = font.render(option, True, TEXT_DEFAULT_COLOR)
        text_rect = text.get_rect(center=(screen.get_width() // 2, text_y))
        screen.blit(text, text_rect)
        text_y += font.get_height() + 50  # Increase y-coordinate for the next option

    pygame.display.flip()  # Update the display

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if "Return to Main Menu" in settings_options:
                    return True  # Return True indicating a request to go back to the main menu
    return False  # No request to go back to the main menu


def render_first_level(screen):
    # Placeholder function for the first level scene
    screen.fill(BLACK)  # Clear the screen
    font = pygame.font.Font(None, 36)
    text = font.render("First Level Scene", True, TEXT_DEFAULT_COLOR)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()  # Update the display


# Entry point
def main():
    pygame.init()
    screen = pygame.display.set_mode((INITIAL_WIDTH, INITIAL_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Game")
    show_menu(screen)