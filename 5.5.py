
import datetime

content = open('ips.txt').read()

lines = content.split('\n')

currentDate = datetime.date(2023, 1, 11)

skippedFirst = False
for line in lines:
    if skippedFirst is False:
        skippedFirst = True
    else:
        data = line.split(';')
        if data[0] and data[1] and data[2]:
            [pesel, land, birthPlace] = data
            year = int(pesel[0] + pesel[1])
            month = int(pesel[2] + pesel[3])
            day = int(pesel[4] + pesel[5])
            century = 1900
            if month > 12:
                century = 2000
                month = month - 20

            year = century + year
            date = datetime.date(year, month, day)

            daysDifference = (currentDate - date).days
            print(daysDifference)

print()