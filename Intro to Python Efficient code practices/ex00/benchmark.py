import timeit

def get_gmail_loop(emails):
    result = []
    for email in emails:
        if '@gmail.com' in email:
            result.append(email)
    return result

def get_gmail_comprehension(emails):
    return [email for email in emails if '@gmail.com' in email]


def main():
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com']

    emails = emails * 5

    loop_time = timeit.timeit(
        lambda: get_gmail_loop(emails),
        number=9000000
    )

    comprehension_time = timeit.timeit(
        lambda: get_gmail_comprehension(emails),
        number=9000000
    )

    if comprehension_time <= loop_time:
        print("It is better to use a list comprehension")
        print(f'{comprehension_time} vs {loop_time}')

    else:
        print('It is better to use a loop')
        print(f'{loop_time} vs {comprehension_time}')

if __name__ == '__main__':
    main()