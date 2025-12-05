def part_one(lines):
    ranges = []
    ids = []
    add_ids = False
    for line in lines:
        if add_ids:
            ids.append(int(line))
        elif line == "":
            add_ids = True
        else:
            ranges.append(tuple(map(int, line.split("-"))))
    count = 0
    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                count += 1
                break
    return count


def part_two(lines):
    ranges = []
    for line in lines:
        if line == "":
            break
        else:
            ranges.append(list(map(int, line.split("-"))))

    ranges.sort(key= lambda x: x[1], reverse=True)
    ranges.sort(key= lambda x: x[0])

    count = ranges[0][1] - ranges[0][0] + 1
    i = 1
    while i < len(ranges):
        if ranges[i][1] <= ranges[i-1][1]:
            ranges.pop(i)
        else:
            if ranges[i][0] <= ranges[i-1][1]:
                ranges[i][0] = ranges[i-1][1] + 1
            count += ranges[i][1] - ranges[i][0] + 1
            i += 1

    return count
    

if __name__ == "__main__":
    file = open(r"2025\day05\input.txt", "r")
    lines = file.read().splitlines()
    file.close()

    print(part_one(lines))
    print(part_two(lines))