# Main project file for RPG

import pygame
import sys

# CONSTANTS
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)


# Runs the pygame project
def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guardians Ascension RPG")

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

if __name__ == '__main__':
    main()
    pass
