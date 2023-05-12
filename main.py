import sys
import time

import pygame

import bounceingcorners
import trappedknight
import turtletrace
import transition

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
    framelimiter = True
    steplimiter = False
    intransition = False

    effectindex = 0
    transitionindex = 0

    effect0 = bounceingcorners.Bounceingcorners(screen)
    effect1 = turtletrace.Turtletrace(screen)
    effect2 = trappedknight.Trappedknight(screen, 200)
    effects = []

    transition0 = transition.Transition(screen)
    transitions = []


    effects.append(effect0)
    effects.append(effect1)
    effects.append(effect2)

    transitions.append(transition0)

    lastframe = pygame.time.get_ticks()

    start = time.time()

    frames = 0

    while running:
        t = pygame.time.get_ticks()
        dt = (t - lastframe) / 1000.0
        cumulativetime += dt
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                effectindex += 1
                if effectindex >= len(effects):
                    effectindex = 0
                transitions[transitionindex].starttransition(screen, 120)
                effects[effectindex].reinit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                effect1.freeroam = not effect1.freeroam
                effect1.cameraposition = (-effect1.position[0] + screen.get_width() / 2, -effect1.position[1] + screen.get_height() / 2)

        effects[effectindex].step()


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
            ###
            transitions[transitionindex].step()
            pygame.display.update()
            cumulativetime = 0
            #print(effectindex)

            #pygame.display.update()
            ###
            ###write effects above
            ###

        #elif not framelimiter:
            
         #   effects[effectindex].step()
          #  transitions[transitionindex].step()
           # pygame.display.update()
            #cumulativetime = 0

            #if effect1.freeroam:
             #   key_input = pygame.key.get_pressed()
              #  if key_input[pygame.K_LEFT]:
               #     effect1.cameraposition = (effect1.cameraposition[0] + 5, effect1.cameraposition[1])
                #if key_input[pygame.K_RIGHT]:
                 #   effect1.cameraposition = (effect1.cameraposition[0] - 5, effect1.cameraposition[1])
                #if key_input[pygame.K_UP]:
                 #   effect1.cameraposition = (effect1.cameraposition[0], effect1.cameraposition[1] + 5)
                #if key_input[pygame.K_DOWN]:
                 #   effect1.cameraposition = (effect1.cameraposition[0], effect1.cameraposition[1] - 5)

        lastframe = t
        dt = 0
    
    pygame.quit()
    sys.exit(0)



    # pygame.draw.rect(screen, BLUE, (0, 0, 100, 100))


if __name__ == "__main__":
    main()

