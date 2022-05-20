from os import path as path
from os import stat as stat
from os import scandir

def_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
root_dir = path.join('.', 'some_data')
for file in scandir(root_dir):
    file_stat = stat(file)
    size = file_stat.st_size
    if size <= 100:
        def_dict[100] += 1
    if 100 < size <= 1000:
        def_dict[1000] += 1
    if 1000 < size <= 10000:
        def_dict[10000] += 1
    if 10000 < size <= 100000:
        def_dict[100000] += 1

print(def_dict)
print(
    f'Тут {def_dict[100]} файл размером не более 100 байт; {def_dict[1000]} файлов больше 100 и не больше 1000 байт, {def_dict[10000]} файлов больше 1000 и не больше 10000 байт')
