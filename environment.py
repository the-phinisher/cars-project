import pygame
from car import car

with open('outertrack.dat', 'r') as file:
    content = file.read()
try:
    outertrack = [tuple(map(int, i.split(','))) for i in content.split('\n')]
except:
    outertrack = []
print(outertrack)

with open('innertrack.dat', 'r') as file:
    content = file.read()
try:
    innertrack = [tuple(map(int, i.split(','))) for i in content.split('\n') if i !='']
except:
    innertrack = []
print(innertrack)

pygame.init()
screen = pygame.Surface((1280, 720))
window = pygame.display.set_mode((1680, 720))
clock = pygame.time.Clock()
running = True
cum_rew = 0
colors = []
while running:
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w]:
        acc = 1
    elif keypress[pygame.K_s]:
        acc = -1
    else:
        acc = 0
    if keypress[pygame.K_a]:
        turn = -1
    elif keypress[pygame.K_d]:
        turn = 1
    else:
        turn = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60)
    screen.fill("purple")
    if len(outertrack) >= 3: pygame.draw.polygon(screen, 'darkgray', outertrack)
    if len(innertrack) >= 3: pygame.draw.polygon(screen, 'cyan',innertrack)
    nocar = screen.copy()
    nocarscreen = car.view(nocar)
    color = nocarscreen.get_at((100, 100))
    if color == (0, 255, 255, 255): reward = -10
    elif color == (160, 32, 240, 255): reward = -5
    elif color == (169, 169, 169, 255): reward = -1
    car.update(acc, turn, dt, -reward)
    car.render(screen)
    carscreen = car.view(screen)
    cum_rew = 0.9 * reward + 0.1 * cum_rew
    print(cum_rew)
    window.blit(screen, (0, 0))
    window.blit(pygame.transform.rotate(carscreen, 90), (1280, 0))
    window.blit(pygame.transform.rotate(nocarscreen, 90), (1480, 0))
    pygame.display.flip()

pygame.quit()
print(colors)