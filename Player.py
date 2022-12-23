import math
import random
import pygame


class Player:
    def __init__(self, screen, max_w, max_h, sx, sy):
        self.score = 0
        self.sx = sx
        self.sy = sy
        self.max_w = max_w
        self.max_h = max_h
        self.color = (100, 100, 100)
        self.index_x = random.randint(0, self.max_w - 1)
        self.index_y = random.randint(0, self.max_h - 1)
        self.sticky_note = None
        self.player_rect = pygame.draw.rect(screen, self.color,
                                            (self.index_x * self.sx,
                                             self.index_y * self.sy,
                                             self.sx,
                                             self.sy), 0)
        self.body = [(self.index_x * self.sx, self.index_y * self.sy)]

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, self.color,
                             (x, y,
                              self.sx,
                              self.sy), 0)

    def handle_head_and_body_collision(self):
        return self.body[0] in self.body[1:]

    def handle_touching_limits(self):
        if self.index_x >= self.max_w or self.index_x < 0 or self.index_y >= self.max_h or self.index_y < 0:
            return True
        return False

    def handle_keys_ai(self, index):
        if index == 0 and self.sticky_note != 'right':
            self.index_x -= 1
            self.sticky_note = 'left'
        elif index == 1 and self.sticky_note != 'left':
            self.index_x += 1
            self.sticky_note = 'right'
        elif index == 2 and self.sticky_note != 'down':
            self.index_y -= 1
            self.sticky_note = 'up'
        elif index == 3 and self.sticky_note != 'up':
            self.index_y += 1
            self.sticky_note = 'down'
        elif self.sticky_note == 'right':
            self.index_x += 1
        elif self.sticky_note == 'left':
            self.index_x -= 1
        elif self.sticky_note == 'up':
            self.index_y -= 1
        elif self.sticky_note == 'down':
            self.index_y += 1

        self.body.pop()
        self.body.insert(0, (self.index_x * self.sx, self.index_y * self.sy))

    def getDirection(self):
        if self.sticky_note == 'up':
            return 1
        if self.sticky_note == 'down':
            return 2
        if self.sticky_note == 'left':
            return 3
        if self.sticky_note == 'right':
            return 4
        return 5

    def increase_body(self):
        self.body.append(self.body[-1])

    def getX(self):
        return self.index_x

    def getY(self):
        return self.index_y

    def increaseScore(self):
        self.score += 1

    def food_collision(self, c):
        if self.getX() == c.getX() and self.getY() == c.getY():
            return True
        return False

    def getAngleFromCandy(self, c):
        return math.atan2((self.index_x - c.index_x), (self.index_y - c.index_y))

    def getDistanceFromCandy(self, c):
        return math.sqrt((self.index_x - c.index_x) ** 2 + (self.index_y - c.index_y) ** 2)

    def isFoodUp(self, c) -> int:
        if self.index_y > c.index_y:
            return 0
        return 1

    def isFoodDown(self, c) -> int:
        if self.index_y < c.index_y:
            return 0
        return 1

    def isFoodLeft(self, c) -> int:
        if self.index_x > c.index_x:
            return 0
        return 1

    def isFoodRight(self, c) -> int:
        if self.index_x < c.index_x:
            return 0
        return 1

    def getDistanceFromLeftWall(self) -> int:
        return math.dist((self.index_x, self.index_y), (0, self.index_y)) / 10

    def getDistanceFromRightWall(self) -> int:
        return math.dist((self.index_x, self.index_y), (self.max_w, self.index_y)) / 10

    def getDistanceFromTopWall(self) -> int:
        return math.dist((self.index_x, self.index_y), (self.index_x, 0)) / 10

    def getDistanceFromBottomWall(self) -> int:
        return math.dist((self.index_x, self.index_y), (self.max_w, self.max_h)) / 10

    def isMyEntireDownClear(self) -> int:
        for x, y in self.body:
            if x == self.index_x and y > self.index_y:
                return 0
        return 1

    def isMyEntireUpClear(self) -> int:
        for x, y in self.body:
            if x == self.index_x and y < self.index_y:
                return 0
        return 1

    def isMyEntireLeftClear(self) -> int:
        for x, y in self.body:
            if y == self.index_y and x < self.index_x:
                return 0
        return 1

    def isMyEntireRightClear(self) -> int:
        for x, y in self.body:
            if y == self.index_y and x > self.index_x:
                return 0
        return 1

    def isMyEntireTopLeftClear(self) -> int:
        for x, y in self.body:
            if x + y < self.index_x + self.index_y:
                return 0
        return 1

    def isMyEntireTopRightClear(self) -> int:
        for x, y in self.body:
            if x + y > self.index_x + self.index_y:
                return 0
        return 1

    def isMyEntireBottomLeftClear(self) -> int:
        for x, y in self.body:
            if x + y > self.index_x + self.index_y:
                return 0
        return 1

    def isMyEntireBottomRightClear(self) -> int:
        for x, y in self.body:
            if x + y < self.index_x + self.index_y:
                return 0
        return 1
