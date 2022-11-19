from playsound import playsound
import collections
import datetime
from datetime import datetime


def get_datatime() -> datetime:
    date_format = '%H-%M %d-%m-%Y'
    today = datetime.now()
    today = today.strftime(date_format)
    return today


def check_and_count():
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
    return barcode_list


def count_barcode(barcode_list: list):
    count = collections.Counter()
    for word in barcode_list:
        count[word] += 1
    return count


def save_to_file(count, time):
    with open(f"result{time}.txt", "w") as file:
        file.write(str(count))
