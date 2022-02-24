import numpy
import pygame

class Transition():
    def __init__(self, screen):
        self.screen = screen
        self.fadesurface = pygame.Surface(screen.get_size())
        self.fadesurface.blit(self.screen, (0,0))
        self.screen.blit(self.fadesurface, (0,0))

        
    def step(self):
        for i in range(0, self.fadesurface.get_width()):
            for j in range(0, self.fadesurface.get_height()):
                    self.fadesurface.set_at((i, j), self.fadesurface.get_at((i, j))[3])

        self.screen.blit(self.fadesurface, (0,0))
