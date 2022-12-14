import re

def pass_check():
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Пароль должен содержать не менее 6 символов")
        print("False")
    elif re.search('[0-9]',password) is None:
        print("Пароль должен содержать хотя бы одну цифру")
        print("False")
    elif "password" in password:
        print("Пароль не должен содержать слово 'password' в любом регистре")
        print("False")
    elif "PASSWORD" in password:
        print("Пароль не должен содержать слово 'password' в любом регистре")
        print("False")
    elif password.isdigit() is True:
        print("Пароль не может состоять только из цифр")
        print("False")
    else:
        print("Пароль соответствует требованиям")
        print("True")
pass_check()