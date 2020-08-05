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
        os.system('clear')
        self.setAllPositions()
        self.print2DArray(displayArray)
        

    def setBorder(self):
        displayArray[0] = ['#']*len(displayArray[0])                           # Sets the upper row
        displayArray[-1] = ['#']*len(displayArray[-1])                         # Sets the lower row

        for i in range(len(displayArray)):
            displayArray[i][0] = '#'                                                   # Sets the left column
            displayArray[i][-1] = '#'                                                  # Sets the right column

    def setXY(self, x, y, char):
        global displayArray
        displayArray[y][x] = char

    def setAllPositions(self):
        for i in range(1, len(displayArray)-1):
            for j in range(1,len(displayArray[i])-1):
                displayArray[i][j] = ' '                                                 # Sets the left column

        for i in rounds:
            self.setXY(i.getX(), i.getY(), i.getType())

        for i in enemies:
            self.setXY(i.getX(), i.getY(), i.getType())

        self.setXY(player.getX(), player.getY(), player.getSpaceship())

        



class COLLITION_MANAGER: #-------------------------------------------------------------------------------------------------------------------------

#   Methods
    def manageBulletCollition(self, roundIndex):
        global rounds, enemies
        self.victimIndex = 0
        self.victimX = rounds[roundIndex].getX()
        self.victimY = rounds[roundIndex].getY() -1

        for i in enemies:
            if i.getX() == self.victimX and i.getY() == self.victimY:
                self.victimIndex = enemies.index(i)
                rounds.pop(roundIndex)                                                      # Deleting the round
                enemies[self.victimIndex].changeHealth(rounds[roundIndex].getDamage())        # Subtract the taken damage
                if enemies[self.victimIndex].getHealth() <= 0:                                # Deleting the enemy when his hp is <= 0
                    enemies.pop(self.victimIndex)
                break



    def manageEnemyCollition(self, enemyIndex):
        global rounds, enemies

        self.roundX = enemies[enemyIndex].getX()
        self.roundY = enemies[enemyIndex].getY() +1

        for i in rounds:                                                                      # Testing if object is a round
            if i.getX == self.roundX and i.getY == self.roundY:
                self.roundIndex = rounds.index(i)
                rounds.pop(self.roundIndex)                                                   # Deleting the round
                enemies[enemyIndex].changeHealth(rounds[self.roundIndex].getDamage())         # Subtract the taken damage
                if enemies[self.roundIndex].getHealth() <= 0:                                 # Deleting the enemy when his hp is <= 0
                    enemies.pop(self.roundIndex)
                break
        
        if player.getX == self.roundX and player.getY == self.roundY:                         # Testing if object is the player
            player.removeHealth(enemies[enemyIndex].getDamage())
            if player.getHealth < 0:
                # Action when player dies



        

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
        if displayArray[self.yPosition][self.xPosition +1] == ' ':
            self.moveDown()
            return 0
        else:
            return 1





class ENEMY:    #---------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, type = '?', hp = 100, damage = 25):
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
        if displayArray[self.yPosition][self.xPosition +1] == ' ':
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
        rounds.extend([ROUND(self.xPosition, self.yPosition -1, '|', 100)])




#-------------------------------------------------------------------------------------------------------------------------------------------------


# Attributes
displayArray = []
display = DISPLAY(50, 20)
rounds = []
player = PLAYER(int(display.SizeX/2), display.SizeY-3, 'A')
enemies = []
collition_manager = COLLITION_MANAGER()

timer = 0

# Functions

def addEnemy(x, y, type = 'O', hp = 100):
    global enemies
    enemies.extend([ENEMY(x, y, type, hp)])


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




# RUN     ----------------------------------------------------------------------------------------------------------------------------------------

with KeyPoller.KeyPoller() as keyPoller:
    display.setBorder()
    keyPoller = KeyPoller.KeyPoller()
    while True:
        timer += 1
        display.refresh()

        if timer%15 == 0:
            moveRounds()
        elif timer > 120 and timer < 123:
            moveEnemies()
        elif timer > 240:
            addEnemy(random.randint(1, (len(displayArray[1])-2)), 1)
            timer = 0

        c = keyPoller.poll() 
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
                break
