def main():
    time_str = input("Enter the time in 24-H format: ")

    time_convert = convert(time_str)

    if time_convert:
        print(f"es hora del {time_convert}")
    else:
        print("No es hora de comer")
    


def convert(time):
    hora, min = time.split(":")
    check = int(hora) + int(min) / 60.0
    
    # Representación decimal de la hora
    if 7.0 <= check <= 8.0:
        return "Desayuno"
    elif 12.0 <= check <= 13.0:
        return "Almuerzo"
    elif 18.0 <= check <= 19.0:
        return "Cena"
    else:
        return None



if __name__ == "__main__":
    main()