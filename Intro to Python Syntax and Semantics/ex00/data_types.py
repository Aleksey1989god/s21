def data_types():
    var_int = 12
    var_str = "name"
    var_float = 3.14
    var_bool = True
    var_list = [1, 2, 3, "four", 5]
    var_dict = {"name": "Alex", "age": 35}
    var_tuple = (1, 2, 3, "four", 3.15)
    var_set = {1, 2, 3, 4, 5}

    types = [
        var_int,
        var_str,
        var_float,
        var_bool,
        var_list,
        var_dict,
        var_tuple,
        var_set
    ]

    type_names = []
    for t in types:
        type_names.append(type(t).__name__)

    print(f"[{', '.join(type_names)}]")


if __name__ == '__main__':
    data_types()