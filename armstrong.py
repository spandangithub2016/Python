# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
num =input("Enter a number: ")

# initialise sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   #print(digit)
   sum += digit ** 3
   #print(sum)
   temp //=10
   #print(temp)
    
# display the result
if num == sum:
   print num,"is an Armstrong number"
else:
   print num,"is not an Armstrong number"
