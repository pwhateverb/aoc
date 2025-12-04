def part_one(banks):
    sum = 0
    for bank in banks:
        hi_one_idx = 0
        hi_one = 0
        hi_two = 0
        n = len(bank)

        for i in range(n-1):
            current_one = int(bank[i])
            if current_one > hi_one:
                hi_one = current_one
                hi_one_idx = i

        for j in range(hi_one_idx + 1, n):
            current_two = int(bank[j])
            if current_two > hi_two:
                hi_two = current_two
        
        sum += int(str(hi_one) + str(hi_two))
        
    return sum


def part_two(banks):
    sum = 0
    batteries = 12
    for bank in banks:
        n = len(bank)
        start = 0
        bank_sum = ""
        for i in range(batteries):
            hi = 0
            for j in range(start, n-batteries+i+1):
                current = int(bank[j])
                if current > hi:
                    hi = current
                    start = j + 1
            bank_sum += str(hi)
        
        sum += int(bank_sum)
        
    return sum
    

if __name__ == "__main__":
    file = open(r"2025\day03\input.txt", "r")
    banks = file.read().splitlines()
    file.close()
    print(part_one(banks))
    print(part_two(banks))

