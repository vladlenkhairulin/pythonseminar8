from work_with_file import print_data
from user_data import read_file

def get_user_file(user_file_path):
    try:
        with open(user_file_path, 'a') as new_f:
            pass
    except FileNotFoundError:
        print(f"File not found")

def copy_str(file_path, new_file_path):
    print_data(file_path)
    number_of_str = int(input("Введите номер строки, которую хотите скопировать"))
    contacts = read_file(file_path)
    contacts_list = contacts.strip().split('\n')
    flag = False
    while flag == False:
        if number_of_str > len(contacts_list) or number_of_str < 1:
            number_of_str = input("Введите номер строки, которую хотите скопировать")
        else:
            flag = True
    #if flag == True:
    for i in range(len(contacts_list)):
        if i == number_of_str-1:
            copied_str = contacts_list[i]
    with open(new_file_path, 'a') as new_f1:
        new_f1.write(copied_str + '\n')

