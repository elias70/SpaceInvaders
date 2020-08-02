class ENEMY:

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
