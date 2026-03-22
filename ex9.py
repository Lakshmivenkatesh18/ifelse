a=int(input("Enter the mark of Tamil :"))
b=int(input("Enter the mark of English :"))
c=int(input("Enter the mark of Science :"))
d=int(input("Enter the mark of Social :"))
e=int(input("Enter the mark of Maths :"))
f=a+b+c+d+e
avg=f/5
if(avg<35):
    print("Additional class is required")
else:
    print("You are good to go")