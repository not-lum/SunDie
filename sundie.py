import pygame

WIDTH = 800
HEIGHT = 500
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

r = 0
g = 0
b = 0

x = WIDTH // 2
y = HEIGHT // 2 - 100

x2 = WIDTH // 2 + 100
y2 = HEIGHT // 2 - 100

r2 = 255
g2 = 255
b2 = 255


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Sundie")
clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 80)
text = font.render("The Sundie", 1, BLACK)
place = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))

move = True
run = True
move2 = False
while run:
	screen.blit(text, place)
	pygame.display.update()
	clock.tick(10)

	r += 11
	g += 11
	b += 11

	if r > 255:
		r = 255
	if g > 255:
		g = 255
	if b > 255:
		b = 255

	text = font.render("The Sundie", 1, (r, g, b))
	pygame.display.update()





	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((r2, g2, b2))
	clock.tick(FPS)
	pygame.draw.circle(screen, WHITE, (x, y), 50)
	pygame.draw.circle(screen, (r2, b2, g2), (x2, y2), 45)
	if move:
		r2 -= 7
		g2 -= 7
		b2 -= 7
		x2 -= 1

		if r2 < 0:
			r2 = 0
		if g2 < 0:
			g2 = 0
		if b2 < 0:
			b2 = 0

		if x2 == x:
			move = False
			pygame.time.delay(1000)
			move2 = True
	if move2:
		r2 += 7
		g2 += 7
		b2 += 7
		x2 -= 1

		if r2 > 255:
			r2 = 255
		if g2 > 255:
			g2 = 255
		if b2 > 255:
			b2 = 255
		if r2 == 255 and g2 == 255 and b2 == 255:
			font = pygame.font.SysFont('Verdana', 50)
			text = font.render("Thanks for watching!", 1, BLACK)
			place = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))


	pygame.display.update()
