import sys
import pygame
import random

width = int(input("Please, enter the width.\n"))
height = int(input("Please, enter the height.\n"))
x = 0
y = 0
name = f"{random.randint(0, 1000000)}.png"

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Window")
surface = pygame.Surface((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    surface.set_at((x, y), (r, g, b))
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    if x == width and y == height:
        break
    elif x <= width:
        x += 1
    else:
        y += 1
        x = 0

pygame.image.save(screen, name)
print(f"\nRandom image saved as {name}.")
