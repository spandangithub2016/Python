import codecs

#Reading dictionary
infile=codecs.open("dict.txt","r", encoding="UTF-8")
inp=input("enter your word in english only:")
flag=False

for data in infile.readlines():
    #Encoding
    one=data.split('\ufeff')
    #print("1: ",one)
    one="".join(one)
    #print("2: ",one)
    one=one.split(':')
    #print("3: ",one)
    
    #checking dictionary for match
    if(inp==one[0]):
        flag=True
        for mean in one:
            if(mean==one[0]):
                continue
            else:
                print(mean)
    else:
        continue
    
if(flag==False):
    print("Does Not Exists In Dictionary..Update soon !")
