# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
# Для хождения по директориям используйте стандартную функцию. Результат выдавайте списком, List например.


import os
from typing import List


def print_all_files_recursive_in_one_function(dir_name: str) -> List:
    files_in_dir = []

    qualified_item_names = (os.path.join(dir_name, filename) for filename in os.listdir(dir_name))

    for item in qualified_item_names:

        if os.path.isfile(item):
            files_in_dir.append(os.path.join(dir_name, item))

        elif os.path.isdir(item):
            new_dir_name = os.path.join(dir_name, item)
            files_in_dir.extend(print_all_files_recursive_in_one_function(new_dir_name))

    return files_in_dir


print(print_all_files_recursive_in_one_function('/Users/dmitriy.trifonov/Desktop'))
