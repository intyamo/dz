"""
1. Напишите параметрический декоратор, который вызывает оборачиваемую функцию
несколько раз (по умолчанию - 2).


2. Напишите параметрический декоратор, превращает в html тэг с атрибутами.

Имя html тэга передаётся в виде позиционного аргумента, а его атрибуты -
через именованные аргументы. Булевые атрибуты¹ передаются в виде `attribute=True`.

1: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes#boolean_attributes
"""


def repeat(n=2):
    def my_decorator(function_to_decorate):
        def wrapped(*args, **kwargs):
            for i in range(n):
                result = function_to_decorate()
            return result

        return wrapped

    return my_decorator


def html(tag: str, **attributes):
    def my_decorator(function_to_decorate):
        def wrapped(*args, **kwargs):
            result = function_to_decorate()
            dict_1 = ['']
            for i, j in attributes.items():
                if j != True and j != False:
                    dict_1.append(str(i) + '=' + '"' + str(j) + '"')
                else:
                    dict_1.append(str(i))
            result = '<' + tag + ' '.join(dict_1) + '>' + result + '</' + tag + '>'
            print(result)
            return result

        return wrapped

    return my_decorator
