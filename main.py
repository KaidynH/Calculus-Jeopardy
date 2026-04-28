import pygame, random
import numpy as np
from buttons import button
import question
import asyncio

# Pygame Setup
WIDTH = 1200
HEIGHT = 800
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Only Way to Study For Finals :)")
BG_COLOR = (70, 100, 70)
SCREEN.fill(BG_COLOR)
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
FPS = 30


# Sections Dicitionary and List
sections_dic = {
    7:np.array([f"7.{i}" for i in range(1,9)]),
    8:np.array(["8.1", "8.2"]),
    9:np.array(["9.1", "9.3", "9.5"]),
    10:np.array([f"10.{i}" for i in range(1,5)]),
    11:np.hstack([np.array([f"11.{i}" for i in range (1,7)]), np.array([f"11.{i}" for i in range (8,10)])])
            }

sections_dic.update({11:np.append(sections_dic.get(11), 11.11)})
sections_ary = np.hstack([sections_dic.get(i) for i in range(7,12)])

# Four Units
units_dic = {
    1:np.array([f"7.{i}" for i in range (1,8)]),
    2:np.array(["7.8", "8.1", "8.2", "9.1", "9.3", "9.5", "10.1", "10.2"]),
    3:np.array(["10.3", "10.4", "11.1", "11.2", "11.3", "11.4"]),
    4:np.array(["11.5", "11.6", "11.8", "11.9", "11.11"])
}

# Buttons for all the questions
buttons_grp = pygame.sprite.Group()
for section in sections_ary:
    buttons_grp.add(button(section, units_dic, sections_dic, font))

# Main Runn
async def main():
    running = True
    while running:
        # Delay between frames then wipe screen before drawing
        clock.tick(FPS)
        SCREEN.fill(BG_COLOR)


        # Handle Events
        for event in pygame.event.get():
            # Close the window
            if event.type == pygame.QUIT:
                running = False

            # Check if button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button_sprt in buttons_grp:
                    if button_sprt.rect.collidepoint(event.pos):
                        await question.run(SCREEN, button_sprt.section_str)
        

        # Update pygame window
        # pygame.draw.line(SCREEN, (0,255,0), (0, HEIGHT/2), (WIDTH, HEIGHT/2))
        # pygame.draw.line(SCREEN, (0,255,0), (WIDTH/2, 0), (WIDTH/2, HEIGHT))
        buttons_grp.update(SCREEN)
        pygame.display.update()
        await asyncio.sleep(0)

asyncio.run(main())
