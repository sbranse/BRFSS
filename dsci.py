import pyreadr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_2014 = pyreadr.read_r('cleaned_data/data14.rds')
df_14=data_2014[None]

data_2015_18 = pyreadr.read_r('cleaned_data/data1518.rds')
df_1518=data_2015_18[None]

'''
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet_name_1')
'''

titles=df_14.keys()
print(titles)

for title in titles:
    title_14 = df_14[title].value_counts()
    title_df_14 = title_14.rename_axis(title + "14").reset_index(name='counts').sort_values(title + "14")
    title_df_14.plot(x = title + '14', y='counts', kind='bar')
    plt.savefig('distributions/'+title+'_14.png')

    title_1518 = df_1518[title].value_counts()
    title_df_1518 = title_1518.rename_axis(title + '1518').reset_index(name='counts').sort_index(ascending=0).sort_values(title+"1518")
    title_df_1518.plot(x = title+'1518', y='counts', kind='bar')
    plt.savefig('distributions/'+title+'_1518.png')

