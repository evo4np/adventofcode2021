
import statistics
import math


def problem_one(values):
    median = statistics.median(values)
    cost = sum(abs(n - median) for n in values)
    print('Least fuel cost is:', cost)


def problem_two(values):
    mean = statistics.mean(values)

    print(math.floor(mean))
    cost = (sum(abs(n-math.floor(mean)) *
                (abs(n-math.floor(mean)) + 1) // 2 for n in values))
    print('Least fuel cost is:', cost)


if __name__ == '__main__':
    with open('day_07.txt') as f:
        data = [int(i) for i in f.read().split(',')]

# problem_one(data)
problem_two(data)
