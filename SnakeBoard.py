import neat.nn
import pygame


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
        # start_time = datetime.datetime.now()
        FPS = 25

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            nn_output = nn.activate([
                player.getX(),
                player.getY(),
                player.getDirection(),
                player.getDistanceFromCandy(candy),
                player.getAngleFromCandy(candy),
                player.isFoodUp(candy),
                player.isFoodDown(candy),
                player.isFoodLeft(candy),
                player.isFoodRight(candy),
                player.isMyEntireUpClear(),
                player.isMyEntireDownClear(),
                player.isMyEntireLeftClear(),
                player.isMyEntireRightClear(),
                player.isMyEntireTopLeftClear(),
                player.isMyEntireTopRightClear(),
                player.isMyEntireBottomLeftClear(),
                player.isMyEntireBottomRightClear(),
                player.getDistanceFromLeftWall(),
                player.getDistanceFromRightWall(),
                player.getDistanceFromBottomWall(),
                player.getDistanceFromTopWall(),
            ])
            nn_decision = nn_output.index(max(nn_output))
            player.handle_keys_ai(nn_decision)
            self.board_background()
            player.draw(self.screen_pointer)
            candy.draw(self.screen_pointer)
            pygame.display.update()

            if player.handle_touching_limits() or player.handle_head_and_body_collision():
                genome1.fitness -= 10
                print("score ", player.score, genome1.fitness)
                break

            # if abs(datetime.datetime.now().second - start_time.second) >= 10:
            #     genome1.fitness -= 15
            #     print("score ", player.score, genome1.fitness)
            #     break

            if player.food_collision(candy):
                genome1.fitness += 20
                candy.kill()
                candy.respawn(self.screen_pointer, player)
                player.increase_body()
                player.increaseScore()
