import timeit
import sys
from functools import reduce

def get_sum(number_sum):
    total  = 0
    for number in range(1, number_sum + 1):
        squares = number * number
        total  += squares
    return total

def get_reduce(number_sum):
    result = reduce(lambda total, number: total + number * number, range(1, number_sum + 1))
    return result

def main():
    if len(sys.argv) != 4:
        print("Usage: python benchmark.py <method> <number_of_calls> <number_sum>")
        sys.exit(1)
    method_arg = sys.argv[1]
    try:
        number_of_calls = int(sys.argv[2])
        number_sum = int(sys.argv[3])
    except ValueError:
        print("Error: shift must be an integer")
        sys.exit(1)

    if method_arg not in ['loop', 'reduce']:
        print("Error: method must be 'loop' or 'reduce'")
        sys.exit(1)
    if method_arg == 'loop':
        result = timeit.timeit(lambda: get_sum(number_sum), number=number_of_calls)
    else:
        result = timeit.timeit(lambda: get_reduce(number_sum), number=number_of_calls)

    print(result)

if __name__ == '__main__':
    main()