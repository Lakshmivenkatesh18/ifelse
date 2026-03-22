a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
operation=input("Choose any one operation,add/sub/mul/div :")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("Invalid operation")