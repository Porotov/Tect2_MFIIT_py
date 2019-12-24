from Marks import Mark
import re


def AddMark():
    student = input()
    subject = input()
    year = (int)(input())
    crossSection = input()
    points = (int)(input())

    if 1960 > year or year < 2100:
        print('Год указан неверно')

    if re.match('[A-z]+', student):
        print('Имя должно содержать русские буквы')
        return None

    #if re.match('[A-z]+', subject):
    #    print('Предмет должно содержать русские буквы')
    #    return None

    if re.match('[A-z]+', crossSection):
        print('Семестр должно содержать русские буквы и цифр')
        return None

    if points > 0 and points < 100:
        print('Баллы должны быть больше 0 и меньше 100')

    return Mark(student, subject, year, crossSection, points)