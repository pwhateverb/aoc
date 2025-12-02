def part_one(ranges):
    sum = 0
    for id_range in ranges:
        start_str, end_str = id_range.split("-")
        current = int(start_str)
        end = int(end_str)
        while (current <= end):
            current_str = str(current)
            length = len(current_str)
            if length % 2 != 0:
                current = 10 ** length
            elif current_str[:length//2] == current_str[length//2:]:
                sum += current
                current += 1
            else:
                current += 1
    return sum


def part_two(ranges):
    sum = 0
    for id_range in ranges:
        start_str, end_str = id_range.split("-")
        current = int(start_str)
        end = int(end_str)
        while (current <= end):
            current_str = str(current)
            length = len(current_str)
            pattern = current_str[0]
            i = 1
            while i < length:
                remainder = current_str[i:]
                while(remainder.startswith(pattern)):
                    if remainder == pattern:
                        break
                    if i > len(remainder):
                        break
                    remainder = remainder[i:]
                if remainder == pattern:
                    sum += current
                    break
                pattern = pattern + current_str[i]
                i += 1
                
            current += 1
    return sum
    

if __name__ == "__main__":
    file = open(r"2025\day02\input.txt", "r")
    ranges = file.readline().split(",")
    file.close()
    print(part_one(ranges))
    print(part_two(ranges))

