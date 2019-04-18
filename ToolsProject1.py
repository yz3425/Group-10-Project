#!/usr/bin/env python
# coding: utf-8

# In[17]:


from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
mypath='/Users/yuchenchen/Desktop/Lyrics'
file_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
list_file_name = [file.split('~') for file in file_name]
lyric_list = []
for file in file_name:
    path='/Users/yuchenchen/Desktop/Lyrics/'+file
    f = open(path,'r',encoding="utf8")
    lyric_list.append(f.read())


# In[24]:


index=np.array(list_file_name).T[0]
artist=np.array(list_file_name).T[1]
lyrics=np.array(list_file_name).T[2]
dataframe_ = pd.DataFrame({"Aritist":artist,
                         "Song":lyrics, 
                          "lyric":lyric_list})
dataframe_.to_excel('tools.xlsx')
dataframe_


# In[ ]:




