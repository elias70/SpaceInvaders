class DISPLAY:

#   Constructor/Attributes
    def __init__(self, xSize, ySize):
        self.displayArray = [[' ' for i in range(xSize)] for j in range (ySize)]

#   Methods

    def printArray(self, array):
        for i in array:
            print(i, end='')                    # Prints every element without a seperator
        print()                                 # Ends the line with a break

    def print2DArray(self, array2D):
        for i in array2D:
            self.printArray(i)                  # Prints one line

    def refresh(self):
        self.print2DArray(self.displayArray)

    def setBorder(self):
        self.displayArray[0] = ['*']*len(self.displayArray[0])                           # Sets the upper row
        self.displayArray[-1] = ['*']*len(self.displayArray[-1])                         # Sets the lower row

        for i in range(len(self.displayArray)):
            self.displayArray[i][0] = '*'                                                   # Sets the left column
            self.displayArray[i][-1] = '*'                                                  # Sets the right column

    def setXY(self, x, y, char):
        self.displayArray[x][y] = char