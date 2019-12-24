import unittest
from io import StringIO
from unittest.mock import patch
import GroupsManager
from Groups import Group

groups = [Group('М-ФИИТ-19', 2019, 2), Group('Б-ФИИТ-19', 2019, 4)]

class Tester(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_true(self, mock_out):
        user_input = ['М-ФИИТ-19',2019,2]
        with patch('builtins.input', side_effect=user_input):
            new_group = GroupsManager.AddGroups()
        self.assertEqual(new_group.name,user_input[0])
        self.assertEqual(new_group.year,user_input[1])
        self.assertEqual(new_group.duration,user_input[2])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_false(self, mock_out):
        user_input = ['M-FIIT-19',2019,2]
        with patch('builtins.input', side_effect=user_input):
            GroupsManager.AddGroups()
        self.assertEqual(mock_out.getvalue(),'Имя должно содержать русские буквы\n')

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_false2(self, mock_out):
        user_input = ['М-ФИИТ-19',1956,2]
        with patch('builtins.input', side_effect=user_input):
            GroupsManager.AddGroups()
        self.assertEqual(mock_out.getvalue(),'Дата указана неверно\n')

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_false3(self, mock_out):
        user_input = ['М-ФИИТ-19',2020,2]
        with patch('builtins.input', side_effect=user_input):
            GroupsManager.AddGroups()
        self.assertEqual(mock_out.getvalue(),'Дата указана неверно\n')

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_true2(self, mock_out):
        user_input = ['М-ФИИТ-19',2019,3]
        with patch('builtins.input', side_effect=user_input):
            new_group = GroupsManager.AddGroups()
        self.assertEqual(new_group.name,user_input[0])
        self.assertEqual(new_group.year,user_input[1])
        self.assertEqual(new_group.duration,user_input[2])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_true3(self, mock_out):
        user_input = ['М-ФИИТ-19',2019,4]
        with patch('builtins.input', side_effect=user_input):
            new_group = GroupsManager.AddGroups()
        self.assertEqual(new_group.name,user_input[0])
        self.assertEqual(new_group.year,user_input[1])
        self.assertEqual(new_group.duration,user_input[2])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_true4(self, mock_out):
        user_input = ['М-ФИИТ-19',2019,5]
        with patch('builtins.input', side_effect=user_input):
            new_group = GroupsManager.AddGroups()
        self.assertEqual(new_group.name,user_input[0])
        self.assertEqual(new_group.year,user_input[1])
        self.assertEqual(new_group.duration,user_input[2])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_true5(self, mock_out):
        user_input = ['М-ФИИТ-19',2019,6]
        with patch('builtins.input', side_effect=user_input):
            new_group = GroupsManager.AddGroups()
        self.assertEqual(new_group.name,user_input[0])
        self.assertEqual(new_group.year,user_input[1])
        self.assertEqual(new_group.duration,user_input[2])

    @patch('sys.stdout', new_callable=StringIO)
    def testCreateGroup_false4(self, mock_out):
        user_input = ['М-ФИИТ-19',2019,1]
        with patch('builtins.input', side_effect=user_input):
            GroupsManager.AddGroups()
        self.assertEqual(mock_out.getvalue(),'Дата обучения задана неверно\n')

    @patch('sys.stdout', new_callable=StringIO)
    def testWatchGroup_true(self, mock_out):
        GroupsManager.WatchGroups(groups)
        self.assertEqual(mock_out.getvalue(),'М-ФИИТ-19\nБ-ФИИТ-19\n')



if __name__ == '__main__':
    unittest.main()
