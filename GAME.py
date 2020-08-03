import time, sys, os



class DISPLAY:  #---------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, xSize, ySize):
        global displayArray
        displayArray = [[' ' for i in range(xSize)] for j in range (ySize)]
        self.SizeX = xSize
        self.SizeY = ySize

#   Methods

    def printArray(self, array):
        for i in array:
            print(i, end='')                    # Prints every element without a seperator
        print()                                 # Ends the line with a break

    def print2DArray(self, array2D):
        for i in array2D:
            self.printArray(i)                  # Prints one line

    def refresh(self):
        os.system('clear')
        self.print2DArray(displayArray)

    def setBorder(self):
        displayArray[0] = ['#']*len(displayArray[0])                           # Sets the upper row
        displayArray[-1] = ['#']*len(displayArray[-1])                         # Sets the lower row

        for i in range(len(displayArray)):
            displayArray[i][0] = '#'                                                   # Sets the left column
            displayArray[i][-1] = '#'                                                  # Sets the right column

    def setXY(self, x, y, char):
        displayArray[x][y] = char





class COLLITION_MANAGER: #-------------------------------------------------------------------------------------------------------------------------

#   Methods
    def manageBulletCollition(self, roundIndex):
        global rounds, enemies

        self.victimX = rounds[roundIndex].getX
        self.victimY = rounds[roundIndex].getY -1

        for i in enemies:
            if enemies[i].getX == self.victimX and enemies[i].getY == self.victimY:
                self.victimIndex = i
                break

        enemies[self.victimIndex].changeHealth(rounds[roundIndex].getDamage)        # Subtract the taken damage

        if enemies[self.victimIndex].getHealth <= 0:                                # Deleting the enemy when his hp is <= 0
            enemies.pop(self.victimIndex)

        rounds.pop(roundIndex)                                                      # Deleting the round


    def manageEnemyCollition(self, enemyIndex):
        global rounds, enemies

        self.roundX = enemies[enemyIndex].getX
        self.roundY = enemies[enemyIndex].getY +1

        for i in rounds:
            if rounds[i].getX == self.roundX and rounds[i].getY == self.roundY:
                self.roundIndex = i
                break

        enemies[enemyIndex].changeHealth(rounds[self.roundIndex].getDamage)         # Subtract the taken damage

        if enemies[self.roundIndex].getHealth <= 0:                                 # Deleting the enemy when his hp is <= 0
            enemies.pop(self.roundIndex)

        rounds.pop(enemyIndex)                                                      # Deleting the round



        












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

    def tryMoveDown(self):                        # Trying to move down, return 0 when successful and 1 when not
        if displayArray[self.xPosition][self.yPosition +1] == ' ':
            self.moveDown()
            return 0
        else:
            return 1





class ENEMY:    #---------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, type = '?', hp = 100):
        self.xPosition = x
        self.yPosition = y
        self.enemyType = type
        self.health = hp

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

    def changeHealth(self, subtractedValue):
        self.health -= subtractedValue

    def getHealth(self):
        return self.health

    def moveDown(self):
        self.yPosition += 1

    def tryMoveDown(self):                        # Trying to move down, return 0 when successful and 1 when not
        if displayArray[self.xPosition][self.yPosition +1] == ' ':
            self.moveDown()
            return 0
        else:
            return 1





class ROUND:    #----------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, roundType = '?', damage = 100):
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

    def tryMoveUp(self):                        # Trying to move up, return 0 when successful and 1 when not
        if displayArray[self.xPosition][self.yPosition -1] == ' ':
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

    def changeHealth(self, value):
        self.health = value

    def getHealth(self):
        return self.health

    def moveUp(self):
        self.yPosition -= 1

    def moveLeft(self):
        self.xPosition -= 1

    def moveRight(self):
        self.xPosition += 1

    def shoot(self):        
        global rounds
        rounds.extend(ROUND(self.xPosition, self.yPosition+1, '|', 100))



    # TryMove methods needed









#-------------------------------------------------------------------------------------------------------------------------------------------------


# Attributes
displayArray = []
display = DISPLAY(20, 8)
rounds = []
player = PLAYER(display.SizeX-3, int(display.SizeY/2), 'A')
enemies = []
collition_manager = COLLITION_MANAGER()

# Functions

def addEnemy(self, x, y, type, hp):
    global enemies
    enemies.extend(ENEMY(self.xPosition, self.yPosition+1, 'O', 100))


def moveRounds(self):
    global rounds, collition_manager
    for i in rounds:
        if i.tryMoveUp == 1:
            collition_manager.manageBulletCollition(i)

def moveEnemies(self):
    global enemies, collition_manager
    for i in enemies:
        if i.tryMoveUp == 1:
            collition_manager.manageBulletCollition(i)




# RUN     ----------------------------------------------------------------------------------------------------------------------------------------

try:
    display.setBorder()
    while True:
        display.refresh()





except KeyboardInterrupt:
    sys.exit()