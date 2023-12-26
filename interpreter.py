n = input("expression: ")

x, op, z = n.split(" ")

x = int(x)
z = int(z)

match op:
    case "+":
        y = x + z
    case "-":
        y = x - z
    case "*":
        y = x * z
    case "/":
        y = x / z
    case _:
        z = "operador no valido"

y = float(y)

print (f"el resultado de {x} {op} {z} es: {y}")

