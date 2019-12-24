import datetime


class Student:
    code = 0
    fio = ''
    brithdate = ''
    email = ''
    phone = 0

    def __init__(self, c, f, b, e, p):
        self.code = c
        self.fio = f
        if type(b) == datetime.datetime:
            self.brithdate = b
        else:
            self.brithdate = datetime.datetime.strptime(b, '%d.%m.%Y')
        self.email = e
        self.phone = p

