palabra = str(input("input: "))

nueva_palabra =''
for x in palabra:
    if x.lower() not in ("a", "e", "i", "o", "u"):
        nueva_palabra += x

print (nueva_palabra)
