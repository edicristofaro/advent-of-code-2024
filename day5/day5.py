def update_is_valid(update, rules):
    is_valid = True
    for r in rules:
        if r[0] in update and r[1] in update:
            if update.index(r[1]) < update.index(r[0]):
                is_valid = False

    return is_valid


def part1(rules, updates):
    valid = []
    midpoints = []

    for u in updates:
        if update_is_valid(u, rules):
            valid.append(u)
            midpoints.append(u[int((len(u) - 1) / 2)])

    return sum(midpoints)


def part2(rules, updates):
    invalid = []
    fixed = []
    midpoints = []

    for u in updates:
        if not update_is_valid(u, rules):
            invalid.append(u)

    while len(invalid) > 0:
        for x, i in enumerate(invalid):
            for r in rules:
                if r[0] in i and r[1] in i:
                    if i.index(r[1]) < i.index(r[0]):
                        # yes, i know we can swap with one buffer variable and not two
                        i_0 = i[i.index(r[0])]
                        i_1 = i[i.index(r[1])]
                        i[i.index(i_0)] = i_1
                        i[i.index(i_1)] = i_0

            if update_is_valid(i, rules):
                fixed.append(i)
                del invalid[x]

    for i in fixed:
        midpoints.append(i[int((len(i) - 1) / 2)])

    return sum(midpoints)


def main():
    # Read input
    with open("input5.txt", "r") as f:
        input_data = f.readlines()

    input_data = [i.replace("\n", "") for i in input_data]
    rules = []
    updates = []

    for i in input_data:
        if "|" in i:
            line = i.split("|")
            rules.append([int(x) for x in line])
        if "," in i:
            line = i.split(",")
            updates.append([int(x) for x in line])

    # Solve and print results
    print("Part 1:", part1(rules, updates))
    print("Part 2:", part2(rules, updates))


if __name__ == "__main__":
    main()
