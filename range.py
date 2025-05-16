range(10)
print(list(range(10)))

range(1,50)
print(list(range(1,5)))

range(0,100,5)
print(list(range(0,10,5)))

#index
numbers = range(1,21)

print(numbers[9])
print(numbers[19])

#slicing
numbers = list(range(1,40,4))
print(numbers[:6])

print(numbers[1:6])

#DATA STRUCTURE

#lIST

#membuat list
names = ["Raka","Raissa","Reynard"]                 #Biasa
print(names[1])  #mengakses item

names =list(("Raka","Raissa","reynard"))            #List constructor
print(names[2])  #mengakses item

name = "Raka"
letters = list(name)                                #itarable object
print(list(name))                                   #------"------"------

#dapat dimanipulasi
names = ["Raka","Raissa","Reynard"]
names.append("bunda & Ayah")   # menambahkan item

names[0] = "Rakageva"          #mengubah item

names.remove("bunda & Ayah")        #menghapus item
print(names)

#TUPLE

#membuat tuple
names = ("Bena","Beno","Beni")          #biasa
print(names[2])
names = tuple(("Bena","Beno","Beni"))   #tuple constructor
print(names[1])
name  = "Bena"                          #iterable object
letters = tuple(name)                   #-------"-----"------
print(tuple(name))

#tidak dapat dimanipulasi(konversi dulu dlm bentuk list)
names = ("Bena","Beno","Beni")
names_list = list(names)               #konversi dlm list
      
names_list.append ("Benu")             #lakuakan manipulasi    

names_list[0] = ("benanana")           #lakuakan manipulasi   

names_list.remove ("benanana")         #lakuakan manipulasi   

names= tuple(names_list)                #konversi dlm tuple

print(tuple(names_list))

#SET

#membuat set
names = {"Apple","Banana","Cherry"}
print(names)
names = set(("Apple","Banana","Cherry"))
#print(names[2]) klo pke ini error, krn set tidak berurut jadi itemnya gabisa diakses
name ="Apple"
letters= set(name)
print(set(name))

# tapi bisa di manipulasi
names = {"Apple","Banana","Cherry","durian","pear"}
names.add("dragon fruit")
names.discard("Apple")
names.discard("orange")
names.remove("durian")
names.pop()

print(names)