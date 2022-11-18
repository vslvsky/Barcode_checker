import collections

i = "start"
barcode_list = []

while i != "stop":
    barcode = input("штрихкод: ")
    barcode_list.append(barcode)
    i = barcode
    print(barcode_list)

count = collections.Counter()
for word in barcode_list:
    count[word] += 1

print(count)

