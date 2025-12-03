class Must_Read:

    file_name = '../../datasets/data.csv'

    with open(file_name, 'r') as f:
        contents = f.read()
        print(contents)
