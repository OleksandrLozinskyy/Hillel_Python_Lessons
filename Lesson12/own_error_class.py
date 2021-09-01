class CredentialsError(Exception):
    """
    Класс исключения срабатывающий при  неверно введенных учетных данных.
    """
    msg = 'Invalid credentials. Please try again'

    def __init__(self, value=None):
        if value is not None:
            self.msg = value

    def __str__(self):
        return self.msg


def user_login(username: str, password: str):
    """
    Функция проверки учетных данных

    :param username: Имя пользователя
    :param password: Пароль
    :return: None
    """

    _username = 'student'
    _password = '123456'

    try:
        if username != _username or password != _password:
            raise CredentialsError('Incorrect login or password!')
    except CredentialsError as err:
        print(err.__str__())
    else:
        print(f'Hello {_username}!')


# вызов функции с некорректными учетными данными
user_login('student', '124356')
# вызов функции с корректными учетными данными
user_login('student', '123456')
