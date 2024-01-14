# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
# Для хождения по директориям используйте стандартную функцию. Результат выдавайте списком, List например.


import os
from typing import List


import os


def print_all_files(dir_name: str) -> List:
    files_in_dir = []
    print_all_files_recursive(dir_name, dir_name, files_in_dir)

    return files_in_dir


def print_all_files_recursive(dir_name: str,
                              home_dir_name: str,
                              files_in_dir: List) -> None:

    qualified_item_names = (os.path.join(dir_name, filename) for filename in os.listdir(dir_name))
    for item in qualified_item_names:

        if os.path.isfile(item):
            files_in_dir.append(os.path.relpath(os.path.join(dir_name, item), home_dir_name))

        elif os.path.isdir(item):
            new_dir_name = os.path.join(dir_name, item)
            print_all_files_recursive(new_dir_name, home_dir_name, files_in_dir)
