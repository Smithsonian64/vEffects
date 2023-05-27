from copy import copy
from itertools import cycle
from random import randint, shuffle, choice
import pygame
from pygame import Color

scale = 2


class Langtonsant:
    def __init__(self, screen):
        self.ruleslist = None
        self.direction = None
        self.rules = None
        self.position = None
        self.grid = None
        self.index = 0
        self.screen = screen
        self.canvas = pygame.Surface((screen.get_width(), screen.get_height()))
        self.colorlist = ['gray50', 'white', 'red', 'green', 'blue', 'magenta', 'cyan', 'yellow', 'orange', 'teal',
                          'violet', 'aqua']
        self.colornumberlist = {0: 'gray50', 1: 'white', 2: 'red', 3: 'green', 4: 'blue', 5: 'magenta', 6: 'cyan',
                                7: 'yellow', 8: 'orange', 9: 'teal', 10: 'violet', 11: 'aqua'}
        self.colors = cycle(self.colorlist)
        self.directionslist = ['North', 'East', 'South', 'West']
        self.directions = cycle(['North', 'East', 'South', 'West'])
        self.actions = ['L', 'R']
        self.extendedactions = ['F', 'B']

        self.reinit()

    def step(self):

        currentcolor = self.grid[self.position[0]][self.position[1]]

        temp = cycle(iter(self.rules))
        for key in temp:
            if key == currentcolor:
                self.grid[self.position[0]][self.position[1]] = next(temp)
                break

        if self.rules[currentcolor] == 'L':
            # for i in range(len(self.colorlist) - 2):
            next(self.directions)
            next(self.directions)
            self.direction = next(self.directions)
        elif self.rules[currentcolor] == 'R':
            self.direction = next(self.directions)
        else:
            next(self.directions)
            self.direction = next(self.directions)

        if self.direction == 'North':
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == 'East':
            self.position = (self.position[0] + 1, self.position[1])
        elif self.direction == 'South':
            self.position = (self.position[0], self.position[1] + 1)
        elif self.direction == 'West':
            self.position = (self.position[0] - 1, self.position[1])

        if self.position[0] >= self.screen.get_width() / scale:
            self.position = (self.position[0] - self.screen.get_width(), self.position[1])
        if self.position[1] >= self.screen.get_height() / scale:
            self.position = (self.position[0], self.position[1] - self.screen.get_height())
        if self.position[0] < 0:
            self.position = (self.screen.get_width() - 1 + self.position[0], self.position[1])
        if self.position[1] < 0:
            self.position = (self.position[0], self.screen.get_height() - 1 + self.position[1])

        pygame.draw.rect(self.canvas, Color(currentcolor), (self.position[0] * scale, self.position[1] * scale, 1*scale, 1*scale))

        self.screen.blit(self.canvas, (0, 0))

    def generaterules(self, defaultcolor):  # (color, action)
        length = randint(2, len(self.colorlist) - 1)
        tmp = copy(self.colorlist)
        tmp.remove(defaultcolor)
        shuffle(tmp)
        rules = [(tmp[i], self.actions[randint(0, len(self.actions) - 1)]) for i in range(length)]
        rules[0] = (defaultcolor, self.actions[randint(0, len(self.actions) - 1)])

        rpresent = False
        lpresent = False

        for rule in rules:
            if 'R' in rule:
                rpresent = True

        for rule in rules:
            if 'L' in rule:
                lpresent = True

        if not rpresent:
            rules[0] = (rules[0][0], 'R')

        if not lpresent:
            rules[0] = (rules[0][0], 'L')

        self.ruleslist = []
        for rule in rules:
            self.ruleslist.append(rule[0])
        self.ruleslist = cycle(self.ruleslist)
        print(rules)
        return dict(rules)

    def reinit(self):
        defaultcolor = choice(self.colorlist)
        self.grid = [[defaultcolor for _ in range(self.screen.get_height())] for _ in range(self.screen.get_width())]
        self.position = (int(self.screen.get_width() / 2 / scale), int(self.screen.get_height() / 2 / scale))
        self.rules = self.generaterules(defaultcolor)
        self.direction = self.directionslist[0]
        self.canvas = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.index = 0
