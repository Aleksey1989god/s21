import timeit
import sys


def get_gmail_loop(emails):
    result = []
    for email in emails:
        if '@gmail.com' in email:
            result.append(email)
    return result

def get_gmail_comprehension(emails):
    return [email for email in emails if '@gmail.com' in email]

def get_gmail_map(emails):
    def is_gmail(email):
        return email if '@gmail.com' in email else None

    result = list(map(is_gmail, emails))
    return [email for email in result if email is not None]

def get_gmail_filter(emails):
    return filter(lambda email: '@gmail.com' in email, emails)


def main():
    if len(sys.argv) != 3:
        print("Usage: python benchmark.py <method> <number_of_calls>")
        sys.exit(1)
    method_arg = sys.argv[1]
    try:
        number_of_calls = int(sys.argv[2])
    except ValueError:
        print("Error: shift must be an integer")
        sys.exit(1)

    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com']

    emails = emails * 5

    functions = {
        'loop': get_gmail_loop,
        'list_comprehension': get_gmail_comprehension,
        'map': get_gmail_map,
        'filter': get_gmail_filter
    }
    if method_arg not in functions:
        print("Error: method must be 'loop' or 'list_comprehension' or 'map' or 'filter'")
        sys.exit(1)


    function = functions[method_arg]
    times = timeit.timeit(lambda: function(emails), number=number_of_calls)

    print(times)

if __name__ == '__main__':
    main()