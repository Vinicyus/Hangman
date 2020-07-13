import pygame
import os
import math
import random
 
pygame.init()

#display
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
programIcon = pygame.image.load("hangman.png")
pygame.display.set_icon(programIcon)

#button
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH -(RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
	x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
	y = starty + ((i // 13) * (GAP + RADIUS * 2))
	letters.append([x, y, chr(A + i), True])

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicsans',70)

#images
images = []
for i in range(7):
	images.append(pygame.image.load("hangman" + str(i) + ".png"))

#variables
words = ["HELLO", "PYTHON", "PYGAME", "TEST", "DEVELOPER", "BOTTLE", "MOUSE", "COMPUTER", "SCREEN", "MAN", "WOMAN", "PHONE", "KEYBOARD", "COLOR", "RICE", "MAGIC",
"GAME", "CAMERA", "MIRROR", "DOOR", "GLASSES", "WIRE", "LOVE", "HATE", "PHILOSOPHY", "STONE", "BOOK", "GLASS", "HOUSE", "SHIP", "GOLD", "SILVER", "SCIENCE", "ALCHEMY",
"HONEST", "APPEARANCE", "PROPERTY", "TRANSFORM", "DIFFERENT", "NEED", "RUN", "FUNNY", "ANSWER", "INDUSTRY", "ACTUALLY", "FANCY", "PERHAPS", "MAYBE", "SORT", "HACK"]
word = random.choice(words)


#colors
white = (255,255,255)
black = (0,0,0)


def draw():
	win.fill(white)
	#draw title
	text = TITLE_FONT.render("HANGMAN!", 1, black)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

	#draw word
	display_word = ""
	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "
	text = WORD_FONT.render(display_word, 1, black)
	win.blit(text, (400, 200))


	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win, black, (x, y), RADIUS, 3)
			text = LETTER_FONT.render(ltr, 1, black)
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

	win.blit(images[hangman_status], (150,100))
	pygame.display.update()


def display_message(message):
	pygame.time.delay(1000)
	gameOver = True
	while gameOver:
		win.fill(white)
		text = WORD_FONT.render(message, 1, black)
		press_Q = WORD_FONT.render("Press Q to quit!", 1, black)
		press_P = WORD_FONT.render("Press P to play it again!", 1, black)
		win.blit(text, (WIDTH/2 - text.get_width()/2, (HEIGHT/2 - text.get_height()/2) - 100))
		win.blit(press_Q, (WIDTH/2 - press_Q.get_width()/2, (HEIGHT/2 - press_Q.get_height()/2) - 50))
		win.blit(press_P, (WIDTH/2 - press_P.get_width()/2, HEIGHT/2 - press_P.get_height()/2))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
				if event.key == pygame.K_p:
					main()

def main():
	global hangman_status
	global word
	global words
	global guessed

	FPS = 60
	clock = pygame.time.Clock()
	run = True
	hangman_status = 0
	word = random.choice(words)
	guessed = []
	for letter in letters:
		letter[3] = True

	draw()


	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				for letter in letters:
					x, y, ltr, visible = letter
					if visible:
						dis = math.sqrt((x - m_x)**2 + (y -m_y)**2)
						if dis < RADIUS:
							letter[3] = False
							guessed.append(ltr)
							if ltr not in word:
								hangman_status += 1

		draw()

		won = True
		for letter in word:
			if letter not in guessed:
				won = False
				break

		if won:
			display_message("You Won!") 
			break
			
		
		if hangman_status == 6:
			display_message("You lost!")
			break
		
main()
pygame.quit()