import serial, pygame, sys
from game_objs import Helicoptor, Obstacle

#Pygame setup
pygame.init()

FPS = 35
fpsClock = pygame.time.Clock()

#Colors
BLACK = (  0,   0,   0, 255)
WHITE = (255, 255, 255, 255)
RED   = (255,   0,   0 , 255)
GREEN = (  0, 255,   0, 255)
BLUE  = (  0,   0, 255, 255)

#Screen
(width, height) = (700,800)
screen = pygame.display.set_mode((width,height))


#Serial setup
ser = serial.Serial('/dev/tty.usbmodem1411', 9600, timeout=1)
curr = 0.0
prev = 0.0

#Helicoptor initialization
heli = Helicoptor(GREEN)
helis = pygame.sprite.Group()
helis.add(heli)

#Block initialization
blocks = pygame.sprite.Group()
spawn_timer = 0.0

def blockHandler():
	for block in blocks:
		if pygame.sprite.collide_rect(heli,block):
			#End Game
			print("Collision")
		if block.rect.x <= 0:
			block.kill()


def readInput():
	val = ser.readline()
	if val != '':
		curr = float(val.strip('\n').strip('\r'))
        if prev == 0.0:
    		prev = curr
	return (curr-prev)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#Collision detection
	blockHandler()

	#Block spawn
	if spawn_timer == 35:
		blocks.add(Obstacle(RED))
		spawn_timer = 0
	
	spawn_timer += 1

	helis.update(readInput())
	blocks.update()
	screen.fill(BLACK)
	helis.draw(screen)
	blocks.draw(screen)
	pygame.display.update()
	fpsClock.tick(FPS)

