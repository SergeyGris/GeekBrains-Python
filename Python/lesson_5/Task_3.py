def tutors_with_groups(tutors, groups):
    tut_len = len(tutors)
    group_len = len(groups)
    if len(tutors) <= len(groups):
        print('Результат, где учеников меньше')
    else:
        print('Результат, где учеников больше')
    print('Ученики:', tutors)
    print('Классы:', groups)
    print('Тип объекта: ', type(gen))
    print('Все значения генератора:')

    for i in range(tut_len):
        try:
            answer = tutors[i], groups[i]
            print(answer)
            yield answer
        except IndexError:
            answer = tutors[i], None
            print(answer)
            yield answer


# Если учеников больше классов
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А',
    # '10Б', '9А'

]

gen = tutors_with_groups(tutors, groups)
i = 0
while i <= len(tutors):
    try:
        next(gen)
        i += 1
    except StopIteration:
        break
print('============================================================')
# Если учеников меньше классов
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = tutors_with_groups(tutors, groups)
i = 0
while i <= len(tutors):
    try:
        next(gen)
        i += 1
    except StopIteration:
        break
