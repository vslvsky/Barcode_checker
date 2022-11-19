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
    barcode = input("штрихкод: ")
    barcode_list.append(barcode)
    i = barcode
    #print(barcode_list)


#подсчет количества баркодов
count = collections.Counter()
for word in barcode_list:
    count[word] += 1


#запись количества в файл
with open(f"result_{get_datatime()}.txt", "w") as file:
    for key, value in count.items():
        file.write(f"{key} : {value}\n")