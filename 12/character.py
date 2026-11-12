import pygame

class Character:

    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/death_speaker2.png')
        # self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
