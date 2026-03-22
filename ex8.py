salary=int(input("Enter the salary:"))
age=int(input("Enter the age:"))
if(salary>=20000 or age<=25):
    loan=int(input("Enter required loan amount:"))
    if(loan<=50000):
        print("You are eligible for loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("you are not eligible")