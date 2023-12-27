
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
		   "Frontend-разработчик с нуля"]

durations = [14, 20, 12, 20]


def list_of_courses():
	courses_list = []
	for c, i in zip(courses, durations):
		course_dict = {"title": c, "duration": i}
		courses_list.append(course_dict)

	return courses_list


min = min([item["duration"] for item in list_of_courses()])
max = max([item["duration"] for item in list_of_courses()])

maxes = []
minis = []
for idx, dur in enumerate(durations):
	if dur == max:
		maxes.append(idx)
	elif dur == min:
		minis.append(idx)

courses_min = []
courses_max = []
for id in minis:
	courses_min.append(list_of_courses()[id]["title"])
for id in maxes:
	courses_max.append(list_of_courses()[id]["title"])

courses_min = ", ".join(courses_min)
courses_max = ", ".join(courses_max)

print(f'Самый короткий курс(ы): {courses_min} - {min} месяца(ев)')
print(f'Самый длинный курс(ы): {courses_max} - {max} месяца(ев)')
