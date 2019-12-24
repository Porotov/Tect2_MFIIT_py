from Groups import Group
import re
import datetime

def AddGroups():
    name = input()
    year = (int)(input())
    duration = (int)(input())

    if re.match('[A-z]+', name):
        print('Имя должно содержать русские буквы')
        return None
    if 1957 > year or datetime.datetime.today().year < year:
        print('Дата указана неверно')
        return None
    if duration != 2 and duration != 3 and duration != 4 and duration != 5 and duration != 6:
        print('Дата обучения задана неверно')
        return None

    return Group(name,year,duration)



def WatchGroups(groups):
    print('\n'.join([x.name for x in groups]))
