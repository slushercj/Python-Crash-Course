import pygame

class Rocket:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load('images/rocket.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.moving_right = self.moving_left = self.moving_down = self.moving_up = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update_position(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)