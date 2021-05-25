# https://inf-ege.sdamgia.ru/problem?id=35482

file = open('24.txt', 'r')

letterList = [0] * (ord('Z') - ord('A') + 1)

m = 100000
bestString = ''

for line in file:
    if line.count('G') < m: # < !
        m = line.count('G')
        bestString = line

for i in range(len(bestString) - 1):
    letterList[ord(bestString[i]) - ord('A')] += 1

for i in range(len(letterList)-1, -1, -1): # Идём в обратном порядке
    if letterList[i] == max(letterList):
        print(chr(i + ord('A')))
        break

file.close()
