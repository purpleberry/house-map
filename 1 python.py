import csv

total = 0
count = 0

with open('pp-monthly-update-new-version.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        print(row[1]+row[3])
        total = total + int(row[1])
        count = count + 1

print(total/count)

str1 = "RG1 9LO"

pos = str1.find(" ")
print(str1[:pos])
