<h1 align="center">Snake-NEAT</h1><br>
<p align="center">
  <img alt="Snake-NEAT" title="Snake-NEAT" src="https://user-images.githubusercontent.com/94694895/209307089-d58b8b2c-af66-485a-a187-35c1d4f24717.gif" width="450"><br>
</p>

<h4 align="center">A self-learning snake game implemented using genetic NEAT algorithm (NeuroEvolution of Augmenting Topologies)</h4>

## About

Project developed for fun and acquiring knowledge while serving in the army.

## Project

After 1500 generations snake's best score was 70 apples.

## How to run

Install dependencies

```bash
pip install -r proj_requirements.txt
```

Run

```bash
python main.py
```

## Dependencies

* **[Pygame](https://github.com/pygame/)**: Pygame is a cross-platform set of Python modules designed for writing video games.
* **[neat-python](https://github.com/CodeReclaimers/neat-python)**: NeuroEvolution of Augmenting Topologies (NEAT) is a genetic algorithm (GA) for the generation of evolving artificial 
                                                                    neural networks (a neuroevolution technique) developed by Kenneth Stanley .

## Fitness function (in SnakeBoard.py)

* If we detect a collision between snake's head to the wall - Decreasing fitness by 10 points.

* If we detect a collision between snake's head to his body - Decreasing fitness by 10 points.

* If we detect that the snake is eating food (candy) - Increasing fitness by 20 points.

## Inputs

1. **player.getX**: location of player in axis x
2. **player.getY**: location of player in axis y
3. **player.getDirection**: get direction of the snake (up, down..)
4. **player.getDistanceFromCandy**: get snake's distance from candy
5. **player.getAngleFromCandy**: get the angle between them
6. **player.isFoodUp\Down\Left\Right**: where is the food (candy)
7. **player.isMyEntireUp\Down\Left\RightClear**: check where is the snake's body
8. **player.getDistanceFromLeft\Right\Top\BottomWall**: get the distance between snake's head to each wall

> You can see those inputs in SnakeBoard.py

<p align="center">
  <img alt="Training Mode" title="Training Mode" src="https://user-images.githubusercontent.com/94694895/209309634-d521e192-3d14-48b6-97de-177ff75d60ff.gif" width="450"><br>
</p>

## Outputs

* **0**: Turn left
* **1**: Turn right
* **2**: Turn up
* **3**: Turn down
