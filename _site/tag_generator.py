#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
import yaml

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')

total_tags = []

# Modifications
yaml_lines = []

for filename in filenames:
    f = open(filename, 'r', encoding="utf8")
    for line in f:
       if line.strip() == '---':
        break
    for line in f:
       if line.strip() == '---':
           break
       else:
          yaml_lines.append(line)
yaml_string = "".join(yaml_lines)
yaml_list = yaml.load(yaml_string)
print(yaml_list)
