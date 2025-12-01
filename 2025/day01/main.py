def part_one(file):
    current = 50
    count = 0
    for line in file:
        jump = int(line[1:])
        if line[0] == "R":
            current = (current + jump) % 100
        else:
            current = (current - jump) % 100
        if current == 0:
            count += 1
    print(count)


def part_two(file):
    current = 50
    count = 0
    for line in file:
        jump = int(line[1:])
        if line[0] == "R":
            count += (current + jump) // 100
            current = (current + jump) % 100
        else:
            count += (jump // 100)
            if current <= (jump % 100) and current != 0:
                count += 1
            current = (current - jump) % 100
    print(count)


if __name__ == "__main__":
    file = open(r"2025\day01\input.txt")
    part_one(file)
    part_two(file)
    file.close()