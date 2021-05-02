#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import os
import shutil
import subprocess

cmd_sp = 'ls | grep Dataset'
datasets_dir = subprocess.check_output(cmd_sp, shell=True).decode('utf-8').rstrip("\n")
cmd_sp = 'ls | grep RGB'
images_dir = subprocess.check_output(cmd_sp, shell=True).decode('utf-8').rstrip("\n")
cmd_sp = 'ls ' + datasets_dir + ' | grep capture'
ls_filenames = subprocess.check_output(cmd_sp, shell=True).decode('utf-8').strip().split('\n')

target_dir = 'target'

if os.path.exists(target_dir):
    shutil.rmtree(target_dir)

os.makedirs(target_dir)

file_numb = 0

for filename in ls_filenames:
    filename = datasets_dir + '/' + filename
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    for i in range(0, len(data['captures'])):
        image_filename = data['captures'][i]['filename']
        label_name = data['captures'][i]['annotations'][0]['values'][0]['label_id']

        target_label_dir = target_dir + '/' + str(label_name)
        if not os.path.exists(target_label_dir):
            os.makedirs(target_label_dir)

        image_org_filename = image_filename
        image_target_filename = target_label_dir + '/' + str(file_numb) + '.png'
        shutil.copyfile(image_org_filename, image_target_filename)
        file_numb += 1
