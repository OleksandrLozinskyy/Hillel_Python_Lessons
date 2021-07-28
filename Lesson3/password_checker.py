secure_dict = {'Aleksandr': '12345', 'Ivan': 'qwerty', 'Oleg': 'qweasd', 'Maria': '123qweasd'}

login = input('Please enter your login: ')

if secure_dict.get(login):
    password = input('Please enter your password: ')
    if password == secure_dict[login]:
        print('Your credentials are success!')
    else:
        print('Please, verify your credentials and try again!')
else:
    print('You are not a registered user!')