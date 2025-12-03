import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python names_extractor.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding='utf-8') as file:
            lines = file.read().splitlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    with open('employees.tsv', "w") as out:
        out.write("Name\tSurname\tEmail\n")
        for line in lines:
            if not line.strip():
                continue
            try:
                email = line.split("@")[0]
                name = email.split(".")[0].capitalize()
                surname = email.split(".")[1].capitalize()
                out.write(f"{name}\t{surname}\t{line}\n")
            except IndexError:
                print(f"Warning: Invalid email format: {line}")
                continue


if __name__ == '__main__':
    main()