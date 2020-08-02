class ROUND:

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
        self.yPosition -= 1