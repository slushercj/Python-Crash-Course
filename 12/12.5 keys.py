import pygame
import sys

class KeysGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Key's game")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(event.key)

            pygame.display.flip()

if __name__ == '__main__':
    kg = KeysGame()
    kg.run_game()