from students import *
import consts
import pygame
from randerer import *


def


pygame.init()
game = True
screen = pygame.display.set_mode((600, 600))
renderer = Renderer(screen)
factory = giveStudentFacroty('Bot', 'DIHT', 2)
student = factory.createUnit()
clock = pygame.time.Clock()
while game:
    pygame.time.delay(15)
    delta_t = clock.tick_busy_loop() / 1000
    renderer.renderStaticUnit(student)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for u in units:
        pygame.display.update()
pygame.quit()
