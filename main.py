import pygame, random
import numpy as np
import question
import asyncio
from buttons import button
from sonic import sonic_sprite
from players import player_sprite


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

# Draw grid for positioning
def draw_grd():
    pygame.draw.line(SCREEN, (0,0,0), (0, HEIGHT/2), (WIDTH, HEIGHT/2))
    pygame.draw.line(SCREEN, (0,0,0), (WIDTH/2, 0), (WIDTH/2, HEIGHT))


# Sections Dicitionary
sections_dic = {
    7:np.array(["7.1", "7.2", "7.3", "7.4", "7.7", "7.8"]),
    8:np.array(["8.1", "8.2"]),
    9:np.array(["9.3", "9.5"]),
    10:np.array([f"10.{i}" for i in range(1,5)]),
    11:np.hstack([np.array([f"11.{i}" for i in range (1,7)]), np.array([f"11.{i}" for i in range (8,10)])])
            }

# 11.10 looks like 11.11 behind the scenes and it's annoying
sections_dic.update({11:np.append(sections_dic.get(11), 11.11)})
# Future me here - just type out the numbers holy fuck this is sm more annoying to read

# Array of all the section numbers
sections_ary = np.hstack([sections_dic.get(i) for i in range(7,12)])

# Four Units
units_dic = {
    1:np.array(["7.1", "7.2", "7.3", "7.4", "7.7", "7.8"]),
    2:np.array(["7.8", "8.1", "8.2", "9.3", "9.5", "10.1", "10.2"]),
    3:np.array(["10.3", "10.4", "11.1", "11.2", "11.3", "11.4"]),
    4:np.array(["11.5", "11.6", "11.8", "11.9", "11.11"])
}
# See this is prettier to look at. No one cares you know list comprehension and f strings

# Buttons for all the questions
buttons_grp = pygame.sprite.Group()
for section in sections_ary:
    buttons_grp.add(button(section, units_dic, sections_dic, font))

# The man himself
sonic_sprt = sonic_sprite()
sonic_alive = True

# Player Initizalization
player1 = player_sprite(1, "Ella", font)
player2 = player_sprite(2, "Joshua", font)
players_grp = pygame.sprite.Group(player1, player2)

# This isn't my fav way to do this, but it'll work for now
sonic_damage = 0
sonic_gettin_shot = False

# Main Runner
async def main():
    running = True
    # await sonic_sprt.intro(SCREEN, buttons_grp)
    # await player1.intro(SCREEN, buttons_grp)
    # await player2.intro(SCREEN, buttons_grp)

    # Are they here yet??
    sonic_here = False
    p1_here = False
    p2_here = False

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button_sprt in buttons_grp:
                    if button_sprt.rect.collidepoint(event.pos):
                        # Run the question corresponding to button pressed
                        sonic_damage = await question.run(SCREEN, button_sprt.section_str)
                        print(sonic_damage)
                        sonic_sprt.damage(sonic_damage)
            

            elif event.type == pygame.KEYDOWN:
            # Bring em in
                if event.key == pygame.K_SPACE:
                    if not sonic_here:
                        await sonic_sprt.intro(SCREEN, buttons_grp)
                        sonic_here = True
                    elif not p1_here:
                        await player1.intro(SCREEN, buttons_grp, sonic_sprt)
                        p1_here = True
                    elif not p2_here:
                        await player2.intro(SCREEN, buttons_grp, sonic_sprt, player1)
                        p2_here = True
                    else:  
                        print("Gang's all here")

        # Did we kill him?


        # Update pygame window and async
        # draw_grd()
        buttons_grp.update(SCREEN)
        sonic_sprt.update(SCREEN)
        players_grp.update(SCREEN)
        pygame.display.update()
        await asyncio.sleep(0)


asyncio.run(main())
