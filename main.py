import pygame, sys
from setting import *
from debug import *
from level import *
from setting import *
class Game:#create class with name Game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))#set width and heigth for screen
        pygame.display.set_caption('Zelda')#set name for window
        self.clock = pygame.time.Clock()#clock count back to start game
        self.level = Level()#level for character
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#if even is quick, end the game
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')#set up background for screen
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()


