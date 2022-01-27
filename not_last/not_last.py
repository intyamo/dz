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
    pupils = dict(pupils)
    new_values = pupils.values()
    sort_values = list(set((new_values)))
    sort_values.sort(reverse=True)
    b = sort_values[-2]
    new_name = []
    for keys, value in pupils.items():
        if value == b:
            new_name.append(keys)

    new_name.sort()
    return new_name
