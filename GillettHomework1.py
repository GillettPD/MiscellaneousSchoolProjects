#Homework1
import re

#read from file to string
f = open('Tongue_Twister_Corpus.txt')
raw = f.read()

#split string into list
raw_list = re.split(r'\W+', raw)

#sort list
sorted_list = sorted(set(raw_list))

#lowercase                     
words = [w.lower() for w in sorted_list]

#count & store in dictionary

word_dict = {
    1 : 1
}
   

for i in raw_list:
    j = raw_list.count(i)
    word_dict[i] = j

#print
for x in word_dict:
    print(x)
    print(word_dict[x])



#close file
f.close()
