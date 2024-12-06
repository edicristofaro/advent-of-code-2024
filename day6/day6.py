def part1(grid, grid_size, start_pos):
    pos = start_pos
    orientation = "U"  # Up, Down, Left, Right
    visited = []
    while pos[0] in range(0, grid_size) and pos[1] in range(0, grid_size):
        visited.append(pos)
        while collision_ahead(orientation, grid, pos):
            orientation = turn_rt_90(orientation)
        pos = move(orientation, pos)

    return len(set(visited))


def part2(grid, grid_size, start_pos):
    pos = start_pos
    orientation = "U"  # Up, Down, Left, Right
    obstacles = []

    for x in range(0, grid_size):
        for y in range(0, grid_size):
            pos = start_pos
            orientation = "U"
            tmp_grid = grid.copy()
            tmp_grid[(x, y)] = "#"
            loop_count = 0
            while pos[0] in range(0, grid_size) and pos[1] in range(0, grid_size):
                loop_count += 1
                while collision_ahead(orientation, tmp_grid, pos):
                    orientation = turn_rt_90(orientation)
                pos = move(orientation, pos)
                if loop_count > grid_size**2:
                    obstacles.append(pos)
                    break

    return len(obstacles)


def turn_rt_90(orientation):
    if orientation == "U":
        return "R"
    elif orientation == "R":
        return "D"
    elif orientation == "D":
        return "L"
    else:
        return "U"


def move(orientation, pos):
    x, y = pos
    if orientation == "U":
        return (x, y - 1)
    elif orientation == "R":
        return (x + 1, y)
    elif orientation == "D":
        return (x, y + 1)
    else:
        return (x - 1, y)


def collision_ahead(orientation, grid, pos):
    x, y = pos
    if orientation == "U":
        return grid.get((x, y - 1), None) == "#"
    elif orientation == "R":
        return grid.get((x + 1, y), None) == "#"
    elif orientation == "D":
        return grid.get((x, y + 1), None) == "#"
    else:
        return grid.get((x - 1, y), None) == "#"


def main():
    # Read input
    with open("input6.txt", "r") as f:
        input_data = f.readlines()

    input_data = [i.replace("\n", "") for i in input_data]

    start_pos = (0, 0)
    grid_size = len(input_data)
    grid = dict()

    for i, y in enumerate(input_data):
        for j, x in enumerate(y):
            if x == "#":
                grid[(j, i)] = "#"
            elif x == ".":
                grid[(j, i)] = "."
            else:
                grid[(j, i)] = "."
                start_pos = (j, i)

    # Solve and print results
    print("Part 1:", part1(grid, grid_size, start_pos))
    print("Part 2:", part2(grid, grid_size, start_pos))


if __name__ == "__main__":
    main()
