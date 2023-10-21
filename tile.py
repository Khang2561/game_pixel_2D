import pygame
from setting import *

class Tile(pygame.sprite.Sprite):
    #create a basic rock
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('D:/drive/Project (1)/Game/Zelda_game/UI/UI/graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        #create the hitbox for rock
        self.hitbox = self.rect.inflate(0,-10)#top and bottom -10
