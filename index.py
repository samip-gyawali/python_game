import pygame,sys

class game_object(object):
    def __init__(self,speed,position,image):
        self.speed = speed
        self.position = position
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        

screen = pygame.display.set_mode((1366,768))
BALL = game_object([0,0],[0,0],'intro_ball.gif')
ball_rect= BALL.rect

screen.fill((0,0,0))
screen.blit(BALL.image, ball_rect)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            thisKey = pygame.key.get_pressed()
            if thisKey[pygame.K_UP]:
                BALL.speed[1] -= 1

            elif thisKey[pygame.K_DOWN]:
                BALL.speed[1] += 1

            elif thisKey[pygame.K_LEFT]:
                BALL.speed[0] -= 1
    
            elif thisKey[pygame.K_RIGHT]:
                BALL.speed[0] += 1
    

        if event.type == pygame.QUIT:
            sys.exit()


    if ball_rect.left < 0 or ball_rect.right > 1366:
        BALL.speed[0] = -BALL.speed[0]
    
    if ball_rect.top<0 or ball_rect.bottom > 768:
        BALL.speed[1] = -BALL.speed[1]

    ball_rect = ball_rect.move(BALL.speed)
    screen.fill((0,0,0))
    screen.blit(BALL.image, ball_rect)
    pygame.display.flip()