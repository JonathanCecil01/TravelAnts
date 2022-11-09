import numpy as np
import random
import pygame
from pygame import *
import math

pygame.font.init()
init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


CITIES = 10
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
class Town:
    SIZE = 11
    def __init__(self, name):
        self.name = name
        self.loc_x = random.randint(0, SCREEN_WIDTH)
        self.loc_y = random.randint(0, SCREEN_HEIGHT)


class City:
    SIZE = 12
    def __init__(self):
        self.name = 0
        self.vals = []
        self.loc_x = random.randint(0, SCREEN_WIDTH)
        self.loc_y = random.randint(0, SCREEN_HEIGHT)
        self.color = (255, 255, 255)

    def draw(self):
        draw.circle(screen, self.color, (self.loc_x, self.loc_y), City.SIZE)

class Graph:
    def __init__(self):
        self.cities = []
        self.towns = []
        self.set_towns()
        self.set_cities()



    def set_towns(self):
        for i in range(CITIES):
            self.towns.append(Town(i))

    def set_cities(self):
        for i in range(CITIES):
            city = []
            for j in range(CITIES):
                if i == j:
                    c  = City()
                    c.vals = [i, 0, 0]
                    c.name = i
                    city.append(c)
                    continue
                c = City()
                c.vals = [j, math.dist((self.towns[i].loc_x,self.towns[i].loc_y), (self.towns[j].loc_x, self.towns[j].loc_y)), 0]
                c.name = j
                city.append(c)
            self.cities.append(city)

        for i in range(CITIES):
            for j in range(CITIES):
                self.cities[i][j].loc_x = self.towns[self.cities[i][j].name].loc_x
                self.cities[i][j].loc_y = self.towns[self.cities[i][j].name].loc_y

    def display(self):
        print(self.cities[0])

# g = Graph()
# g.display()

