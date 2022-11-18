from playsound import playsound

i = 1
while i != 0:
    first = input("первый штрихкод: ")
    playsound("sms.mp3", False)

    second = input("второй штрихкод: ")

    if first == second:
        playsound("ok.mp3", False)
        print("ok")
    else:
        playsound("no.mp3", False)
        print("no")