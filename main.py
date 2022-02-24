import pygame
import numpy
import time
import sys
from pygame.locals import *
import random
import bounceingcorners
import turtletrace
import transition
import trappedknight

screensize = (800, 480)


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(screensize)
    screen.fill((0, 0, 0))
    pygame.display.update()

    framerate = 60
    cumulativetime = 0

    running = True
    framelimiter = False
    steplimiter = False

    effectindex = 0

    effect0 = bounceingcorners.Bounceingcorners(screen)
    effect1 = turtletrace.Turtletrace(screen)
    effect2 = trappedknight.Trappedknight(screen, 200)
    effects = []

    effects.append(effect0)
    effects.append(effect1)
    effects.append(effect2)

    trans = transition.Transition(screen)
    trans = transition.Transition(screen)

    lastframe = pygame.time.get_ticks()

    start = time.time()

    while running:
        t = pygame.time.get_ticks()
        dt = (t - lastframe) / 1000.0
        cumulativetime += dt
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                effect1.freeroam = not effect1.freeroam
                effect1.cameraposition = (-effect1.position[0] + screen.get_width() / 2, -effect1.position[1] + screen.get_height() / 2)
         

        currenttime = time.time() - start

        if cumulativetime > 1 / framerate and framelimiter:
           
            if effect1.freeroam:
                key_input = pygame.key.get_pressed()
                if key_input[pygame.K_LEFT]:
                    effect1.cameraposition = (effect1.cameraposition[0] + 5, effect1.cameraposition[1])
                if key_input[pygame.K_RIGHT]:
                    effect1.cameraposition = (effect1.cameraposition[0] - 5, effect1.cameraposition[1])
                if key_input[pygame.K_UP]:
                    effect1.cameraposition = (effect1.cameraposition[0], effect1.cameraposition[1] + 5)
                if key_input[pygame.K_DOWN]:
                    effect1.cameraposition = (effect1.cameraposition[0], effect1.cameraposition[1] - 5)
            ###
            ###write effects below
            ###i
            effects[2].step()

            pygame.display.update()
            ###
            ###write effects above
            ###
            cumulativetime = 0
        elif not framelimiter:
            
            effects[2].step()
            pygame.display.update()
            cumulativetime = 0
            if effect1.freeroam:
                key_input = pygame.key.get_pressed()
                if key_input[pygame.K_LEFT]:
                    effect1.cameraposition = (effect1.cameraposition[0] + 5, effect1.cameraposition[1])
                if key_input[pygame.K_RIGHT]:
                    effect1.cameraposition = (effect1.cameraposition[0] - 5, effect1.cameraposition[1])
                if key_input[pygame.K_UP]:
                    effect1.cameraposition = (effect1.cameraposition[0], effect1.cameraposition[1] + 5)
                if key_input[pygame.K_DOWN]:
                    effect1.cameraposition = (effect1.cameraposition[0], effect1.cameraposition[1] - 5)

        lastframe = t
        dt = 0
    
    pygame.quit()
    sys.exit(0)

    # pygame.draw.rect(screen, BLUE, (0, 0, 100, 100))


if __name__ == "__main__":
    main()
