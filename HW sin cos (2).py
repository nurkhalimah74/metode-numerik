import math
math.pi
#---------------sin----------------------#
pi = 3.141592653589793
def factorial (n):
    if n<2 :
        return 1
    else :
        return n*factorial (n-1)
def sin (y,n) :
    a = 0
    x = pi*y/180 
    for i in range (n) :
        a = a +((-1)**i*(x**(2*i+1)))/factorial ((2*i)+1)
    return a

print (sin (50,10))
 
#-----------------cos--------------------#
pi = 3.141592653589793
def factorial (n):
    if n<2 :
        return 1
    else :
        return n*factorial (n-1)
def cos (y,n) :
    a = 0
    x = pi*y/180 
    for i in range (n) :
        a = a +((-1)**i*(x**(2*i+1)))/factorial ((2*i)+1)
    return a

print (cos (50,10))

#------------percobaan if n<0-------------------------#
pi = 3.141592653589793
def factorial (n):
    if n < 0:
        print('Ga bisa Bro!')
    elif n<2 :
        return 1
    else:
        return n*factorial (n-1)