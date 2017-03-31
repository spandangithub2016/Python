def findpos(find_Word,new):
    count,new_String=0,[]
    for words in range(0,len(new)):
        if(new[words]==find_Word):
            new_String.append(words)
            count=1
        else:
            continue

    if(count):
        print(",And "'"',find_Word,'"'" is found at position:",new_String)
    else:
        print('\nDoesn''t Found:',False) 
string="we dont need no education we dont need no thought control no we dont"
new=string.split(" ")
print(new)
find_Word=str(input("enter a word you want to find: "))
print("You have given:",find_Word,end=" ")
findpos(find_Word,new)


        
