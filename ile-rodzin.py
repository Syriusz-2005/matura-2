

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

rodziny = {}

for palindrom in palindromy:
    length = len(palindrom)
    rodziny[length] = True

liczbaRodzin = len(rodziny)
print(liczbaRodzin)