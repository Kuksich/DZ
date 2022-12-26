import re

def pass_check(password):
    """Функция проверки пароля
    
    Принимает:
        password - пароль пользователя
    Проверяет пароль по пунктам:
        1.Пароль должен содержать не менее 6 символов
        2.Пароль должен сдержать хотя бы одну цифру
        3.Пароль не может состоять только из цифр
        4.Пароль не можент сожержать слово "Password" в любом регистре
    Возвращает:
        True или False
    """
    #password = input("Введите пароль: ")
    if len(password) < 6:
        #print("Пароль должен содержать не менее 6 символов")
        return False
    elif re.search('[0-9]',password) is None:
        #print("Пароль должен содержать хотя бы одну цифру")
        return False
    elif "password" in password:
        #print("Пароль не должен содержать слово 'password' в любом регистре")
        return False
    elif "PASSWORD" in password:
        #print("Пароль не должен содержать слово 'password' в любом регистре")
        return False
    elif "PASSWORD" and "password" in password:
        return False
    elif password.isdigit() is True:
        #print("Пароль не может состоять только из цифр")
        return False
    else:
        #print("Пароль соответствует требованиям")
        return True
