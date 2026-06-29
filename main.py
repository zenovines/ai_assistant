from actions import open_safari, speak

Running = True

while Running:
    user = input("You > ").lower()
    if user == "exit":
        print("Aki > goodbye")
        Running = False
    elif user == "name":
        print("Aki > Hi i am Aki!")
    elif user == "hello":
        print("Aki > Hello.")
        speak("Hello")
    elif user == "open safari":
        print("Aki > Opening Safari..")
        open_safari()
    else:
        print("Aki > i don't understand that command yet")
    
    