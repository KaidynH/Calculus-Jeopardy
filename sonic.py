import pygame, random, asyncio
import numpy as np

WIDTH = 1200
HEIGHT = 800
BG_COLOR = (70, 100, 70)
clock = pygame.time.Clock()
FPS = 30

class sonic_sprite(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize sprite class
        super().__init__()

        # Image initialize
        self.size = 300
        self.original_image = pygame.image.load("images/sonic_image.png")
        self.rect = self.original_image.get_rect()
        self.image = pygame.transform.smoothscale_by(self.original_image, self.size/self.rect.height)
        self.rect = self.image.get_rect(center=(WIDTH + self.size, 200))
        self.mask = pygame.mask.from_surface(self.image)
        self.final_x = WIDTH/2


        # Sonic things
        self.original_health = 10000
        self.health = self.original_health
        self.in_position = False


    def damage(self, damage):
        self.health -= damage
        print("Sonic Health Left:", self.health)



    # General update function
    def update(self, screen):
        # Draw sonic on screen
        screen.blit(self.image, self.rect)

        # White rectangle under a colored rectangle that gets smaller and turns from green to red as the health goes down
        health_bar_width = 125
        health_bar_height = 40
        health_ratio = self.health/self.original_health    
        health_bar_pos = (WIDTH/2-health_bar_width/2, self.rect.bottom + 10)
        if self.in_position:
            pygame.draw.rect(screen, (255, 255, 255), (health_bar_pos[0], health_bar_pos[1], health_bar_width, health_bar_height))
            pygame.draw.rect(screen, ((100-100*health_ratio)*2.55,100*health_ratio*2.55, 0), (health_bar_pos[0] + 5, health_bar_pos[1] + 5, health_ratio*health_bar_width - 10, health_bar_height - 10))

    

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

