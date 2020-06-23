import os
from random import randrange

os.chdir('pred_shark/')
for dirname in os.listdir("."):
    int1 = randrange(1000, 9999)
    int2 = randrange(1000, 9999)
    int3 = randrange(1000, 9999)
    os.rename(dirname, f'{int1}_{int2}_{int3}.jpg')
    
os.chdir('..')
os.chdir('pred_non_shark')
for dirname in os.listdir("."):
    int1 = randrange(1000, 9999)
    int2 = randrange(1000, 9999)
    int3 = randrange(1000, 9999)
    os.rename(dirname, f'{int1}_{int2}_{int3}.jpg')