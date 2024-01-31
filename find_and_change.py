from work_with_file import *
def search_contact():
    print(
        'Варианты поиска:\n'\
        '1 - по фамилии\n'\
        '2 - по имени\n'\
        '3 - по отчеству\n'\
        '4 - по телефону\n'\
        '5 - по адресу(городу)'
        )
    var = input('Выберите необходимый вариант: ')
    while var not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод данных!')
            var = input('Выберите необходимый вариант: ')
            print()            
    i_var = int(var) - 1

    find = input('Введите данные для поиска: ').title()
    print()
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()        
        # print(contact_lst)
        if find in contact_lst[i_var]:
            print(contact_str)
    print()