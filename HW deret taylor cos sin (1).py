import math
def cos(x,n):
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
        
    return cos_approx

def sin(x,n):
    sin_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i+1)
        denom = math.factorial(2*i+1)
        sin_approx += ( coef ) * ( (num)/(denom) )
        
    return sin_approx

print('Deret Taylor untuk sin(0,2):')
print(f'Untuk 2 iterasi didapatkan nilai sebesar {sin(0.2, 2)}')
print(f'Untuk 5 iterasi didapatkan nilai sebesar {sin(0.2, 5)}')
print(f'Untuk 10 iterasi didapatkan nilai sebesar {sin(0.2, 10)}')
print('Dereet Tylor untuk cos(0,2):')
print(f'Untuk 2 iterasi didapatkan nilai sebesar {cos(0.2, 2)}')
print(f'Untuk 5 iterasi didapatkan nilai sebesar {cos(0.2, 5)}')
print(f'Untuk 10 iterasi didapatkan nilai sebesar {cos(0.2, 10)}')