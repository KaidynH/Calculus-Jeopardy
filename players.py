import pygame, random, asyncio
import numpy as np

WIDTH = 1200
HEIGHT = 800
BG_COLOR = (70, 100, 70)
clock = pygame.time.Clock()
FPS = 30
class player_sprite(pygame.sprite.Sprite):
    def __init__(self, player_num, name, pfont):
        # Initialize sprite class
        super().__init__()

        font = pygame.font.Font(None, 45)
        # Image initialize
        self.size = 200
        # Ella is yellow toad, Joshua is orange yoshi
        image_path = "images/yellow_toad.png" if name == "Ella" else "images/orange_yoshi.png"
        self.original_image = pygame.image.load(image_path)
        self.rect = self.original_image.get_rect()
        self.image = pygame.transform.smoothscale_by(self.original_image, self.size/self.rect.height)
        x_gap = 275
        self.x = WIDTH/2 - x_gap if player_num == 1 else WIDTH/2 + x_gap
        self.final_y = HEIGHT - self.size * 0.5 - 50
        self.rect = self.image.get_rect(center=(self.x,HEIGHT+200))
        self.mask = pygame.mask.from_surface(self.image)


        self.text = font.render(name, True, "orange" if name == "Joshua" else "yellow")
        self.text_rect = self.text.get_rect(center=(self.rect.centerx + 15, self.final_y + self.size / 2 + 20))
        

        self.in_position = False

    async def intro(self, screen, buttons, sonic, player1=""):
        move_spd = 10

        running = True
        while running:
            # Delay between frames then wipe screen before drawing
            clock.tick(FPS)
            screen.fill(BG_COLOR)

            # Handle Events
            for event in pygame.event.get():
                # Close the window
                if event.type == pygame.QUIT:
                    running = False
            
            self.rect.centery -= move_spd
            # Just stroll in from the bottom all chill like (slide a static png slowly up from out of frame)
            if abs(self.rect.centery - self.final_y) <= 10:
                self.rect.centery = self.final_y
                self.in_position = True
                running = False
    
            
            
            # pygame and asyncio refresh
            self.update(screen)
            buttons.update(screen)
            sonic.update(screen)
            try:
                player1.update(screen)
            except:
                print("Hello it is me player 1 here I am entering")
        
            pygame.display.update()
        await asyncio.sleep(0)

    # General update function
    def update(self, screen):
        # Draw sonic on screen
        screen.blit(self.image, self.rect)

        if self.in_position:
            screen.blit(self.text, self.text_rect)