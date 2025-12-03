class Research:
    def file_reader(self):
        file_name = '../../datasets/data.csv'

        with open(file_name, 'r') as f:
            result = f.read()
            return result

if __name__ == '__main__':
    file_print = Research().file_reader()
    print(file_print)