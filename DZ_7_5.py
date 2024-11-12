import os
import time

def get_parameters():
    print('-------------------------------------')
    print('Текущая директория', os.getcwd())
    print('-------------------------------------')
    file_path_list = []
    for address, dirs, files in os.walk('.'):
        for name in files:
            file_path_list.append(os.path.join(address, name))

    print(f'Список файлов в директориях текущей директории: {file_path_list}')
    print(f'Список текущей директории: {os.listdir()}')


    file = [f for f in os.listdir() if os.path.isfile(f)]
    dirs  = [d for d in os.listdir() if os.path.isdir(d)]

    filesize = os.path.getsize(file[0])
    filetime = os.path.getmtime(file[0])
    formated_time = time.strftime("%d.%m.%Y.%H.%M", time.localtime(filetime))
    parent_dir = os.path.dirname(os.path.abspath(file[0]))


    return (f'Обнаружен файл: {file[0]}, Путь: {file_path_list[0]},  Размер:  {filesize} байт,'
          f' Время изменения: {formated_time}, '
          f'Родительская директория: {parent_dir}')


if __name__ == '__main__':

    for i in range(4):
        if os.path.exists('DIR_' + str(i+1)):
            os.chdir('DIR_' + str(i+1))
        else:
            os.mkdir('DIR_' + str(i+1))
            os.chdir('DIR_' + str(i+1))

        with open('file_'+ str(i+1) + '.txt', 'w') as f:
            f.write('Hello world')

    print(get_parameters())

    os.chdir('../')
    print(get_parameters())

    os.chdir('../')
    print(get_parameters())

    os.chdir('../')
    print(get_parameters())

    os.chdir('../')
    print(get_parameters())

