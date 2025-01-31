from numpy import array
from random import randint, choice
import pygame


class Taquin:
    def __init__(self):
        self.plateau = array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 0]])
        self.directions = [] #c'est la liste des mouvements utilisés pour mélanger le taquin

    def __str__(self):
        return self.plateau.__str__()
    
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
        i, j = self.poszero() #On regarde là où est le zero
        if i != 0:
            self.plateau[i][j] = self.plateau[i-1][j]
            self.plateau[i-1][j] = 0
    
    def up(self):
        i, j = self.poszero() #On regarde là où est le zero
        if i != 3:
            self.plateau[i][j] = self.plateau[i+1][j]
            self.plateau[i+1][j] = 0
    
    def left(self):
        i, j = self.poszero() #On regarde là où est le zero
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
    
    def graphicplate(self, screen, win = False):
        font = pygame.font.Font(None, 100)
        if win:
            color = (84,8,8)
        else:
            color = (40,58,82)
        for y in range(4):
            for x in range(4):
                if self.plateau[y][x] != 0:
                    pygame.draw.rect(screen, color, pygame.Rect(16+x*146, 16+y*146, 142, 142), border_radius=20)
                    if self.plateau[y][x] < 10:
                        dx = 0
                    else:
                        dx = -16
                    screen.blit( font.render(str(self.plateau[y][x]),1,(255,255,255)) , (70+dx + 144*x , 58 + 144*y) )
    def play(self):
        T.mix()
        pygame.init()
        screen = pygame.display.set_mode((610, 610))
        pygame.display.set_caption('Le jeu du Taquin - Stéphane Pasquet - mathweb.fr')
        green = (9,44,28)
        marroon = (33,21,3)
        marroon_light = (47,32,8)
        running = True
        
        
        while running:
            screen.fill( green )
            pygame.draw.rect(screen, marroon, pygame.Rect(10, 10, 585, 585))
            pygame.draw.rect(screen, marroon_light, pygame.Rect(16, 16, 584, 584))
            
            if (self.plateau == array( [ [1,2,3,4], [5,6,7,8] , [9,10,11,12], [13,14,15,0] ] )).all():
                self.graphicplate(screen, win = True)
            else:
                self.graphicplate(screen)
                
            
            # Fermeture de la fenêtre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.up()
                    elif event.key == pygame.K_DOWN:
                        self.down()
                    elif event.key == pygame.K_LEFT:
                        self.left()
                    elif event.key == pygame.K_RIGHT:
                        self.right()
                
            pygame.display.flip()
            
        pygame.quit()

T = Taquin()
T.mix()
print(T)

        
    