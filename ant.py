
import random
from graph import *


pow_distance = 4
pow_pheromone = 0.2
evap_factor = 0.5

class Swarm:
    def __init__(self, agent_count):
        self.count = agent_count
        self.ants = []
        self.map = Graph()
        #self.pheromone = Graph()
        for i in range(agent_count):
            self.ants.append(Ant(random.randint(0, 9), self.map))





class Ant:
    SIZE = 5
    def __init__(self, start, map: Graph):
        self.map = map
        self.route = []
        self.start = start
        self.current = self.map.cities[start][start]
        self.old_x = self.map.cities[start][start].loc_x
        self.old_y = self.map.cities[start][start].loc_y
        self.new_x = 0
        self.new_y = 0
        self.color = self.get_color()

    def get_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def evaporate(self):
        for cities in self.map.cities:
            for city in cities:
                if city.vals[2]==0:
                    continue
                else:
                    city.vals[2]-=evap_factor*city.vals[2]

    def calc_desirability(self):
        x = self.current.vals[0]
        distances = self.map.cities[x]
        #print(distances)
        desirabilities = []
        for distance in distances:
            #print(distance)
            if distance.vals[0] not in self.route:
                desirability = pow(1/distance.vals[1], pow_distance)+pow(distance.vals[2], pow_pheromone)
            else:
                desirability = 0
            desirabilities.append(desirability)

        return desirabilities

    def nextNode(self):
        desirabilities = self.calc_desirability()
        desirabilities = [100*x for x in desirabilities]
        #print(desirabilities)
        next_node_ls = random.choices(self.map.cities[self.current.vals[0]], weights=desirabilities)
        next_node = next_node_ls[0].vals[0]
        #print(next_node)
        #print(next_node_ls[0])
        #print(self.map.cities[self.current[0]][next_node][2])
        self.map.cities[self.current.vals[0]][next_node].vals[2] += pow_pheromone
        self.map.cities[next_node][self.current.vals[0]].vals[2] += pow_pheromone
        #self.route.append(next_node)
        return next_node_ls[0]

    def ant_trail(self):
        if len(self.route)==CITIES+1:
            return self.route
        self.route.append(self.start)
        while len(self.route) < len(self.map.cities[0]):
            self.current = self.nextNode()
            self.route.append(self.current.name)
            self.new_x = self.current.loc_x
            self.new_y = self.current.loc_y
            self.evaporate()
        self.route.append(self.start)
        return self.route

    def draw(self):
        draw.circle(screen, self.color, (self.old_x, self.old_y), Ant.SIZE)

    def move(self):
        if self.old_x==self.new_x and self.old_y==self.new_y:
            return 0
        dx = self.old_x - self.new_x
        dy = self.old_y - self.new_y
        dist = pow(dx*dx+dy*dy, 0.5)
        vx = int(dx*2/dist)
        vy = int(dy*2/dist)
        self.old_x-=vx
        self.old_y-=vy





# s= Swarm(10)
# for ant in s.ants:
#     route = ant.ant_trail()
#     print(route)
