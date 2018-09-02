# Sudoku Solver

This Python script solves a _relaxed_ N x N Sudoku grid, _with only constraints on rows and columns_.

## Input
The script reads the following from `stdin` (Standard Input):
- `n` - Size of the Sudoku grid.
- Followed by a new line each, `n` lines of input, each containing exactly `n` characters, each representing a grid cell.

For each cell:
- `1, 2, ... n` as grid symbols.
- Any non digit characters represents an empty grid.

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
