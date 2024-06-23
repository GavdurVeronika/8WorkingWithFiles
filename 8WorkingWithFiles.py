filename_work = "phon.txt"

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt(filename_work)

    while (choice!=5):

        if choice==1: # 1. Отобразить весь справочник
            print_result(phone_book)
        elif choice==2: # 2. Найти абонента по фамилии
            last_name = input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3: # 3. Найти абонента по номеру телефона
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice==4: # 4. Удалить абонента по фамилии
            lastname=str(input('lastname '))
            print(delete_by_lastname(phone_book,lastname))
        
        choice=show_menu()

def show_menu(): # Меню, выбор из списка
    print("\nВыберите необходимое действие:\n"
            "1. Отобразить весь справочник\n"
            "2. Найти абонента по фамилии\n"
            "3. Найти абонента по номеру телефона\n"
            "4. Удалить абонента по фамилии\n"
            "5. Закончить работу")
    choice = int(input("From 1-5: "))
    return choice

def read_txt(filename): # Чтение файла
    phone_book=[]
    fields = ['Фамилия',    'Имя',    'Телефон',    'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.split(',')))
           phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book): # Запись файла
    with open(filename,'r+',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

# 1. Отобразить весь справочник
def print_result(phone_book):
    if not phone_book:
        print("Справочник пуст")
    else:
        print(
            "Справочник:\n"
            )
        print(
        " ",
        "Фамилия".ljust(20),
        "Имя".ljust(20),
        "Телефон".ljust(10),
        "Описание".ljust(20),
        sep=" |",
    )
       # Вывод данных
    i = 0
    for item in phone_book:
        i = i + 1
        print(
            i,
            item["Фамилия"].ljust(20),
            item["Имя"].ljust(20),
            item["Телефон"].ljust(10),
            item["Описание"].ljust(20),
            sep=" |",
        )
    
# 2. Найти абонента по фамилии
def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            return phone_book[i]
    return "not found"


# 3. Найти абонента по номеру телефона
def find_by_number(phone_book, number):
    for i in range(len(phone_book)):
        if phone_book[i].get("Телефон", "Нет такого номера") == number:
            return phone_book[i]

# 4. Удалить абонента по фамилии
def delete_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            del phone_book[i]
            return True
    return False

work_with_phonebook()

