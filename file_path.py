def file_list_in_dir():
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_pwd = os.chdir(current_dir)
    file_list = os.listdir()
    return file_list


temp_file_list = []
for i in file_list_in_dir():
    if '.sql' in i:
        temp_file_list.append(i)
file_list = temp_file_list


def seek_in_file(file_list):

    print("Введите подстроку для поиска")
    seek_input = input()
    new_file_list = []
    for i in file_list:
        with open(i, encoding = 'utf-8') as sql:
            text = sql.read()

            if seek_input in text:
                new_file_list.append(i)

    print('Всего найдено файлов', len(new_file_list) )
    file_list = new_file_list

    return seek_in_file(file_list)

seek_in_file(file_list)
