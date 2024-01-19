import inflect
import sys

p = inflect.engine()

names = []

#infinite loop
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break
nombres = p.join(names)
print("Adieu, adieu, to " + nombres)
