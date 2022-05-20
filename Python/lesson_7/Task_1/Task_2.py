
# 1. открыть ямл
# 2. Разделить файл на строки
# 3. Как-то обработать строки, чтобы понять на какому уровне находится файл
# 4. Создать список файлов уровня
# 5. Создать файл из списка

import os
with open(os.path.join('config_2.yaml'), encoding='utf-8') as file_1:
    dir_list=file_1.readlines()
    # root_name='my_project'
    # dir_list=['settings','mainapp','adminapp','authapp']
    # for dirs in dir_list:
    #     dir_path=os.path.join(root_name,dirs)
    #     if not os.path.exists(dir_path):
    #         os.makedirs(dir_path)
    print(dir_list)