# Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. ФИО, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные. Программа должна сохранять данные в текстовом файле. Пользователь может ввести одну из характеристик для поиска определенной записи
# (например имя или фамилию человека). Использование функций. Ваша программа не должна быть линейной


def show_menu():
    print("\nВыберите необходимое действие:/n"
          "1. Отобразить весь справочник\n" 
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n" 
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу\n")       
    choice = int(input())
    return choice


def work_with_phonebook():
	

    choice = show_menu()

    phone_book = read_csv('phonebook.csv')

    while (choice!=7):

        if choice==1:
            print(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)

        choice=show_menu()




def read_csv(filename):
    phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding = 'utf8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


work_with_phonebook()

# Функция для добавления нового контакта в телефонную книгу
def add_contact():
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    address = input("Введите адрес: ")
    phone_book[name] = {"номер": number, "адрес": address}
    print("Контакт успешно добавлен")
    

# Функция для изменения данных контакта
def edit_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phonebook:
        number = input("Введите новый номер телефона: ")
        address = input("Введите новый адрес: ")
        phonebook[name] = {"номер": number, "адрес": address}
        print("Контакт успешно изменен")
    else:
        print("Контакт не найден")

# Функция для удаления контакта из телефонной книги
def delete_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")