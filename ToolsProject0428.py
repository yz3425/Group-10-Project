
# coding: utf-8

# In[104]:

from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import json
get_ipython().system('pip install langdetect')


# In[109]:

####making data frame part
print("enter path to the directory:")  ###C:/Lyrics
mypath = input()
file_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
list_file_name = [file.split('~') for file in file_name]
lyric_list = []
for file in file_name:
    path=mypath+'/'+file
    f = open(path,'r',encoding="utf8")
    lyric_list.append(f.read())
index=np.array(list_file_name).T[0]
artist=np.array(list_file_name).T[1]
lyrics=np.array(list_file_name).T[2]
data = pd.DataFrame({"index":ind#########detecting foreign language
from langdetect import detect
data['Language']=''
for i in range(len(data)):
    data['Language'][i]=detect(data['Lyrics'][i])ex,"Artist":artist,
                         "Song":lyrics, 
                          "Lyrics":lyric_list})


# In[110]:

#########detecting foreign language
from langdetect import detect
data['Language']=''
for i in range(len(data)):
    data['Language'][i]=detect(data['Lyrics'][i])


# In[112]:

# turn columns Song and lyric into string
data = data.astype({"Lyrics": str, "Song": str})
# make lyric lowercase 
for i in range (len(data)):
    data['Lyrics'][i] = data['Lyrics'][i].lower()


# In[116]:

# love related
data['love_count']=''
for i in range (len(data)):
    data['love_count'][i] =sum(map(data['Lyrics'][i].count,('love','loving','sweet','sweetness','baby','babe',
                                                           'sweetheart','cute','cutest','cuteness','honey',
                                                           'loved','affection','adore','adorable',
                                                           'angel','dear','dearest','darling','fond','fondness','heart',
                                                           'kiss','romance','romantic','appreciate','appreciation','amour','attach',
                                                          'enjoy','like','liking','devote','devoted','worship','crush','sugar',
                                                          'idol','cherish','cherishing','beloved','truelove','treasure','sweetie')))
# hate related    
data['hate_count']=''
for i in range (len(data)):    data['hate_count'][i]=sum(map(data['Lyrics'][i].count,('hate','hatred','enemy','resent','disgust','disgusting','horror','horrible',
                                                          'loath','reject','rejection','revolt','detest', 'refuse','loath','hell','shit',
                                                          'rage','lies','lier','lying','lie','lied',
                                                          'cheat','cheater','sick','sickness','nausea','dislike','deceive',
                                                          'disappointed','disappointing','disappoint','fake','faking','faked','victim',
                                                          'scam','burn','fooled','trick','tricked','delude','delusion','deluded','joke','bad','worst')))
# love dimension
data['Love-dimension']=''
for i in range (len(data)):
    data['Love-dimension'][i]=data['love_count'][i]-data['hate_count'][i]
    
    
#love score
percentile_10 = np.percentile(data['Love-dimension'], 10)
percentile_20 = np.percentile(data['Love-dimension'], 20)
percentile_30 = np.percentile(data['Love-dimension'], 30)
percentile_40 = np.percentile(data['Love-dimension'], 40)
percentile_50 = np.percentile(data['Love-dimension'], 50)
percentile_60 = np.percentile(data['Love-dimension'], 60)
percentile_70 = np.percentile(data['Love-dimension'], 70)
percentile_80 = np.percentile(data['Love-dimension'], 80)
percentile_90 = np.percentile(data['Love-dimension'], 90)

data['Love_score']=''
for i in range(len(data)):
    if data['Love-dimension'][i]<percentile_10:
        percentile = 0.1
    elif data['Love-dimension'][i]<percentile_20:
        percentile = 0.2
    elif data['Love-dimension'][i]<percentile_30:
        percentile = 0.3
    elif data['Love-dimension'][i]<percentile_40:
        percentile = 0.4
    elif data['Love-dimension'][i]<percentile_50:
        percentile = 0.5
    elif data['Love-dimension'][i]<percentile_60:
        percentile = 0.6
    elif data['Love-dimension'][i]<percentile_70:
        percentile = 0.7
    elif data['Love-dimension'][i]<percentile_80:
        percentile = 0.8
    elif data['Love-dimension'][i]<percentile_90:
        percentile = 0.9
    else:
        percentile = 1
    data['Love_score'][i]=percentile


# In[117]:

#Not Kid Safe: the higher the count, the less kid friendly
data['NotKidSafe_count']=''
for i in range (len(data)):
    data['NotKidSafe_count'][i] =sum(map(data['Lyrics'][i].count,('fuck', 'fucking', 'shit', 'bloody', 'screw', 'screwed','ass', 
                                                              'asshole', 'dammnit', 'damn', 'bitch','bitches', 'son of a bitch', 'frick',
                                                              'hell', 'dumb', 'butt', 'screw', 'crap', 'idiot', 'cocksucker', 'jerk',
                                                              'motherfucker', 'schmuck', 'jackass', 'bastard', 'dickhead',
                                                             'asshat', 'dumbo', 'moron', 'loser', 'nerd', 'fool', 'kill', 'murder',
                                                             'killing', 'killed', 'injure', 'injured', 'suicide', 'bloodying', 'blood',
                                                             'dick', 'cock', 'piss', 'fuck you', 'fuck off', 'frigger', 'nigga',
                                                             'sucker', 'nigger', 'prick', 'slut', 'whore', 'darn', 'pussy', 'fag',
                                                             'douche', 'bitchy','bitchass', 'bullshit', 'jerk')))
#Kid Safe: the higher the count, the higher kid friendly 
data['KidSafe_count']=''
for i in range (len(data)):
    data['KidSafe_count'][i] =sum(map(data['Lyrics'][i].count,('happy', 'happiness', 'joy', 'active', 'beautiful', 'smiley',
                                                             'inspiring', 'joyous', 'kissable', 'smile', 'smiling', 'amaze', 'amazing', 'dream', 'smart',
                                                             'blessed', 'bright', 'friendly', 'funny', 'cheerful', 'charming', 'gorgeous', 'good', 'playful', 'treasured',
                                                             'cute', 'huggable', 'proud', 'wonderful', 'prince', ' princess', 'wonder', 'friend', 'miracle', 'teddy bear',
                                                             'toys', 'family', 'friend', 'angle', 'star')))    
# kid-safe dimension
data['Kid_Safe-dimension']=''
for i in range (len(data)):
    data['Kid_Safe-dimension'][i]=data['KidSafe_count'][i]-data['NotKidSafe_count'][i]

#kid safe score
percentile_10 = np.percentile(data['Kid_Safe-dimension'], 10)
percentile_20 = np.percentile(data['Kid_Safe-dimension'], 20)
percentile_30 = np.percentile(data['Kid_Safe-dimension'], 30)
percentile_40 = np.percentile(data['Kid_Safe-dimension'], 40)
percentile_50 = np.percentile(data['Kid_Safe-dimension'], 50)
percentile_60 = np.percentile(data['Kid_Safe-dimension'], 60)
percentile_70 = np.percentile(data['Kid_Safe-dimension'], 70)
percentile_80 = np.percentile(data['Kid_Safe-dimension'], 80)
percentile_90 = np.percentile(data['Kid_Safe-dimension'], 90)

data['Kid_Safe_score']=''
for i in range(len(data)):
    if data['Kid_Safe-dimension'][i]<percentile_10:
        percentile = 0.1
    elif data['Kid_Safe-dimension'][i]<percentile_20:
        percentile = 0.2
    elif data['Kid_Safe-dimension'][i]<percentile_30:
        percentile = 0.3
    elif data['Kid_Safe-dimension'][i]<percentile_40:
        percentile = 0.4
    elif data['Kid_Safe-dimension'][i]<percentile_50:
        percentile = 0.5
    elif data['Kid_Safe-dimension'][i]<percentile_60:
        percentile = 0.6
    elif data['Kid_Safe-dimension'][i]<percentile_70:
        percentile = 0.7
    elif data['Kid_Safe-dimension'][i]<percentile_80:
        percentile = 0.8
    elif data['Kid_Safe-dimension'][i]<percentile_90:
        percentile = 0.9
    else:
        percentile = 1
    data['Kid_Safe_score'][i]=percentile


# In[118]:

#Mood Analysis: the higher the positive count, the happier song it is 
data['Happy_count']=''
for i in range (len(data)):
    data['Happy_count'][i] =sum(map(data['Lyrics'][i].count,('happy', 'happiness', 'contented', 'content', 'cheerful', 'cheer', 'cheery', 'merry', 'joyful', 
                                                            'gleeful', 'joke', 'joking', 'smiling', 'delighted', 'smiling', 'smile', 'glowing', 'satisfied', 'satisfy', 'satisfying'
                                                            'sunny', 'sun', 'bless', 'blessing', 'blessed', 'good-humored', 'thrilled', 'blissful', 'lucky', 'blissful', 
                                                           'favorable', 'favorable', 'active', 'beautiful', 'smiley','smiling', 'amaze', 'amazing', 'bright',  'funny', 
                                                           'cheerful', 'lucky', 'heaven', 'glad', 'pleased', 'alive', 'glad', 'excited')))  
data['sad_count']=''
for i in range (len(data)):    
    data['sad_count'][i]=sum(map(data['Lyrics'][i].count,('sad','sadness','tear','tears','cry','cried','cries','crying',
                                                          'blue','fear','fears','feared','weep', 'weeping','sob','sobbing','scream',
                                                          'screaming','lonely','hurt','hurts','hurted','alone','drowning','drowned','broken',
                                                        'break','down')))

# Mood dimension
data['Mood-dimension']=''
for i in range (len(data)):
    data['Mood-dimension'][i]=data['Happy_count'][i]-data['sad_count'][i]
    
    
#Mood score
percentile_10 = np.percentile(data['Mood-dimension'], 10)
percentile_20 = np.percentile(data['Mood-dimension'], 20)
percentile_30 = np.percentile(data['Mood-dimension'], 30)
percentile_40 = np.percentile(data['Mood-dimension'], 40)
percentile_50 = np.percentile(data['Mood-dimension'], 50)
percentile_60 = np.percentile(data['Mood-dimension'], 60)
percentile_70 = np.percentile(data['Mood-dimension'], 70)
percentile_80 = np.percentile(data['Mood-dimension'], 80)
percentile_90 = np.percentile(data['Mood-dimension'], 90)

data['Mood_score']=''
for i in range(len(data)):
    if data['Mood-dimension'][i]<percentile_10:
        percentile = 0.1
    elif data['Mood-dimension'][i]<percentile_20:
        percentile = 0.2
    elif data['Mood-dimension'][i]<percentile_30:
        percentile = 0.3
    elif data['Mood-dimension'][i]<percentile_40:
        percentile = 0.4
    elif data['Mood-dimension'][i]<percentile_50:
        percentile = 0.5
    elif data['Mood-dimension'][i]<percentile_60:
        percentile = 0.6
    elif data['Mood-dimension'][i]<percentile_70:
        percentile = 0.7
    elif data['Mood-dimension'][i]<percentile_80:
        percentile = 0.8
    elif data['Mood-dimension'][i]<percentile_90:
        percentile = 0.9
    else:
        percentile = 1
    data['Mood_score'][i]=percentile  


# In[119]:

data['length']=''
for i in range(len(data)):
    data['length'][i] = len(data['Lyrics'][i])
percentile_75 = np.percentile(data['length'], 75)
percentile_50 = np.percentile(data['length'], 50)
percentile_25 = np.percentile(data['length'], 25)
data['length_score']=''
for i in range(len(data)):
    if data['length'][i]<percentile_25:
        percentile = 0.25
    elif data['length'][i]<percentile_50:
        percentile = 0.5
    elif data['length'][i]<percentile_75:
        percentile = 0.75
    else:
        percentile = 1
    data['length_score'][i]=percentile


# In[120]:

data['word_count']=''
for i in range(len(data)):
    counts = dict()
    words = data['Lyrics'][i].split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    data['word_count'][i] = len(counts)
percentile_75 = np.percentile(data['word_count'], 75)
percentile_50 = np.percentile(data['word_count'], 50)
percentile_25 = np.percentile(data['word_count'], 25)
data['word_count_score']=''
for i in range(len(data)):
    if data['word_count'][i]<percentile_25:
        percentile = 0.25
    elif data['word_count'][i]<percentile_50:
        percentile = 0.5
    elif data['word_count'][i]<percentile_75:
        percentile = 0.75
    else:
        percentile = 1
    data['word_count_score'][i]=percentile
####complexity part


# In[121]:

for i in range (len(data)):  
    if data['Language'][i] != 'en':
        data['Love_score'][i]=None
        data['Kid_Safe_score'][i]=None
        data['Mood_score'][i]=None


# In[122]:

df = data[['Artist','Song','index','Love_score','Kid_Safe_score','Mood_score','length_score','word_count_score']]
print("Type your destination to save your json:")
mypath = input()####### C:\Users\brandon\Downloads
Export = df.to_json(mypath+'/result.json',orient='records')
with open(mypath+'/result.json') as fp:
    data = json.load(fp)
with open(mypath+'/result.json', 'w') as fp:
    json.dump(
        obj=data,
        fp=fp,
        indent=True,  # pretty printing
        sort_keys=True,  # sorting for easier lookup by a human
    )
with open(mypath+'/result.json') as fp:
    data = json.load(fp)
data


# In[ ]:



