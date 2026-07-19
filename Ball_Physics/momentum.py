# create two balls that collide with each other
# ball1 will have a momentum and when it collides with ball2 the momentum will be transferred to ball2

import pygame

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Momentum")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	pygame.display.update()

	clock.tick(40)

pygame.quit()
