import time, sys, os, random, KeyPoller


class DISPLAY:  #---------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, xSize, ySize):
        global displayArray
        self.SizeX = xSize
        self.SizeY = ySize
        displayArray = [[' ' for i in range(self.SizeX)] for j in range (self.SizeY)]
        
#   Methods
    def print2DArray(self, array2D):
        output = ''
        for i in array2D:
            for j in i:
                output += j
            output += '\n'
        print(output)
        
    def refresh(self):
        global stop
        os.system('clear')
        self.setAllPositions()
        self.setHealth()
        self.setScore()
        if stop == True:
            self.setGameOver()
        self.print2DArray(displayArray)
        
    def setBorder(self):
        displayArray[0] = ['#']*len(displayArray[0])                           # Sets the upper row
        displayArray[-1] = ['#']*len(displayArray[-1])                         # Sets the lower row
        for i in range(len(displayArray)):
            displayArray[i][0] = '#'                                                   # Sets the left column
            displayArray[i][-1] = '#'                                                  # Sets the right column

    def clearDisplayArray(self):
        global displayArray
        for y in range(1, len(displayArray)):
            for x in range(1,len(displayArray[y])):
                displayArray[y][x] = ' '

    def setXY(self, x, y, char):
        global displayArray
        displayArray[y][x] = char

    def setStringAtXY(self, string, xCenterOffset = 0, yCenterOffset = 0):
        x = int((self.SizeX/2) +xCenterOffset)
        for i in string:
            self.setXY(x, int(self.SizeY/2) +yCenterOffset, i)
            x += 1

    def setAllPositions(self):                                                      # Sets all positions of all object
        for i in range(1, len(displayArray)-1):
            for j in range(1,len(displayArray[i])-1):
                displayArray[i][j] = ' '                                                 # Sets the left column

        for i in rounds:
            self.setXY(i.getX(), i.getY(), i.getType())

        for i in enemies:
            self.setXY(i.getX(), i.getY(), i.getType())

        for i in items:
            self.setXY(i.getX(), i.getY(), i.getType())

        self.setXY(player.getX(), player.getY(), player.getSpaceship())

    def setHealth(self):
        num = str(player.getHealth())
        self.setXY(self.SizeX -4, 1, num[len(num)-1])
        if len(num) > 1: 
            self.setXY(self.SizeX -5, 1, num[len(num)-2])
            if len(num) > 2:
                self.setXY(self.SizeX -6, 1, num[len(num)-3])

    def setScore(self):
        global score
        num = str(score)
        self.setXY(4, 1, num[len(num)-1])
        if len(num) > 1: 
            self.setXY(3, 1, num[len(num)-2])
            if len(num) > 2:
                self.setXY(2, 1, num[len(num)-3])

    def setGameOver(self):
        self.setStringAtXY('GAME OVER', -4, 0)

    def printMainMenu(self, withContinue):
        os.system('clear')
        self.clearDisplayArray()
        self.setStringAtXY('SPACE INVADERS', -7, -3)
        self.setStringAtXY('[N]EW GAME', -5, -1)
        self.setStringAtXY('[O]PTIONS', -5, 0)
        if withContinue:
            self.setStringAtXY('[C]ONTINUE', -5, 1) 
        self.setBorder()
        display.print2DArray(displayArray)

    def printOptions(self, type = 0):                  # Prints the different option screens, default = 0, difficulty = 1, resolution = 2
        global width, height
        os.system('clear')
        self.clearDisplayArray()
        if type == 0:
            self.setStringAtXY('[D]IFFICULTY', -6, -2)
            self.setStringAtXY('[R]ESOLUTION', -6, -1)
        elif type == 1:
            self.setStringAtXY('[E]ASY', -4, -2)
            self.setStringAtXY('[N]ORMAL', -4, -1)
            self.setStringAtXY('[H]ARD', -4, 0)
        elif type == 2:
            self.setStringAtXY('RESOLUTION:', -5, -2)
            self.setStringAtXY(f'{width} x {height}', -5, -1)
            self.setStringAtXY('[C]HANGE', -5, +1)
        self.setBorder()
        display.print2DArray(displayArray)

        


class COLLITION_MANAGER: #-------------------------------------------------------------------------------------------------------------------------

#   Methods
    def manageBulletCollition(self, roundIndex):
        global rounds, enemies, score
        self.victimIndex = 0
        self.victimX = rounds[roundIndex].getX()
        self.victimY = rounds[roundIndex].getY() -1

        for i in enemies:
            if i.getX() == self.victimX and i.getY() == self.victimY:
                self.victimIndex = enemies.index(i)
                enemies[self.victimIndex].changeHealth(rounds[roundIndex].getDamage())        # Subtract the taken damage
                if enemies[self.victimIndex].getHealth() <= 0:                                # Deleting the enemy when his hp is <= 0
                    enemies.pop(self.victimIndex)
                    score += 3
                break
        for i in items:
            if i.getX() == self.victimX and i.getY() == self.victimY:
                self.victimIndex = items.index(i)
                items.pop(self.victimIndex)                                            # Deleting the item
                break
        rounds.pop(roundIndex)                                                              # Deleting the round

    def manageEnemyCollition(self, enemyIndex):
        global rounds, enemies, displayArray

        self.targetX = enemies[enemyIndex].getX()
        self.targetY = enemies[enemyIndex].getY() +1

        for i in rounds:                                                                      # Testing if object is a round
            if i.getX == self.targetX and i.getY == self.targetY:
                self.roundIndex = rounds.index(i)
                rounds.pop(self.roundIndex)                                                   # Deleting the round
                enemies[enemyIndex].changeHealth(rounds[self.roundIndex].getDamage())         # Subtract the taken damage
                if enemies[self.roundIndex].getHealth() <= 0:                                 # Deleting the enemy when his hp is <= 0
                    enemies.pop(self.roundIndex)
                break
        
        if player.getX() == self.targetX and player.getY() == self.targetY:                         # Testing if object is the player
            player.removeHealth(enemies[enemyIndex].getDamage())                              # Subtract the taken damage
            enemies.pop(enemyIndex)                                                      # Deleting the enemy
            if player.getHealth() <= 0:
                gameOver()
        else:
            gameOver()         


    def manageItemCollition(self, itemIndex):
        global rounds, items, score

        self.targetX = items[itemIndex].getX()
        self.targetY = items[itemIndex].getY() +1

        for i in rounds:                                                                      # Testing if object is a round
            if i.getX == self.targetX and i.getY == self.targetY:
                self.roundIndex = rounds.index(i)
                rounds.pop(self.roundIndex)                                                   # Deleting the round
                items.pop(self.roundIndex)                                                    # Deleting the item
                break
        
        if player.getX() == self.targetX and player.getY() == self.targetY:                   # Testing if object is the player
            if items[itemIndex].getType() == '+':
                player.removeHealth(-25)
                score += 1
            items.pop(itemIndex)                                                              # Deleting the enemy
        else:
            items.pop(itemIndex)



   
class ITEM: #-------------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, type = '?'):
        self.xPosition = x
        self.yPosition = y
        self.itemType = type

#   Methods
    def moveX(self, x):
        self.xPosition += x

    def moveY(self, y):
        self.yPosition += y

    def getX(self):
        return self.xPosition

    def getY(self):
        return self.yPosition

    def changeItemType(self, newType):
        self.itemType = newType

    def getType(self):
        return self.itemType

    def moveDown(self):
        self.yPosition += 1

    def tryMoveDown(self):                        # Trying to move down, returns 0 when successful and 1 when not
        if displayArray[self.yPosition +1][self.xPosition] == ' ':
            self.moveDown()
            return 0
        else:
            return 1




class ENEMY:    #---------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, type = 'O', hp = 100, damage = 25):
        self.xPosition = x
        self.yPosition = y
        self.enemyType = type
        self.health = hp
        self.damage = damage

#   Methods
    def moveX(self, x):
        self.xPosition += x

    def moveY(self, y):
        self.yPosition += y

    def getX(self):
        return self.xPosition

    def getY(self):
        return self.yPosition

    def changeEnemyType(self, newType):
        self.enemyType = newType

    def getType(self):
        return self.enemyType

    def getDamage(self):
        return self.damage

    def changeHealth(self, subtractedValue):
        self.health -= subtractedValue

    def getHealth(self):
        return self.health

    def moveDown(self):
        self.yPosition += 1

    def tryMoveDown(self):                        # Trying to move down, returns 0 when successful and 1 when not
        if displayArray[self.yPosition +1][self.xPosition] == ' ':
            self.moveDown()
            return 0
        else:
            return 1




class ROUND:    #----------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, roundType = '|', damage = 100):
        self.xPosition = x
        self.yPosition = y
        self.ammoType = roundType
        self.damage = damage

#   Methods
    def moveX(self, x):
        self.xPosition += x

    def moveY(self, y):
        self.yPosition += y

    def getX(self):
        return self.xPosition

    def getY(self):
        return self.yPosition

    def changeAmmo(self, newType):
        self.ammoType = newType

    def getType(self):
        return self.ammoType

    def getDamage(self):
        return self.damage

    def moveUp(self):
        self.yPosition -= 1

    def tryMoveUp(self):                        # Trying to move up, returns 0 when successful and 1 when not
        if displayArray[self.yPosition -1][self.xPosition] == ' ':
            self.moveUp()
            return 0
        else:
            return 1



class PLAYER:   #----------------------------------------------------------------------------------------------------------------------------------


#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, spaceship = '?'):
        self.xPosition = x
        self.yPosition = y
        self.playerSpaceship = spaceship
        self.round = '|'
        self.health = 100

#   Methods
    def moveX(self, x):
        self.xPosition += x

    def moveY(self, y):
        self.yPosition += y

    def getX(self):
        return self.xPosition

    def getY(self):
        return self.yPosition

    def changeSpaceship(self, newSpaceship):
        self.playerSpaceship = newSpaceship

    def getSpaceship(self):
        return self.playerSpaceship

    def changeRound(self, newRound):
        self.round = newRound

    def getRound(self):
        return self.round

    def removeHealth(self, value):
        self.health -= value

    def getHealth(self):
        return self.health

    def moveUp(self):
        self.yPosition -= 1

    def moveDown(self):
        self.yPosition += 1

    def moveLeft(self):
        self.xPosition -= 1

    def moveRight(self):
        self.xPosition += 1

    def tryMoveUp(self):                        # Trying to move up, returns 0 when successful and 1 when not, returns 2 when hitting a wall
        if displayArray[self.yPosition-1][self.xPosition] == ' ':
            self.moveUp()
            return 0
        elif displayArray[self.yPosition-1][self.xPosition] == '#':
            return 2
        else:
            return 1

    def tryMoveDown(self):                        # Trying to move down, returns 0 when successful and 1 when not, returns 2 when hitting a wall
        if displayArray[self.yPosition +1][self.xPosition] == ' ':
            self.moveDown()
            return 0
        elif displayArray[self.yPosition +1][self.xPosition] == '#':
            return 2
        else:
            return 1

    def tryMoveRight(self):                        # Trying to move right, returns 0 when successful and 1 when not, returns 2 when hitting a wall
        if displayArray[self.yPosition][self.xPosition +1] == ' ':
            self.moveRight()
            return 0
        elif displayArray[self.yPosition][self.xPosition +1] == '#':
            return 2
        else:
            return 1

    def tryMoveLeft(self):                        # Trying to move left, returns 0 when successful and 1 when not, returns 2 when hitting a wall
        if displayArray[self.yPosition][self.xPosition -1] == ' ':
            self.moveLeft()
            return 0
        elif displayArray[self.yPosition][self.xPosition -1] == '#':
            return 2
        else:
            return 1

    def shoot(self):        
        global rounds
        rounds.extend([ROUND(self.xPosition, self.yPosition -1)])


#-------------------------------------------------------------------------------------------------------------------------------------------------

# Attributes
stop = False
score = 0
timer = 0
optionType = 0
width = 40
height = 16
#difficulty = 1                          # -> 1:easy 2:normal 3:hard
difficultyMultiplier = 1                # -> 0.5:easy 1:normal 2:hard

displayArray = []
display = DISPLAY(width, height)
rounds = []
player = PLAYER(int(display.SizeX/2), display.SizeY-3, 'A')
enemies = []
items = []
collition_manager = COLLITION_MANAGER()
keyPoller = KeyPoller.KeyPoller()


# Functions
def reset():
    global displayArray, display, rounds, player, enemies, items, collition_manager, stop, score, timer, optionType, width, height
    
    stop = False
    score = 0
    timer = 0
    optionType = 0

    displayArray = []
    display = DISPLAY(width, height)
    rounds = []
    player = PLAYER(int(display.SizeX/2), display.SizeY-3, 'A')
    enemies = []
    items = []
    collition_manager = COLLITION_MANAGER()
    

def runAtRate(func, rate = 30):
    sleepTime = 1/rate
    while True:
        x = 0
        startTime = time.perf_counter()
        while x < rate:
            if func() == False:
                return None
            time.sleep(sleepTime)
        sleepTime = (startTime - time.perf_counter())/rate

def addEnemy(x, y, type = 'O', hp = 100):
    global enemies
    enemies.extend([ENEMY(x, y, type, hp)])

def addItem(x, y, type = '+'):
    global items
    items.extend([ITEM(x, y, type)])

def moveRounds():
    global rounds, collition_manager
    for i in rounds:
        if i.tryMoveUp() == 1:
            collition_manager.manageBulletCollition(rounds.index(i))

def moveEnemies():
    global enemies, collition_manager
    for i in enemies:
        if i.tryMoveDown() == 1:
            collition_manager.manageEnemyCollition(enemies.index(i))

def moveItems():
    global items, collition_manager
    for i in items:
        if i.tryMoveDown() == 1:
            collition_manager.manageItemCollition(items.index(i))

def gameOver():
    global stop, display
    stop = True
    display.refresh()

def getResolutionInput():
    global width, height
    while True:    
        try:
            x = input("WIDTH: min.20/max.200 >")
            print(x)
            x = int(x)
            if x >= 20 and x <= 200:
                break
        except ValueError:
            continue
    while True:
        try:
            y = input("HEIGHT: min.8/max.50 >")
            print(y)
            y = int(y)
            if x >= 20 and x <= 200:
                break
        except ValueError:
            continue
    width = x
    height = y


def runOptions():              
    global display, keyPoller, optionType, width, height, difficultyMultiplier               # optionType -> default = 0, difficulty = 1, reolution = 2
    x = optionType
    c = keyPoller.poll()                                        # Gets user input
    if not c is None:
        if c == "d" and x == 0:
            optionType = 1
            display.printOptions(1)
        elif c == "r" and x == 0:
            optionType = 2
            display.printOptions(2)
        elif c == "c" and x == 2:
            getResolutionInput()
            reset()
            display.printOptions(2)
        elif c == "e" and x == 1:
            difficultyMultiplier = 0.5
            optionType = 0
            display.printOptions(0)
        elif c == "n" and x == 1:
            difficultyMultiplier = 1
            optionType = 0
            display.printOptions(0)
        elif c == "h" and x == 1:
            difficultyMultiplier = 2
            optionType = 0
            display.printOptions(0)
        elif c == "q" and x == 0:
            return False
        elif c == "q":
            optionType = 0
            display.printOptions(0)

#----------------------------------------------------------------------------------------------------------------------------------------
def runGame():
    global timer, display, keyPoller
    timer += 1
    display.refresh()

    if timer%5 == 0:
        moveRounds()
        if timer%(30/difficultyMultiplier) == 0:
            moveEnemies()
            moveItems()
            if timer%(60/difficultyMultiplier) == 0:
                addEnemy(random.randint(1, (len(displayArray[1])-2)), 1,'O' , 100/difficultyMultiplier)
                if timer > (120/difficultyMultiplier):
                    nextXPos = random.randint(1, (len(displayArray[1])-2))
                    if displayArray[1][nextXPos] == ' ':
                        addItem(nextXPos, 1, '+')  
                    timer = 0

    c = keyPoller.poll()                                        # Gets user input
    if not c is None:
        if c == "w":
            player.tryMoveUp()
        elif c == "s":
            player.tryMoveDown()
        elif c == "d":
            player.tryMoveRight()
        elif c == "a":
            player.tryMoveLeft()
        elif c == " ":
            player.shoot()
        elif c == "q":
            return False



display.printMainMenu(False)

with KeyPoller.KeyPoller() as keyPoller:
    keyPoller = KeyPoller.KeyPoller()
    while True:
        c = keyPoller.poll()                                       # Gets user input
        if not c is None:
            if c == "n":
                reset()
                display.setBorder()
                runAtRate(runGame, 60)
                display.printMainMenu(score != 0)
            elif c == "c":
                display.setBorder()
                runAtRate(runGame, 60)
                display.printMainMenu(score != 0)
            elif c == "o":
                display.printOptions(0)
                runAtRate(runOptions, 15)
                display.printMainMenu(score != 0)
            elif c == "q":
                break