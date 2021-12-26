# Homework

## Задания

### 1. Числа и арифметические выражения

- circle
- pizza_delivery

### 2. Логические выражения, `bool`, `if`-`else if`-`else`

- coins
- leap_year
- lessons

### 3. Строки `str`

- str_remove_fragment
- password_checker
- chess_fen
- atbash_cipher

## Краткая инструкция

1. Установите `git` и `pytest`

    ```sh
    pip install pytest
    ```

2. Сделайте fork данного репозитория (т.е. https://github.com/intyamo/dz)

   Через кнопку `fork` и `git clone`:

    ```sh
    git clone https://github.com/<github_username>/homework.git
    # ssh
    git clone git@github.com:<github_username>/homework.git
    ```

   Или через [GitHub CLI](https://github.com/cli/cli#installation):

    ```sh
    gh repo fork intyamo/dz
    ```

3. Создайте отдельную ветку для текущего ДЗ

    ```sh
    git switch -c dz_<номер_дз>
    ```

4. Решите задание

   Каждое задание находится в отдельной папке:

    ```sh
    circle
    ├── circle.py       # само задание
    └── test_circle.py  # а это тесты
    ```

    Вам необходимо реализовать только функции,

5. Проверьте тесты

    ```sh
    # из корневой папки
    pytest <папка_с_заданием>

    # или непосредственно из папки с заданием, например
    cd <папка_с_заданием>
    pytest
    ```

6. Commit, push

   Перед коммитом отформатируйте код

    - через PyCharm (`Code -> Reformat code`)
    - или [`black`](https://github.com/psf/black)

    ```sh
    # установить (один раз)
    pip install black

    # отформатировать нужные файлы
    black circle/circle.py pizza_delivery/pizza.py
    ```

7. Открыть Pull Request (PR) на GitHub
