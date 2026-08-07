# A* Search for the 8-Puzzle

A Python implementation of the **A\*** (A-Star) search algorithm to solve the classic **8-puzzle problem**. The program searches for the lowest-cost sequence of moves required to transform an initial puzzle configuration into a specified goal configuration using a heuristic-guided search.

This project was created as an introduction to artificial intelligence search algorithms and heuristic-based pathfinding.

---

## Features

- Solves the 8-puzzle using the A* search algorithm
- Uses the Manhattan distance heuristic
- Supports user-defined start and goal states
- Demonstrates heuristic search in a simple console application
- Uses custom movement costs for each tile movement direction

---

## Algorithm

A* evaluates each puzzle state using the following evaluation function:

```
f(n) = g(n) + h(n)
```

Where:

- **g(n)** is the accumulated path cost from the initial state.
- **h(n)** is the heuristic estimate of the remaining cost to reach the goal.
- **f(n)** is the estimated total cost.

The program maintains a frontier of possible puzzle states, always expanding the state with the lowest estimated cost until the goal configuration is reached.

---

## Heuristic

This implementation uses a modified **Manhattan Distance** heuristic.

Unlike the traditional 8-puzzle where each move has equal cost, this project assigns different movement costs:

| Move | Cost |
|------|-----:|
| Left | 2 |
| Right | 2 |
| Down | 1 |
| Up | 3 |

The accumulated movement cost becomes the node's `g(n)` value while the heuristic estimates the remaining distance to the goal.

---

## Example Input

Initial state:

```
1 2 3
4 - 6
7 5 8
```

Goal state:

```
1 2 3
4 5 6
7 8 -
```

---

## Running the Program

Clone the repository:

```bash
git clone https://github.com/AustinHall2424/AI-AStar.git
```

Navigate to the project:

```bash
cd AI-AStar
```

Run the program:

```bash
python main.py
```

The program will prompt for:

1. Initial puzzle state
2. Goal puzzle state

Each row should be entered on a separate line with spaces between values. Use `-` to represent the blank tile.

---

## Example Output

During execution the program displays:

- Current puzzle configuration
- Current path cost (`g`)
- Heuristic value (`h`)
- The sequence of explored puzzle states

Once the heuristic reaches zero, the goal state has been found.

---

## Concepts Demonstrated

- Artificial Intelligence
- A* Search
- Heuristic Search
- State Space Search
- Graph Traversal
- Priority-Based Search
- Python Programming

---

## Limitations

This project was developed as an educational demonstration and does not include some optimizations commonly found in production implementations, such as:

- Duplicate state detection
- Closed-set lookup using hashing
- Solvability checking
- Path reconstruction from the goal state
- Priority queue (`heapq`) for the frontier
