

file = open('slowa.txt')
content = file.read()
words = content.split('\n')

palindromy = []

for word in words:
    for i in range(0, len(word)):
        if i >= len(word) - 1 - i:
            palindromy.append(word)
            break
        if word[i] != word[len(word) - 1 - i]:
            break

rodziny: dict[int, list] = {}

for palindrom in palindromy:
    length = len(palindrom)
    if not rodziny.get(length):
        rodziny[length] = []
    rodziny[length].append(palindrom)


plikRodziny = open('rodziny.txt', 'w')

for dlugosc in rodziny:
    wyrazy = rodziny[dlugosc]
    wyrazy.sort()
    line = ''
    for wyraz in wyrazy: line += ' ' + wyraz
    line = line.replace(' ', '', 1)
    plikRodziny.write(line + '\n')



