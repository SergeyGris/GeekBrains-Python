import os
root_name='my_project'
dir_list=['settings','mainapp','adminapp','authapp']
for dirs in dir_list:
    dir_path=os.path.join(root_name,dirs)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

