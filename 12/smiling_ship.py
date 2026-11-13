import pygame

class SmilingShip:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load('images/Smiling-spaceship-game-character.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_down = False
        self.moving_up = False

    def update_position(self):
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top >= 0:
            self.y -= self.settings.ship_speed

        self.rect.y = self.y


    def draw(self):
        self.screen.blit(self.image, self.rect)