import sys, pygame, random
from random import randint

WIDTH = 800
HEIGHT = 650
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Casino")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_score_fond_bar(surface, x, y):
	BAR_LENGHT = 160
	BAR_HEIGHT = 35
	fill = BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLACK, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_credit_fond_bar(surface, x, y):
	BAR_LENGHT = 160
	BAR_HEIGHT = 35
	fill = BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLACK, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Box1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[4] # squirtle
		#self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 240
		self.rect.centery = 250

	def update(self):

		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			num1 = randint(1,15)
			if num1 == 1:
				self.image = box_images[5] # 7
			if num1 == 2:
				self.image = box_images[1] # pokeb
			if num1 >= 3 and num1 <= 5:
				self.image = box_images[0] # cherry
			if num1 >= 6 and num1 <= 9:
				self.image = box_images[2] # pika
			if num1 >= 10 and num1 <= 12:
				self.image = box_images[3] # star
			if num1 >= 13:
				self.image = box_images[4] # squirtle
			
class Box2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[2] # pika
		#self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 400
		self.rect.centery = 250

	def update(self):

		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			num2 = randint(1,15)
			if num2 == 1:
				self.image = box_images[5] # 7
			if num2 == 2:
				self.image = box_images[1] # pokeb
			if num2 >= 3 and num2 <= 5:
				self.image = box_images[0] # cherry
			if num2 >= 6 and num2 <= 9:
				self.image = box_images[2] # pika
			if num2 >= 10 and num2 <= 12:
				self.image = box_images[3] # star
			if num2 >= 13:
				self.image = box_images[4] # squirtle

class Box3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[3] # star
		#self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 560
		self.rect.centery = 250

	def update(self):

		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			num3 = randint(1,15)
			if num3 == 1:
				self.image = box_images[5] # 7
			if num3 == 2:
				self.image = box_images[1] # pokeb
			if num3 >= 3 and num3 <= 5:
				self.image = box_images[0] # cherry
			if num3 >= 6 and num3 <= 9:
				self.image = box_images[2] # pika
			if num3 >= 10 and num3 <= 12:
				self.image = box_images[3] # star
			if num3 >= 13:
				self.image = box_images[4] # squirtle

		
def show_go_screen():
	
	screen.fill(BLACK)#background, [0,0])
	draw_text(screen, "Casino", 65, WIDTH // 2, HEIGHT // 4)
	draw_text(screen, "Cherry en primera casilla  =>  10 pts.", 20, WIDTH // 2, HEIGHT * 3/7)
	draw_text(screen, "3 figuras iguales  =>  100 pts.", 20, WIDTH // 2, HEIGHT * 4/8)
	draw_text(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 625)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

box_images = []
box_list1 = ["img/cherry.png", "img/pokeb.png", "img/pika.png", "img/st.png",
				"img/sq.png" , "img/7.png"]

for img in box_list1:
	box_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(85,85)))

background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(800,650))

game_over = True
running = True
while running:
	if game_over:
		show_go_screen()
		game_over = False
		screen.blit(background, [0,0])
		all_sprites = pygame.sprite.Group()
		box1 = Box1()
		box2 = Box2()
		box3 = Box3()
		all_sprites.add(box1, box2, box3)	
		scounter = True
		counter = True
		score = 50
		payout = 0

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
	
	if score == 0:
		game_over =True 
	
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_f]:
		if scounter:
			score -= 1
			payout = 0
			scounter = False
		counter = True
	elif not keystate[pygame.K_f]:
		scounter = True
		if counter:
			if box1.image == box2.image == box3.image == box_images[0]: # cherry
				score += 6
				payout = 6
				counter = False
			elif box1.image == box2.image == box3.image == box_images[2]: # pika
				score += 8
				payout = 8
				counter = False
			elif box1.image == box2.image == box3.image == box_images[4]: # squirtle
				score += 10
				payout = 10
				counter = False
			elif box1.image == box2.image == box3.image == box_images[3]: # star
				score += 15
				payout = 15
				counter = False
			elif box1.image == box2.image == box3.image == box_images[1]: # pokeb
				score += 50
				payout = 50
				counter = False
			elif box1.image == box2.image == box3.image == box_images[5]: #  7
				score += 300
				payout = 300
				counter = False
				
	all_sprites.update()

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	draw_score_fond_bar(screen, 201,36)
	draw_credit_fond_bar(screen, 440,36)
	draw_text(screen, str(score), 35, 280, 37)
	draw_text(screen, str(payout), 35, 520, 37)

	pygame.display.flip()