import datetime
import random
import threading
import pygame


class Candy:
    def __init__(self, screen, max_w, max_h, sx, sy):
        self.anim = 0.98
        self.sx = sx
        self.sy = sy
        self.max_w = max_w
        self.max_h = max_h
        self.color = (255, 0, 0)
        self.index_x = random.randint(0, max_w - 1)
        self.index_y = random.randint(0, max_h - 1)
        print("ball - ", self.index_x, self.index_y)
        self.player_rect = pygame.draw.rect(screen, self.color,
                                            (self.index_x * self.sx,
                                             self.index_y * self.sy,
                                             self.sx * self.anim,
                                             self.sy * self.anim), 0, 20, 20, 20, 20, 20)
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color,
                             (self.index_x * self.sx,
                              self.index_y * self.sy,
                              self.sx * self.anim,
                              self.sy * self.anim), 0, 20, 20, 20, 20, 20)

    def kill(self):
        self.alive = False

    def respawn(self, screen, player):
        self.index_x = random.randint(0, self.max_w - 1)
        self.index_y = random.randint(0, self.max_h - 1)

        while (self.index_x * self.sx, self.index_y * self.sy) in player.body:
            self.index_x = random.randint(0, self.max_w - 1)
            self.index_y = random.randint(0, self.max_h - 1)

        self.player_rect = pygame.draw.rect(screen, self.color,
                                            (self.index_x * self.sx,
                                             self.index_y * self.sy,
                                             self.sx,
                                             self.sy), 0, 20, 20, 20, 20, 20)
        self.alive = True

    def animate(self):
        self.anim = self.anim * 0.95 if self.anim == 0.98 else 0.98
