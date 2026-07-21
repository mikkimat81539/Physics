# create ball -- DONE 
# create a booster
	# Create booster class using line as the shape
	# Increase booster along the y-axis
	# To increase booster use spacebar
	# velocity needs to increase when spacebar is held
	# have a max velocity of 10

# GOAL: When spacebar is held and than release ball shoots based on velocity after release

import pygame
from Ball_Object import Ball

pygame.init()

# BOOSTER CLASS
class Booster:
	def __init__(self, x_pos, y_pos, color, thickness):
		self.x_pos = x_pos
		self.y_pos = y_pos

		self.start_pos = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.end_pos = pygame.math.Vector2(self.x_pos, self.y_pos + 5)

		self.color = color
		self.thickness = thickness

	def draw_line(self, surface):
		pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, self.thickness)

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("BOOSTER")

# BALL
ball = Ball(20, 250, 10, "black", 7)

# BOOSTER
booster = Booster(480, 300, "red", 5)

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# DRAW
	ball.draw_ball(screen)

	booster.draw_line(screen)

	pygame.display.flip()

	clock.tick(40)

pygame.quit()



