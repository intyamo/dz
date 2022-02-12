"""
1. Напишите параметрический декоратор, который вызывает оборачиваемую функцию
несколько раз (по умолчанию - 2).


2. Напишите параметрический декоратор, превращает в html тэг с атрибутами.

Имя html тэга передаётся в виде позиционного аргумента, а его атрибуты -
через именованные аргументы. Булевые атрибуты¹ передаются в виде `attribute=True`.

1: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes#boolean_attributes
"""


def repeat(n=2):
    def dec(fun):
        def wrapper(*args, **kwargs):
            for i in range(n):
                fun_n = fun(*args, **kwargs)
            return fun_n

        return wrapper

    return dec

def html(tag: str, **attributes):
    def dec(fun):
        def wrapper(*args, **kwargs):
            result_fun = fun(*args, **kwargs)
            itog = ['']
            for at_x, at_y in attributes.items():
                itog.append(at_x) if at_y == True or at_y == False else itog.append(f'{at_x}="{at_y}"')
            result_fun = f'<{tag}{" ".join(itog)}>{result_fun}</{tag}>'
            return result_fun

        return wrapper

    return dec

