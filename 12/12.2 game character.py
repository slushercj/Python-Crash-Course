import sys
import pygame

from character import Character

class GameCharacter:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        self.character = Character(self)

        pygame.display.set_caption('The Witcher')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((130, 200, 235))
            self.character.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    gc = GameCharacter()
    gc.run_game()