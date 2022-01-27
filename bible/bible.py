#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""


from pathlib import Path


f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text()


def most_freq_bible_words(n: int) -> list:
    from pathlib import Path
    import re
    f = Path(__file__).parent.absolute() / "king_james_bible.txt"
    BIBLE = f.read_text().lower()
    word = re.findall(r'\w+', BIBLE)
    c = {}

    for i in word:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1

    lst = list()
    for key, val in c.items():
        lst.append((val, key))
    lst.sort(reverse=True)

    k = []
    for val, key in lst[:n]:
        k.append(key)
    return k


if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
