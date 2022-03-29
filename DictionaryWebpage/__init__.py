import django
django.setup()

from DictionaryWebpage.models import Word



import csv
import sys

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

file = open("C:/Users/Rafist0/PycharmProjects/DictionaryWebpage/english-dictionary.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
print(len(rows))
file.close()

for row in rows:
    b = Word(word=row[0], wordtype=row[1], definition=row[2])
    b.save()


