"""
# http://www.webopedia.com/quick_ref/textmessageabbreviations.asp

Python program for expanding shorten word used in SMS.
Input: 1) A text file have shorten word and their expansion.
       2) A text file/ or text having mixed text and shorten words.

Output: A text file in which all the shorten words are expended.

Example: Input: After reading your jokes, I was LOL.
         Ouput: After reading your jokes, I was laughing out loud.

"""

#Import required modules
import re

#Define a function to exapand the shorten word
def meaning_search(word):
    shakes = open("output.txt", "r")
    for line in shakes:
        if re.match(word,line):
            return shakes.next()
    shakes.close()
    

def join_words(split_list):
    line=' '.join(word for word in split_list)
    line= line+".\n"
    print(line)
    #save=open("chat2.txt","a")
    #save.write(line)

def sentence_split(sentence):
    sentence = sentence.rstrip()
    sentence=sentence.replace(".",'')
    sp=[]
    sp=sentence.split(" ")
    for i in sp:
        if re.match("^[A-Z0-9?.<@%;^/&-]*$",i) :
            ind=sp.index(i)
            sp[ind]=meaning_search(i).replace("\n",'')
            join_words(sp)
            break

#Take user input (file or text)
def read():
    f=open("chat.txt","r")
    for line in f:
        print(line)
        sentence_split(line)
        
read()
