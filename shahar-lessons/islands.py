def count_islands(grid):
    n_islands = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                n_islands += 1
                map_island(grid, i, j)
    return n_islands


def map_island(grid, loc_r, loc_c):
    grid[loc_r][loc_c] = -1
    new_locations = [
        (loc_r - 1, loc_c - 1),
        (loc_r - 1, loc_c),
        (loc_r - 1, loc_c + 1),
        (loc_r + 1, loc_c),
        (loc_r, loc_c - 1),
        (loc_r, loc_c + 1),
        (loc_r + 1, loc_c + 1),
        (loc_r + 1, loc_c - 1),
    ]
    for loc in new_locations:
        if valid(loc, grid) and grid[loc[0]][loc[1]] == 1:
            map_island(grid, loc[0], loc[1])


def valid(loc, grid):
    nrows = len(grid)
    ncols = len(grid[0])
    ret = [
        loc[0] >= 0,
        loc[0] < nrows,
        loc[1] >= 0,
        loc[1] < ncols
    ]
    return all(ret)  # there's also any, which is "or on everything"


grid = [
    [0,0,1,0,1],
    [0,0,0,1,0],
    [1,1,1,1,1],
    [1,0,0,0,0],
]

print(count_islands(grid))

grid = [
    [0,0,1,0,1],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [1,0,0,0,0],
]

print(count_islands(grid))