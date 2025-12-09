def part_one(lines):
    col = len(lines[0])
    row = len(lines)
    count = 0
    lines[1][lines[0].index("S")] = "|"
    for i in range(2, row, 2):
        for j in range(col):
            if lines[i-1][j] == "|":
                if lines[i][j] == "^":
                    count += 1
                    lines[i+1][j+1] = "|"
                    lines[i+1][j-1] = "|"
                else:
                    lines[i+1][j] = "|"
    return count


def part_two(lines):
    col = len(lines[0])
    row = len(lines)
    lines[1] = [0] * col
    lines[1][lines[0].index("S")] = 1
    for i in range(2, row, 2):
        lines[i+1] = [0] * col
        for j in range(col):
            current = lines[i-1][j]
            if lines[i][j] == "^":
                lines[i+1][j+1] += current
                lines[i+1][j-1] += current
            else:
                lines[i+1][j] += current

    sum = 0
    for x in lines[-1]:
        sum += x
    return sum

if __name__ == "__main__":
    file = open(r"2025\day07\input.txt", "r")
    lines = [list(line) for line in file.read().splitlines()]
    file.close()

    print(part_one(lines))
    print(part_two(lines))