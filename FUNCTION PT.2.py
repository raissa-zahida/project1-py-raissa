#FUNCTION KEYWORD ARGUMEN 

def fullname (fname, lname=""):
    return fname + " " + lname

print(fullname(lname="Raissa", fname= "Zahida"))

#ARGS

def addition(*numbers):
    result = 0
    
    for n in numbers:
        result =+ n
        
    return result   

