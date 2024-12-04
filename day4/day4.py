def check_up_down(input_data, word, x, y):
    len_word = len(word)
    maxlength = len(input_data[0])  # assuming a square here
    count = 0

    # check down
    check_str = ""
    if y + len_word <= maxlength:
        for i in range(y, y + len_word):
            check_str += input_data[i][x]
        if check_str == word:
            count += 1

    # check up
    check_str = ""
    if y - len_word + 1 >= 0:
        for i in range(y, y - len_word, -1):
            check_str += input_data[i][x]
        if check_str == word:
            count += 1

    return count


def check_left_right(input_data, word, x, y):
    len_word = len(word)
    maxlength = len(input_data[0])  # assuming a square here
    count = 0

    # check right
    check_str = ""
    if x + len_word <= maxlength:
        for i in range(x, len_word + x):
            check_str += input_data[y][i]
        if check_str == word:
            count += 1

    # check left
    check_str = ""
    if x - len_word + 1 >= 0:
        for i in range(x, x - len_word, -1):
            check_str += input_data[y][i]
        if check_str == word:
            count += 1

    return count


def check_diagonal(input_data, word, x, y):
    len_word = len(word)
    count = 0

    # check -/-
    check_str = ""
    for i in range(0, len_word):
        try:
            check_str += input_data[y + i][x + i]
        except:
            pass
    if check_str == word:
        count += 1

    # check +/+
    check_str = ""
    if y - len_word + 1 >= 0 and x - len_word + 1 >= 0:
        for i in range(0, len_word):
            check_str += input_data[y - i][x - i]
        if check_str == word:
            count += 1

    # check -/+
    check_str = ""
    if x - len_word + 1 >= 0:
        for i in range(0, len_word):
            try:
                check_str += input_data[y + i][x - i]
            except:
                pass
        if check_str == word:
            count += 1

    # check +/-
    check_str = ""
    if y - len_word + 1 >= 0:
        for i in range(0, len_word):
            try:
                check_str += input_data[y - i][x + i]
            except:
                pass
        if check_str == word:
            count += 1

    return count


def part1(input_data):
    total = 0
    for y, row in enumerate(input_data):
        for x, col in enumerate(row):
            total += check_up_down(input_data, "XMAS", x, y)
            total += check_left_right(input_data, "XMAS", x, y)
            total += check_diagonal(input_data, "XMAS", x, y)

    return total


def part2(input_data):
    len_data = len(input_data)
    total = 0
    for y in range(1, len_data - 1):
        for x in range(1, len_data - 1):
            val = input_data[y - 1][x - 1] + input_data[y][x] + input_data[y + 1][x + 1]
            opposite_val = (
                input_data[y + 1][x - 1] + input_data[y][x] + input_data[y - 1][x + 1]
            )
            if (val == "MAS" or val == "SAM") and (
                opposite_val == "MAS" or opposite_val == "SAM"
            ):
                total += 1
    return total


def main():
    # Read input
    with open("input4.txt", "r") as f:
        input_data = f.readlines()

    input_data = [i.replace("\n", "") for i in input_data]

    # Solve and print results
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))


if __name__ == "__main__":
    main()
