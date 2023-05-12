import numpy
import pygame


class Transition:
    def __init__(self, screen):
        self.frames = 0
        self.start = 0
        self.fadeimage = None
        self.screen = screen
        self.transitioning = False

    def step(self):
        if self.frames > 0:
            self.fadeimage.set_alpha(int(255 - (self.start - self.frames) * 255 / self.start))
            self.screen.blit(self.fadeimage, (0, 0))
            self.frames -= 1
        else:
            self.transitioning = False

    def starttransition(self, screen, frames):
        if not self.transitioning:
            self.frames += frames
            self.start = frames
            self.fadeimage = screen.copy()
            self.transitioning = True
