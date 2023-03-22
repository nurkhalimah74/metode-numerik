#----------------NO.2--------------------

#---------METODE ITERASI JACOBI----------
import numpy as np
ITERATION_LIMIT=20
#inisialisasi matriks
N = np.array([[10.,-1.,2.,0.],\
            [-1.,11.,-1.,3.],\
            [2.,-1.,10.,-1.],\
            [0.,3.,-1.,8]])
#insialisasi vektor 
M = np.array([6.,25.,-11.,15])
#print sistem
print("Sistem:")
for i in range(N.shape[0]):
    row = ["{}*x{}" .format(N[i, j], j + 1) for j in range(N.shape[1])]
    print (" + ".join(row), "=", M[i])
print()

Y = np.zeros_like(M)
for it_count in range(ITERATION_LIMIT):
    print("Current solution:", Y)
    Y_baru = np.zeros_like(Y)
    
    for i in range(N.shape[0]):
        s1 = np.dot(N[i, :i], Y[:i])
        s2 = np.dot(N[i, i+1:], Y[i+1:])
        Y_baru[i]=(M[i] - s1 - s2) / N[i, i]
        
    if np.allclose(Y, Y_baru, atol=1e-10, rtol=0.):
        break
    Y = Y_baru
    
print("Solution:")
print(Y)
error = np.dot(N, Y) - M
print("Error:")
print(error)

#---------METODE ITERASI GAUSS SEIDEL----------
from numpy import array,zeros
#inisialisasi matriks N
N = array([[10.,-1.,2.,0.],\
            [-1.,11.,-1.,3.],\
            [2.,-1.,10.,-1.],\
            [0.,3.,-1.,8]])
print(N)
#inisialisasi vektor M
M = array([[6.],\
         [25],\
         [-11],\
         [15]])
print(M)
n=len(N)
iterasi=100
toleransi=0.0000001
xlama=zeros((n,1))
xbaru=zeros((n,1))
c=zeros((n,1))
Z=zeros((n,n))
#menghitung matriks Z dan c
for j in range(0,n-1):
    for i in range(0,n):
        if i==j:
            i=i+1
        Z[j][i]=-1.*N[j][i]/N[j][j]
    c[j][0]=M[j][0]/N[j][j]
j=n-1
for i in range(0,n-1):
    Z[j][i]=-1*N[j][i]/N[j][j]
c[j][0]=M[j][0]/N[j][j]
#metode Gauss Seidel
for m in range(i,iterasi):
    S=0
    for i in range(0,n):
        S=S+Z[0][i]*xlama[i][0]
    xbaru[0][0]=S+c[0][0]
    for k in range(0,n):
        P=0
        for j in range(0,k):
            P=P+Z[k][j]*xbaru[j][0]
        S=0
        for i in range(k,n):
            S=S+Z[k][i]*xlama[i][0]
        xbaru[k][0]=P+S+c[k][0]
    normselisih=((xbaru-xlama)/xbaru)
    if all(normselisih<toleransi):
        break
    xlama=xbaru.copy() 
#lencetak hasil perhitungan
print ('iterasi ke',m)
print (xbaru)



#----------------NO.4--------------------

#---------(A)GREGORY MAJU----------
#Menghitung nilai d
def s_cal(s,n):
    
    temp = s;
    for i in range(1, n):
        temp = temp*(s-i);
    return temp;

#Menghitung Nilai Faktorial untuk suatu n
def fact(n):
    f=1;
    for i in range (2, n + 1):
        f*=i;
    return f;

#Nilai n dan x yang diberikan
n = 5;
x = [ 0.1, 0.6, 1.1, 1.6, 2.1 ];

#Z[][] tabel selisih maju
Z = [[0 for a in range(n)] 
        for b in range(n)]; 
Z[0][0] = 1.1052; 
Z[1][0] = 1.8221; 
Z[2][0] = 3.0042; 
Z[3][0] = 4.9530; 
Z[4][0] = 8.1662;

#Menghitung selisih maju
for a in range(1, n): 
    for b in range(n - a): 
        Z[b][a] = Z[b + 1][a - 1] - Z[b][a - 1]; 

#Menampilkan Tabel Selisih Maju
for a in range(n): 
    print(x[a], end = "\t"); 
    for b in range(n - a): 
        print(Z[a][b], end = "\t"); 
    print("  "); 

#Nilai x yang di interpolasikan
nilai = 2.00;

#Inisialisasi u dan jumlahnya
jum = Z[0][0];
h = (x[1]-x[0]);
s = (nilai - x[0])/h;
for i in range(1,n):
    jum = jum + (s_cal(s, i)*Z[0][i])/fact(i);

print("Nilai f(x) untuk x =", nilai,  
      "adalah", round(jum, 6)); 
      
           
#---------(A)GREGORY MUNDUR----------

#Menghitung nilai d
def d_cal(d,a):
    
    temp = d;
    for i in range(1, a):
        temp = temp*(d+i);
    return temp;

#Menghitung Nilai Faktorial untuk suatu N
def fact(N):
    f = 1;
    for i in range (2, N+1):
        f*=i;
    return f;

#Nilai N dan x yang diberikan
N = 5;
x = [ 0.1, 0.6, 1.1, 1.6, 2.1];

#Z[][] tabel selisih mundur
Z = [[0 for i in range(N)] 
        for j in range(N)]; 
Z[0][0] = 1.1052; 
Z[1][0] = 1.8221; 
Z[2][0] = 3.0042; 
Z[3][0] = 4.9530; 
Z[4][0] = 8.1662;

#Menghitung selisih mundur
for i in range(1, N): 
    for j in range(N):  
        Z[j][i] = Z[j][i - 1] - Z[j - 1][i - 1]; 

#Menampilkan Tabel Selisih Mundur
for i in range(N): 
    print(x[i], end = "\t"); 
    for j in range(i+1): 
        print(Z[i][j], end = "\t"); 
    print("  "); 

#Nilai x yang di interpolasikan
nilai = 2.00;

#Inisialisasi d dan jumlahnya
jum = Z[N - 1][0];
d = (nilai - x[N - 1])/(x[1]- x[0]);
for i in range(1, N):
    jum = jum + (d_cal(d, i)*Z[N-1][i])/fact(i);

print("Nilai f(x) untuk x =", nilai,  
      "adalah", round(jum, 6)); 
      
      
      
      
      

#----------------NO.7--------------------

#definisi fungsi
def fungsi1 (x):
    y=(2*x/3)+58/3
    return y
print ("f(x)=(2*x/3)+58/3")
N=int(input("Masukkan nilai x0 : "))
M=int(input("Masukkan nilai x : "))
for iterasi in range(1,5,1):
    n=4
    h=(b-a)/n
print("h = ",h)
    
#simpson
jumlahganjil=0
jumlahgenap=0
xi=a+h
xj=a+2*h
for isimpson in range (1,n,2):
    jumlahganjil+= fungsi1(xi)
    xi+=(2*h)
for jsimpson in range (2,n-1,2):
    jumlahgenap+= fungsi1(xj)
    xj+=(2*h)
Is=(h/3)*((fungsi1(a)+(4*jumlahganjil)+(2*jumlahgenap)+fungsi1(b)))
print (iterasi,"\t\t",n,"\t\t",Is)

def fungsi2 (x):
    y2=(13*x/3)-19/3
    return y2

print ("f(x)=(13*x/3)-19/3")
a=int(input("Masukkan nilai x0 : "))
b=int(input("Masukkan nilai x : "))

for iterasi in range(1,5,1):
    n=4
    h=(b-a)/n
print("h = ",h)
    
#simpson
jumlahganjil=0
jumlahgenap=0
xi=a+h
xj=a+2*h
for isimpson in range (1,n,2):
    jumlahganjil+= fungsi2(xi)
    xi+=(2*h)
for jsimpson in range (2,n-1,2):
    jumlahgenap+= fungsi2(xj)
    xj+=(2*h)
Is2=(h/3)*((fungsi2(a)+(4*jumlahganjil)+(2*jumlahgenap)+fungsi2(b)))
print (iterasi,"\t\t",n,"\t\t",Is2)

def fungsi3 (x):
    y3=(9*x/5)+19
    return y3
print ("f(x)=(9*x/5)+19")

a=int(input("Masukkan nilai x0 : "))
b=int(input("Masukkan nilai x : "))

for iterasi in range(1,5,1):
    n=4
    h=(b-a)/n
print("h = ",h)

#trapesium
xi=a
y=0
for i in range (1,n):
    xi=xi+h
    y+= fungsi3(xi)
It=(h)*((fungsi3(a)+(2*y)+fungsi3(b))/2)
print (iterasi,"\t\t",n,"\t\t",It)
jarak = Is+Is2+It
print("Maka estimasi jarak terbaik adalah", jarak,"m.")














