import pygame


class Tool:
	def __init__(self,surface):
		self.screen = surface
		self.text_font = pygame.font.Font(None,40)
		self.score_font = pygame.font.Font(None,25)
		self.txt = None
		self.txt_rect = None

	def show_banner(self):
		banner = pygame.Surface((500,70))
		banner.fill('White')
		self.screen.blit(banner,(0,0))

	def display_score(self,score,highscore,power):
		score_text = self.score_font.render(f'Score: {score}',True, 'Black')
		score_rect = score_text.get_rect(topleft = (10,5))
		self.screen.blit(score_text,score_rect)

		hs_text = self.score_font.render(f'Highscore: {highscore}',True, 'Black')
		hs_rect = hs_text.get_rect(topright = (490,5))
		self.screen.blit(hs_text,hs_rect)

		if power == 5:
			x = 'Ready!'
			color = 'Red'
		else:
			x = 'Not Ready'
			color = 'Black'

		power_text = self.score_font.render(f'Power',True, 'Black')
		power_rect = power_text.get_rect(topright = (475,25))
		self.screen.blit(power_text,power_rect)	

		power2_text = self.score_font.render(f'{x}',True, color)
		power2_rect = power2_text.get_rect(topright = (490,45))
		self.screen.blit(power2_text,power2_rect)	

	def display_life(self,life):
		life_text = self.score_font.render(f'Lives: {life}',True, 'Black')
		life_rect = life_text.get_rect(topleft = (10,25))
		self.screen.blit(life_text,life_rect)

	def user_type(self,user_input):
		self.txt = self.text_font.render(user_input,True, 'Black')
		# self.txt_rect = self.txt.get_rect(center = (250,35))
		box= self.textbox()
		self.screen.blit(self.txt,(box.x + 5, box.y + 10))

	def textbox(self):
		box_len = max(250,self.txt.get_width() + 10)
		box = pygame.Rect(120,10,box_len,50)
		# txtbox_rect = txtbox.get_rect(center = (250,35))
		pygame.draw.rect(self.screen,'Red',box,3)
		return box

	def get_hs(self):
		with open('highscore.txt','r') as f:
			saved_hs = f.readline()
			return int(saved_hs)

	def save_highscore(self,score,high_score):
		with open('highscore.txt','r+') as f:
			saved_hs = f.readline()
			if int(saved_hs) <= score >= high_score:
				high_score = score
				f.truncate(0)
				f.seek(0)
				f.write(str(high_score))
			else: 
				high_score = int(saved_hs)
		return high_score