import pygame
from settings import Settings

class Ship:

    def __init__(self, ai_game):

        self.settings = ai_game.settings

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/64_2.png')
        self.image = pygame.transform.smoothscale(self.image, self.settings.ship_size)
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.update()
        self.screen.blit(self.image, self.rect)
