# Create a ball (O) -- DONE
	# When spacebar is pressed activate ball
	# Ball needs to move in the -y direction

# Create a charge bar (|) or (*)
	# When spacebar is held increase velocity by 1
		# One press is 1
	# Add | or * as spacebar is held
	# store velocity as new velocity
	# start velocity at 0
	# Display charge bar on the side and have it display going up on the y_axis
	# when spacebar is released ball should move


import curses

# Ball Class
class Ball:
	def __init__(self, y_pos, x_pos):
		self.y_pos = y_pos
		self.x_pos = x_pos
		self.text = "O"

		self.velocity = 5

	def draw(self, surface):
		surface.addch(self.y_pos, self.x_pos, self.text)

	def move(self):
		pass

# Booster Class
class Booster:
	pass


def main(surface):
	surface.clear()
	curses.noecho()

	win_x = 40
	win_y = 0
	win_width = 50
	win_height = 20

	win = curses.newwin(win_height, win_width, win_y, win_x)

	curses.curs_set(0)

	win.border()

	ball = Ball(win_height - 2, win_width//2)
	ball.draw(win)

	win.refresh()

	win.getkey()

	curses.endwin()

screen = curses.initscr()

curses.wrapper(main)
