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
    minim = pupils[0][1]
    pupils_1 = []
    for i in range(1, len(pupils)):
        if pupils[i][1] <= minim:
            minim = pupils[i][1]
    for j in range(len(pupils)):
        if pupils[j][1] != minim:
            pupils_1.append(pupils[j])
    minim_2 = pupils_1[0][1]
    pupils_2 = []
    for k in range(1, len(pupils_1)):
        if pupils_1[k][1] <= minim_2:
            minim_2 = pupils_1[k][1]
    for l in range(len(pupils_1)):
        if pupils_1[l][1] == minim_2:
            pupils_2.append(pupils_1[l])
    pupils_2.sort(key=lambda n: n[0])
    return pupils_2


pupils = [("Ярик", 2.7), ("Саня", 2.8), ('Яша', 3.2), ("Миша", 3.6), ("Рома", 4.8), ("Гоша", 2.2)]
print('список школьников и их годовых оценок:', *pupils, sep='\n')
print('-' * 7)
print('список школьников, имеющих вторую с конца годовую оценку:', *last_but_one(pupils), sep='\n')
