content = open('ips.txt').read()

lines = content.split('\n')

incorrectControlNumbersCount = 0

skippedFirst = False
for line in lines:
    if skippedFirst is False:
        skippedFirst = True
    else:
        data = line.split(';')
        if data[0] and data[1] and data[2]:
            [pesel, land, birthPlace] = data
            [a, b, c, d, e, f, g, h, i, j, k] = pesel
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            e = int(e)
            f = int(f)
            g = int(g)
            h = int(h)
            i = int(i)
            j = int(j)
            k = int(k)
            temp = (a + b * 3 + c * 7 + d * 9 + e + f * 3 + g * 7 + h * 9 + i + j * 3) % 10
            correctControlNumber = 0
            if temp == 0: correctControlNumber = 0
            else: correctControlNumber = 10 - temp

            if correctControlNumber != k: incorrectControlNumbersCount += 1


print(incorrectControlNumbersCount)