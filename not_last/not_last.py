#!/usr/bin/env python

"""
Вася Пупкин поспорил со своим одноклассником Петей, что не закончит последним по средней годовой оценки,
а будет вторым с конца. Помогите Васе узнать, выиграет ли он спор или нет.

Дан список школьников и их годовых оценок:
`[("Вася Пупкин", 3.2), ("Артур Пирожков", 3.5)]`

Необходимо вернуть список школьников, имеющих вторую с конца годовую оценку.
Имена должны идти в алфавитном порядке.
"""


def last_but_one(pupils: list[(str, float)]) -> list[str]:
    a = dict(pupils)
    test = sorted(a.values())
    list1 = {}
    name = []
    for i in test:
        for j in a.keys():
            if a[j] == i:
                list1[j] = a[j]
    sorted_list = list1.values()
    new_sorted_list = list(set(sorted_list))
    new_sorted_list.sort(reverse=True)
    list2 = new_sorted_list[-2]
    for k, v in list1.items():
        if v == list2:
            name.append(k)
    name.sort()
    return name

