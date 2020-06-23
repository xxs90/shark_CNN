#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:49:12 2020
@author: Zac Yung-Chun Liu
"""
#import os
import pandas as pd
import shutil

# based on the prediction label, move the file classified as shark/ non-shark to another folder
source_files = 'dataset/test_set/shark/'
shark_folder = 'pred_shark/'
non_shark_folder = 'pred_non_shark/'

# load csv file
df = pd.read_csv('class_prediction.csv')
class_predicted = df['class_predicted'].tolist()
test_label = df['filename'].tolist()

# move the file based on the label
for i in range(len(class_predicted)):
    if class_predicted[i] == 1:
        label = test_label[i].split('/')
        label = label[1]
        shutil.move(source_files + label, shark_folder + label)
        print(i)
    if class_predicted[i] == 0:
        label = test_label[i].split('/')
        label = label[1]
        shutil.move(source_files + label, non_shark_folder + label)
        print(i)