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
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        #sprite setup
        self.create_map()
    def create_map(self):
        #print game map
        #for row_index, row in enumerate(WORLD_MAP):
        #    for col_index, col in enumerate(row):
        #        x = col_index * TILESIZE
        #        y = row_index * TILESIZE
        #        #set x is rock and p is player
        #        if col == 'x':
        #            Tile((x, y), [self.visible_sprites,self.obstacles_sprites])#output rock
        #        if col == 'p':
        #            self.player = Player((x, y), [self.visible_sprites],self.obstacles_sprites)#output player
        self.player = Player((400, 300), [self.visible_sprites], self.obstacles_sprites)  # output player
    def run(self):
        #update and draw the game when move
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


#create camera
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()#from window form into map left and top

        #creating the floor
        self.floor_surf = pygame.image.load('D:/drive/Project (1)/Game/Zelda_game/UI/UI/graphics/tilemap/ground.png').convert()#input the image the floor
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self,player):

        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft-self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):#character font the rock when character font the rock
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)