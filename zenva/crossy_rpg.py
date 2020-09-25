# Pygame development 1
# Start the basic game set up
# Set up the display

# Gain access to pygame library
import pygame

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:

	# Typical rate of 60, equivalent to FPS
	TICK_RATE = 60

	# Initialiser for the game class to set up the title, width and height
	def __init__(self, image_path, title, width, height):
		self.title = title
		self.width = width
		self.height = height

		# Create a window of the specified size to display the game
		self.game_screen = pygame.display.set_mode((width, height))
		# Set the game window color to white
		self.game_screen.fill(WHITE_COLOR)
		# Set the game window title
		pygame.display.set_caption(title)

		background_image = pygame.image.load(image_path)
		self.image = pygame.transform.scale(background_image, (width, height))


	def run_game_loop(self):

		is_game_over = False
		did_win = False
		direction = 0

		player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
		enemy_0 = NonPlayerCharacter('enemy.png', 20, 400, 50, 50)
		treasure = GameObject('treasure.png', 375, 50, 50, 50)

		# Main game loop, used to update all gameplay such as movement, checks and graphics
		# Runs until is_game_over = True
		while not is_game_over:

			# A loop to get all of the events occurring at any given time
			# Events are most often mouse movement, mouse and button clicks, or exit events
			for event in pygame.event.get():
				# If we have a quit type of event then exit out of game loop
				if event.type == pygame.QUIT:
					is_game_over = True
				# Detect when key is pressed down
				elif event.type == pygame.KEYDOWN:
					# Move up if up key pressed
					if event.key == pygame.K_UP:
						direction = 1
					# Move down if down key pressed
					elif event.key == pygame.K_DOWN:
						direction = -1
				# Detect when key is released
				elif event.type == pygame.KEYUP:
					# Stop movement when key no longer pressed
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						direction = 0

				print(event)

			# Redraw the screen to be a blank white window
			self.game_screen.fill(WHITE_COLOR)
			self.game_screen.blit(self.image, (0, 0))

			# Draw the treasure
			treasure.draw(self.game_screen)

			# Update the player position
			player_character.move(direction, self.height)
			# Draw the player at the new position
			player_character.draw(self.game_screen)

			enemy_0.move(self.width)
			enemy_0.draw(self.game_screen)

			# End game if collision between you and enemy or treasure
			if player_character.detect_collision(enemy_0):
				is_game_over = True
				did_win = False
				text = font.render('You lose!', True, BLACK_COLOR)
				self.game_screen.blit(text, (275, 350))
				pygame.display.update()
				clock.tick(1)
				break
			elif player_character.detect_collision(treasure):
				is_game_over = True
				did_win = True
				text = font.render('You win!', True, BLACK_COLOR)
				self.game_screen.blit(text, (275, 350))
				pygame.display.update()
				clock.tick(1)
				break

			# Update all game graphics
			pygame.display.update()
			# Tick the clock to update everything within the game
			clock.tick(self.TICK_RATE)

		# Restart game loop if we won
		# Break out of game loop and quit if we lose
		if did_win:
			self.run_game_loop()
		else:
			return


class GameObject:

	def __init__(self, image_path, x, y, width, height):
		# Load the player image from the file directory
		object_image = pygame.image.load(image_path)
		# Scale the image up
		self.image = pygame.transform.scale(object_image, (width, height))

		self.x_pos = x
		self.y_pos = y
		self.width = width
		self.height = height

	# Draw the object by blitting it onto the background (game screen)
	def draw(self, background):
		background.blit(self.image, (self.x_pos, self.y_pos))


# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

	# How many tiles the character moves per second
	SPEED = 10

	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)

	# Move function will move character up if direction > 0 and down if < 0
	def move(self, direction, max_height):
		if direction > 0:
			self.y_pos -= self.SPEED
		elif direction < 0:
			self.y_pos += self.SPEED
		# Make sure the character never goes past the bottom of the screen
		if self.y_pos >= max_height - 40:
			self.y_pos - max_height - 40

	# Return False (no collision) if x positions and y poistions do not overlap
	# Return True if x and y positions overlap
	def detect_collision(self, other_body):
		# Check if objects are on the same vertical plane
		if self.y_pos > other_body.y_pos + other_body.height:
			return False
		elif self.y_pos + self.height < other_body.y_pos:
			return False
		# Check if objects are on the same horizontalal plane
		if self.x_pos > other_body.x_pos + other_body.width:
			return False
		elif self.x_pos + self.width < other_body.x_pos:
			return False
		# If all above checks fail, collision has happened so return True
		return True


# Class to represent the enemies moving left to right and right to left
class NonPlayerCharacter(GameObject):

	# How many tiles the enemy moves per second
	SPEED = 10

	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)

	# Move function will move enemy right once it hits far left of the
	# screen and left once it hits the far right of the screen
	def move(self, max_width):
		if self.x_pos <= 20:
			self.SPEED = abs(self.SPEED)
		elif self.x_pos >= max_width - 40:
			self.SPEED = -abs(self.SPEED)
		self.x_pos += self.SPEED
		


# Initilise pygame
pygame.init()

# Initialise the game class
new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
# Call the run_game_loop method of the Game class to run the game
new_game.run_game_loop()


# Quit pygame and the program
pygame.quit()
quit()


# Draw a rectangle on top of the game screen canvas (x, y, width, height)
			#pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
			# Draw a circle on top of the game screen (x, y, radius)
			#pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)
			#game_screen.blit(player_image, (375, 375))
