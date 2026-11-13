import sys
import pygame

from smiling_ship import SmilingShip
from sideways_shooter_settings import SidewaysShooterSettings
from sideways_shooter_bullet import SidewaysShooterBullet

class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.settings = SidewaysShooterSettings()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.ship = SmilingShip(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption('Sideways Shooter')

    def run_game(self):
        while True:
            self.handle_events()
            self.update_game()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._handleKeyDown(event)
            if event.type == pygame.KEYUP:
                self._handleKeyUp(event)

    def update_game(self):
        self.ship.update_position()
        self._update_bullets()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)

    def render(self):
        self.screen.fill((30, 30, 30))
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()
        pygame.display.flip()

    def _handleKeyDown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.max_bullets:
            new_bullet = SidewaysShooterBullet(self)
            self.bullets.add(new_bullet)

    def _handleKeyUp(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False


if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()