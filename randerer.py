from students import *
import consts
import pygame

class Renderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def renderStaticUnit(self, u: Unit):
        x = u.x
        y = u.y
        image = u.imgBody
        self.screen.blit(image, (x, y))

    def rotateImg(self, image, angle):
        """rotate a Surface, maintaining position."""

        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite



