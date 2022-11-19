from playsound import playsound
import collections
import datetime
from datetime import datetime


def get_datatime() -> datetime:
    date_format = '%H-%M %d-%m-%Y'
    today = datetime.now()
    today = today.strftime(date_format)
    return today


i = "start"
barcode_list = []

#сверка двух подряд ШК и их подсчет если они одинаковые
while i != "stop":
    first = input("первый штрихкод: ")
    i = first
    playsound("sms.mp3", False)

    # если "стоп" то остановится
    if i != 'stop':
        second = input("второй штрихкод: ")

        if first == second:
            playsound("ok.mp3", False)
            barcode_list.append(first)
            print("OK")
        else:
            playsound("no.mp3", False)
            print("Check again!!")

#подсчет количества баркодов
count = collections.Counter()
for word in barcode_list:
    count[word] += 1

#запись количества в файл
with open(f"result{get_datatime()}.txt", "w") as file:
    file.write(str(count))
