import timeit
import random
from collections import Counter



def generate_list(a=0, b=100):
    date = []
    for _ in range(1000000):
        result = random.randint(a, b)
        date.append(result)
    return date
def dict_number_counts(date):
    counts = {}
    for item in date:
        counts[item] = counts.get(item, 0) + 1
    return counts

def most_common_numbers(date):
    counts = dict_number_counts(date)
    counts_item = counts.items()
    counts_sorted = sorted(counts_item, key=lambda item: item[1], reverse=True)
    return counts_sorted[:10]

def counter_dict_number_counts(date):
    counts = Counter(date)
    return counts

def counter_most_common_numbers(date):
    counts = Counter(date)
    return counts.most_common(10)


def main():
    date = generate_list()

    functions = [
        ('my function', dict_number_counts),
        ('Counter', counter_dict_number_counts),
        ('my top', most_common_numbers),
        ("Counter's top", counter_most_common_numbers)
    ]

    for method, function in functions:
        times = timeit.timeit(lambda: function(date), number=5)

        print(f'{method}: {times:.7f}')



if __name__ == '__main__':
    main()