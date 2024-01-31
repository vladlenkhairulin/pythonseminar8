from user_data import *

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone} {address}'

def data_input(file):
    contact = create_contact()
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{contact}\n')

def print_data(file):    
    contacts = read_file(file)
    contacts_list = contacts.strip().split('\n')
    for contact in enumerate(contacts_list, 1):
        print(*contact)