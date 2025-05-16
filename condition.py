           #Conditional Statement

score = 75

min_citeria = 75

if score == min_citeria:
 print("Anda Berhasil Naik Level!")

elif score < min_citeria:
 print("Anda belum berhasil naik level")

else:
 print("Nilai anda tidak ditemukan")

            #PRACTICE

#memberikan nilai berdasarkan skor
 
nilai = input("masukkan skor =")

nilai = int(nilai) #dijadiin nilai karena data stringnya mau dijadiin data angka

if nilai >= 85:
 print("Nilai A")

elif nilai >= 75:
 print ("Nilai B")

else:
 print ("Nilai C")

             #LOOP
number = 10 

while number <= 10:
    print("I like phyton")
    number
 numbers = range(10)

for n in numbers:
   print ("I like phyton ", n)

#for
for i in range(1,6):
  print(i)
  
 #while

jumlah= input("input count = ")
jumlah = int(jumlah)

count = 1
while count <= jumlah:
   print("halo")
   count += 1