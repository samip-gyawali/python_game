import pygame, sys, random

class game_object():
    def __init__(self,objType,position,image):
        self.image = pygame.image.load(f"./images/{image}")
        self.rect = self.image.get_rect()
        self.rect.right = position[0]
        self.rect.top = position[1]
        self.moveLeft = False
        self.moveRight = False
        self.type = objType
        self.deleted = False
        objects.append(self)
        

    def delete(self):
        self.image = pygame.image.load('./images/empty.png')
        
        if self.type == 'enemy':
            enemies.pop(enemies.index(self))

        self.deleted = True

objects = []
bullets = []
enemies = []

def createBullets():
    newBullet = game_object('bullet',[space_ship.rect.right-6,768//1.5],'shot.png')
    bullets.append(newBullet)

def createEnemy():
    randomXCoordinate = random.randint(1,272) * 5
    newEnemy = game_object('enemy',[randomXCoordinate,50],'enemy.png')
    enemies.append(newEnemy)

def gameLogic():
    global gameOver
    for bullet in  bullets:
        for enemy in enemies:
            if pygame.Rect.colliderect(bullet.rect,enemy.rect):
                enemy.delete()
                bullet.delete()


def main():
    global screen, space_ship, enemyPresent
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == enemyCreateEvent : createEnemy()

        if event.type == logicEvent: gameLogic()
        
        if event.type == moveEvent:
            for enemy in enemies:
                enemy.rect.bottom += 10

        if event.type == pygame.KEYDOWN:
            key_pressed = event.key

            if key_pressed == pygame.K_RIGHT or key_pressed == pygame.K_d:
                space_ship.moveLeft = False
                space_ship.moveRight = True
            
            elif key_pressed == pygame.K_LEFT or key_pressed == pygame.K_a:
                space_ship.moveRight = False
                space_ship.moveLeft = True

            if key_pressed == pygame.K_f:
                createBullets()

        if event.type == pygame.KEYUP:
            key_removed = event.key

            if key_removed == pygame.K_RIGHT or key_removed == pygame.K_d:
                space_ship.moveRight = False
            
            elif key_removed == pygame.K_LEFT or key_removed == pygame.K_a:
                space_ship.moveLeft = False

    
    if space_ship.moveRight:
        space_ship.rect.left += 3
    
    if space_ship.moveLeft:
        space_ship.rect.left -= 3

    if space_ship.rect.left < 5:
        space_ship.rect.left = 5
    
    if space_ship.rect.right > 1360:
        space_ship.rect.right = 1360

    for bullet in bullets:
        bullet.rect.bottom -= 1
        if bullet.rect.top < 0:
            bullets.pop(bullets.index(bullet))
            bullet.delete()
    
    
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for obj in objects:
        screen.blit(obj.image,obj.rect)
        
    pygame.display.flip()


screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Protect the Earth")
background = pygame.image.load('./images/bg.jpg')
space_ship = game_object('space-ship',[5,768//1.5],'spaceship.png')
gameOver = False
enemyPresent = False

enemyCreateEvent = pygame.USEREVENT + 1
logicEvent = pygame.USEREVENT + 2
moveEvent = pygame.USEREVENT + 3

pygame.time.set_timer(enemyCreateEvent, 3000)
pygame.time.set_timer(moveEvent, 100)
pygame.time.set_timer(logicEvent,50)

createEnemy()

while not gameOver:
    main()