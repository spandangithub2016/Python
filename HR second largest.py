numbers= list()
num1 = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num1)):
    n = raw_input("num :")
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
