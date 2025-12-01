def rotate(is_positive, current, jump):
    answer = 0
    if is_positive:
        answer = (current + jump) % 100
    else:
        answer = current - (jump % 100)
        if answer < 0:
            answer += 100
    return answer

def part_one():
    current = 50
    count = 0

    with open(r"2025\day01\input.txt") as f:
        for line in f:
            if line[0] == "R":
                current = rotate(True, current, int(line[1:]))
            else:
                current = rotate(False, current, int(line[1:]))
            if current == 0:
                count += 1

    print(count)


if __name__ == "__main__":
    part_one()