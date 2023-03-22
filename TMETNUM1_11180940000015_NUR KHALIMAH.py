 #---1.Tulis program python utk dpt menentukan bil.genap atau ganjil dlm interval 1<=angka<=200 disetiap iterasi---
for x in range (1,201):
    if x%2==0:
        print (x,"adalah genap")
    else:
        print (x,"adalah ganjil")
        
        
#---2.Tulis program python utk dpt menentukan apakah sebuah angka yg diinput oleh user adlh bil.prima atau bukan---
x = int (input ('masukkan angka sesuka anda:'))
if x>=2:
    prima=True
    for i in range (2,x):
        if x%i==0:
            prima=False
    if prima:
        print (x,'adalah bilangan prima')
    else:
        print (x,'adalah bukan bilangan prima')
        
    
#---3.Tulis program python utk dpt memisahkan kumpulan angka yg diinput oleh user menjadi 3 buah kategori, yaitu +, - dan 0. Kemudian hitung masing-masing banyaknya anggota tiap kategori--- 
angka = []
n = int (input ('berapa banyak angka yang ingin dimasukkan ke dalam array?'))
for i in range (0,n):
    x = int (input ('masukkan angkanya:'))
    angka.append(x)
print ('list angka:',angka)

positif = []
negatif = []
nol = []
for a in angka:
    if a==0:
        nol.append(a)
    elif a>0:
        positif.append(a)
    else:
        negatif.append(a)

print ('positif: ada sebanyak', len(positif), ',yaitu angka', positif)
print ('negatif: ada sebanyak', len(negatif), ',yaitu angka', negatif)
print ('nol: ada sebanyak', len(nol), ',yaitu angka', nol)