

def print_main():
    print ('Выберите меню:\n' \
                          '1. Данные о студентах\n2. Данные о баллах' \
                          '\n3. Данные о срезах\n4. Экспорт данных\n5. Импорт данных\n6. Выход')

def print_group_menu():
    print('1. Посмотреть группы\n2. Добавить группы\n3. Назад')

def print_mark_menu():
     print('1. Посмотреть баллы\n2. Добавить баллы\n3. Назад')

def print_cross_menu():
     print('1. Посмотреть срезы\n2. Добавить срез\n3. Назад')


def print_menu(user_state, user_input):
    if user_input == '1' and user_state == '0':
        print_group_menu()
        user_state = '1'
    elif user_input == '2' and user_state == '0':
        print_mark_menu()
        user_state = '2'
    elif user_input == '3' and user_state == '0':
        print_cross_menu()
        user_state = '3'
    elif user_input == '6' and user_state == '0':
        user_state = '6'


def main():
    from os import system
    print_main()
    cur_state = '0'
    user_input = -1

    while (cur_state != '0' or user_input != '6'):
        user_input = input()
        print_menu(cur_state, user_input)

if __name__ == '__main__':

    main()
