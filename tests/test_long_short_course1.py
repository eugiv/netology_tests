from col_long_short_course1 import list_of_courses, max_min_crs

test_courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python"]

test_durations = [14, 20]


def test_list_of_courses():
    result = list_of_courses(test_courses, test_durations)
    expected = [{'title': 'Java-разработчик с нуля', 'duration': 14},
                {'title': 'Fullstack-разработчик на Python', 'duration': 20}]

    assert result == expected


test_courses_list_result = list_of_courses(test_courses, test_durations)


def test_max_min_crs():
    result = max_min_crs(test_courses_list_result, test_durations)
    expected = (['Java-разработчик с нуля'], ['Fullstack-разработчик на Python'])

    assert result == expected
