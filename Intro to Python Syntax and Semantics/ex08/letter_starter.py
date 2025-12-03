import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python letter_starter.py <email>")
        sys.exit(1)

    email_arg = sys.argv[1]

    try:
        with open('employees.tsv', 'r', encoding='utf-8') as file:
            lines = file.read().splitlines()
    except Exception as e:
        print(f"Error reading employees.tsv: {e}")
        sys.exit(1)

    found = False
    for line in lines[1:]:
        name, surname, email = line.split('\t')
        if email == email_arg:
            print(
                f'Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')
            found = True
            break

    if not found:
        print(f"Email {email_arg} not found in employees.tsv")
        sys.exit(1)


if __name__ == '__main__':
    main()