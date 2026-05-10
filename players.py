import pygame, random, asyncio
import numpy as np

WIDTH = 1200
HEIGHT = 800
BG_COLOR = (70, 100, 70)
clock = pygame.time.Clock()
FPS = 30

class player_sprite(pygame.sprite.Sprite):
    def __init__(self, player_num, name):
        # Initialize sprite class
        super().__init__()

        # Image initialize
        self.size = 250
        image_path = "images/"
        self.original_image = pygame.image.load("images/sonic_image.png")
        self.rect = self.original_image.get_rect()
        self.image = pygame.transform.smoothscale_by(self.original_image, self.size/self.rect.height)
        x = WIDTH/2 - 200 if player_num == 1 else WIDTH/2 + 200
        y = HEIGHT - self.size * 1.5
        self.rect = self.image.get_rect(center=(x,y))
        self.mask = pygame.mask.from_surface(self.image)

    async def intro(self, screen, buttons):
        move_speed = -(self.rect.centerx - self.final_x) /15
        # moving = True
        bounces = 0


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
            

            # Im hardcoding this bc I'm low on time, which is disgusting and I sincerely apologize future me

            # Shoot left across the screen, right slightly slower, then slowkly to the middle
            # Assert dominance
            left_barrier = -1000
            right_barrier = WIDTH + 1000
            self.rect.centerx += move_speed
            if self.rect.centerx < left_barrier or self.rect.centerx > right_barrier:
                move_speed *= -0.7
                bounces += 1
            if bounces >= 2 and abs(self.rect.centerx - self.final_x) < 20:
                self.rect.centerx = self.final_x
                self.in_position = True
                running = False
            
            
            
            
            # pygame and asyncio refresh
            self.update(screen)
            buttons.update(screen)
            pygame.display.update()
        await asyncio.sleep(0)

    # General update function
    def update(self, screen):
        # Draw sonic on screen
        screen.blit(self.image, self.rect)