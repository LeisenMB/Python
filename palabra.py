palabra = str(input("ingrese la palabra: "))

nueva_palabra = ''
for a in palabra:
    if a.isupper():
        nueva_palabra += "_" + a.lower()
    else:
        nueva_palabra += a
        
print (nueva_palabra)