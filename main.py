# coding: utf-8

# In[1]:


from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
# ! pip install langdetect
from langdetect import detect
import json


# In[2]:


####making data frame part
print("enter path to the directory:")  ##/Users/mariazhang/Dropbox/Maria/IEOR/Spring 2019/Tools/project/Lyrics
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
dataframe = pd.DataFrame({"id":index,
                    "artist":artist,
                    "title":lyrics, 
                    "lyric":lyric_list})


# In[3]:


# turn columns Song and lyric into string
dataframe = dataframe.astype({"lyric": str, "title": str})
# make lyric lowercase 
for i in range (len(dataframe)):
    dataframe['lyric'][i] = dataframe['lyric'][i].lower()
# remove .txt from the title 
for i in range (len(dataframe)):
    dataframe['title'][i] = dataframe['title'][i][:-4]


# In[4]:


# function used to calculate the score for love,kid_safe and mood
def score_calculator(list):
    percentile_10 = np.percentile(list, 10)
    percentile_20 = np.percentile(list, 20)
    percentile_30 = np.percentile(list, 30)
    percentile_40 = np.percentile(list, 40)
    percentile_50 = np.percentile(list, 50)
    percentile_60 = np.percentile(list, 60)
    percentile_70 = np.percentile(list, 70)
    percentile_80 = np.percentile(list, 80)
    percentile_90 = np.percentile(list, 90)
    
    score = np.array([])
    for i in range(len(list)):
        if list[i]<percentile_10:
            percentile = 0.1
        elif list[i]<percentile_20:
            percentile = 0.2
        elif list[i]<percentile_30:
            percentile = 0.3
        elif list[i]<percentile_40:
            percentile = 0.4
        elif list[i]<percentile_50:
            percentile = 0.5
        elif list[i]<percentile_60:
            percentile = 0.6
        elif list[i]<percentile_70:
            percentile = 0.7
        elif list[i]<percentile_80:
            percentile = 0.8
        elif list[i]<percentile_90:
            percentile = 0.9
        else:
            percentile = 1
        score=np.append(score,percentile)
        
    return score


# In[93]:


# love score
def Love_score(string)-> str:
    love_words={'love','loving','sweet','sweetness','baby','babe',
               'sweetheart','cute','cutest','cuteness','honey',
               'loved','affection','adore','adorable',
               'angel','dear','dearest','darling','fond','fondness','heart',
               'kiss','romance','romantic','appreciate','appreciation','amour','attach',
              'enjoy','like','liking','devote','devoted','worship','crush','sugar',
              'idol','cherish','cherishing','beloved','truelove','treasure','sweetie'}
    love_count= sum(map(string.count,love_words))
    
    hate_words = {'hate','hatred','enemy','resent','disgust','disgusting','horror','horrible',
                  'loath','reject','rejection','revolt','detest', 'refuse','loath','hell','shit',
                  'rage','lies','lier','lying','lie','lied',
                  'cheat','cheater','sick','sickness','nausea','dislike','deceive',
                  'disappointed','disappointing','disappoint','fake','faking','faked','victim',
                  'scam','burn','fooled','trick','tricked','delude','delusion','deluded','joke','bad','worst'}
    hate_count= sum(map(string.count,hate_words))

    love=love_count-hate_count
    return love

love_count = [0 for x in range(len(dataframe))] 
for i in range (len(dataframe)):
    love_count[i]=Love_score(dataframe['lyric'][i])
dataframe['love']=score_calculator(love_count)


# In[94]:


# kid_safe score
def Kid_score(string)-> str:
    KidSafe_words={'happy', 'happiness', 'joy', 'active', 'beautiful', 'smiley',
                 'inspiring', 'joyous', 'kissable', 'smile', 'smiling', 'amaze', 'amazing', 'dream', 'smart',
                 'blessed', 'bright', 'friendly', 'funny', 'cheerful', 'charming', 'gorgeous', 'good', 'playful', 'treasured',
                 'cute', 'huggable', 'proud', 'wonderful', 'prince', ' princess', 'wonder', 'friend', 'miracle', 'teddy bear',
                 'toys', 'family', 'friend', 'angel', 'star'}
    KidSafe_count=sum(map(string.count,KidSafe_words)) 
    
    NotKidSafe_words={'fuck', 'fucking', 'shit', 'bloody', 'screw', 'screwed','ass', 
                      'asshole', 'dammnit', 'damn', 'bitch','bitches', 'son of a bitch', 'frick',
                      'hell', 'dumb', 'butt', 'screw', 'crap', 'idiot', 'cocksucker', 'jerk',
                      'motherfucker', 'schmuck', 'jackass', 'bastard', 'dickhead',
                     'asshat', 'dumbo', 'moron', 'loser', 'nerd', 'fool', 'kill', 'murder',
                     'killing', 'killed', 'injure', 'injured', 'suicide', 'bloodying', 'blood',
                     'dick', 'cock', 'piss', 'fuck you', 'fuck off', 'frigger', 'nigga',
                     'sucker', 'nigger', 'prick', 'slut', 'whore', 'darn', 'pussy', 'fag',
                     'douche', 'bitchy','bitchass', 'bullshit'}
    NotKidSafe_count=sum(map(string.count,NotKidSafe_words))
    
    kid_safe=KidSafe_count-NotKidSafe_count
    return kid_safe

kid_safe_count = [0 for x in range(len(dataframe))] 
for i in range (len(dataframe)):
    kid_safe_count[i]=Kid_score(dataframe['lyric'][i])
dataframe['kid_safe']=score_calculator(kid_safe_count)


# In[97]:


# mood score
def Mood_score(string)-> str:
    sad_words={'sad','sadness','tear','tears','cry','cried','cries','crying',
            'blue','fear','fears','feared','weep', 'weeping','sob','sobbing','scream',
            'screaming','lonely','hurt','hurts','hurted','alone','drowning','drowned','broken',
            'break','down'}
    sad_count=sum(map(string.count,sad_words))

    
    happy_words={'happy', 'happiness', 'content', 'cheerful', 'cheery', 'merry', 'joyful', 
                    'gleeful', 'joke', 'joking', 'delighted', 'smiling', 'smile', 'glowing', 'satisfied', 'satisfy', 'satisfying'
                    'sunny', 'sun', 'blessing', 'blessed', 'good-humored', 'thrilled', 'blissful', 'lucky',  
                   'favorable', 'active', 'beautiful', 'smiley','smiling', 'amaze', 'amazing', 'bright',  'funny', 
                  'lucky', 'heaven', 'glad', 'pleased', 'alive', 'glad', 'excited'}
    happy_count=sum(map(string.count,happy_words))
    
    mood=happy_count-sad_count

    return mood

mood_count = [0 for x in range(len(dataframe))] 
for i in range (len(dataframe)):
    mood_count[i]=Mood_score(dataframe['lyric'][i])
dataframe['mood']=score_calculator(mood_count)


# In[99]:


# function used to calculate the score for love,kid_safe and mood
def length_and_complexity_score_calculator(list):
    percentile_25 = np.percentile(list, 25)
    percentile_50 = np.percentile(list, 50)
    percentile_75 = np.percentile(list, 75)
    
    score = np.array([])
    for i in range(len(list)):
        if list[i]<percentile_25:
            percentile = 0.25
        elif list[i]<percentile_50:
            percentile = 0.5
        elif list[i]<percentile_75:
            percentile = 0.75
        else:
            percentile = 1
        score=np.append(score,percentile)
    return score

# length score
length_count = [0 for x in range(len(dataframe))] 
for i in range (len(dataframe)):
    length_count[i]=len(dataframe['lyric'][i])
dataframe['length']=length_and_complexity_score_calculator(length_count)


# In[9]:


# function to calculate how many unique words in a string
def unique_word_count(string)-> str:
    counts = dict()
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return len(counts)

# complexity score
complexity_count = [0 for x in range(len(dataframe))] 
for i in range (len(dataframe)):
    complexity_count[i]=unique_word_count(dataframe['lyric'][i])
dataframe['complexity']=length_and_complexity_score_calculator(complexity_count)


# In[10]:


for i in range (len(dataframe)): 
    if str(detect(dataframe['lyric'][i])) != 'en':
        dataframe['love'][i]='N/A'
        dataframe['kid_safe'][i]='N/A'
        dataframe['mood'][i]='N/A'


# In[14]:

data2 = dataframe[['id','artist','title','kid_safe','love','mood','length','complexity']]
Export = data2.to_json('result.json',orient='records')
with open('result.json') as fp:
    data = json.load(fp)
with open('result.json', 'w') as fp:
    json.dump(
        obj=data,
        fp=fp,
        indent=True,  
        sort_keys=True,  
    )
with open('result.json') as fp:
    data = json.load(fp)
    
new_dict = {}
new_dict['characterization'] = data

new_dict
