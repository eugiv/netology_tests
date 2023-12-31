import pytest

from col_top3_names1 import mentors, extract_names, names_count


def test_extract_names():
    result = extract_names(mentors)
    expected = [
        "Евгений", "Олег", "Дмитрий", "Кирилл", "Александр", "Александр", "Александр", "Антон", "Максим", "Елена",
        "Азамат", "Роман", "Филипп", "Анна", "Иван", "Анатолий", "Юрий", "Илья","Иван", "Ринат", "Вадим", "Тимур",
        "Максим", "Никита", "Алексей", "Денис", "Антон", "Сергей", "Максим", "Евгений", "Константин", "Сергей",
        "Павел", "Евгений", "Олег", "Александр", "Александр", "Кирилл", "Александр", "Роман", "Адилет", "Александр",
        "Алена", "Денис", "Владимир", "Эдгар", "Евгений", "Максим", "Елена", "Владимир", "Эдгар", "Евгений", "Валерий",
        "Татьяна", "Александр", "Александр", "Алена", "Александр", "Денис", "Николай", "Михаил"
    ]
    assert result == expected


test_extracted_names = extract_names(mentors)


@pytest.mark.parametrize(
    'list_length, expected', [
        [1, [('Александр', 10)]],
        [2, [('Александр', 10), ('Евгений', 5)]],
        [3, [('Александр', 10), ('Евгений', 5), ('Максим', 4)]]
    ]
)
def test_names_count(list_length, expected):
    result = names_count(test_extracted_names, list_length)
    assert result == expected
