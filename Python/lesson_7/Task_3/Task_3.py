import os
import shutil
root_dir=os.path.join('.')
for root,dirs,files in os.walk(root_dir):
    dst = os.path.join(root_dir, 'my_project', 'templates')
    if 'templates' in root:
        if len(dirs)!=0:
            src=os.path.join(root,dirs[0])
            dst=os.path.join(dst,dirs[0])
            try:
                shutil.copytree(src,dst,symlinks=False)
            except FileExistsError:
                continue