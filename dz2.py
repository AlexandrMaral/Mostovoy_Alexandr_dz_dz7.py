# 1 Задача


import os

p_list = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, value in p_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))


# 3 Задача


from os import path, walk, listdir
import shutil

project_name = 'my_project_1'

try:
    for root, dirs, files in walk(project_name):
        if 'templates' in dirs and root != project_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(project_name, 'templates', entry))
except FileExistsError:
    print("Already worked with these templates!")


# Задача 4


import os
import django
from collections import defaultdict


def dir_info():
    root_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            django_files[size] += 1

    for size, nums in sorted(django_files.items()):
        print(f'{size}: {nums}')


dir_info()
