from sys import stdin

def readline():
    return stdin.readline().rstrip()


def readgrid(n):
    repl = lambda x : int(x) if x.isdigit() else 0

    grid = []
    unsolved = []
    for i in range(n):
        in_row = readline()
        row = []
        for j, c in enumerate(in_row):
            row.append(repl(c))
            if repl(c) ==  0:
                unsolved.append((i, j))

        grid.append(row)

    return grid, unsolved


def print_grid(grid, n):
    repl = lambda x : "_" if not x else str(x)
    for i in range(n):
        line = ""
        for c in grid[i]:
            line += (repl(c) + " ")

        print(line)


def valid_row(row):
    reduced = [c for c in row if c]
    return len(set(reduced)) == len(reduced)


def valid_grid(grid, n):
    for row in grid:
        if not valid_row(row):
            return False

    for row in zip(*grid):
        if not valid_row(row):
            return False

    return True


def solve(grid, n, unsolved):
    # Init solution grid
    curr = 0
    while curr < len(unsolved):
        #print("\t%d" % curr)
        #print_grid(grid, n)
        i, j = unsolved[curr]

        # backtrack to previous cell
        if grid[i][j] == n:
            grid[i][j] = 0
            curr -= 1
            continue

        # increment this cell
        grid[i][j] += 1
        if valid_grid(grid, n):
            curr += 1

    return grid


def main():
    # Input
    n = int(readline())
    grid, unsolved = readgrid(n)

    # print input
    print("---- Input ----")
    print_grid(grid, n)
    print()

    # Solve
    solution = solve(grid, n, unsolved)

    # Outputs
    print("---- Full Solution ----")
    print_grid(solution, n)
    print()

    print("---- Solution ----")
    for i in range(n):
        line = ""
        for j in range(n):
            if (i, j) in unsolved:
                line += str(solution[i][j])
            else:
                line += "_"
            line += " "
        print(line)


if __name__ == "__main__":
    main()
