def standard_solution():
    with open('ds.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()

    processed_lines = []

    for line in lines:
        line = line.rstrip('\n\r')
        parts = []
        in_quotes = False
        current_part = ""
        i = 0

        while i < len(line):
            char = line[i]

            if char == '"':
                if i + 1 < len(line) and line[i + 1] == '"':
                    current_part += '"'
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                parts.append(current_part)
                current_part = ""
            else:
                current_part += char
            i += 1

        parts.append(current_part)
        tsv_line = "\t".join(parts) + "\n"
        processed_lines.append(tsv_line)

    with open('ds.tsv', 'w', encoding='utf-8') as tsv_file:
        tsv_file.writelines(processed_lines)


if __name__ == "__main__":
    standard_solution()