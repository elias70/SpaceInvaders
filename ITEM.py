class ITEM:

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
