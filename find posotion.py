def findpos(list1,x):
    pos=[]
    (found,i)=('false',0)
    while(i<len(list1)):
        if list1[i]==x:
            pos.append(i)    
        i=i+1
    return pos

list1=input("enter a list: ")
x=input("enter a number to search: ")
if(findpos(list1,x)):
    print "given value found at position ",findpos(list1,x)
else:
    print "not found"

