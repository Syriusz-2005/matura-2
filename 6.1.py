
def getPointsCount(kandydat):
    [id, nazwisko, imie, urodzenie, laureat, swiadecstwo, egzamin, wolontariat, konkursy, profil] = kandydat
    totalPoints = int(swiadecstwo) + int(egzamin) + int(wolontariat) + int(konkursy)
    if int(laureat) == 1: totalPoints += 200

    return totalPoints



file = open('Kandydaci.txt')
content = file.read()
lines = content.split('\n')

lines.pop(0)
lines.pop(len(lines) - 1)

lines.sort(key=lambda line: getPointsCount(line.split(';')))

print(lines)
for kandydat in lines:
    pointsCount = getPointsCount(kandydat.split(';'))
    print(pointsCount)
