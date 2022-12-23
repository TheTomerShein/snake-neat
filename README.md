<h1 align="center">Snake-NEAT</h1><br>
<p align="center">
  <img alt="Snake-NEAT" title="Snake-NEAT" src="https://i.imgur.com/BDdGfBC.gif" width="450"><br>
</p>

<h4 align="center">A self-learning snake game implemented using genetic NEAT algorithm (NeuroEvolution of Augmenting Topologies)</h4>

## About

Project developed for fun and acquiring knowledge while serving in the army.

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

## Fitness function

```python
SnakeLength - TurnedQuantity * 0.01
```

* **SnakeLength**: Snake length defined by how many apples it ate

* **TurnedQuantity**: How many times did the snake change direction, either left or right

## Inputs

1. **cd_left**: Collision-free units at left
2. **cd_top**: Collision-free units at top
3. **cd_right**: Collision-free units at right
4. **cd_bottom**: Collision-free units at bottom
5. **cd_top_left**: Collision-free units at top left
6. **cd_top_right**: Collision-free units at top right
7. **cd_bottom_left**: Collision-free units at bottom left
8. **cd_bottom_right**: Collision-free units at bottom right
9. **apple_x_distance**: If there is an apple on the right or left, this variable contains the distance in units to the apple
10. **apple_y_distance**: If there is an apple on the top or bottom, this variable contains the distance in units to the apple

> You can "see" these inputs in debug mode

<p align="center">
  <img alt="Debug Mode" title="Debug Mode" src="https://i.imgur.com/m60tMox.gif" width="450"><br>
</p>

## Outputs

* **0**: Don't change direction
* **1**: Turn right
* **2**: Turn left
