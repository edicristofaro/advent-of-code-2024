def all_increasing(report):
    for i in range(0, len(report) - 1):
        if report[i + 1] <= report[i]:
            return False
    return True


def all_decreasing(report):
    for i in range(0, len(report) - 1):
        if report[i + 1] >= report[i]:
            return False
    return True


def all_within_distance(report, low, high):
    for i in range(0, len(report) - 1):
        if abs(report[i + 1] - report[i]) not in range(low, high + 1):
            return False
    return True


def part1(reports):
    safe = 0
    for r in reports:
        if (all_increasing(r) or all_decreasing(r)) and all_within_distance(r, 1, 3):
            safe += 1

    return safe


def part2(reports):
    safe = []
    unsafe = []

    for r in reports:
        if (all_increasing(r) or all_decreasing(r)) and all_within_distance(r, 1, 3):
            safe.append(r)
        else:
            unsafe.append(r)

    # check if a report becomes safe if we remove a level
    for r in unsafe:
        for i, level in enumerate(r):
            tmp_report = r.copy()
            del tmp_report[i]
            if (
                all_increasing(tmp_report) or all_decreasing(tmp_report)
            ) and all_within_distance(tmp_report, 1, 3):
                safe.append(r)
                break

    return len(safe)


def main():
    # Read input
    with open("input2.txt", "r") as f:
        input_data = f.read().splitlines()

    reports = []
    for s in input_data:
        s = s.split()
        reports.append([int(n) for n in s])

    # Solve and print results
    print("Part 1:", part1(reports))
    print("Part 2:", part2(reports))


if __name__ == "__main__":
    main()
