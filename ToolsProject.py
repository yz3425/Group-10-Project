#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


index=np.array(list_file_name).T[0]
artist=np.array(list_file_name).T[1]
lyrics=np.array(list_file_name).T[2]
data = pd.DataFrame({"Aritist":artist,
                         "Song":lyrics, 
                          "lyric":lyric_list})
data.to_excel('tools.xlsx')
data


# In[66]:


import numpy as np
import pandas as pd
data = pd.read_excel('tools.xlsx', index_col=0) 
# turn columns Song and lyric into string
data = data.astype({"lyric": str, "Song": str})
# make lyric lowercase 
for i in range (len(data)):
    data['lyric'][i] = data['lyric'][i].lower()


# In[67]:


# turn columns Song and lyric into string
data = data.astype({"lyric": str, "Song": str})
# make lyric lowercase 
for i in range (len(data)):
    data['lyric'][i] = data['lyric'][i].lower()

# love related
data['love_count']=''
for i in range (len(data)):
    data['love_count'][i] =sum(map(data['lyric'][i].count,('love','loving','sweet','sweetness','baby','babe',
                                                           'sweetheart','cute','cutest','cuteness','honey',
                                                           'loved','affection','adore','adorable',
                                                           'angel','dear','dearest','darling','fond','fondness','heart',
                                                           'kiss','romance','romantic','appreciate','appreciation','amour','attach',
                                                          'enjoy','like','liking','devote','devoted','worship','crush','sugar',
                                                          'idol','cherish','cherishing','beloved','truelove','treasure','sweetie')))

# hate related  
data['hate_count']=''
for i in range (len(data)):    
    data['hate_count'][i]=sum(map(data['lyric'][i].count,('hate','hatred','enemy','resent','disgust','disgusting','horror','horrible',
                                                          'loath','reject','rejection','revolt','detest', 'refuse','loath','hell','shit',
                                                          'rage','lies','lier','lying','lie','lied',
                                                          'cheat','cheater','sick','sickness','nausea','dislike','deceive',
                                                          'disappointed','disappointing','disappoint','fake','faking','faked','victim',
                                                          'scam','burn','fooled','trick','tricked','delude','delusion','deluded','joke','bad','worst')))
    


#Not Kid Safe: the higher the count, the less kid friendly
data['NotKidSafe_count']=''
for i in range (len(data)):
    data['NotKidSafe_count'][i] =sum(map(data['lyric'][i].count,('fuck', 'fucking', 'shit', 'bloody', 'screw', 'screwed','ass', 
                                                              'asshole', 'dammnit', 'damn', 'bitch','bitches', 'son of a bitch', 'frick',
                                                              'hell', 'dumb', 'butt', 'screw', 'crap', 'idiot', 'cocksucker', 'jerk',
                                                              'motherfucker', 'schmuck', 'jackass', 'bastard', 'dickhead',
                                                             'asshat', 'dumbo', 'moron', 'loser', 'nerd', 'fool', 'kill', 'murder',
                                                             'killing', 'killed', 'injure', 'injured', 'suicide', 'bloodying', 'blood',
                                                             'dick', 'cock', 'piss', 'fuck you', 'fuck off', 'frigger', 'nigga',
                                                             'sucker', 'nigger', 'prick', 'slut', 'whore', 'darn', 'pussy', 'fag',
                                                             'douche', 'bitchy','bitchass', 'bullshit', 'jerk')))




# In[68]:


data


# In[ ]:




