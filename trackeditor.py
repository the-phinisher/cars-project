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
skidoff = False
while running:
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_b]:
        outer = True
    else:
        outer = False
    if keypress[pygame.K_r]:
        delete = True
    else:
        delete = False
    if keypress[pygame.K_g]:
        selall = True
    else:
        selall = False
    if keypress[pygame.K_w]:
        acc = 50
    elif keypress[pygame.K_s]:
        acc = -50
    else:
        acc = 0
    if keypress[pygame.K_a]:
        turn = -25
    elif keypress[pygame.K_d]:
        turn = 25
    else:
        turn = 0
    if keypress[pygame.K_l]:
        skidoff = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepress = pygame.mouse.get_pressed()
            if mousepress[0]:
                if outer:
                    if delete:
                        if selall: outertrack = []
                        elif len(outertrack) > 0: outertrack.pop()
                    else:
                        outertrack.append(pygame.mouse.get_pos())
                else:
                    if delete:
                        if selall: innertrack = []
                        elif len(innertrack) > 0: innertrack.pop()
                    else:
                        innertrack.append(pygame.mouse.get_pos())
    
    dt = clock.tick(60)
    screen.fill("purple")
    if len(outertrack) >= 3: pygame.draw.polygon(screen, 'darkgray', outertrack)
    if len(innertrack) >= 3: pygame.draw.polygon(screen, 'cyan',innertrack)
    car.update(acc, turn, dt)
    car.render(screen)
    carscreen = car.view(screen)
    window.blit(screen, (0, 0))
    window.blit(carscreen, (1280, 0))
    pygame.display.flip()

pygame.quit()

print(innertrack)
innertrack = [','.join(map(str, x)) for x in innertrack]
innertrackcsv = '\n'.join(innertrack)
with open('innertrack.dat', 'w') as file:
    file.write(innertrackcsv)

print(outertrack)
outertrack = [','.join(map(str, x)) for x in outertrack]
outertrackcsv = '\n'.join(outertrack)
with open('outertrack.dat', 'w') as file:
    file.write(outertrackcsv)
