import codecs
infile=codecs.open("text.txt", "r", encoding="UTF-8")
inp=input("enter your word in english only:")
for data in infile.readlines():
    one=data.split(':')

    if(inp==one[1]):
        
        for mean in one:
            
            if(mean==one[1]):
                continue
            else:
                print(mean)
        break
    else:
        print("Not matched,,Try Another")
