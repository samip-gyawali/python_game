import pygame, sys, random, os

pygame.font.init()

class game_object():
    def __init__(self,objType,position,image):
        self.image = pygame.image.load(f"./images/{image}")
        self.rect = self.image.get_rect()
        self.rect.centerx = position[0]
        self.rect.top = position[1]
        self.moveLeft = False
        self.moveRight = False
        self.type = objType
        self.deleted = False
        objects.append(self)
        

    def delete(self):
        self.image = pygame.image.load('./images/empty.png')
        objects.pop(objects.index(self))
        if self.type == 'enemy':
            enemies.pop(enemies.index(self))

        if self.type == 'bullet':
            bullets.pop(bullets.index(self))
            
        self.deleted = True

objects = [] # stores every single game object
bullets = [] # stores game_objects that are bullets
enemies = [] # stores game_objects that are enemies
currentSelect = 'launch' # stores which one of the options is currently selected
pauseSelect = 'resume'
life = 5
score = 0

def createBullets():
    newBullet = game_object('bullet',[space_ship.rect.centerx,768//1.5],'shot.png')
    bullets.append(newBullet)

def createEnemy():
    randomXCoordinate = random.randint(1,272) * 5
    newEnemy = game_object('enemy',[randomXCoordinate,50],'enemy.png')
    enemies.append(newEnemy)

def gameLogic():
    global gameOver, life, score, enemyCreateTime, makeGameHarder
    for enemy in enemies:
        if pygame.Rect.colliderect(enemy.rect, space_ship.rect):
            gameOver = True

    for bullet in  bullets:
        for enemy in enemies:
            if pygame.Rect.colliderect(bullet.rect,enemy.rect):
                # pygame.event.post(enemyDestroyEvent)
                enemy.delete()
                bullet.delete()
                score += 10
                makeGameHarder += 10
                if score > 0 and makeGameHarder%40 == 0:
                    makeGameHarder = 0
                    enemyCreateTime = round(int(enemyCreateTime/1.1),-2)
                    pygame.time.set_timer(enemyCreateEvent, enemyCreateTime)

                changeScore()

def drawInitialScreen():
    global screen, currentSelect
    # font definition
    gameFont = pygame.font.Font('./fonts/earth.otf',25)
    nameFont = pygame.font.Font('./fonts/evil_empire.ttf', 70)
    normalText = pygame.font.Font('./fonts/normal.ttf',30)
    launchColor = (255,255,255)
    settingsColor = (255,255,255)
    exitColor = (255,255,255)

    if currentSelect == 'launch':
        launchColor = (0,255,128)
    elif currentSelect == 'settings':
        settingsColor = (0,255,128)
    elif currentSelect == 'exit':
        exitColor = (0,255,128)


    texts = [
        {"content": (nameFont.render("""COSMIC COMBAT""", True, (0,128,255))), "position": (1366//2,100)},
        {"content": (normalText.render("""SEARGENT, AN ALIEN INVASION IS HAPPENING! IT'S YOUR DUTY""",True, (255,255,255))), "position":(1366//2,200)},
        {"content": (normalText.render("""TO SAVE THE EARTH. HURRY, LAUNCH YOUR SPACESHIP NOW""",True, (255,255,255))), "position":(1366//2, 230)},
        {"content": (gameFont.render("""Created © by Samip Gyawali 2023""", True, (255,255,255))), "position":(1366//2,700)}
    ]

    buttons = [
        {"content": (gameFont.render("""LAUNCH""", True, launchColor)), "position": (1366//2,350)},
        {"content": (gameFont.render("""SETTINGS""",True, settingsColor)), "position":(1366//2,400)},
        {"content": (gameFont.render("""EXIT""", True, exitColor)), "position": (1366//2,450)}
    ]

    screen.fill((0,0,0))
    for text in texts:
        text_rect = text['content'].get_rect()
        text_rect.center = text['position']
        screen.blit(text['content'],text_rect)

    for button in buttons:
        button_rect = button['content'].get_rect()
        button_rect.center = button['position']
        screen.blit(button['content'],button_rect)
    
    pygame.display.flip()

def setHighScore():
    global score,highScore,newHighScore
    if score > highScore:
        newHighScore = True
        with open('high_score.txt','w') as writeFile:
            writeFile.write(str(score))
    
def gameInit():
    global currentSelect, gameStart

    drawInitialScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            thisKey = event.key
            if currentSelect == 'launch':
                if thisKey == pygame.K_UP:
                    currentSelect = 'exit'
                elif thisKey == pygame.K_DOWN:
                    currentSelect = 'settings'
                elif thisKey == pygame.K_RETURN:
                    gameStart = True


            elif currentSelect == 'settings':
                if thisKey == pygame.K_UP:
                    currentSelect = 'launch'
                elif thisKey == pygame.K_DOWN:
                    currentSelect = 'exit'

            elif currentSelect == 'exit':
                if thisKey == pygame.K_UP:
                    currentSelect = 'settings'
                elif thisKey == pygame.K_DOWN:
                    currentSelect = 'launch'
                elif thisKey == pygame.K_RETURN:
                    sys.exit()
            
            drawInitialScreen()

def pause():
    global screen, pauseSelect
    drawPauseScreen()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key_pressed = event.key
                if key_pressed == pygame.K_ESCAPE:
                    paused = False
                
                elif key_pressed == pygame.K_DOWN:
                    if pauseSelect == 'resume':
                        pauseSelect = 'settings'
                    elif pauseSelect == 'settings':
                        pauseSelect = 'exit'
                    elif pauseSelect == 'exit':
                        pauseSelect = 'resume'
                
                elif key_pressed == pygame.K_UP:
                    if pauseSelect == 'resume':
                        pauseSelect = 'exit'
                    elif pauseSelect == 'settings':
                        pauseSelect = 'resume'
                    elif pauseSelect == 'exit':
                        pauseSelect = 'settings'
                
                elif key_pressed == pygame.K_RETURN:
                    if pauseSelect == 'resume':
                        paused = False
                    elif pauseSelect =='settings':
                        paused = False
                    elif pauseSelect == 'exit':
                        sys.exit()
                drawPauseScreen()
                                
def drawPauseScreen():
    global screen, pauseSelect
    gameFont = pygame.font.Font('./fonts/earth.otf',25)
    pauseFont = pygame.font.Font('./fonts/evil_empire.ttf', 70)

    resumeColor = (255,255,255)
    settingsColor = (255,255,255)
    exitColor = (255,255,255)

    if(pauseSelect == 'resume'):
        resumeColor = (0,255,128)
    elif pauseSelect == 'settings':
        settingsColor = (0,255,128)
    elif pauseSelect == 'exit':
        exitColor = (0,255,128)

    
    pauseText = {"content":pauseFont.render("Paused",True,(255,255,255)),"position":(1366//2,200)}
    pauseButtons = [
        {"content":gameFont.render("Resume",True,resumeColor),"position":(1366//2,300)},
        {"content":gameFont.render("Settings",True,settingsColor),"position":(1366//2,350)},
        {"content":gameFont.render("Exit",True,exitColor),"position":(1366//2,400)}
    ]

    screen.fill((0,0,0))

    pauseText_rect = pauseText['content'].get_rect()
    pauseText_rect.center = pauseText['position']

    screen.blit(pauseText['content'],pauseText_rect)

    for button in pauseButtons:
        newButton = button['content']
        newButton_rect = newButton.get_rect()
        newButton_rect.center = button['position']
        screen.blit(newButton,newButton_rect)
        
    pygame.display.flip()

def changeScore():
    global screen, score, score_text, score_text_rect
    normalText = pygame.font.Font('./fonts/normal.ttf',20)
    score_text = normalText.render(f"Score : {score}", True, (255,255,255))
    score_text_rect = score_text.get_rect()
    score_text_rect.left = 10
    score_text_rect.top = 30
    
def changeLife():
    global screen, life, life_text, life_text_rect
    normalText = pygame.font.Font('./fonts/normal.ttf',20)
    life_text = normalText.render(f"Life : {life}", True, (255,255,255))
    life_text_rect = life_text.get_rect()
    life_text_rect.left = 10
    life_text_rect.top = 10

def final():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: sys.exit()

    screen.fill((0,0,0))
    drawExitScreen()

def drawExitScreen():
    global newHighScore, screen
    nameFont = pygame.font.Font('./fonts/evil_empire.ttf', 70)
    normalText = pygame.font.Font('./fonts/normal.ttf',30)
    gameFont = pygame.font.Font('./fonts/earth.otf',25)

    gameOverText = nameFont.render("Game Over",True,(255,255,255))
    gameOverText_rect = gameOverText.get_rect()
    gameOverText_rect.center= (1366//2,100)
    screen.blit(gameOverText,gameOverText_rect)

    if newHighScore:
        highScoreText = gameFont.render("New High Score Set",True,(255,255,255))
        highScoreText_rect = highScoreText.get_rect()
        highScoreText_rect.center = (1366//2,350)
        screen.blit(highScoreText,highScoreText_rect)
    
    finalTexts = [
        {'text': normalText.render("Well done, Seargent! You bought us some time. Reinforcements are on there way.",True,(255,255,255)),'position':(1366//2,200)},
        {'text': normalText.render("You can join them on a new spaceship if you want",True,(255,255,255)),'position':(1366//2,240)},
        {'text':normalText.render("Press Enter to exit",True,(255,255,255)),'position':(1366//2,450)},
        {'text': gameFont.render("""Created © by Samip Gyawali 2023""", True, (255,255,255)), 'position':(1366//2,700)}
        ]
    
    for finalText in finalTexts:
        finalText_rect = finalText['text'].get_rect()
        finalText_rect.center = finalText['position']
        screen.blit(finalText['text'],finalText_rect)

    pygame.display.flip()

def main():
    global screen, space_ship, enemyPresent, life, score
    normalText = pygame.font.Font('./fonts/normal.ttf',20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == enemyCreateEvent : createEnemy()

        if event.type == logicEvent: gameLogic()
        
        # if event.type == enemyDestroyed:
        #     createEnemy()

        if event.type == moveEvent:
            for enemy in enemies:
                enemy.rect.bottom += 10
                if enemy.rect.top > 768:
                    enemy.delete()
                    changeLife()
                    life -= 1

        if event.type == pygame.KEYDOWN:
            key_pressed = event.key

            if key_pressed == pygame.K_RIGHT or key_pressed == pygame.K_d:
                space_ship.moveLeft = False
                space_ship.moveRight = True
            
            elif key_pressed == pygame.K_LEFT or key_pressed == pygame.K_a:
                space_ship.moveRight = False
                space_ship.moveLeft = True

            elif key_pressed == pygame.K_f or key_pressed == pygame.K_SPACE:
                createBullets()
            
            elif key_pressed == pygame.K_ESCAPE:
                pause()

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
            bullet.delete()
    

    
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for obj in objects:
        screen.blit(obj.image,obj.rect)
    
    screen.blit(life_text,life_text_rect)
    screen.blit(score_text,score_text_rect)
    pygame.display.flip()


screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("COSMIC COMBAT v_1.0")
background = pygame.image.load('./images/bg.jpg')
space_ship = game_object('space-ship',[5,768//1.5],'spaceship.png')
gameOver = False
gameStart = False
gameExit = False
enemyPresent = False
newHighScore = False

makeGameHarder = 0

enemyCreateEvent = pygame.USEREVENT + 1
logicEvent = pygame.USEREVENT + 2
moveEvent = pygame.USEREVENT + 3
# enemyDestroyed = pygame.USEREVENT + 4
# enemyDestroyEvent = pygame.event.Event(enemyDestroyed)

createEnemy()

enemyCreateTime = 3000

pygame.time.set_timer(enemyCreateEvent, enemyCreateTime)
pygame.time.set_timer(moveEvent, 100)
pygame.time.set_timer(logicEvent,50)

while not gameStart:
    gameInit()


score_text = ''
score_text_rect = ''
life_text = ''
life_text_rect = ''
changeScore()
changeLife()

if os.path.exists('high_score.txt'): 
    with open('high_score.txt','r') as readFile:
        highScore = int(readFile.readline())
else:
    highScore = 0

while not gameOver:
    main()
    if life < 0:
        gameOver = True


setHighScore()

while not gameExit:
    final()

sys.exit()