

def problem_one(values):
    increased = 0

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            increased += 1
    print(increased)


def problem_two(values):
    increased = 0

    for i in range(2, len(values) - 1):
        if (values[i] + values[i - 1] + values[i - 2]) < (values[i + 1] + values[i] + values[i - 1]):
            increased += 1
    print(increased)


if __name__ == '__main__':

    with open('day_one.txt') as f:
        data = [int(line.strip()) for line in f]

    problem_one(data)
    problem_two(data)
