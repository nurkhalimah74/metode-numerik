#mengecek satu bilangan bulat, satu-satu gitu lohh
a = int (input ("masukan bilangan bulat: "))
if a==0:
        print("angka yang diinput adalah angka Nol")
elif a>0:
    if a%2 == 0:
        print ("angka yang diinput adalah angka Positif dan Genap")
    else:
        print ("angka yang diinput adalah angka Positif dan Ganjil")
else:
    if a%2 == 0:
        print ("angka yang diinput adalah angka Negatif dan Genap")
    else:
        print ("angka yang diinput adalah angka Negatif dan Ganjil")


#mengecek beberapa bilangan bulat (1)
A=[]
n=int(input("masukan banyaknya bilangan: "))

for i in range(n):
    a=int(input("masukan bilangan bulat: "))
    A.append(a)

for j in range(n):
    if A[j]==0:
        print("angka %d adalah angka Nol" %A[j])
    elif A[j]>0:
        if A[j]%2 == 0:
            print("angka %d adalah angka Positif dan Genap" %A[j])
        else:
            print("angka %d adalah angka Positif dan Ganjil" %A[j])
    else:
        if A[j]%2 == 0:
            print("angka %d adalah angka Negatif dan Genap" %A[j])
        else:
            print("angka %d adalah angka Negatif dan Ganjil" %A[j])


#mengecek beberapa bilangan bulat (2) lebih simplenyaaaaa
A=[]
n=int(input("masukan banyaknya bilangan: "))

for i in range(n):
    a=int(input("masukan bilangan bulat: "))
    A.append(a)

for j in A:
    if j==0:
        print("angka %d adalah angka Nol" %j)
    elif j>0:
        if j%2 == 0:
            print("angka %d adalah angka Positif dan Genap" %j)
        else:
            print("angka %d adalah angka Positif dan Ganjil" %j)
    else:
        if j%2 == 0:
            print("angka %d adalah angka Negatif dan Genap" %j)
        else:
            print("angka %d adalah angka Negatif dan Ganjil" %j)


#mengecek beberapa bilangan bulat (3) input langsung keluar keterangannya
n=int(input("masukan banyaknya bilangan: "))

for i in range(n):
    a=int(input("masukan bilangan bulat: "))
    A.append(a)
    if a==0:
        print("angka yang diinput adalah angka Nol")
    elif a>0:
        if a%2 == 0:
            print("angka yang diinput adalah angka Positif dan Genap")
        else:
            print("angka yang diinput adalah angka Positif dan Ganjil")
    else:
        if a%2 == 0:
            print("angka yang diinput adalah angka Negatif dan Genap")
        else:
            print("angka yang diinput adalah angka Negatif dan Ganjil")


#hasil pengerjaanku           
angka=[]
n=int(input('berapa banyak angka yang ingin dimasukkan ke dalam array?'))
for i in range(0,n):
    x=int(input('masukkan angkanya:'))
    angka.append(x)
print('list angka:',angka)

posnap=[]
posjil=[]
negnap=[]
negjil=[]
nol=[]
for a in angka:
    if a==0:
        nol.append(a)
    elif a>0:
        if a%2==0:
         posnap.append(a)
        else:
         posjil.append(a)
    else:
        if a%2 == 0:
         negnap.append(a)
        else:
         negjil.append(a)

print('positif dan genap: ada sebanyak',len(posnap),',yaitu angka',posnap)
print('positif dan ganjil: ada sebanyak',len(posjil),',yaitu angka',posjil)
print('negatif dan genap: ada sebanyak',len(negnap),',yaitu angka',negnap)
print('negatif dan ganjil: ada sebanyak',len(negjil),',yaitu angka',negjil)
print('nol: ada sebanyak',len(nol),',yaitu angka',nol)