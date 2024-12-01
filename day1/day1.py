"""
Sample data:
3   4
4   3
2   5
1   3
3   9
3   3
"""


def part1(list1, list2):
    # sort each list asc, then zip them
    # return the cumulative abs difference between each tuple element

    combined = zip(sorted(list1), sorted(list2))

    total = 0

    for c in combined:
        total += abs(c[0] - c[1])

    return total


def part2(list1, list2):
    # for each element in list1, count the occurrences of e in list 2, multiply those together
    # return the cumulative sum
    total = 0
    for i in list1:
        total += i * list2.count(i)

    return total


def main():
    # Read input
    with open("input1.txt", "r") as f:
        input_data = f.readlines()

    # split into two lists of ints by column
    list1 = []
    list2 = []

    for i in input_data:
        vals = i.split()
        list1.append(int(vals[0]))
        list2.append(int(vals[1]))

    # Solve and print results
    print("Part 1:", part1(list1, list2))
    print("Part 2:", part2(list1, list2))


if __name__ == "__main__":
    main()
