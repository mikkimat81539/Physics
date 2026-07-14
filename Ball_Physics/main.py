import pygame

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	pygame.display.flip()

pygame.quit()
