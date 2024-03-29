import math

class Punto():

    def __init__(self):
        self.x = 0
        self.y = 0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self, y):
        return self.y

    def calcularDistancia(self, p):
        return math.sqrt((self.x - p.getX())**2 + (self.y - p.getY())**2)