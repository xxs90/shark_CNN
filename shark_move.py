import os
import shutil
import pandas as pd
import re
import urllib.request
import sys

pd.options.mode.chained_assignment = None

os.chdir('false_positive/')
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f
pwd_list = list(listdir_nohidden(os.getcwd()))

df = pd.DataFrame(pwd_list, columns=['img_name'])

os.chdir('dataset/test_set/not_shark/')

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f
            
pwd_list = list(listdir_nohidden(os.getcwd()))

for i in df.index:

	name = df['img_name'][i]
	'''
	name_use = name + '.jpg'
	'''
	try:
		shutil.move(f'{name}', 'tmp/')
	except FileNotFoundError:
		continue
