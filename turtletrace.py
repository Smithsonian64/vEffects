import random
import pygame
import numpy
import myutils


class Turtletrace:
    def __init__(self, screen):

        self.screen = screen

        self.canvas = pygame.Surface((10000, 10000))

        self.angle = myutils.randomangle()
        self.position = myutils.centersurface(self.canvas)
        self.lastposition = self.position

        self.velocity = random.random()
        self.deltaangle = myutils.degrees(90)
        self.angleacceleration = 1

        self.colorangle = myutils.randomangle()
        self.colordeltaangle = myutils.degrees(1)

        self.freeroam = False
        self.cameraposition = self.position

        #self.changerate = random.randint(1, 360)

        self.linesize = 3

    def step(self):
        self.position = myutils.getnextposition(self.position, self.velocity, self.angle)

        # print(self.position)
        pygame.draw.line(self.canvas, (
        int(127 * (numpy.cos(0.2 * self.colorangle) + 1)), int(127 * (numpy.sin(0.5 * self.colorangle) + 1)),
        numpy.abs(int(127 * (numpy.cos(0.9 * self.colorangle) + 1)))), self.lastposition, self.position, self.linesize)
        if not self.freeroam:
            self.screen.blit(self.canvas, (
            -self.position[0] + self.screen.get_width() / 2 + self.velocity * numpy.cos(self.angle),
            -self.position[1] + self.screen.get_height() / 2 - self.velocity * numpy.sin(self.angle)))
        else:
            self.screen.blit(self.canvas, self.cameraposition)

        self.lastposition = self.position
        self.angle += self.deltaangle
        self.deltaangle += numpy.pi / 360 + random.random() / 10 - 0.2
        self.colorangle += self.colordeltaangle

        # self.linesize += 1

    def reinit(self):
        self.angle = myutils.randomangle()
        self.position = myutils.centersurface(self.canvas)
        self.lastposition = self.position

        self.colorangle = myutils.randomangle()
        self.cameraposition = self.position
        self.velocity = random.random() * 4 - 8
        #self.changerate = random.randint(1, 360)

        self.canvas.fill((0, 0, 0))

