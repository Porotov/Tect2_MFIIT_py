import unittest
from io import StringIO
from unittest.mock import patch
import datetime
import StudentsManager
from Students import Student

Students = [Student(191364, 'Иванов Иван Иванович', '1.01.2000', 'ivan@gmail.com', 89141234567)]

class Tester(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_true(self, mock_out):
        user_input = [191364, 'Иванов Иван Иванович', '1.01.2000', 'ivan@gmail.com', 89141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code,user_input[0])
        self.assertEqual(new_student.fio,user_input[1])
        self.assertEqual(new_student.brithdate,datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email,user_input[3])
        self.assertEqual(new_student.phone,user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false(self, mock_out):
        user_input = [1, 'Иванов Иван Иванович', '1.01.2000', 'ivan@gmail.com', 89141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code, user_input[0])
        self.assertEqual(new_student.fio, user_input[1])
        self.assertEqual(new_student.brithdate, datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email, user_input[3])
        self.assertEqual(new_student.phone, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false2(self, mock_out):
        user_input = [1000000, 'Иванов Иван Иванович', '1.01.2000', 'ivan@gmail.com', 89141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code, user_input[0])
        self.assertEqual(new_student.fio, user_input[1])
        self.assertEqual(new_student.brithdate, datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email, user_input[3])
        self.assertEqual(new_student.phone, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false3(self, mock_out):
        user_input = [191364, 'Иванов Иван j', '1.01.2000', 'ivan@gmail.com', 89141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code, user_input[0])
        self.assertEqual(new_student.fio, user_input[1])
        self.assertEqual(new_student.brithdate, datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email, user_input[3])
        self.assertEqual(new_student.phone, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false4(self, mock_out):
        user_input = [191364, 'Иванов Иван Иванович', '1.01.1900', 'ivan@gmail.com', 89141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code, int(user_input[0]))
        self.assertEqual(new_student.fio, user_input[1])
        self.assertEqual(new_student.brithdate, datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email, user_input[3])
        self.assertEqual(new_student.phone, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false5(self, mock_out):
        user_input = [1, 'Иванов Иван Иванович', '1.01.2100', 'ivan@gmail.com', 89141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code, user_input[0])
        self.assertEqual(new_student.fio, user_input[1])
        self.assertEqual(new_student.brithdate, datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email, user_input[3])
        self.assertEqual(new_student.phone, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false6(self, mock_out):
        user_input = [191364, 'Иванов Иван Иванович', '1.01.2000', 'ivan.gmail.com', 89141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code,user_input[0])
        self.assertEqual(new_student.fio,user_input[1])
        self.assertEqual(new_student.brithdate,datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email,user_input[3])
        self.assertEqual(new_student.phone,user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false7(self, mock_out):
        user_input = [191364, 'Иванов Иван Иванович', '1.01.2000', 'ivan@gmail.com', 9141234567]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code,user_input[0])
        self.assertEqual(new_student.fio,user_input[1])
        self.assertEqual(new_student.brithdate,datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email,user_input[3])
        self.assertEqual(new_student.phone,user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateStudent_false8(self, mock_out):
        user_input = [191364, 'Иванов Иван Иванович', '1.01.2000', 'ivan@gmail.com', 891412345678]
        with patch('builtins.input', side_effect=user_input):
            new_student = StudentsManager.AddStudents()
        self.assertEqual(new_student.code,user_input[0])
        self.assertEqual(new_student.fio,user_input[1])
        self.assertEqual(new_student.brithdate,datetime.datetime.strptime(user_input[2],'%d.%m.%Y'))
        self.assertEqual(new_student.email,user_input[3])
        self.assertEqual(new_student.phone,user_input[4])


if __name__ == '__main__':
    unittest.main()
