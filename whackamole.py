import pygame
import random

def main():
    try:
        pygame.init()

        #loads the mole image
        mole_image = pygame.image.load("mole.png")

        #sets up the screen and clock
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        #defines grid settings
        grid_size = 32
        rows = 16
        cols = 20

        #origins
        mole_x = 0
        mole_y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #checks for mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mole_col = random.randrange(0, cols)
                    mole_row = random.randrange(0, rows)
                    mole_x = mole_col * grid_size
                    mole_y = mole_row * grid_size

            screen.fill("light green")

            #draws the grid using lines
            for row in range(rows + 1):
                #horizontal lines
                pygame.draw.line(screen, "black", (0, row * grid_size), (cols * grid_size, row * grid_size), 1)

            for col in range(cols + 1):
                #vertical lines
                pygame.draw.line(screen, "black", (col * grid_size, 0), (col * grid_size, rows * grid_size), 1)

            #draws the mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

            #display
            pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
