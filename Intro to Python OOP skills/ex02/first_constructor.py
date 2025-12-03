import sys
import os



class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self):
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError('File not found')

        with open(self.file_path, 'r') as f:
            file_content = f.read()

        self._validate(file_content)
        return file_content

    def _validate(self, file_content):
        lines = file_content.split('\n')
        if len(lines) < 2:
            raise ValueError('File must contain at least header and one data line.')

        header = lines[0].split(',')
        if len(header) != 2:
            raise ValueError('Header must contain exactly two columns.')
        for i, line in enumerate(lines[1:], 2):
            values = line.split(',')
            if len(values) != 2:
                raise ValueError(f'Line {i}: must contain exactly two values')
            if not (values[0].strip() in ['0', '1'] and values[1].strip() in ['0', '1']):
                raise ValueError(f'Line {i}: values must be 0 or 1')
            if values[0].strip() == values[1].strip():
                raise ValueError(f'Line {i}: values cannot be both {values[0]}')

def main():
    if len(sys.argv) != 2:
        print('Usage: python first_constructor.py "../../datasets/data.csv"')
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        result = research.file_reader()
        print(result)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()