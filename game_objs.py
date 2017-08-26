import pygame, sys, random

class Helicoptor (pygame.sprite.Sprite):
	def __init__(self, color):
		super(Helicoptor, self).__init__()
		self.color = color
		self.radius = 20
		self.image = pygame.Surface((self.radius*2,self.radius*2))
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.center = (60,350)

	def update(self, dy):
		self.yPos += dy

class Obstacle (pygame.sprite.Sprite):
	def __init__(self, color):
		super(Obstacle,self).__init__()
		self.color = color
		self.width = 40
		self.height = random.randint(50,600)
		self.image = pygame.Surface((self.width,self.height))
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.center = (700-self.width/2,random.choice([self.height/2,700-self.height/2]))

	def update(self):
		self.rect.x -= 5


