import unittest
from io import StringIO
from unittest.mock import patch
import MarksManager
from Marks import Mark

Marks = [Mark('Иванов Иван Иванович', 'Информатика', 2019, '1 семестр', 80)]

class Tester(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_true(self, mock_out):
        user_input = ['Иванов Иван Иванович', 'Информатика', 2019, '1 семестр', 80]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student,user_input[0])
        self.assertEqual(new_mark.subject,user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection,user_input[3])
        self.assertEqual(new_mark.points,user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_false(self, mock_out):
        user_input = ['Иванов Иван j', 'Информатика', 2019, '1 семестр', 80]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student, user_input[0])
        self.assertEqual(new_mark.subject, user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection, user_input[3])
        self.assertEqual(new_mark.points, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_false2(self, mock_out):
        user_input = ['Иванов Иван Иванович', 'info', 2019, '1 семестр', 80]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student, user_input[0])
        self.assertEqual(new_mark.subject, user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection, user_input[3])
        self.assertEqual(new_mark.points, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_false3(self, mock_out):
        user_input = ['Иванов Иван Иванович', 'Информатика', 1960, '1 семестр', 80]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student, user_input[0])
        self.assertEqual(new_mark.subject, user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection, user_input[3])
        self.assertEqual(new_mark.points, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_false4(self, mock_out):
        user_input = ['Иванов Иван Иванович', 'Информатика', 2100, '1 семестр', 80]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student, user_input[0])
        self.assertEqual(new_mark.subject, user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection, user_input[3])
        self.assertEqual(new_mark.points, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_false5(self, mock_out):
        user_input = ['Иванов Иван Иванович', 'Информатика', 2019, '1 s', 80]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student, user_input[0])
        self.assertEqual(new_mark.subject, user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection, user_input[3])
        self.assertEqual(new_mark.points, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_false6(self, mock_out):
        user_input = ['Иванов Иван Иванович', 'Информатика', 2019, '1 семестр', -15]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student, user_input[0])
        self.assertEqual(new_mark.subject, user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection, user_input[3])
        self.assertEqual(new_mark.points, user_input[4])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateMark_false7(self, mock_out):
        user_input = ['Иванов Иван Иванович', 'Информатика', 2019, '1 семестр', 180]
        with patch('builtins.input', side_effect=user_input):
            new_mark = MarksManager.AddMark()
        self.assertEqual(new_mark.student, user_input[0])
        self.assertEqual(new_mark.subject, user_input[1])
        self.assertEqual(new_mark.year, user_input[2])
        self.assertEqual(new_mark.crossSection, user_input[3])
        self.assertEqual(new_mark.points, user_input[4])

if __name__ == '__main__':
    unittest.main()
