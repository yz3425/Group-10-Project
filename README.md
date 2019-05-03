# Group 10
> Yuchen Chen yc3540 <br /> 
> Brandon Park bjp2152 <br />
> Yizhou Zhang yz3425 <br />
# General Information
This project is created in order to analyze the lyrics for each given song. When we input the lyrics of the song, we could get back the song's id, artist, title, and the scores corresponding to the dimensions of kid-safe, love, mood, length and complexity. Additionally, the output of this project is a JSON object that has the above information for each individual song. 
# Tools we used in this project:
* **pandas:** <br />
```
# import pandas 
import pandas as pd
```
**Description**: Pandas is the package included in Anaconda, which is used for data analysis and data structures. <br />
**Usage**: We used pandas to create a dataframe of the lyrics file to make it more clearly to view and manage. <br />
**Behavior**: The dataframe generated contains columns for id, artist, title, lyric, love, kid_safe, mood, length and complexity. For id, love, kid_safe, mood, length and complexity, they are all numbers. For artist, title, lyric, they are all strings. <br />
For more information on the pandas package: [http://pandas.pydata.org](http://pandas.pydata.org)

* **numpy:** <br />
```
# import numpy 
import numpy as np
```
**Description**: Numpy is the package in Anaconda that is used for creating the large arrays. Operations like mathmatical functions, logical statements, statistical opertaions and other manipulations could be done on arrays using Numpy.    
**Usage**: We used numpy in accordance with pandas to build a dataframe. Numpy allows us to put all the index, artist, and the lyrics of each given song into three different arrays. We then assign each array to the column in the dataframe of id, artist, and title. <br />
**Behavior**: The values in the array for index are all numbers, where the values in the array for artist are all strings, and the values in the array for lyrics are strings as well.  <br />
For more information on the numpy package: [https://docs.scipy.org/doc/](https://docs.scipy.org/doc/)

* **json:** <br />
```
# import json 
import json
```
**Description**: Json is used for changing the data format. <br />
**Usage**: We used json at the end of our code to interchange our generated output into a json object. <br />
**Behavior**：The json object is the final output of our project, and when we open the json object, it should have the form of a dictionary. Each song generates a dictionary, and the key is each characterization, like id, artist, title, and so on.    <br />
For more information on the json: [https://docs.python.org/3/library/json.html#module-json](https://docs.python.org/3/library/json.html#module-json)


# Key Characterization:
* **'id':** <br />
The key 'id' in the characterization is the identification number from the lyric file. It is directly provided as the begining of the three numbers given from the name of each song. 
* **'artist':** <br />
The key 'artist' is directly provided through the name of the given lyric file. 
* **'title':** <br />
The key 'title' is also given from each individual lyric file name. 
* **'kid_safe':** <br />
The key 'kid_safe' provides information on whether the song is friendly or not for kids based on the lyrics. That is, the function is generated to see if the lyric for a song has a greater number on bad, bloody, and the curse words than the good and adorable words. <br />
Moreover, each score ranges from 0 to 1. The score is created based on the distribution of all given songs in percentile. A low score indicates the given song has a larger amount of bad words than kid-friendly words, or in other words, it is not a kid-friendly song. A high score reveals the given song has a larger amount of kid-friendly words than bad words, or, it is a kid-friendly song. 
* **'love':** <br />
The key 'love' is an indicator on whether the song is a love song or not. A function is created to count if the number of the love words is greater than the number of hate words.  <br />
Each score ranges from 0 to 1, a low score indicates the song given is more to a hate song rather than a love song, where a high score indicates the song given is more to a love song comparing to a hate song. Also, the score is generated based on the percentile of love scores of all the songs. 
* **'mood':** <br />
The key 'mood' reveals the mood of a given song based on its lyrics. The score also ranges from 0 to 1. If the number of sad words exceeds the number of happy words, a low score would be created. On the contrary, if the number of happy words exceeds the number of sad words, a high score would be generated. Each individual score is also based on its percentile. 
* **'length':** <br />
The key 'length' indicates whether it is a long song or a short song. A low score indicates it is a short song, and vice versa. It is also based on percentile. 
* **'complexity':** <br />
The key 'Complexity' shows if the song is a easy song. A function is created to count the repeating words in lyrics. A low score for complexity indicates it is a easy song, and vice versa. Each individual score for complexity is also based on the percentile. 
