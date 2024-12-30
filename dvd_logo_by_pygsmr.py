import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncing DVD Logos')

# DVD logo dimensions
logo_width, logo_height = 50, 25

# Colors
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

# Directions
RIGHT = 'right'
LEFT = 'left'
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (RIGHT, LEFT, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

class DVDLogo:
    def __init__(self):
        self.color = random.choice(colors)
        self.x = random.randint(0, width - logo_width)
        self.y = random.randint(0, height - logo_height)
        self.direction = random.choice(DIRECTIONS)
        self.speed = 2  # Adjust speed as needed

    def update(self):
        if self.direction == RIGHT:
            self.x += self.speed
        elif self.direction == LEFT:
            self.x -= self.speed
        elif self.direction == UP_RIGHT:
            self.x += self.speed
            self.y -= self.speed
        elif self.direction == UP_LEFT:
            self.x -= self.speed
            self.y -= self.speed
        elif self.direction == DOWN_RIGHT:
            self.x += self.speed
            self.y += self.speed
        elif self.direction == DOWN_LEFT:
            self.x -= self.speed
            self.y += self.speed

        # Bounce off edges and change color
        if self.x <= 0 and (self.direction == LEFT or self.direction == UP_LEFT or self.direction == DOWN_LEFT):
            self.direction = RIGHT
            self.color = random.choice(colors)  # Change color on left bounce
        elif self.x >= width - logo_width and (self.direction == RIGHT or self.direction == UP_RIGHT or self.direction == DOWN_RIGHT):
            self.direction = LEFT
            self.color = random.choice(colors)  # Change color on right bounce
        if self.y <= 0:
            self.direction = DOWN_RIGHT if 'U' in self.direction else DOWN_LEFT
        elif self.y >= height - logo_height:
            self.direction = UP_RIGHT if 'D' in self.direction else UP_LEFT

    def draw(self):
        # Draw the "DVD" text
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render("DVD", True, self.color)
        text_rect = text_surface.get_rect(center=(self.x + logo_width // 2, self.y + logo_height // 2))
        screen.blit(text_surface, text_rect)

# Create a list of DVD logos
logos = [DVDLogo() for _ in range(115)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update and draw logos
    for logo in logos:
        logo.update()
        logo.draw()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()