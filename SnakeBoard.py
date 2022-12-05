import datetime
import math
import time
import neat.nn
import pygame


def food_collision(p, c):
    if p.getX() == c.getX() and p.getY() == c.getY():
        return True
    return False


def getAngle(p, c):
    return math.atan2((p.index_x - c.index_x), (p.index_y - c.index_y))

def getDistance(p, c):
    return math.sqrt((p.index_x - c.index_x) ** 2 + (p.index_y - c.index_y) ** 2)


def isFoodUp(p, c) -> int:
    if p.index_y > c.index_y:
        return 1
    return 0


def isFoodDown(p, c) -> int:
    if p.index_y < c.index_y:
        return 1
    return 0


def isFoodLeft(p, c) -> int:
    if p.index_x > c.index_x:
        return 1
    return 0


def isFoodRight(p, c) -> int:
    if p.index_x < c.index_x:
        return 1
    return 0


class SnakeBoard:
    def __init__(self, name, height, width, sx, sy):
        self.screen_pointer = None
        self.board_name = name
        self.width = width
        self.height = height
        self.sx = sx
        self.sy = sy

    def build_screen(self):
        self.screen_pointer = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.board_name)

        LIGHT_GREEN = (144, 238, 144)
        self.screen_pointer.fill(LIGHT_GREEN)

    def board_background(self):
        for i in range((self.width + self.sx - 1) // self.sx):
            for j in range((self.height + self.sy - 1) // self.sy):
                c = (154, 221, 125) if (i + j) % 2 == 0 else (165, 230, 137)
                pygame.draw.rect(self.screen_pointer, c, (i * self.sx, j * self.sy, self.sx, self.sy))

    def train_ai(self, genome1, config, player, candy):
        nn = neat.nn.FeedForwardNetwork.create(genome1, config)
        clock = pygame.time.Clock()
        start_time = datetime.datetime.now()

        # last_dist = 0
        while True:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            nn_output = nn.activate(
                [player.getX(),
                 player.getY(),
                 candy.getX(),
                 candy.getY(),
                 player.moving_side_to_int(),
                 getAngle(player, candy),
                 getDistance(player, candy),
                 isFoodUp(player, candy),
                 isFoodDown(player, candy),
                 isFoodLeft(player, candy),
                 isFoodRight(player, candy),
                 player.distanceFromLeftWall(),
                 player.distanceFromRightWall(),
                 player.distanceFromUpperWall(),
                 player.distanceFromBottomWall(),
                 ])
            nn_decision = nn_output.index(max(nn_output))
            player.handle_keys_ai(nn_decision)

            self.board_background()
            player.draw(self.screen_pointer)
            candy.draw(self.screen_pointer)
            pygame.display.update()

            if player.handle_touching_limits() or player.handle_head_and_body_collision():
                genome1.fitness -= 25
                print("score ", player.score, genome1.fitness)
                break

            # if abs(datetime.datetime.now().second - start_time.second) >= 10 or \
            #         abs(datetime.datetime.now().minute - start_time.minute) >= 1:
            #     genome1.fitness -= 25
            #     print("score ", player.score, genome1.fitness)
            #     break

            if food_collision(player, candy):
                genome1.fitness += 50
                candy.kill()
                candy.respawn(self.screen_pointer, player)
                player.increase_body()
                player.increaseScore()

            # genome1.fitness += 0.1  # fitness is the score of the snake
            # curr_dist = getDistance(player, candy)
            # if last_dist > curr_dist:
            #     genome1.fitness += 1
            #     last_dist = curr_dist
            # else:
            #     genome1.fitness -= 1
            #     last_dist = curr_dist
