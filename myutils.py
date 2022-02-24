import numpy
import random
import pygame

def randomangle():
    return random.uniform(0, 2*numpy.pi)

def degrees(angle):
    return angle * 2*numpy.pi / 360

def centersurface(surface):
    return (surface.get_width() / 2, surface.get_height() / 2)

def getnextposition(position, velocity, angle):
    return (position[0] + velocity*numpy.cos(angle), 
            position[1] + velocity*numpy.sin(angle))

class Cyclenumber:
    def __init__(self, lower, upper, initial=0):
        value = initial


