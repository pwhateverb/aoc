def part_one(lines):
    signs = lines[-1].split()
    numbers = []
    for i in range(len(lines)-1):
        numbers.append(lines[i].split())
    
    sum = 0
    for i in range(len(signs)):
        if signs[i] == "*":
            tmp = 1
            for number in numbers:
                tmp *= int(number[i])
            sum += tmp
        elif signs[i] == "+":
            for number in numbers:
                sum += int(number[i])
        else:
            print("Oh no")
    return sum


def part_two(lines):
    signs = lines[-1] + " -"

    sum = 0
    i = 0
    while i < len(signs) - 1:
        sign = signs[i]
        tmp = 1
        while signs[i+1] == " ":
            number = ""
            for j in range(len(lines)-1):
                number += lines[j][i]
            
            if sign == "*":
                tmp *= int(number)
            elif sign == "+":
                sum += int(number)
            else:
                print("Oh no")
            i += 1
        i += 1
        if sign == "*":
            sum += tmp

    return sum
    

if __name__ == "__main__":
    file = open(r"2025\day06\input.txt", "r")
    lines = file.read().splitlines()
    file.close()

    print(part_one(lines))
    print(part_two(lines))