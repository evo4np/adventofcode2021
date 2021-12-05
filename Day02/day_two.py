def problem_one(datas):
    horizontal = 0
    depth = 0
    for data in datas:
        option = data.split()[0]
        value = int(data.split()[1])

        if option == 'forward':
            horizontal += value
        elif option == 'down':
            depth += value
        elif option == 'up':
            depth -= value
    result = horizontal * depth
    print(result)


def problem_two(datas):
    horizontal = 0
    depth = 0
    aim = 0
    for data in datas:
        option = data.split()[0]
        value = int(data.split()[1])

        if option == 'forward':
            horizontal += value
            depth += (value * aim)

        elif option == 'down':
            # depth += value
            aim += value

        elif option == 'up':
            # depth -= value
            aim -= value
    result = horizontal * depth
    print(result)


if __name__ == '__main__':

    with open('day_two_puzzle.txt') as f:
        puzzle_data = [str(line.strip()) for line in f]

    problem_one(puzzle_data)
    problem_two(puzzle_data)
