# Sudoku Solver

The project's goal is to solve Sudoku puzzles.


### How to run

Install NumPy. 

```
pip install numpy
```

Create a 9x9 2D NumPy array representing the unsolved Sukdoku puzzle. For example

```
board = np.array([
    [9, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 8, 0, 0, 0, 7, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 3],
    [0, 9, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0]
])
```

Pass the NumPy array to the solve function. 

```
solve(board)
```


## Authors

* **James Nanji** - [ninjananjo](https://github.com/ninjananjo)