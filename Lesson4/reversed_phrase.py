phrase = ''
while True:
    phrase = input('Введите два слова. Чтобы прекратить введите q :')
    if phrase != 'q':
        print(phrase, '=>', phrase.lower()[::-1].title())
    else:
        break
