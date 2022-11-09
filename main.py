import numpy as np
from pygame import *
import pygame
from ant import *
#from ant import Ant, Swarm




def fit(swarm : Swarm):
    run = True
    while run:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        for city in swarm.map.cities[0]:
            city.draw()

        routes = []
        print(".....Travelling Ants ......")
        for ant in swarm.ants:
            route = ant.ant_trail()
            for i in route:
                new_x = swarm.map.towns[i].loc_x
                new_y = swarm.map.towns[i].loc_y
                ant.new_x = new_x
                ant.new_y = new_y
                print(i, end=" ")
                while ant.move()!=0:
                    ant.draw()
                    display.update()
            print("")
        #break


s = Swarm(6)
fit(s)