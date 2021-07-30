phrase = ''
while True:
    phrase = input('Введите два слова. Чтобы прекратить введите q :')
    if phrase != 'q':
        phrase1 = phrase.lower()
        print(phrase, '=>', phrase1[::-1].title())
    else:
        break
