import unittest
from io import StringIO
from unittest.mock import patch
import MyProgram

main_menu_string = 'Выберите меню:\n' \
                          '1. Данные о студентах\n2. Данные о баллах' \
                          '\n3. Данные о срезах\n4. Экспорт данных\n5. Импорт данных\n6. Выход\n'
group_menu_string = '1. Посмотреть группы\n2. Добавить группы\n3. Назад\n'
mark_menu_string = '1. Посмотреть баллы\n2. Добавить баллы\n3. Назад\n'
cross_menu_string = '1. Посмотреть срезы\n2. Добавить срез\n3. Назад\n'

class Tester(unittest.TestCase):
    def test_main_menu(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_print:
            MyProgram.print_main()
        self.assertEqual(mock_print.getvalue(), main_menu_string)

    def test_group_menu(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_print:
            MyProgram.print_group_menu()
        self.assertEqual(mock_print.getvalue(), group_menu_string)

    def test_mark_menu(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_print:
            MyProgram.print_mark_menu()
        self.assertEqual(mock_print.getvalue(), mark_menu_string)

    def test_cross_menu(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_print:
            MyProgram.print_cross_menu()
        self.assertEqual(mock_print.getvalue(), cross_menu_string)


    @patch('sys.stdout', new_callable=StringIO)
    def test_main_to_group(self, mock_out):
        user_input = ['1','3','6']
        with patch('builtins.input', side_effect=user_input):
            MyProgram.main()
        self.assertEqual(mock_out.getvalue(), main_menu_string + group_menu_string)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_to_mark(self, mock_out):
        user_input = ['2']
        with patch('builtins.input', side_effect=user_input):
            MyProgram.main()
        self.assertEqual(mock_out.getvalue(), main_menu_string + mark_menu_string)


    @patch('sys.stdout', new_callable=StringIO)
    def test_main_to_cross(self, mock_out):
        user_input = ['3']
        with patch('builtins.input', side_effect=user_input):
            MyProgram.main()
        self.assertEqual(mock_out.getvalue(), main_menu_string + cross_menu_string)

if __name__ == '__main__':
    unittest.main()

