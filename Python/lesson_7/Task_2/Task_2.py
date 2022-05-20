import os

space = '  '
with open(os.path.join('.', 'config_2.yaml'), encoding='utf-8') as file_1:
    for line in file_1:
        level = line.count(space)
        name = line.strip().replace('- ', '').replace('  ' * level, '')
        tp = 'file'
        if name.endswith(':'):
            name=name.replace(':', '')
            tp = 'directory'
        if level == 0:
            main_dir_name = name
        if level == 0 and not os.path.exists(os.path.join('.', name)):
            if tp == 'directory':
                os.mkdir(os.path.join('.', main_dir_name))
            else:
                try:
                    with open(os.path.join('.', name), 'x', encoding='utf-8') as file_2:
                        pass
                except FileExistsError:
                    continue
        if level == 1:
            level1_name = name
        if level == 1 and not os.path.exists(os.path.join('.', main_dir_name, level1_name)):
            if tp == 'directory':
                os.mkdir(os.path.join('.', main_dir_name, level1_name))
            else:
                try:
                    with open(os.path.join('.', main_dir_name, level1_name), 'x', encoding='utf-8') as file_2:
                        pass
                except FileExistsError:
                    continue
        if level == 2:
            level2_name = name
        if level == 2 and not os.path.exists(os.path.join('.', main_dir_name, level1_name, level2_name)):
            if tp == 'directory':
                os.mkdir(os.path.join('.', main_dir_name, level1_name, level2_name))
            else:
                try:
                    with open(os.path.join('.', main_dir_name, level1_name, level2_name), 'x',
                              encoding='utf-8') as file_2:
                        pass
                except FileExistsError:
                    continue
        if level == 3:
            level3_name = name
        if level == 3 and not os.path.exists(os.path.join('.', main_dir_name, level1_name, level2_name, level3_name)):
            if tp == 'directory':
                os.mkdir(os.path.join('.', main_dir_name, level1_name, level2_name, level3_name))
            else:
                try:
                    with open(os.path.join('.', main_dir_name, level1_name, level2_name, level3_name), 'x',
                              encoding='utf-8') as file_2:
                        pass
                except FileExistsError:
                    continue
        if level == 4:
            level4_name = name
        if level == 4 and not os.path.exists(
                os.path.join('.', main_dir_name, level1_name, level2_name, level3_name, level4_name)):
            if tp == 'directory':
                os.mkdir(os.path.join('.', main_dir_name, level1_name, level2_name, level3_name, level4_name))
            else:
                try:
                    with open(os.path.join('.', main_dir_name, level1_name, level2_name, level3_name, level4_name), 'x',
                              encoding='utf-8') as file_2:
                        pass
                except FileExistsError:
                    continue
