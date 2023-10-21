import pygame
from setting import *
from tile import *
from player import *
from debug import debug
class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        #set visible and obstancles
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        #sprite setup
        self.create_map()
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites,self.obstacles_sprites])#output rock
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites],self.obstacles_sprites)#output player

    def run(self):
        #update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)