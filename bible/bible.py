#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""
import re
from pathlib import Path


f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text().lower()


def most_freq_bible_words(n: int) -> list:
    list_word = re.findall(r'\w+', BIBLE)
    dict_word = {}
    list_key = []
    ready_list = []
    for word in list_word:
        if word in dict_word:
            dict_word[word] += 1
        else:
            dict_word[word] = 1
    for key, value in dict_word.items():
        list_key.append((value, key))
    list_key.sort(reverse=True)

    for value, key in list_key[:n]:
        ready_list.append(key)
    return ready_list















#if __name__ == "__main__":
#    print(*most_freq_bible_words(10), sep="\n")
