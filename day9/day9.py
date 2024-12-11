def part1(input_data):
    stream = []
    id = 0
    for index, value in enumerate(input_data):
        if index % 2 == 0:
            for j in range(0, int(value)):
                stream.append(["F", id])
            id += 1
        else:
            for k in range(0, int(value)):
                stream.append([".", None])
    checksum = 0
    end = len(stream) - 1
    for pos in range(0, len([s for s in stream if s[0] != "."])):
        val = stream[pos]
        if val[0] == "F":
            checksum += val[1] * pos
        elif val[0] == ".":
            while stream[end][0] == ".":
                end -= 1
            checksum += stream[end][1] * pos
            stream.pop()
            end -= 1

    return checksum


def part2(input_data):
    files = {}
    spaces = []
    id = 0
    pos = 0
    checksum = 0
    for index, value in enumerate(input_data):
        if index % 2 == 0:
            files[id] = {"pos": pos, "size": int(value)}
            id += 1
        else:
            spaces.append([pos, int(value)])
        pos += int(value)

    reversed_files = sorted([k for k in files.keys()], reverse=True)

    # we aren't dealing with consecutive spaces that should combine into one, probably
    for id in reversed_files:
        spaces = space_scan(spaces)
        file_len = files[id]["size"]
        for s, space in enumerate(spaces):
            if space[1] >= file_len:
                temp_space = spaces.pop(s)
                files[id]["pos"] = temp_space[0]
                if temp_space[1] >= file_len:
                    modified_space = [
                        temp_space[0] + file_len,
                        temp_space[1] - file_len,
                    ]
                    spaces.append(modified_space)
                break

    for k, v in files.items():
        for i in range(v["pos"], v["pos"] + v["size"]):
            checksum += i * k

    return checksum


def space_scan(spaces):
    space_len = len(spaces)
    for i in range(1, len(spaces)):
        if len(spaces) > i:
            if spaces[i][0] == spaces[i - 1][0] + spaces[i - 1][1]:
                spaces[i - 1][1] = spaces[i][1] + spaces[i - 1][1]
                spaces.pop(i)
    spaces = sorted(spaces, key=lambda x: x[0])
    if space_len == len(spaces):
        return spaces
    else:
        spaces = space_scan(spaces)

    return spaces


def main():
    # Read input
    with open("input9.txt", "r") as f:
        input_data = f.read()

    # Solve and print results
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))


if __name__ == "__main__":
    main()
