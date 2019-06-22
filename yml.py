#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:24:59 2019

@author: jdummer
"""

import yaml
import os
import glob

def extract_yaml(filename):
    yml_lines = []
    with open(filename, encoding='utf8') as file:
        for line in file:
            if line.strip() == '---':
                break
        for line in file:
            if line.strip() == '---':
                break
            else:
                yml_lines.append(line)

    yml_string = "".join(yml_lines)
    return yaml.load(yml_string)

if __name__ == '__main__':
    post_dir = '_posts'
    tag_dir = 'tag/'

    filenames = glob.glob(os.path.join(post_dir, '*md'))
    total_tags = []
    for filename in filenames:
        post_yaml = extract_yaml(filename)
        if post_yaml is not None:
            tags = post_yaml.get('tags', [])
            tags = [indiv_tag.replace(' ','+') for indiv_tag in tags]
            total_tags.extend(tags)
    total_tags = set(total_tags)
    print(total_tags)

    old_tags = glob.glob(tag_dir + '*.md')
    for old_tag_page in old_tags:
        os.remove(old_tag_page)

    if not os.path.exists(tag_dir):
        os.makedirs(tag_dir)

    for tag in total_tags:
        tag_filename = tag_dir + tag + '.md'
        tag_page = open(tag_filename, 'a')
        tag2 = tag.replace('+',' ')
        write_str = '---\nexclude: true\nlayout: tagpage\ntitle: \"Tagged: ' + tag2 + '\"\ntag: ' + tag2 + '\nrobots: noindex\n---\n'
        tag_page.write(write_str)
        tag_page.close()
    print("Tags generated, count", total_tags.__len__())

    # need to review tags to find duplicates (alternate spellings)
    # need to check the URL of tag pages so that tags can be linked to those pages (does that change things here?)
