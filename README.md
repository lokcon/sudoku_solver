# Sudoku Solver

This Python script solves a relaxed N x N Suduku grid, with only rows and columns constraints.

## Input
The scripts read the following from `stdin` (Standard Input)
- `n` - Size of the Sudoku Grid.
- Followed by a new line, `n` lines of input, each containing exactly `n` characters, each representing a grid.

For each cell:
- `1, 2, ... n`.
- Any non digit characters represents an empty grid

### Example Input
```
3
123
3.2
231
```

In the example above, the input is a 3 x 3 grid, with the centre grid empty.

### Example Output
```
---- Input ----
1 2 3
3 _ 2
2 3 1

---- Full Solution ----
1 2 3
3 1 2
2 3 1

---- Solution ----
_ _ _
_ 1 _
_ _ _
```
