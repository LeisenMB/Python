from pyfiglet import Figlet
import sys
import random

#declaraciones de figlet para simplificar
fig = Figlet()
fonts = fig.getFonts()

if len(sys.argv) == 1:
    texto = input(str("ingrese el texto: "))
    tipo = random.choice(fonts)
    fig.setFont(font=tipo)
    print(fig.renderText(texto))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    texto = input(str("ingrese el texto: "))
    tipo = sys.argv[2]
    fig.setFont(fonts=tipo)
    print(fig.renderText(texto))
    
else:
    sys.exit("invalid Usage")