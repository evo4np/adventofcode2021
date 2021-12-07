
import statistics


def problem_one(values):
    median = statistics.median(values)
    cost = sum(abs(n - median) for n in values)
    print('Least fuel cost is:', cost)


def problem_two(values):
    mean = statistics.mean(values)
    cost = (sum(abs(n-mean) * (abs(n-mean) + 1) // 2 for n in values))
    print('Least fuel cost is:', cost)


if __name__ == '__main__':
    with open('test.txt') as f:
        data = [int(i) for i in f.read().split(',')]

problem_one(data)
# problem_two(data)
