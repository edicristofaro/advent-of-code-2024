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
        print(i + 1, len(stones))

    return len(new_stones)


def part2(stones, blinks):
    # Brute force isn't going to work, but let's try it anyway.
    return part1(stones, blinks)  # Nope!


def main():
    # Read input
    with open("sample.txt", "r") as f:
        input_data = f.read()

    stones = input_data.split()
    print(stones)

    # Solve and print results
    print("Part 1:", part1(stones, 25))
    print("Part 2:", part2(stones, 75))


if __name__ == "__main__":
    main()
