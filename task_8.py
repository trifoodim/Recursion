# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
# Для хождения по директориям используйте стандартную функцию. Результат выдавайте списком, List например.


import os


def print_all_files(dir_name):
    print_all_files_recursive(dir_name, dir_name)


def print_all_files_recursive(dir_name, home_dir_name):
    qualified_item_names = (os.path.join(dir_name, filename) for filename in os.listdir(dir_name))

    files_in_curr_dir = []
    for item in qualified_item_names:
        if os.path.isfile(item):
            files_in_curr_dir.append(os.path.relpath(os.path.join(dir_name, item), home_dir_name))

        elif os.path.isdir(item):
            new_dir_name = os.path.join(dir_name, item)
            print_all_files_recursive(new_dir_name, home_dir_name)

    print(files_in_curr_dir)
