# Enter your code here. Read input from STDIN. Print output to STDOUT
#import sys

numbers= list()
num1 = raw_input()
for i in range(int(num1)):
    #inp = map(int,sys.stdin.readline().split()) 
   n = raw_input()
   numbers.append(n) 
if (numbers[0]>numbers[1]):
    m, m2 = numbers[0], numbers[1]
else:
    m, m2 = numbers[1], numbers[0]
for x in numbers[2:]:
    if x>m2:
        if x>m:
            m2, m = m, x
        else:
            m2 = x
print(m2)
