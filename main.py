import neat
import os
import pygame
import SnakeBoard
import Player
import Candy


def eval_genomes(genomes, config):
    pygame.init()

    MATRIX = 20
    SCREEN_HEIGHT, SCREEN_WIDTH = 700, 700

    sx, sy = int(SCREEN_WIDTH / MATRIX), int(SCREEN_HEIGHT / MATRIX)
    max_w = (SCREEN_WIDTH + sx - 1) // sx
    max_h = (SCREEN_HEIGHT + sy - 1) // sy

    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0
        board = SnakeBoard.SnakeBoard('Snake By Tomer Shein', width=SCREEN_WIDTH, height=SCREEN_HEIGHT, sx=sx,
                                      sy=sy)
        board.build_screen()
        player = Player.Player(board.screen_pointer, max_w=max_w, max_h=max_h, sx=sx, sy=sy)
        candy = Candy.Candy(board.screen_pointer, max_w=max_w, max_h=max_h, sx=sx, sy=sy)
        board.train_ai(genome1, config, player, candy)


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    p.run(eval_genomes, 300)

    # Display the winning genome.
    # print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    run(config_path)
