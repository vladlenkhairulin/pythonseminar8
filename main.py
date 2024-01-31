from work_with_file import *
from find_and_change import search_contact
from find_and_change import *
from copy_string import *
def interface(filefile="phonebook.txt"):
    while True:
        flag = False
        while not flag:
            try:
                with open(filefile, 'a') as ff:
                    pass
            except Exception as e:
                print("Error")
                break
            else:
                flag = True
        choice = ''
        while choice != '4':
            print(
                "Варианты действия: \n"
                "1 - Ввод данных контакта \n"
                "2 - Вывести данные на экран \n"
                "3 - Поиск контакта \n"
                "4 - Выход \n"
                "5 - Создание нового файла \n"
                "6 - Копирование строки в новый файл \n"
                "7 - Выбор другого файла."
            )
            choice = input("Выберите номер действия: ")
            while choice not in ('1', '2', '3', '4', '5', '6', '7'):
                print("Некорректный ввод данных!")
                choice = input("Выберите номер действия: ")
                print()
            if choice == '7':
                change_file = input("Выберите имя файла, с которым хотите работать: ")
                filefile = change_file
                print(f"Теперь вы работаете с файлом {change_file}")
                break
            match choice:
                case '1':
                    data_input(filefile)
                case '2':
                    print_data(filefile)
                case '3':
                    search_contact(filefile)
                case '4':
                    print('Всего доброго!')
                case '5':
                    newfile = input("Введите путь к новому файлу: ")
                    get_user_file(newfile)
                case '6':
                    newfile1 = input("Введите имя файла, откуда хотите копировать: ")
                    newfile2 = input("Введите имя файла, куда хотите копировать: ")
                    copy_str(newfile1, newfile2)

if __name__ == '__main__':
    interface()