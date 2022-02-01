#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""

import string
from pathlib import Path

f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text()


def most_freq_bible_words(n: int) -> list:
    bible = BIBLE.lower()
    without_punkts = bible.translate(bible.maketrans('', '', string.punctuation))
    without_digits = without_punkts.translate(without_punkts.maketrans('', '', string.digits))
    dict = {}
    for i in without_digits.split():
        dict[i] = dict.get(i, 0) + 1
    list1 = list(dict.items())
    list1.sort(key=lambda k: k[1], reverse=True)
    list_end = []
    for j in range(n):
        list_end.append(list1[j][0])
    return list_end


if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
