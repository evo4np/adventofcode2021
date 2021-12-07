
def problem_one(values):
    for _ in range(256):
        for index, value in enumerate(values):
            values[index] -= 1
            if values[index] == -1:
                values.append(9)
                values[index] = 6

    print('Number of lanternfish:', len(values))


if __name__ == '__main__':
    with open('day_six_puzzle.txt') as f:
        # with open('test.txt') as f:
        data = [int(i) for i in f.read().split(',')]

(problem_one(data))
