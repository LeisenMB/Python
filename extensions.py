n = str(input("Enter de file's name: "))
n_extension = n.split(".")[-1]

if n.endswith((".gif", ".jpg", ".jpeg", ".png")):
    print (f"image/{n_extension}.")
elif n.endswith((".pdf", ".txt", ".zip")):
    print (f"application/{n_extension}.")
else:
    print("no tiene extension.")