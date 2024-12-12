def part1(stones, blinks):
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """

    for i in range(0, blinks):
        new_stones = []
        for s in stones:
            if int(s) == 0:
                new_stones.append("1")
            elif len(s) % 2 == 0:
                left = s[0 : int(len(s) / 2)]
                right = s[int(len(s) / 2) :]
                new_stones.append(str(int(left)))
                new_stones.append(str(int(right)))
            else:
                new_stones.append(str(int(s) * 2024))
        stones = new_stones

    return len(new_stones)


def part2(stones, blinks):
    # Brute force isn't going to work, but let's try it anyway.
    # return part1(stones, blinks)  # Nope!
    stone_counts = {}
    for s in stones:
        stone_counts[s] = 1

    for b in range(1, blinks + 1):
        new_counts = {}
        for k, v in stone_counts.items():
            # handle 0s
            if k == "0":
                new_counts["1"] = new_counts.get("1", 0) + v
            # handle numbers of even length
            elif len(k) % 2 == 0:
                left = k[0 : int(len(k) / 2)]
                right = k[int(len(k) / 2) :]
                new_counts[str(int(left))] = new_counts.get(str(int(left)), 0) + v
                new_counts[str(int(right))] = new_counts.get(str(int(right)), 0) + v
            else:
                new_counts[str(int(k) * 2024)] = (
                    new_counts.get(str(int(k) * 2024), 0) + v
                )
        stone_counts = new_counts

    return sum([v for v in stone_counts.values()])


def main():
    # Read input
    with open("input.txt", "r") as f:
        input_data = f.read()

    stones = input_data.split()

    # Solve and print results
    print("Part 1:", part1(stones, 25))
    print("Part 2:", part2(stones, 75))


if __name__ == "__main__":
    main()
