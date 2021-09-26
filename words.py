import pygame
from random import randint

class Words(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.font = pygame.font.Font(None,30)
		self.screen = screen
		self.word = ''
		self.image = self.font.render(self.get_word(),True, 'White')
		self.rect = self.image.get_rect(center = (randint(100,450),randint(605,630)))

	def get_word(self):
		with open('wordlist.10000.txt','r') as txt:
			words = txt.read().splitlines()
		self.word = words[randint(0,10000)]
		return self.word

	def move(self):
		self.rect.y -= 2

	def destroy(self):
		if self.rect.y < -2:
			self.kill()

	def update(self):
		self.move()
		self.destroy()


