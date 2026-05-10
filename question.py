import asyncio
import pygame

WIDTH = 1200
HEIGHT = 800
BG_COLOR = (70, 100, 70)

async def run(screen, section, ):

    # Image initializing
    background_img = pygame.image.load("images/jeopardy_background.png").convert_alpha()
    bg_img_rect = background_img.get_rect()
    bg_img_rect.center = (WIDTH/2, HEIGHT/2)     
    
    # $100, $200, $300
    choices = [pygame.Rect(WIDTH/2 -400 /2, 120, 400, 150), pygame.Rect(WIDTH/2 -400 /2, 320, 400, 150), pygame.Rect(WIDTH/2 -400 /2, 520, 400, 150)]

    # Show question gate
    show_q = False

    running = True
    while running:
        screen.fill(BG_COLOR)

        # Handle Events
        for event in pygame.event.get():
            # Close the window
            if event.type == pygame.QUIT:
                running = False
            
            # Check if button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                for choice in choices:
                    if choice.collidepoint(event.pos):
                        try:
                            money = (choices.index(choice) + 1) * 100
                            question_img = pygame.image.load(f"images/questions/{section}-{money}.png").convert_alpha()
                            q_img_rect = question_img.get_rect()
                            q_img_rect.center = (WIDTH/2, HEIGHT/2) 
                            show_q = True
                        except:
                            print("pass")
        

        # Blit images
        screen.blit(background_img, bg_img_rect)
        if show_q:
            screen.blit(question_img, q_img_rect)

        # pygame and asyncio refresh
        pygame.display.update()
        await asyncio.sleep(0)