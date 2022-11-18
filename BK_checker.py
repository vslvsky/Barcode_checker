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

while i != "stop":
    first = input("первый штрихкод: ")
    playsound("sms.mp3", False)
    i = first

    second = input("второй штрихкод: ")

    if first == second:
        playsound("ok.mp3", False)
        barcode_list.append(first)
        print("ok")
    else:
        playsound("no.mp3", False)
        print("no")

count = collections.Counter()
for word in barcode_list:
    count[word] += 1

now = get_datatime()

with open(f"result{now}.txt", "w") as file:
    file.write(str(count))