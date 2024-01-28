# Conway's Game of Life (Python)

This is a Python implementation of the famous Game of Life. This project was created just for fun. 
Maybe some improvements will be done in the future to have a more powerful and modern version.

## Launch the game
In the file [`main.py`](main.py), you can change the global parameters that are present in the header of
the file. You can change the size of the grid, the number of iterations and percentage of initial alive cells.

To launch a game you have to execute the following command:
```bash
python3 main.py
```
## The cells
The cells are represented with the `Cell`class. The cell is randomly initialised according the percentage given in parameter. Two methods were created, one to update the score according the neighborhood of this cell. Then, we can update the state of the cell thanks to this new score.

## The grid
The grid class represents a grid of cells. It has a length and a width and all cell is initialised with a `Cell`. Multiplemethods are defined : to compute all current scores,update the states of all cells, to return a boolean array corresponding to the state of each cell.

### Enjoy! 