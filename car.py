from math import sin, cos, pi
import pygame

def relu(x):
    if x > 0:
        return x
    return 0

def cap(x, a, b):
    if x > a:
        if x < b:
            return x
        else:
            return b
    else:
        return a

class Car:
    def __init__(self):
        self.pos = [800, 100]
        self.vvec = [0,0]
        self.angle = 0
        self.vel = 0
        self.MAX_ACC=50
        self.MAX_VEL=100
        self.HEIGHT = 14
        self.WIDTH = 6
        self.MAX_R = 60
    
    def corner_points(self):
        h2 = self.HEIGHT /2 
        w2 = self.WIDTH /2
        alpha = self.angle * pi / 180
        points = []
        x = self.pos[0]
        y = self.pos[1]
        for i,j in ((1, 1), (1, -1), (-1, -1), (-1, 1)):
            dx = i * h2 * cos(alpha) - j * w2 * sin(alpha)
            dy = i * h2 * sin(alpha) + j * w2 * cos(alpha)
            points.append([x+dx, y+dy])
        return points

    def update(self, acc=0, turn = 0, dt=0.01, overboard=0):
        drag = 0.005 * self.vel ** 2 + 10 * overboard
        a = self.MAX_ACC * acc - drag
        alpha = self.angle * pi / 180
        self.vel = max(0, self.vel + a * dt / 1000)
        self.vvec = [self.vel * cos(alpha), self.vel * sin(alpha)]
        self.pos[0] += self.vvec[0] * dt / 1000
        self.pos[1] += self.vvec[1] * dt / 1000
        self.angle += self.vel * turn * dt * 180 / (max(self.MAX_R, 0.025 * self.vel ** 2) * 1000 * pi)

    def render(self, screen):
        pygame.draw.polygon(screen, 'yellow', self.corner_points())
    
    def view(self, screen):
        alpha = self.angle * pi / 180
        x_, y_ = self.pos[0] - 640, self.pos[1] - 360
        nx_ = x_ * cos(alpha) + y_ * sin(alpha)
        ny_ = -x_ * sin(alpha) + y_ * cos(alpha)
        rotscr = pygame.transform.rotate(screen, self.angle)
        rect = rotscr.get_rect()
        nx = rect.width / 2 + nx_
        ny = rect.height / 2 + ny_
        trimmed = pygame.Surface((400, 200))
        trimmed.fill('purple')
        trimmed.blit(rotscr, (0,0), (nx-100, ny-100, 400, 200))
        return trimmed
        

car = Car()