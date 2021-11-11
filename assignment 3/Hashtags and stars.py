# Hashtags and stars
m=int(input("addad aval "))
n=int(input('addad dovom '))
def z(m,n):
    for x in range(1,m+1):
        for y in range(1,n+1):
            if (x+y)%2==0:
                print("*",end=" ")
            else:
                print("#",end=" ")
        print("")
print (z(m,n))