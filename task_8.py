# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
# Для хождения по директориям используйте стандартную функцию. Результат выдавайте списком, List например.


import os
from typing import List


import os


def print_all_files_recursive_in_one_function(dir_name: str) -> None:

    qualified_item_names = (os.path.join(dir_name, filename) for filename in os.listdir(dir_name))

    for item in qualified_item_names:

        if os.path.isfile(item):
            print(os.path.join(dir_name, item))

        elif os.path.isdir(item):
            new_dir_name = os.path.join(dir_name, item)
            print_all_files_recursive_in_one_function(new_dir_name)
