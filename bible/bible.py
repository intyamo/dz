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
    # text = BIBLE.lower()
    text_minus_punkt = BIBLE.lower().translate(BIBLE.lower().maketrans('', '', string.punctuation))
    text_minus_digit = text_minus_punkt.translate(text_minus_punkt.maketrans('', '', string.digits))
    dict_1 = {}
    for i in text_minus_digit.split():
        dict_1[i] = dict_1.get(i, 0) + 1
    spis_1 = list(dict_1.items())
    spis_1.sort(key=lambda j: j[1], reverse=True)
    spis_itog = []
    for k in range(n):
        spis_itog.append(spis_1[k][0])
    return spis_itog


# n = int(input())
if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
