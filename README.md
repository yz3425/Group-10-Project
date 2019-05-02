# Group 10
> Yuchen Chen yc3540 <br /> 
> Brandon Park bjp2152 <br />
> Yizhou Zhang yz3425 <br />
# General Information
This project is created in order to analyze the lyrics for each given song. When we input the lyrics of the song, we could get back the song's id, artist, title, and the scores corresponding to the dimensions of kid-safe, love, mood, length and complexity. Additionally, the output of this project is a JSON object that has the above information for each individual song. 
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
