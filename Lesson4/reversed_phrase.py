phrase = ''
while True:
    phrase = input('Введите два слова. Чтобы прекратить введите q :')
    if phrase != 'q':
        lst = phrase.lower().split()
        lst = lst[::-1]
        phrase1 = ' '.join(lst[::-1])
        print(phrase, '=>', phrase1[::-1].title())
    else:
        break
