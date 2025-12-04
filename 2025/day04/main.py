def part_one(map):
    n_row = len(map)
    n_col = len(map[0])
    count = 0

    for i in range(n_row):
        for j in range(n_col):
            if map[i][j] == "@":
                neighbours = -1
                for k in range(max(i-1, 0), min(i+1, n_row-1)+1):
                    for l in range(max(j-1, 0), min(j+1, n_col-1)+1):
                        if map[k][l] == "@":
                            neighbours += 1
            
                if neighbours < 4:
                    count += 1

    return count


def part_two(map):
    n_row = len(map)
    n_col = len(map[0])
    count = 0
    changed = True

    while (changed):
        changed = False
        for i in range(n_row):
            for j in range(n_col):
                if map[i][j] == "@":
                    neighbours = -1
                    for k in range(max(i-1, 0), min(i+1, n_row-1)+1):
                        for l in range(max(j-1, 0), min(j+1, n_col-1)+1):
                            if map[k][l] == "@":
                                neighbours += 1
                
                    if neighbours < 4:
                        count += 1
                        map[i] = map[i][:j] + "." + map[i][j+1:]
                        changed = True

    return count
    

if __name__ == "__main__":
    file = open(r"2025\day04\input.txt", "r")
    map = file.read().splitlines()
    file.close()
    print(part_one(map))
    print(part_two(map))

