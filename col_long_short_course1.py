
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
		   "Frontend-разработчик с нуля"]

durations = [14, 20, 12, 20]


def list_of_courses(courses, durations):
	courses_list = []
	for c, i in zip(courses, durations):
		course_dict = {"title": c, "duration": i}
		courses_list.append(course_dict)

	return courses_list


def max_min_crs(courses_lst, durat):
	min_val = min([item["duration"] for item in courses_lst])
	max_val = max([item["duration"] for item in courses_lst])

	maxes = []
	minis = []
	for idx, dur in enumerate(durat):
		if dur == max_val:
			maxes.append(idx)
		elif dur == min_val:
			minis.append(idx)

	courses_min = []
	courses_max = []
	for id_min in minis:
		courses_min.append(courses_lst[id_min]["title"])
	for id_max in maxes:
		courses_max.append(courses_lst[id_max]["title"])

	return courses_min, courses_max


if __name__ == "__main__":
	courses_list = list_of_courses(courses, durations)
	max_min_crs(courses_list, durations)
