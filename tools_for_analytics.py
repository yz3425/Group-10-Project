
# coding: utf-8

# In[2]:

####making data frame part
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
###############getting file directory
print("enter path to the directory:")
a = input()
song_name = a.split('\\')[-1].split('~')[2]
##########   
mypath='C:/Lyrics'
file_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
list_file_name = [file.split('~') for file in file_name]
lyric_list = []
for file in file_name:
   path='C:/Lyrics/'+file
   f = open(path,'r',encoding="utf8")
   lyric_list.append(f.read())
index=np.array(list_file_name).T[0]
artist=np.array(list_file_name).T[1]
lyrics=np.array(list_file_name).T[2]
dataframe_ = pd.DataFrame({"Aritist":artist,
                        "Song":lyrics, 
                         "lyric":lyric_list})
Dataframe_
#####making data frame part

# turn columns Song and lyric into string
data = data.astype({"lyric": str, "Song": str})
# make lyric lowercase 
for i in range (len(data)):
   data['lyric'][i] = data['lyric'][i].lower()

love
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
for i in range (len(data)):    data['hate_count'][i]=sum(map(data['lyric'][i].count,(('hate','hatred','enemy','resent','disgust','disgusting','horror','horrible',
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
data['Love_score']   

data
   


Kid-safe
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
data['Kid_Safe_score']   

data

 






Mood

#Mood Analysis: the higher the positive count, the happier song it is 
data['Happy_count']=''
for i in range (len(data)):
   data['Happy_count'][i] =sum(map(data['lyric'][i].count,('happy', 'happiness', 'contented', 'content', 'cheerful', 'cheer', 'cheery', 'merry', 'joyful', 
                                                           'gleeful', 'joke', 'joking', 'smiling', 'delighted', 'smiling', 'smile', 'glowing', 'satisfied', 'satisfy', 'satisfying'
                                                           'sunny', 'sun', 'bless', 'blessing', 'blessed', 'good-humored', 'thrilled', 'blissful', 'lucky', 'blissful', 
                                                          'favorable', 'favorable', 'active', 'beautiful', 'smiley','smiling', 'amaze', 'amazing', 'bright',  'funny', 
                                                          'cheerful', 'lucky', 'heaven', 'glad', 'pleased', 'alive', 'glad', 'excited')))   
   
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
data['Mood_score']   

data    





# sadness related
data['sad_count']=''
for i in range (len(data)):    
   data['sad_count'][i]=sum(map(data['lyric'][i].count,('sad','sadness','tear','tears','cry','cried','cries','crying',
                                                         'blue','fear','fears','feared','weep', 'weeping','sob','sobbing','scream',
                                                         'screaming','lonely','hurt','hurts','hurted','alone','drowning','drowned','broken',
                                                       'break','down')
   





####length part
data['length']=''
for i in range(len(data)):
   data['length'][i] = len(data['lyric'][i])
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
data['length_score']
####length part

########complexity part
data['word_count']=''
for i in range(len(data)):
   counts = dict()
   words = data['lyric'][i].split()
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



# love dimension

data['Love_dimension']=''
for i in range (len(data)):
   data['Love_dimension'][i]=data['love_count'][i]-data['hate_count'][i]

# kidsafe dimension
data['kid-dimension']=''
for i in range (len(data)):
   data['kid-dimension'][i]=data['KidSafe_count'][i]-data['NotKidSafe_count'][i]




# mood dimension
data['mood-dimension']=''
for i in range (len(data)):
   data['mood-dimension'][i]=data['Happy_count'][i]-data['sad_count'][i]



#####extractingdata of the song name
print(song_name)
print(data['Song'])
data_final = data[(data['Song']==song_name)]                                  
data_final                                 
####extractring data of the song name

