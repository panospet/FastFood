import pygame, sys

pygame.init()

background = pygame.image.load("a.jpg")
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)
running = 1

pygame.display.set_caption('Basic Pygame program')

clock = pygame.time.Clock()
fps = 24 
five_sec = fps * 5
totalframes = 0

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		pygame.quit()
		running = 0
	screen.blit(background, backgroundRect)
	pygame.display.flip()

	clock.tick(fps)
	totalframes += 1 	# totalframes counting inside while loop.

	if totalframes == five_sec:
		background = pygame.image.load("b.jpg")
		backgroundRect = background.get_rect()
		font = pygame.font.Font(None, 90)
		text = font.render("Hello There", 1, (10, 10, 10))
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx
		background.blit(text, textpos)
	elif totalframes == (five_sec*2):
		running = 0