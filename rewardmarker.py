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

with open('rewardlines.dat', 'r') as file:
    content = file.read()
try:
    reward_lines = []
    for line in content.split('\n'):
        x1, y1, x2, y2 = map(int, line.split(','))
        reward_lines.append(((x1, y1), (x2, y2)))
except:
    reward_lines = []
print(reward_lines)

def save():
    x = [(line[0][0], line[0][1], line[1][0], line[1][1]) for line in reward_lines]
    content = '\n'.join([','.join(map(str, line)) for line in x])
    with open('rewardlines.dat', 'w') as file:
        file.write(content)
    print('Saved')
    print(content)

pygame.init()
screen = pygame.Surface((1280, 720))
window = pygame.display.set_mode((1680, 720))
clock = pygame.time.Clock()
running = True
firstpoint = True
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
    if keypress[pygame.K_o]:
        save()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if firstpoint:
                initpoint=pygame.mouse.get_pos()
                firstpoint = False
            else:
                endpoint = pygame.mouse.get_pos()
                firstpoint = True
                reward_lines.append((initpoint, endpoint))

    dt = clock.tick(60)
    screen.fill("purple")
    if len(outertrack) >= 3: pygame.draw.polygon(screen, 'darkgray', outertrack)
    if len(innertrack) >= 3: pygame.draw.polygon(screen, 'cyan',innertrack)
    for line in reward_lines: pygame.draw.line(screen, 'red', line[0], line[1])
    nocar = screen.copy()
    nocarscreen = car.view(nocar)
    car.update(acc, turn, dt)
    car.render(screen)
    carscreen = car.view(screen)
    window.blit(screen, (0, 0))
    window.blit(pygame.transform.rotate(carscreen, 90), (1280, 0))
    window.blit(pygame.transform.rotate(nocarscreen, 90), (1480, 0))
    pygame.display.flip()

pygame.quit()

def save():
    print(reward_lines)
    x = [(line[0][0], line[0][1], line[1][0], line[1][1]) for line in reward_lines]
    content = '\n'.join([','.join(map(str, line)) for line in x])
    with open('rewardlines.dat', 'w') as file:
        file.write(content)
    print('Saved')
    print(content)