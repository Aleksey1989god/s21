def list_of_tuples():
    return [
    ('Russia', '25'),
    ('France', '132'),
    ('Germany', '132'),
    ('Spain', '178'),
    ('Italy', '162'),
    ('Portugal', '17'),
    ('Finland', '3'),
    ('Hungary', '2'),
    ('The Netherlands', '28'),
    ('The USA', '610'),
    ('The United Kingdom', '95'),
    ('China', '83'),
    ('Iran', '76'),
    ('Turkey', '65'),
    ('Belgium', '34'),
    ('Canada', '28'),
    ('Switzerland', '26'),
    ('Brazil', '25'),
    ('Austria', '14'),
    ('Israel', '12')
    ]

def main():
    list_dict = {key: int(value) for key, value in list_of_tuples()}
    sorted_countries = dict(sorted(list_dict.items(), key=lambda item: (-item[1], item[0])))
    for country, number in sorted_countries.items():
        print(country)


if __name__ == '__main__':
    main()