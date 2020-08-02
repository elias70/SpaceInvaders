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

    def changeHealth(self, value):
        self.health += ValueError

    def getHealth(self):
        return self.health

    def moveDown(self):
        self.yPosition += 1





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

    def moveUp(self):
        global displayArray
        if displayArray[self.xPosition][self.yPosition-1] == ' ':    
            self.yPosition -= 1






class PLAYER:   #----------------------------------------------------------------------------------------------------------------------------------

#   Constructor/Attributes
    def __init__(self, x = 0, y = 0, spaceship = '?'):
        self.xPosition = x
        self.yPosition = y
        self.playerSpaceship = spaceship
        self.round = '|'
        self.health = 100

        self.round = []

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
        self.health += ValueError

    def getHealth(self):
        return self.health

    def moveUp(self):
        self.yPosition -= 1

    def moveLeft(self):
        self.xPosition -= 1

    def moveRight(self):
        self.xPosition += 1

    def shoot(self):
        self.round.addend(ROUND(self.xPosition, self.yPosition+1, '|', 20))













#-------------------------------------------------------------------------------------------------------------------------------------------------


# Attributes
displayArray = []
display = DISPLAY(20, 8)
player = PLAYER(display.SizeX-3, int(display.SizeY/2), 'A')

# Functions







# RUN     ----------------------------------------------------------------------------------------------------------------------------------------

try:
    display.setBorder()
    while True:
        display.refresh()





except KeyboardInterrupt:
    sys.exit()


