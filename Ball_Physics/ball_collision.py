import pygame, random


class Ball_Object:
	def __init__(self, x_pos, y_pos, color, radius):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.color = color
		self.radius = radius

		self.vel_x = 21
		self.vel_y = 17

	def drawObject(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

	def moveObject(self):
		self.center[0] += self.vel_x # x-axis movement
		self.center[1] += self.vel_y # y-axis movement

		self.collision()

	def collision(self):
		boundary_x, boundary_y = (500 - self.radius), (500 - self.radius)
		
		if self.center[0] >= boundary_x or self.center[0] <= 5:
			self.vel_x = -self.vel_x

		if self.center[1] >= boundary_y or self.center[1] <= 5:
			self.vel_y = -self.vel_y

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


# Ball Object
ball = Ball_Object(random.randint(10, 420), random.randint(10, 420), "white", 20)

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("#c296ff")

	# MOVEMENT
	ball.moveObject()

	# DRAW
	ball.drawObject(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
