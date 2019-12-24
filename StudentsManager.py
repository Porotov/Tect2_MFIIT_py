from Students import Student
import re
import datetime


def AddStudents():
    code = (int)(input())
    fio = input()
    brithdate = input()
    email = input()
    phone = (int)(input())

    if 600000 > code or code < 190000:
        print('Код указан неверно')

    if re.match('[A-z]+', fio):
        print('Имя должно содержать русские буквы')
        return None
    if re.match('[A-z]+[.]+[A-z]+[@]+[A-z]+[.]+[A-z]', email):
        print('Почта указана неверно')
        return None
    #if len(phone) != 11 :
    #    print('Телефон должен иметь 11 цифр. Например:89141234567')


    return Student(code, fio, brithdate, email, phone)
