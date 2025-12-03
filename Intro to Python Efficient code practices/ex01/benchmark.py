import timeit

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

def main():
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com']

    emails = emails * 5

    loop_time = timeit.timeit(
        lambda: get_gmail_loop(emails),
        number=900000
    )

    comprehension_time = timeit.timeit(
        lambda: get_gmail_comprehension(emails),
        number=900000
    )

    map_time = timeit.timeit(
        lambda: get_gmail_map(emails),
        number=900000
    )

    dict_items = {
        loop_time:'loop',
        comprehension_time:'list comprehension',
        map_time:'map'
    }
    sorted_dict = sorted(dict_items.items())
    first_key, first_value = sorted_dict[0]
    second_key, second_value = sorted_dict[1]
    third_key, third_value = sorted_dict[2]

    print(f"It is better to use a {first_value}")
    print(f'{first_key} vs {second_key} vs {third_key}')


if __name__ == '__main__':
    main()