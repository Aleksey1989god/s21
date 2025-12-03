import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python caesar.py <encode|decode> <string> <shift>")
        sys.exit(1)

    arg_1 = sys.argv[1]
    arg_2 = sys.argv[2]

    try:
        arg_3 = int(sys.argv[3])
    except ValueError:
        print("Error: shift must be an integer")
        sys.exit(1)

    if arg_1 not in ['encode', 'decode']:
        print("Error: action must be 'encode' or 'decode'")
        sys.exit(1)


    for char in arg_2:
        if ('а' <= char <= 'я') or ('А' <= char <= 'Я' or char in ['ё', 'Ё']):
            print('The script does not support your language yet.')
            sys.exit(1)

    if arg_1 == "decode":
        arg_3 = -arg_3

    result = ""
    for char in arg_2:
        if 'a' <= char <= 'z':
            shift = chr((ord(char) - ord('a') + arg_3) % 26 + ord('a'))
            result += shift
        elif 'A' <= char <= 'Z':
            shift = chr((ord(char) - ord('A') + arg_3) % 26 + ord('A'))
            result += shift
        else:
            result += char

    print(result)

if __name__ == '__main__':
    main()