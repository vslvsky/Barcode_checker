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

count = collections.Counter()
for word in barcode_list:
    count[word] += 1

now = get_datatime()

with open(f"result{now}.txt", "w") as file:
    file.write(str(count))

#print(count)

