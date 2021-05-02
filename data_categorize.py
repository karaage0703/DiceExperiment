#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import json
import os
import shutil

parser = argparse.ArgumentParser(description='data_categorize')
parser.add_argument('--datasets_dir', default='')
parser.add_argument('--images_dir', default='')
parser.add_argument('--images_numb', default='100')

args = parser.parse_args()

datasets_dir = args.datasets_dir
images_dir = args.images_dir
images_numb = int(args.images_numb)

filename = datasets_dir + '/captures_000.json'
target_dir = 'target'

if os.path.exists(target_dir):
    shutil.rmtree(target_dir)

os.makedirs(target_dir)

with open(filename, mode='r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(0, images_numb):
    image_filename = data['captures'][i]['filename']
    label_name = data['captures'][i]['annotations'][0]['values'][0]['label_id']

    target_label_dir = target_dir + '/' + str(label_name)
    if not os.path.exists(target_label_dir):
        os.makedirs(target_label_dir)

    image_org_filename = image_filename
    image_target_filename = target_label_dir + '/' + str(i) + '.png'

    shutil.copyfile(image_org_filename, image_target_filename)

# Usage
# python3 data_categorize.py --datasets_dir="Datasetac6d0869-b074-4323-87f6-c2881bcc0ca7" --images_dir="RGBd50ab295-b98b-4d48-a68b-c8bdaa6e554f" --images_numb=100
