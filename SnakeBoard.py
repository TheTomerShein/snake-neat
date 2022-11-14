import math

import neat.nn
import pygame


def food_collision(p, c):
    if p.index_x == c.index_x and p.index_y == c.index_y:
        return True
    return False


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

    def building_net(self):
        for i in range((self.width + self.sx - 1) // self.sx):
            for j in range((self.height + self.sy - 1) // self.sy):
                c = (154, 221, 125) if (i + j) % 2 == 0 else (165, 230, 137)
                pygame.draw.rect(self.screen_pointer, c, (i * self.sx, j * self.sy, self.sx, self.sy))

    def train_ai(self, genome1, config, player, candy):
        nn = neat.nn.FeedForwardNetwork.create(genome1, config)
        clock = pygame.time.Clock()

        while True:
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # nn_output = nn.activate(
            #     (abs(player.index_x - candy.index_x),
            #      abs(player.index_y - candy.index_y)))
            # nn_decision = nn_output.index(max(nn_output))
            nn_output = nn.activate(
                [math.sqrt((player.index_x - candy.index_x) ** 2 + (player.index_y - candy.index_y) ** 2),
                 abs(player.index_x - candy.index_x),
                 abs(player.index_y - candy.index_y), ])
            nn_decision = nn_output.index(max(nn_output))
            player.handle_keys_ai(nn_decision)

            # print(nn_output)

            self.building_net()
            player.handle_keys()
            player.draw(self.screen_pointer)
            candy.draw(self.screen_pointer)
            pygame.display.update()

            if player.handle_touching_limits() or player.handle_head_and_body_collision() or player.score > 20:
                genome1.fitness += player.score
                print(player.score)
                break

            if food_collision(player, candy):
                player.score += 1
                candy.kill()
                candy.respawn(self.screen_pointer, player)
                player.increase_body()
