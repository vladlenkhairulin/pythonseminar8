from user_data import *

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}'

def data_input():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f'{contact}\n\n')

def print_data():    
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    for contact in enumerate(contacts_list, 1):
        print(*contact)