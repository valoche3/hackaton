from numpy import array
from random import randint, choice
import pygame


class Taquin:
    def __init__(self):
        self.plateau = array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 0]])
        self.directions = [] #c'est la liste des mouvements utilisés pour mélanger le taquin

    def __str__(self):
        for y in range(4):
            for x in range(4):
                if self.plateau[y][x] == 0 : 
                    return y,x
    
    def poszero(self):
        for y in range(4):
            for x in range(4):
                if self.plateau[y][x] == 0: 
                    return y,x

    def possible_mouvements(self):
        i, j = self.poszero()
        impossible = []
        possible = ['L', 'R', 'U', 'D'] #left, right, up, down
        if i == 0:
            impossible.append('D')
        if i == 3:
            impossible.append('U')
        if j == 0:
            impossible.append('R')
        if j == 3 : 
            impossible.append('L')
        return [i for i in possible if i not in impossible]

    def down(self):
        i, j = self.poszero #On regarde là où est le zero
        if i != 0:
            self.plateau[i][j] = self.plateau[i-1][j]
            self.plateau[i-1][j] = 0
    
    def up(self):
        i, j = self.poszero #On regarde là où est le zero
        if i != 3:
            self.plateau[i][j] = self.plateau[i+1][j]
            self.plateau[i+1][j] = 0
    
    def left(self):
        i, j = self.poszero #On regarde là où est le zero
        if j != 3:
            self.plateau[i][j] = self.plateau[i][j+1]
            self.plateau[i][j+1] = 0
    
    def right(self):
        i, j = self.poszero()
        if j != 0:
            self.plateau[i][j] = self.plateau[i][j-1]
            self.plateau[i][j-1] = 0
    
    def mix(self): #mélange le plateau initial de manière aléatoire
        for _ in range(10,100):
            direction = choice(self.possible_mouvements())
            self.directions.append(direction)
            match direction :
                case 'L' : self.left()
                case 'R' : self.right()
                case 'U' : self.up()
                case _ : self.down()
    

T = Taquin()
T.mix()
print(T)

        
    