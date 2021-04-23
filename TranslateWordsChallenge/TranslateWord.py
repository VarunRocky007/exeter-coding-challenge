import pandas as pd
import csv
dataset=pd.read_csv('french_dictionary.csv')
english_words=dataset.iloc[:,0].values.tolist()
french_words=dataset.iloc[:,1].values.tolist()

words=[]
words_converted=[]
to_be_converted=[]
file=open("find_words.txt","r")
for word in file:
    words.append(word[:-1])
for i in words:
    if i in english_words:
        words_converted.append(french_words[english_words.index(i)])
    else:
        words_converted.append(i)

words_freq=[0]*len(words)
file_convert=open("t8.shakespeare.txt","r")
for sentence in file_convert:
    for word in sentence.split():
        to_be_converted.append(word)








for i in range(0,len(to_be_converted)):
    if  to_be_converted[i] in english_words:
        words_freq[english_words.index(to_be_converted[i])] += 1
        to_be_converted[i] =french_words[english_words.index(to_be_converted[i].lower())]



    else:
        for j in range(0,len(english_words)):
            if to_be_converted[i].lower().find(english_words[j])>0:
                str=to_be_converted[i]
                if len(str)>len(english_words[j]):
                    to_be_converted[i]=str[:to_be_converted[i].find(english_words[j])]+french_words[j]+str[len(english_words[j])-1:]
                    words_freq[j]+=1



file_converted=open("t8.shakespeare.translated.txt","w")
for i in to_be_converted:
    file_converted.write(i+" ")
with open('frequency.csv','w') as freq_file:
    writer=csv.writer(freq_file)
    writer.writerow(["Englisg word","French word","Frequency"])
    for i in range(0,len(words)):
        writer.writerow([words[i],words_converted[i],words_freq[i]])




