def caesar(word, shift): # word - само слово, shift - смещение по алфавиту
    result = []

    for c in word:
        if 'a' <= c <= 'z':
            x = ord(c) - ord('a')
            # (ord('z') - ord('a') + 1) - количество букв в английском алфавите
            x_new = (x + shift) % (ord('z') - ord('a') + 1)
            c = chr(ord('a') + x_new)
        if 'A' <= c <= 'Z':
            x = ord(c) - ord('A')
            # (ord('z') - ord('a') + 1) - количество букв в английском алфавите
            x_new = (x + shift) % (ord('z') - ord('a') + 1)
            c = chr(ord('A') + x_new)
        result.append(c)

    return result

in_word = False

line = input()

word = []

for c in line:
    if in_word: # В слове
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z': # Буква
            word.append(c)
        else: # Не буква (конец слова)
            print(*caesar(word, len(word)), c, sep='', end='')
            # print(c, end='')
            in_word = False
    else: # Не в слове
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z': # Буква:
            in_word = True
            word[:] = [c] # Очищаем word и добавляем туда символ c
        else: # Не буква
            print(c)
