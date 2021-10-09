import pygame,sys
from banner import Tool
from words import Words

pygame.init()

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('Typing Maniac')
clock = pygame.time.Clock()
tool = Tool(screen)
user_input = ''
word = pygame.sprite.Group()
score = 0
words = []
life = 10
powerup = 0
running = True
speed = 1

spawn_word = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_word,1000)

power = pygame.USEREVENT + 2
pygame.time.set_timer(power,2000)

speedup_timer = pygame.USEREVENT + 2
pygame.time.set_timer(speedup_timer,2000)

def submit(input):
	global score
	for i in word.sprites():
		if input == i.word:
			score += 1
			words.remove(i.word)
			i.kill()

def speedup():
	global speed
	speed += 0.1
	for i in word.sprites():
		i.speed = speed


def activate_power():
	global score
	count = 0
	for i in word.sprites():
		if i.rect.y < 600:
			count += 1
	score += count

def gameover():
	gameover = tool.text_font.render('GAME OVER',True, 'Yellow')
	gameover_rect = gameover.get_rect(center = (250,350))
	screen.blit(gameover,gameover_rect)
	word.empty()

while True:
	for event in pygame.event.get():	
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if event.type == spawn_word:
			Word = Words(screen,speed)
			word.add(Word)
			words.append(Word.word)

		if event.type == power:
			powerup += 1

		if event.type == speedup_timer:
			if speed < 4:
				speedup()

		if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			if powerup != 5:
				user_input = ''
				score = 0
				life = 10
				speed = 1
				running = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSPACE:
				user_input = user_input[:-1]

			elif event.key == pygame.K_RETURN:
				submit(user_input)
				user_input = ''

			elif event.key == pygame.K_SPACE:
				if powerup == 5:
					activate_power()
					powerup = 0

			else:
				user_input += event.unicode

	if running:
		screen.fill('Black')

		word.draw(screen)
		word.update()

		tool.show_banner()
		tool.display_score(score,tool.get_hs(),powerup)
		tool.user_type(user_input)
		tool.textbox()
		tool.save_highscore(score,tool.get_hs())
		tool.display_life(life)
		for i in word.sprites():
			if i.rect.y < 0:
				life -= 1
				i.kill()

		if life == 0:
			running = False
	else:
		gameover()



	pygame.display.flip()
	clock.tick(60)