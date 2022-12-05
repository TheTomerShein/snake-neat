import pickle
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

    max_genome_fitness = 0
    max_genome = None
    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0
        board = SnakeBoard.SnakeBoard('Snake By Tomer Shein', width=SCREEN_WIDTH, height=SCREEN_HEIGHT, sx=sx,
                                      sy=sy)
        board.build_screen()
        player = Player.Player(board.screen_pointer, max_w=max_w, max_h=max_h, sx=sx, sy=sy)
        candy = Candy.Candy(board.screen_pointer, max_w=max_w, max_h=max_h, sx=sx, sy=sy)
        board.train_ai(genome1, config, player, candy)

        if genome1.fitness > max_genome_fitness:
            max_genome_fitness = genome1.fitness
            max_genome = genome1

    pickle.dump(max_genome, open("winner123.pkl", "wb"))


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-978')

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(200))
    # genome = pickle.load(open('winner2.pkl', 'rb'))
    # genomes = [(1, genome)]
    # eval_genomes(genomes, config)
    # p.run(eval_genomes, 100)
    # winner = p.run(eval_genomes, 400)
    # print(winner)
    # pickle.dump(winner, open("winnerr.pkl", "wb"))


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    run(config_path)
