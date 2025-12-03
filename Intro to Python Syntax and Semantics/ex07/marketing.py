import sys


def clients():
    list_clients = ['andrew@gmail.com',
            'jessica@gmail.com',
            'ted@mosby.com',
            'john@snow.is',
            'bill_gates@live.com',
            'mark@facebook.com',
            'elon@paypal.com',
            'jessica@gmail.com']
    return set(list_clients)

def participants():
    list_participants = ['walter@heisenberg.com',
            'vasily@mail.ru',
            'pinkman@yo.org',
            'jessica@gmail.com',
            'elon@paypal.com',
            'pinkman@yo.org',
            'mr@robot.gov',
            'eleven@yahoo.com']
    return set(list_participants)

def recipients():
    list_recipients = ['andrew@gmail.com',
            'jessica@gmail.com',
            'john@snow.is']
    return set(list_recipients)


def main():
    if len(sys.argv) != 2:
        raise Exception("Argument required")
    arg = sys.argv[1].lower()
    if arg == 'call_center':
        result = list(clients() - recipients())
    elif arg == 'potential_clients':
        result = list(participants() - clients())
    elif arg == 'loyalty_program':
        result = list(clients() - participants())
    else:
        raise Exception("Incorrect argument")

    print(result)


if __name__ == '__main__':
    main()