
class Mark:
    student = ''
    subject = ''
    year = 0
    crossSection = ''
    points = 0

    def __init__(self, st, su, y, cs, p):
        self.student = st
        self.subject = su
        self.year = y
        self.crossSection = cs
        self.points = p