import random
import sys
import pygame
pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN =  (0,255,0)
BLACK = (0,0,0)
BALLCOLOR =(255,59,0)
PAD1COLOR = (1,144,255)
PAD2COLOR = (137, 36, 253)
BACKGROUNDCOLOR = (168,168,173)
BALLCOLORMOD = (255,59,0)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT=(900,600) # multiple declatration
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BACKGROUNDCOLOR)

ball_centre = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2) #block to draw ball
ball_radius = 20
ball = pygame.draw.circle(screen, BALLCOLOR, ball_centre, ball_radius)

PADDLE_LENGTH = 100
PADDLE_WIDTH = 10

paddle_1_top = (4, (SCREEN_HEIGHT/2)- (PADDLE_LENGTH/2)) #block to draw paddle1
paddle_1_bottom = (4,(SCREEN_HEIGHT/2)+ (PADDLE_LENGTH/2))
paddle1 = pygame.draw.line(screen, PAD1COLOR, paddle_1_top, paddle_1_bottom, PADDLE_WIDTH)

paddle_2_top = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2)- (PADDLE_LENGTH/2)) #block to draw paddle2
paddle_2_bottom = (SCREEN_WIDTH-4, (SCREEN_HEIGHT/2)+ (PADDLE_LENGTH/2))
paddle2 = pygame.draw.line(screen, PAD2COLOR, paddle_2_top, paddle_2_bottom, PADDLE_WIDTH)

boundry1 = pygame.draw.line(screen, PAD1COLOR, (10,0), (10,SCREEN_HEIGHT),2) #block to boundaries
boundry2 = pygame.draw.line(screen, PAD2COLOR, (SCREEN_WIDTH-10,0), (SCREEN_WIDTH-10, SCREEN_HEIGHT),2)


ball_velocity = [random.choice([-1,1]), random.choice(range(-10,10))] #initial velocity declarations
paddle1_velocity = (0,0)
paddle2_velocity = (0,0)

def get_new_position(pos, vel): #funtion defined to calculate new ball position based on current pos and vel
	return (pos[0]+vel[0], pos[1]+vel[1])

while True: # infinite loop to ensure window stays and update postion of ball according to function get_new_position
	pygame.time.Clock().tick(60) #to slow down movement of ball

	if ball_centre[0] - ball_radius < 14:
		if (ball_centre[1]+ball_radius > paddle_1_top[1] and ball_centre[1]-ball_radius < paddle_2_bottom[1]):
			ball_velocity[0]= -ball_velocity[0]
			BALLCOLORMOD = PAD1COLOR
		else:
			ball = pygame.draw.circle(screen ,BACKGROUNDCOLOR, ball_centre, ball_radius)
			ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

			ball_velocity = [random.choice([-1,1]), random.choice(range(-10,10))]
			BALLCOLORMOD = BALLCOLOR

	elif ball_centre[0] + ball_radius > SCREEN_WIDTH-14:
		if (ball_centre[1]+ball_radius > paddle_2_top[1] and ball_centre[1]-ball_radius < paddle_2_bottom[1] ):
			ball_velocity[0]= -ball_velocity[0]
			BALLCOLORMOD = PAD2COLOR
		else:
			ball = pygame.draw.circle(screen ,BACKGROUNDCOLOR, ball_centre, ball_radius)
			ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
			ball_velocity = [random.choice([-1,1]), random.choice(range(-10,10))]
			BALLCOLORMOD = BALLCOLOR
	if ball_centre[1]-ball_radius < 0 or ball_centre[1]+ball_radius > SCREEN_HEIGHT:
		ball_velocity[1]= -ball_velocity[1]

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYDOWN :
			if event.key == pygame.K_w :
				paddle1_velocity = (0,-3)
			elif event.key == pygame.K_s :
				paddle1_velocity = (0,3)
		elif event.type == pygame.KEYUP :
			if event.key == pygame.K_w or event.key == pygame.K_s :
				paddle1_velocity = (0,0)

	if ball_velocity[0] == -1:
		if (paddle_2_top[1]+paddle_2_bottom[1])/2 < (SCREEN_HEIGHT/2):
			paddle2_velocity = (0,4)   #4 is given arbitrarily, just for the paddle to catch up with the ball
		elif (paddle_2_top[1]+paddle_2_bottom[1])/2 > (SCREEN_HEIGHT/2):
			paddle2_velocity = (0,-4)
#	if the ball moving towards paddle2, track its movement.
	elif ball_velocity[0] == 1:
		if (paddle_2_top[1]+paddle_2_bottom[1])/2 < ball_centre[1]:
			paddle2_velocity = (0,4)
		else:
			paddle2_velocity = (0,-4)

	ball = pygame.draw.circle(screen ,BACKGROUNDCOLOR, ball_centre, ball_radius) # erasing ball at previous position
	paddle1 = pygame.draw.line(screen, BACKGROUNDCOLOR, paddle_1_top, paddle_1_bottom, PADDLE_WIDTH)
	paddle2 = pygame.draw.line(screen, BACKGROUNDCOLOR, paddle_2_top, paddle_2_bottom, PADDLE_WIDTH)

	ball_centre = get_new_position(ball_centre,ball_velocity) #calculate new ball position based on current pos and vel
	paddle_1_new_top = get_new_position(paddle_1_top, paddle1_velocity)
	paddle_1_new_bottom = get_new_position(paddle_1_bottom, paddle1_velocity)
	paddle_2_new_top = get_new_position(paddle_2_top,paddle2_velocity)
	paddle_2_new_bottom = get_new_position(paddle_2_bottom,paddle2_velocity)

	if (paddle_2_new_top[1] > 0 and paddle_2_new_bottom[1] < SCREEN_HEIGHT) :
		paddle_2_top = paddle_2_new_top
		paddle_2_bottom = paddle_2_new_bottom
	if (paddle_1_new_top[1] > 0 and paddle_1_new_bottom[1] < SCREEN_HEIGHT) :
		paddle_1_top = paddle_1_new_top
		paddle_1_bottom = paddle_1_new_bottom
	#screen.fill(BACKGROUNDCOLOR) # to erase previous stuff
	#paddle1 = pygame.draw.line(screen, PAD1COLOR, paddle_1_top, paddle_1_bottom, PADDLE_WIDTH) # drawing erased stuff again
	#paddle2 = pygame.draw.line(screen, PAD2COLOR, paddle_2_top, paddle_2_bottom, PADDLE_WIDTH)
	#boundry1 = pygame.draw.line(screen, PAD1COLOR, (10,0), (10,SCREEN_HEIGHT),2)
	#boundry2 = pygame.draw.line(screen, PAD2COLOR, (SCREEN_WIDTH-10,0), (SCREEN_WIDTH-10, SCREEN_HEIGHT),2)
	ball = pygame.draw.circle(screen ,BALLCOLORMOD, ball_centre, ball_radius) # drawing ball at updated position
	paddle1 = pygame.draw.line(screen, PAD1COLOR, paddle_1_top, paddle_1_bottom, PADDLE_WIDTH)
	paddle2 = pygame.draw.line(screen, PAD2COLOR, paddle_2_top, paddle_2_bottom, PADDLE_WIDTH)

	#if (ball_centre[0]+ ball_radius >SCREEN_WIDTH-12) :
	#	if (ball_centre[1]+ball_radius > paddle_2_top[1] and ball_centre[1]-ball_radius < paddle_2_bottom[1]):
	#		ball_velocity[0]= -ball_velocity[0]
	#	else:
	#		ball_center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	#		ball_velocity = [random.choice([-1,1]), random.choice(range(-10,10))]


	#if (ball_centre[0]- ball_radius <12) :
	#	if (ball_centre[1]+ball_radius > paddle_1_top[1] and ball_centre[1]-ball_radius < paddle_2_bottom[1]):
	#		ball_velocity[0]= -ball_velocity[0]
	#	else:
	#		ball_center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	#		ball_velocity = [random.choice([-1,1]), random.choice(range(-10,10))]

	pygame.display.update()
	


