def choose_action(phonebook):
    while True:
        print('Что делаем?')
        user_choice = input('1 - Найти контакт\n2 - Добавить контакт\n\
3 - Изменить контакт\n4 - Удалить контакт\n5 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
       
        if user_choice == '1':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '2':
            add_phone_number(phonebook)
        elif user_choice == '3':
            change_phone_number(phonebook)
        elif user_choice == '4':
            delete_contact(phonebook)
        elif user_choice == '5':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('Пока!')
            break
        else:
            print('Ошибка!')
            print()
            continue


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона', 'Комментарий']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по отчеству\n4 - по телефону\n5 - по комментарию\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите отчество для поиска: ')
        print()
    elif search_field == '4':
        search_value = input('Введите телефон поиска: ')
        print()
    elif search_field == '5':
        search_value = input('Введите комментарий поиска: ')
        print()    
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', '4': 'Номер телефона', '5': 'Комментарий'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Такого контакта нет!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество')
    comment = input('Введите комментарий')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name,middle_name, phone_number, comment


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Нет такого контакта')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Что вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Номер телефона\n5 - Комментарий')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Отчество: ')
    elif field == '4':
        number_to_change[3] = input('Введите номер телефона: ')
    elif field == '5':
        number_to_change[4] = input('Комменарий: ')    
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'phone_book.txt'
    choose_action(file)