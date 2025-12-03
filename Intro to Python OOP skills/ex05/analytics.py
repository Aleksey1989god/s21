from random import randint
class Research:
    def __init__(self, file_path):
        self.file_name = file_path

    def file_reader(self, has_header=True):

        try:
            with open(self.file_name, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError('File not found')
        except Exception as e:
            raise Exception(f'Error while opening {e}')

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
    def __init__(self, data):
        self.data = data

    def counts(self):
        head = 0
        tails = 0
        for row in self.data:
            head += row[0]
            tails += row[1]
        return head, tails

    def fractions(self):
        head, tails = self.counts()
        result = head + tails
        if result == 0:
            return 0, 0
        head_percent = (head/result)*100
        tails_percent = (tails/result)*100

        return head_percent, tails_percent

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, num_of_steps):
        result = []
        for _ in range(num_of_steps):
            num = randint(0, 1)
            if num == 0:
                result.append([0, 1])
            else:
                result.append([1, 0])
        return result

    def predict_last(self):
        if not self.data:
            return None
        return self.data[-1]

    def save_file(self, data, file_name, extension='.txt'):
        full_file_name = file_name + extension
        try:
            with open(full_file_name, 'w') as f:
                f.write(str(data))
            print(f"File {full_file_name} saved successfully.")
        except Exception as e:
            print(f'Error while saving {e}')