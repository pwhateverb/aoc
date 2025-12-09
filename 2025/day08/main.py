from math import sqrt

def get_distance(first, second):
    return sqrt(((first[0] - second[0])**2)+((first[1] - second[1])**2)+((first[2] - second[2])**2))

def part_one(lines):
    distances = []
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            distances.append((i, j, get_distance(lines[i],lines[j])))

    distances.sort(key= lambda x: x[2])
    
    circuits = [[x] for x in range(len(lines))]
    for i in range(1000):
        first = distances[i][0]
        second = distances[i][1]

        first_idx = -1
        second_idx = -1

        for c in range(len(circuits)):
            circuit = circuits[c]
            has_first = first in circuit
            has_second = second in circuit
            if has_first and has_second:
                break
            elif has_first:
                first_idx = c
            elif has_second:
                second_idx = c
        
        if first_idx != -1 and second_idx != -1:
            circuits[first_idx].extend(circuits.pop(second_idx))

    circuits.sort(key= lambda x: len(x), reverse=True)

    ans = 1
    for i in range(3):
        ans *= len(circuits[i])
    return ans


def part_two(lines):
    distances = []
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            distances.append((i, j, get_distance(lines[i],lines[j])))

    distances.sort(key= lambda x: x[2])
    
    circuits = [[x] for x in range(len(lines))]
    for i in range(len(distances)):
        first = distances[i][0]
        second = distances[i][1]

        first_idx = -1
        second_idx = -1

        for c in range(len(circuits)):
            circuit = circuits[c]
            has_first = first in circuit
            has_second = second in circuit
            if has_first and has_second:
                break
            elif has_first:
                first_idx = c
            elif has_second:
                second_idx = c
        
        if first_idx != -1 and second_idx != -1:
            circuits[first_idx].extend(circuits.pop(second_idx))
        
        if (len(circuits) == 1):
            return lines[first][0] * lines[second][0]

if __name__ == "__main__":
    file = open(r"2025\day08\input.txt", "r")
    lines = [list(map(int, line.split(","))) for line in file.read().splitlines()]
    file.close()

    print(part_one(lines))
    print(part_two(lines))