def part1(grid):
    trailheads = [k for k, v in grid.items() if v == 0]
    ends_reached = 0
    for trailhead in trailheads:
        ends_reached += len(find_paths(trailhead, grid))

    return ends_reached


def find_paths(point, grid):
    val = grid.get(point, None)
    x, y = point
    ends_reached = []

    if val is None:
        return 0
    if val == 9:
        ends_reached.append(point)
    elif val >= 0:
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for n in neighbors:
            neighbor = grid.get(n, None)
            if neighbor == val + 1:
                ends_reached.extend(find_paths(n, grid))

    return set(ends_reached)


def part2(grid):
    # Well shit. The thing I originally wrote for part 1 is the solution for part 2, and now I have to remember what I changed.
    trailheads = [k for k, v in grid.items() if v == 0]
    trails = 0
    for trailhead in trailheads:
        trails += find_trails(trailhead, grid)

    return trails


def find_trails(point, grid, ends_reached=0):
    # This was originally what I'd done for part 1, until I did a bunch of print debugging, re-read the problem, and changed it above. Managed to remember what I did and rewrite it.
    val = grid.get(point, None)
    x, y = point

    if val is None:
        return 0
    if val == 9:
        return 1
    elif val >= 0:
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for n in neighbors:
            neighbor = grid.get(n, None)
            if neighbor == val + 1:
                ends_reached += find_trails(n, grid)

    return ends_reached


def main():
    # Read input
    with open("input.txt", "r") as f:
        input_data = f.readlines()

    input_data = [i.replace("\n", "") for i in input_data]
    grid = {}
    for y, yval in enumerate(input_data):
        for x, xval in enumerate(yval):
            grid[(x, y)] = int(xval)

    # Solve and print results
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))


if __name__ == "__main__":
    main()
