"""
Assignemt-2: Calculate simple and compound interest.
Name: SPANDAN MAJUMDER
Email: spandanmajumderjblss@gmail.com
"""

# PYTHON VERSON- 3.6.0 

# Define Simple interest function
def simple_int(p,r,t):
	simple_interest= (p*r*t)/100
	return (simple_interest)

# Define Compound interestfunction
def compound_int(p,r,t):
	compound_interest = (p* (pow((1 + r / 100), t) - 1))
	return(compound_interest)

# Define function for getting user input
def getPrinciple():
	principle = eval(input("Enter principle : "))
	return principle
def getRate():
	rate = eval(input("Enter Interest Rate : "))
	return rate
def getTime():
	time = eval(input("Enter Duration time : "))
	return time

# Call user input
p = getPrinciple()
r = getRate()
t= getTime()


# Call both function and print the output
print("Simple Interest is: "+str(simple_int(p,r,t)))
print("compound Interest is: "+str(compound_int(p,r,t)))
