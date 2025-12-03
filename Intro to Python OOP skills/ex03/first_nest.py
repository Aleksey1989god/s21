import sys
import os


class Research:
    def __init__(self, file_path):
        self.file_name = file_path

    def file_reader(self, has_header=True):
        if not os.path.isfile(self.file_name):
            raise FileNotFoundError('File not found')

        with open(self.file_name, 'r') as f:
            lines = f.readlines()

        header = lines[0].strip().split(',')

        if header in [['0', '1'], ['1', '0']]:
            has_header = False
        data = []
        start_index = 1 if has_header else 0
        for line in lines[start_index:]:
            line = line.strip()
            if line:
                values = line.split(',')
                if len(values) != 2:
                    raise ValueError(f'Must contain exactly two values')
                if not (values[0].strip() in ['0', '1'] and values[1].strip() in ['0', '1']):
                    raise ValueError(f'Values must be 0 or 1')
                if values[0].strip() == values[1].strip():
                    raise ValueError(f'Values cannot be the same')
                data.append([int(values[0]), int(values[1])])
        return data
    class Calculations:
        def counts(self, data):
            head = 0
            tails = 0
            for row in data:
                head += row[0]
                tails += row[1]
            return head, tails

        def fractions(self, head, tails):
            result = head + tails
            if result == 0:
                return 0, 0
            count_10_percent = (head/result)*100
            count_01_percent = (tails/result)*100

            return count_01_percent, count_10_percent



def main():
    if len(sys.argv) != 2:
        print('Usage: python first_constructor.py "../../datasets/data.csv"')
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        result_file_reader = research.file_reader()
        print(result_file_reader)
        calculations = research.Calculations()
        head, tails = calculations.counts(result_file_reader)
        print(f'{head} {tails}')
        result_head, result_tails = calculations.fractions(head, tails)
        print(f'{result_head} {result_tails}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()