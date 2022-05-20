import os
from os import stat as stat
from os import scandir
from json import dumps

def_dict = {100: [0,[]], 1000: [0,[]], 10000: [0,[]], 100000: [0,[]], 1000000: [0,[]]}
root_dir = os.path.join('.', 'some_data_adv')
for file in scandir(root_dir):
    file_stat = stat(file)
    file_size = file_stat.st_size
    _,file_ext=file.name.split('.')
    if file_size <= 100:
        size=100
    if 100 < file_size <= 1000:
        size=1000
    if 1000 < file_size <= 10000:
        size=10000
    if 10000 < file_size <= 100000:
        size=100000
    def_dict[size][0]+=1
    if file_ext not in def_dict[size][1]:
        def_dict[size][1].append(file_ext)
with open(os.path.join('.','some_data_adv_summary.json'), 'w', encoding='utf-8') as file_1:
    dict_json=dumps(def_dict)
    file_1.write(dict_json)

# print(def_dict)
