import pandas as pd

# edit this script to add .jpg or .png to new csv of image lists

df1 = pd.read_csv('sp.csv')

for i in df1.index:
	df1['img_name'][i] =  df1['img_name'][i] + '.jpg'
df1.to_csv('sp.csv', index=False)