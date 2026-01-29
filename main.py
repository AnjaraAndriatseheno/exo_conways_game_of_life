import numpy as np
import time


ROWS = 7
COLS = 7

frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
])

def count_neighbors(padded_grid, i, j):
   
    neighbors = padded_grid[i-1:i+2, j-1:j+2]
    return np.sum(neighbors) - padded_grid[i, j]

def next_generation(grid):
   
    new_grid = np.zeros_like(grid)

    # Ajout du zero padding
    padded_grid = np.pad(grid, pad_width=1, mode='constant', constant_values=0)

    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            alive = padded_grid[i, j]
            neighbors = count_neighbors(padded_grid, i, j)

            if alive == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[i-1, j-1] = 1
            elif alive == 0 and neighbors == 3:
                new_grid[i-1, j-1] = 1
            else:
                new_grid[i-1, j-1] = 0

    return new_grid


generation = 0
while True:
    print(f"Génération {generation}")
    print(frame)
    print("-" * 20)

    frame = next_generation(frame)
    generation += 1
    time.sleep(1)
