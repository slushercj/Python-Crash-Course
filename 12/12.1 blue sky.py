import sys
import pygame

class BlueSky:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('BlueSky')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((135, 206, 235))
            pygame.display.flip()

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()