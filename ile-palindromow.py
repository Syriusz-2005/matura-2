

file = open('slowa.txt')
content = file.read()
words = content.split('\n')

count = 0
for word in words:
    for i in range(0, len(word)):
        if i >= len(word) - 1 - i:
            count += 1
            break
        if word[i] != word[len(word) - 1 - i]:
            break


print(count)
