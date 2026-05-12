import pygame, random
import numpy as np

unit_colors = {1:(120, 50, 235), 2:(235,50,190), 3:(10,160,215), 4:(235,245,76)}

WIDTH = 1200
HEIGHT = 800

class button(pygame.sprite.Sprite):
    def __init__(self, psection, units, sections, font):
        # Initialize sprite class
        super().__init__()

        # Section
        self.section_str = psection
        self.section_float = float(psection)
        self.section_int = int(self.section_float)

        # Unit number and color
        self.unit = 0
        for i in range(1,5):
            if self.section_str in units.get(i):
                self.unit = i
                break
        self.color = unit_colors.get(self.unit)


        # Coordinates and size of button
        self.size = 35
        x_border_size = 200
        x_distance = int(WIDTH - x_border_size * 2) // (len(units)-1)
        y_distance = int(self.size * 2.5)
        y_border_size = int(HEIGHT/2 - (y_distance * (len(units.get(self.unit)) / 2) + 1))
        self.centerx = x_border_size + ((self.unit-1) * x_distance)
        self.centery = y_border_size+y_distance*.5 + np.where(units.get(self.unit) == self.section_str)[0][0] * y_distance

        # Temporary hard coding an annoying thing with unit 2 I don't have time to care about, I disgust myself
        if(self.unit == 2):
            self.centery -= (self.size + 5)
    

        self.center = (self.centerx, self.centery)

        # Collision rect
        self.rect = pygame.Rect(0, 0, self.size*2, self.size*2)
        self.rect.center = self.center

        # Button text
        # I fucking hate you chapter 11.10 :(
        self.text = font.render(self.section_str, True, "black") if self.section_float != 11.11 else font.render("11.10", True, "black")
        self.text_rect = self.text.get_rect(center=self.center)

        
    # Holy shit this one is slightly different than the others  :
    def update(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.center, self.size+5)
        pygame.draw.circle(screen, self.color, self.center, self.size)
        screen.blit(self.text, self.text_rect)








    


        


