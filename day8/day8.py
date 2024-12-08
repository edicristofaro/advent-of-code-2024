def part1(grid, grid_size):
    # for every point in the dict
    # find other the points of the same value in the dict
    # calculate the rise and run between each pair, subtracting the pair point from the current point
    # antinode 1: subtract that rise and run from the pair point
    # antinode 2: add the rise and run from the current point
    # I might be wrong on the above and you need to add to the pair point and subtract from the current point
    antinodes = []

    for p, letter in grid.items():
        same = []
        for k, v in grid.items():
            if v == letter and k != p:
                same.append(k)
        for s in same:
            run = p[0] - s[0]
            rise = p[1] - s[1]
            antinode_1 = (s[0] - run, s[1] - rise)
            antinode_2 = (p[0] + run, p[1] + rise)
            if bounds_check(grid_size, antinode_1):
                antinodes.append(antinode_1)
            if bounds_check(grid_size, antinode_2):
                antinodes.append(antinode_2)

    return len(set(antinodes))


def part2(grid, grid_size):
    # same as above, but repeat the rise/run until out of bounds. each point in a pair will be an antinode of the opposite.
    antinodes = []

    for p, letter in grid.items():
        same = []
        for k, v in grid.items():
            if v == letter and k != p:
                same.append(k)
        antinodes.extend(same)
        for s in same:
            run = p[0] - s[0]
            rise = p[1] - s[1]

            antinode_1 = (s[0] - run, s[1] - rise)
            antinode_2 = (p[0] + run, p[1] + rise)
            while bounds_check(grid_size, antinode_1) or bounds_check(
                grid_size, antinode_2
            ):
                if bounds_check(grid_size, antinode_1):
                    antinodes.append(antinode_1)
                if bounds_check(grid_size, antinode_2):
                    antinodes.append(antinode_2)
                antinode_1 = (antinode_1[0] - run, antinode_1[1] - rise)
                antinode_2 = (antinode_2[0] + run, antinode_2[1] + rise)

    return len(set(antinodes))


def bounds_check(grid_size, point):
    if point[0] in range(0, grid_size) and point[1] in range(0, grid_size):
        return True
    else:
        return False


def main():
    # Read input
    with open("input8.txt", "r") as f:
        input_data = f.readlines()

    input_data = [i.replace("\n", "") for i in input_data]
    grid_size = len(input_data)
    grid = {}
    for y in range(0, len(input_data)):
        for x in range(0, len(input_data[y])):
            if input_data[y][x].isalnum():
                grid[(x, y)] = input_data[y][x]

    # Solve and print results
    print("Part 1:", part1(grid, grid_size))
    print("Part 2:", part2(grid, grid_size))


if __name__ == "__main__":
    main()
