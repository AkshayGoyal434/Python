a = int(input("Enter first number :" ))
b = int(input("Enter second number :" ))
c = int(input("Enter third number : "))

max = a
if(a < b):
    if(b > c):
        max = b
    else:
        max = c
        
else:
    max = c
print(max)


