import numpy
import pygame
import sys
import random
import myutils

class Trappedknight:
    def __init__(self, screen, size):
        self.size = size
        self.screen = screen
        self.squares = self.makespiral(size)
        
        self.xfactor = screen.get_width() / len(self.squares)
        self.yfactor = screen.get_height() / len(self.squares[0])

        self.moves = self.generatemoves()
        self.colorangle = myutils.randomangle()
        
        


        for i in range(0, len(self.squares)):
            for j in range(0, len(self.squares[i])):
                if self.squares[i][j][0] == 1:
                    self.position = (i, j)
                    self.squares[self.position[0]][self.position[1]] = (1, True)
                    break

        





    def step(self):
        lowestnumber = 0
        nextposition = None
        
        
        

        for i in range(0, len(self.moves)):
        
            if self.position[0] + self.moves[i][0] < 0 or self.position[1] + self.moves[i][1] < 0 or self.position[0] + self.moves[i][0] >= len(self.squares) or self.position[1] + self.moves[i][1] >= len(self.squares[0]):
                self.reinit()
                return
            
            if self.squares[self.position[0] + self.moves[i][0]][self.position[1] + self.moves[i][1]][1] == False:
                if self.squares[self.position[0] + self.moves[i][0]][self.position[1] + self.moves[i][1]][0] < lowestnumber or lowestnumber == 0:
                    nextposition = (self.position[0] + self.moves[i][0], 
                                    self.position[1] + self.moves[i][1])
                    lowestnumber = self.squares[self.position[0] + self.moves[i][0]][self.position[1] + self.moves[i][1]][0] 



        if isinstance(nextposition, type(None)):
            self.reinit()
            return

        pygame.draw.line(self.screen, 
                        (int(127*(numpy.cos(0.2*self.colorangle)+1)), int(127*(numpy.sin(0.5*self.colorangle)+1)), numpy.abs(int(127*(numpy.cos(0.9*self.colorangle)+1)))), 
                        (int(self.position[0]*self.xfactor), int(self.position[1]*self.yfactor)), 
                        (int(nextposition[0]*self.xfactor), int(nextposition[1]*self.yfactor)))
        
        self.position = nextposition

        
        
        self.squares[self.position[0], self.position[1]] = (self.squares[self.position[0], self.position[1]], True)

        self.colorangle += myutils.degrees(1) / 15

    def reinit(self):
        self.squares = self.makespiral(self.size)
        self.moves = self.generatemoves()
        self.colorangle = myutils.randomangle()
        self.screen.fill((0, 0, 0))
        pygame.display.update()


        for i in range(0, len(self.squares)):
            for j in range(0, len(self.squares[i])):
                if self.squares[i][j][0] == 1:
                    self.position = (i, j)
                    self.squares[self.position[0]][self.position[1]] = (1, True)
                    break



    def generatemoves(self):
        nummoves = random.randint(1, 8)
        output = []
        for i in range(0, nummoves):
            output.append((random.randint(-2, 2), random.randint(-2, 2)))
        
        return output


    def makespiral(self, size):
        
         
        numbers = numpy.arange(1, size * size + 1)
        array = numbers.reshape(size, size)


        nrows, ncols = array.shape
        idx = numpy.arange(nrows * ncols).reshape(nrows, ncols)[::-1]
        spiral_idx = []
        while idx.size:
            spiral_idx.append(idx[0])

            idx = idx[1:]

            idx = idx.T[::-1]

        spiral_idx = numpy.hstack(spiral_idx)

        spiral = numpy.empty_like(array)
        spiral.flat[spiral_idx] = array.flat[::-1]

        squares = numpy.empty(spiral.shape, dtype=object)

        for i in range(0, len(squares)):
            for j in range(0, len(squares[i])):
                squares[i][j] = (spiral[i][j], False)

        return squares

