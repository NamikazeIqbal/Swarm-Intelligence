
"""
Created on Fri Aug 12 08:24:33 2022

@author: Muhammad Iqbal Maulana

"""

import pygame
import random
import math

class Boid:
    
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def self(self):
        return self
    
    def flock_centering(self):
        
        pos_x = 0
        pos_y = 0
        
        for i in boids:
            if boids[i].self !=  self.self :
                pos_x += boids[i].x 
                pos_y += boids[i].y
                
        pos_x = pos_x/(len(boids) - 1)
        pos_y = pos_y/(len(boids) - 1)
        
        self.dx += (pos_x - self.x)/100
        self.dy += (pos_y - self.y)/100
        
    def avoid_boid(self):
        
        pos_x = 0
        pos_y = 0
        
        for i in boids:
            if boids[i].self !=  self.self :
                if math.sqrt(abs((boids[i].x - self.x)**2 - ((boids[i].y) - (self.y)**2))) < 60:
                    pos_y = ((boids[i].y) - (self.y))**2
                    pos_x = ((boids[i].x) - (self.x))**2
        
        self.dx += pos_x
        self.dy += pos_y
        
    def velocity_matching(self):
        
        x_vel = 0
        y_vel = 0
        
        for i in boids:
            if boids[i].self !=  self.self :
                x_vel += boids[i].dx 
                x_vel += boids[i].dy
                
        x_vel = x_vel/(len(boids) - 1)
        y_vel = y_vel/(len(boids) - 1)
        
        x_vel = x_vel/80
        y_vel = y_vel/80
        
        self.dx += x_vel
        self.dy += y_vel 
        
    def bound_boid(self):
        x_max = 600
        y_max= 400
        x_min = 200
        y_min = 100
        
        if self.x > x_max:
            self.dx = -10 + 0.5
        if self.y > y_max:
            self.dy = -10 + 0.5
        
        if self.x < x_min:
            self.dx = 10 + 0.5
        if self.y < y_min:
            self.dy = 10 + 0.5
        
        
def init_boids(num_boids):
    
    global boids
    boids = {}
    
    i = 0
    
    for j in range(num_boids):
        i += 1
        boids["boid" + str(i)] = Boid(random.randint(0, 10), random.randint(0, 10),0.1,0.1)

def move_boids():
    for i in boids:
        boids[i].flock_centering()
        boids[i].avoid_boid()
        boids[i].velocity_matching()
        boids[i].bound_boid()

        boids[i].x  += boids[i].dx
        boids[i].y  += boids[i].dy
        
    

pygame.init()
window = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
run = True
window.fill((0, 0, 0))

#inilisasi boid
init_boids(5)

for i in boids:
    pygame.draw.circle(window, (255,255,255), (boids[i].x, boids[i].y), 2)
    pygame.display.update()
    
while run:

    clock.tick(10)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

         
    
    #update posisi boid
    move_boids()
    for i in boids:
        pygame.draw.circle(window, (255,255,255), (boids[i].x, boids[i].y), 2)
        
    pygame.display.update()
    window.fill((0, 0, 0))
        
        
        
                    
            
                
        