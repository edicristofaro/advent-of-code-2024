import itertools


def part1(input_data):
    possible = 0
    for i in input_data:
        total, numbers = parse_equation(i)
        combos = [list(i) for i in itertools.product([0, 1], repeat=(len(numbers) - 1))]
        for c in combos:
            check_total = numbers[0]
            for n in range(0, len(numbers) - 1):
                if c[n] == 0:
                    check_total *= numbers[n + 1]

                if c[n] == 1:
                    check_total += numbers[n + 1]

            if total == check_total:
                possible += total
                break

    return possible


def part2(input_data):
    possible = 0
    for i in input_data:
        total, numbers = parse_equation(i)
        combos = [
            list(i) for i in itertools.product([0, 1, 2], repeat=(len(numbers) - 1))
        ]

        for c in combos:
            check_total = numbers[0]
            for n in range(0, len(numbers) - 1):
                if c[n] == 0:
                    check_total *= numbers[n + 1]

                if c[n] == 1:
                    check_total += numbers[n + 1]

                if c[n] == 2:
                    check_total = int(str(check_total) + str(numbers[n + 1]))

            if total == check_total:
                possible += total
                break

    return possible


def parse_equation(line):
    total, numbers = line.split(": ")
    numbers = [int(n) for n in numbers.split()]

    return int(total), numbers


def main():
    # Read input
    with open("input7.txt", "r") as f:
        input_data = f.readlines()

    input_data = [i.replace("\n", "") for i in input_data]

    # Solve and print results
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))


if __name__ == "__main__":
    main()
