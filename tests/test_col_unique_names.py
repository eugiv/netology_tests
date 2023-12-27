from col_unique_names import flat_init_list, extract_names, unique_names

test_list =[
    ["Евгений Шмаргунов", "Олег Булыгин"],
    ["Филипп Воронов", "Анна Юшина"],
    ["Евгений Шмаргунов", "Александр Бардин"],
]


def test_flat_init_list():
    result = flat_init_list(test_list)
    expected = [
    "Евгений Шмаргунов", "Олег Булыгин",
    "Филипп Воронов", "Анна Юшина",
    "Евгений Шмаргунов", "Александр Бардин",
]
    assert result == expected


test_flat_result = flat_init_list(test_list)


def test_extract_names():
    result = extract_names(test_flat_result)
    expected = [
    "Евгений", "Олег",
    "Филипп", "Анна",
    "Евгений", "Александр",
]
    assert result == expected


test_extract_res = extract_names(test_flat_result)


def test_unique_names():
    result = unique_names(test_extract_res)
    expected = [
    "Александр", "Анна",
    "Евгений", "Олег",
    "Филипп",
]
    assert result == expected
