"""
Sample Data: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Pull out anything that matches mul(x,y) within the source string.
"""

import re
from math import prod


def part1(input_data):
    muls = re.findall(r"mul\((\d+,\d+)\)", input_data)
    total = 0

    for m in muls:
        total += prod([int(n) for n in m.split(",")])

    return total


def part2(input_data):
    # We now want only the mul(x,y) statements that fall in between do() and don't() blocks.
    # The problem says that we start with muls enabled, so let's add that to the input data and force a terminator on to the end.
    input_data = "do()" + input_data + "don't()"
    muls = re.findall(r"^|do\(\)(.*?)don't\(\)", input_data)

    # hey, we can re-use part 1 since part 2 is just filtering the input before carrying out the same operation!
    return part1(str(muls))


def main():
    # Read input
    with open("input3.txt", "r") as f:
        input_data = f.read().replace("\n", "")

    # Solve and print results
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))


if __name__ == "__main__":
    main()
