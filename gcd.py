# greatest common division without function
c = int(input("Enter the smallest number first : "))
d = int(input("Enter the largest number now : "))
v = d%c
if(v==0):
    print(c)
else:
    print("invalid")    


# by using function
    import math
    g = math.gcd(c,d)
    print(g)

# or we can print by following     
    # print(f[g])
    
