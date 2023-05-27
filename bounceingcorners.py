import random
import numpy
import pygame

class Bounceingcorners():
    def __init__(self, screen, corners=None):
        self.screen = screen
        self.canvas = pygame.Surface((10000, 10000))
        if corners is None:
            self.faces = random.randint(3, 20)
        else:
            self.faces = corners

        tempcoords = []
        tempangles = []
        self.squarevelocities = []
        self.squarecoords = []
        self.squareangles = []
        
        for i in range(0, self.faces):
            tempcoords.append((random.randint(0, 800), random.randint(0, 480)))
            tempangles.append(random.uniform(0, 2*numpy.pi))
            self.squarevelocities.append(random.random() / 8)
        self.squarecoords = tuple(tempcoords)
        self.squareangles = tempangles
        self.colorvelocity = 0.0001
        self.colorangles = [random.uniform(0, 2*numpy.pi), random.uniform(0, 2*numpy.pi), random.uniform(0, 2*numpy.pi)]
        self.squarecolor = [100, 100, 100]

    def step(self):
        
        if self.squarecolor[0] < 0:
            self.squarecolor[0] += numpy.abs(colorvelocity)
    
        pygame.draw.polygon(self.canvas, self.squarecolor, self.squarecoords)
        temp = []
        for i in range(0, self.faces):
            temp.append((self.squarecoords[i][0] + self.squarevelocities[i]*numpy.cos(self.squareangles[i]),
                         self.squarecoords[i][1] + self.squarevelocities[i]*numpy.sin(self.squareangles[i])))
            
            if temp[i][0] < 0:
                self.squareangles[i] = numpy.pi - self.squareangles[i]
            
            if temp[i][1] < 0: 
                self.squareangles[i] = 0 - self.squareangles[i]

            if temp[i][0] > 800:
                #print(temp[i][0])
                self.squareangles[i] = numpy.pi - self.squareangles[i]
                
            if temp[i][1] > 480:
                self.squareangles[i] = 0 - self.squareangles[i]
                
        self.squarecoords = tuple(temp)
        self.colorangles[0] += numpy.pi*self.colorvelocity
        self.colorangles[1] += numpy.pi*self.colorvelocity
        self.colorangles[2] += numpy.pi*self.colorvelocity
        self.squarecolor[0] = numpy.abs(int(numpy.floor(128 * numpy.sin(self.colorangles[0]))))
        self.squarecolor[1] = numpy.abs(int(numpy.floor(128 * numpy.cos(self.colorangles[1]))))
        self.squarecolor[2] = numpy.abs(int(numpy.floor(128 * numpy.cos(self.colorangles[2]))))
        self.screen.blit(self.canvas, (0,0))
        #print(self.squarecolor)

    def reinit(self, corners=None):

        if corners is None:
            self.faces = random.randint(3, 20)
        else:
            self.faces = corners

        tempcoords = []
        tempangles = []
        self.squarevelocities = []
        self.squarecoords = []
        self.squareangles = []

        for i in range(0, self.faces):
            tempcoords.append((random.randint(0, 800), random.randint(0, 480)))
            tempangles.append(random.uniform(0, 2 * numpy.pi))
            self.squarevelocities.append(random.random() / 8)
        self.squarecoords = tuple(tempcoords)
        self.squareangles = tempangles
        self.colorvelocity = 0.0001
        self.colorangles = [random.uniform(0, 2 * numpy.pi), random.uniform(0, 2 * numpy.pi),
                            random.uniform(0, 2 * numpy.pi)]
        self.squarecolor = [100, 100, 100]
        self.canvas.fill((0, 0, 0))
