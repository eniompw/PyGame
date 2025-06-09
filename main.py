import pygame

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game loop
running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (400, 300), 50)
    pygame.display.flip()
    
    # FPS
    clock.tick(60)

pygame.quit()
