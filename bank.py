n = str(input("Greeting: "))

if n.find("hello") == 0:
    print ("0$")
elif n[0] == "h":
    print ("20$")
else:
    print ("100$")