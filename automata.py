import re
print("E={a,b,c}")
while True:
    print("Press 1. To check Word or String ")
    print("Press 2. To check Sentence ")
    print("Press 3. To Exit ")
    choice=eval(input("Enter Your Choice: "))
    if(choice==1):
        print("Rule 1:  Set of strings should starts with 'a' of length 2")
        print("Rule 2:  Set of strings should starts with 'b' of length 2")
        print("Rule 3:  Set of strings should starts with 'a' and ends with 'a'")
        print("Rule 4:  Set of strings should starts with 'b' and ends with 'b'")
        print("Rule 5:  Set of strings should starts with 'a' and ends with 'b'")
        print("Rule 6:  Set of strings should starts with 'b' and ends with 'a'")
        print("Rule 7:  Set of strings should contain a's only")
        print("Rule 8:  Set of strings should contain b's only")
        print("Rule 9:  Set of strings should starts with 'a' and followed by one 'b'")
        print("Rule 10: Set of string should contain substring 'abc'")
        print("Rule 11: Set of string should have exactly one 'c'")
        print("Press 0 to Exit")

        while True:
            Rule=eval(input("Enter any one Rule Number: "))
            if(Rule==1):
                regex=re.compile('(^a)(a|b|c)$')
                print("E={a,b,c}")
                string=input("enter any string should starts with 'a' of length 2: ")
                if(len(string)==2) and re.match(regex,string) :
                    print("String is Matched")   
                else:
                    print("String is not Matched")
            elif(Rule==2):
                regex=re.compile('(^b)(a|b|c)$')
                print("E={a,b,c}")
                string=input("enter any string should starts with 'b' of length 2: ")
                if(len(string)==2) and re.match(regex,string):
                    print("String is Matched")            
                else:
                    print("String is not Matched")
            elif(Rule==3):
                regex=re.compile('(a)$|((^a)+(a|b|c)*(a)+$)')
                print("E={a,b,c}")
                string=input("enter any string should starts with 'a' and ends with 'a': ")
                if re.match(regex,string):
                    print("String is Matched")    
                else:
                    print("String is not Matched")
            elif(Rule==4):
                regex=re.compile('(b)$|((^b)+(a|b|c)*(b)+$)')
                string=input("enter any string should starts with 'b' and ends with 'b': ")
                if(re.match(regex,string)):
                    print("String is Matched")        
                else:
                    print("String is not Matched")
            elif(Rule==5):
                regex=re.compile('(^a)+(a|b|c)*(b)+$')
                string=input("enter any strings should starts with 'a' and ends with 'b': ")
                if(re.match(regex,string)):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            elif(Rule==6):
                regex=re.compile('(^b)+(a|b|c)*(a)+$')
                string=input("enter any strings should starts with 'b' and ends with 'a': ")
                if(re.match(regex,string)):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            elif(Rule==7):
                string=input("enter any string should contain a's only: ")
                regex=re.compile('(a+)$')
                if re.match(regex,string):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            elif(Rule==8):
                string=input("enter any string should contain b's only: ")
                regex=re.compile('(b+)$')
                if re.match(regex,string):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            elif(Rule==9):
                string=input("enter any strings should starts with 'a' and followed by one 'b': ")
                regex=re.compile('(ab)+$')
                if re.match(regex,string):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            elif(Rule==10):
                string=input("enter any string should contain substring 'abc': ")
                regex=re.compile('(a|b|c)*(abc)(a|b|c)*$')
                if re.match(regex,string):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            elif(Rule==11):
                string=input("enter any string should have exactly one 'c':  ")
                regex=re.compile('(a|b)*c(a|b)*$')
                if re.match(regex,string):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            elif(Rule==12):
                string=input("enter any string even no. of 'b' and odd number of 'c':  ")
                regex=re.compile('(((bb)*c(cc)*)|(c(cc)*(bb)*))$')
                if re.match(regex,string):
                    print("String is Matched")
                else:
                    print("String is not Matched")
            else:
                print("Bye.See you Soon...!")
                break
    
    elif(choice==2):
        print("Rule 1: A sentence sholud start with Rule 1 and followed by single space and then Rule 2: ")
        print("Rule 2: A sentence sholud start with Rule 3 and ends with Rule 4 by seperated by single space then Rule5/Rule6:  ")
        print("Rule 3: A sentence should have \"Rule7 <Rule8> Rule7:\" is recursively repeated")
        print("Press 0 to Exit")
        while True:
            choice=eval(input("Enter any one Rule Number: "))
            if(choice==1):
                print("Syntax:\"Rule1 \s Rule2")
                print("Rule 1:  Set of strings should starts with 'a' of length 2")
                print("Rule 2:  Set of strings should starts with 'b' of length 2")
                regex=re.compile('(^a)(a|b|c)\s(b)(a|b|c)$')
                sentence=input("Enter a sentence: ")
                if(re.match(regex,sentence)):
                    print("Correct Sentence")
                else:
                    print("Incorrect Sentence")
            elif(choice==2):
                print("Syntax: Rule3 Rule5/Rule6 Rule4 ")
                sentence=input("Enter a sentence: ")
                regex=re.compile('((^a)|(^a)+(a|b|c)*(a)+)\s(((a)+(a|b|c)*(b)+)|((b)+(a|b|c)*(a)+))\s((b)$|((b)+(a|b|c)*(b)+$))')
                if(re.match(regex,sentence)):
                    print("Correct Sentence")
                else:
                    print("Incorrect Sentence")
            elif(choice==3):
                print("Syntax: \"Rule7 <Rule8> Rule7\" is recursively repeated")
                sentence=input("Enter a sentence: ")
                regex=re.compile('(a+)(<|\s<|\s<\s)(\s|\s(b|c)+|(c|b)+)(\s|\s>|>)(\s|\sa+|a)(:)(\n)(\t)(((a+)(<|\s<|\s<\s)(\s|\s(b|c)+|(b|c)+)(\s|\s>|>)(\s|\sa+|a)(:)(\n)(\t+))+|(a+)(;))+$')
                if(re.match(regex,sentence)):
                    print("Correct Sentence")
                else:
                    print("Incorrect Sentence")
            else:
                print("Bye.See you Soon...!")
                break
            
    elif(choice==3):
        print("Bye.See you Soon...!")
        break
            
