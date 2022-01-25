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
    pupils.sort(key=lambda j: j[1])
    print(*pupils, sep='\n')
    pupils_itog_1 = []
    for k in range(len(pupils)):
        if pupils[k][1] == pupils[0][1]:
            continue
        else:
            pupils_itog_1.append(pupils[k])
    pupils_itog_2 = []
    for i in range(len(pupils_itog_1)):
        if pupils_itog_1[i][1] == pupils_itog_1[0][1]:
            pupils_itog_2.append(pupils_itog_1[i][0])
        else:
            break
    return sorted(pupils_itog_2)

# pupils = [
#     ("Вася Пупкин", 3.2),
#     ("Петя Дудкин", 3.9),
#     ('Юра Баранкин', 4.100_01),
#     ("Костя Малинин", 3.141_592),
#     ("Зина Фокина", 4.8),
#     ("Артур Пирожков", 3.2),
#     ("Гадя Петрович", 3.141_592)
# ]
#
# x = last_but_one(pupils)
# print(x)
