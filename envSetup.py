def display(name,course,regNo):
    print()
    print("Person Name: "+name)
    print("Course Name: "+course)
    print("Registration Number: "+regNo)
    
def envSetup():
    name=input("Enter Your Name: ")
    course=input("Enter Course Name: ")
    regNo=input("Enter Registration Number: ")
    display(name,course,regNo)
envSetup()
