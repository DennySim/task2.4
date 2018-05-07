import os


def file_list_in_dir():

    file_dir = os.path.dirname(__file__)
    file_list_without_dir = os.listdir(file_dir)
    file_list = []
    for file in file_list_without_dir:
        file_list.append(os.path.join(file_dir, file))
    return file_list


def sql_file_list():
    temp_file_list = []
    for i in file_list_in_dir():
        if i.endswith('.sql'):
            temp_file_list.append(i)
    file_list = temp_file_list
    return file_list


def seek_in_file(file_list):

    print("Введите подстроку для поиска")
    seek_input = input()
    new_file_list = []
    for i in file_list:
        with open(i, encoding='utf-8') as sql:
            text = sql.read()
            if seek_input in text:
                new_file_list.append(i)

    print_searched_files(new_file_list)
    file_list = new_file_list

    return seek_in_file(file_list)


def print_searched_files(new_file_list):
    for n, file in enumerate(new_file_list):
        print(n+1, file)
    print('Всего найдено файлов', len(new_file_list))


file_list = sql_file_list()
seek_in_file(file_list)

