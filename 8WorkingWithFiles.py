filename_work = "phon.txt"

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt(filename_work)

    while (choice!=7):

        if choice==1: # 1. Отобразить весь справочник
            print_result(phone_book)
        elif choice==2: # 2. Найти абонента по фамилии
            last_name = input('lastname ')
            print(find_by_lastname(phone_book,last_name))
            input("Press Enter to continue...")
        elif choice==3: # 3. Найти абонента по номеру телефона
            number = input('number ')
            print(find_by_number(phone_book, number))
            input("Press Enter to continue...")
        elif choice == 4:  # 4. Изменить номер
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
	    	input("Press Enter to continue...")
        elif choice==5: # 5. Удалить абонента по фамилии
            lastname=str(input('lastname '))
            print(delete_by_lastname(phone_book,lastname))
            input("Press Enter to continue...")
        elif choice==6: # 6. Добавить данные
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt(filename_work,phone_book)
            input("Press Enter to continue...")
        choice=show_menu()

def show_menu(): # Меню, выбор из списка
    print("\nВыберите необходимое действие:\n"
            "1. Отобразить весь справочник\n"
            "2. Найти абонента по фамилии\n"
            "3. Найти абонента по номеру телефона\n"
            "4. Изменить номер\n"
            "5. Удалить абонента по фамилии\n"
            "6. Добавить данные\n"
            "7. Закончить работу")
    choice = int(input("From 1-7: "))
    return choice

def read_txt(filename): # Чтение файла
    phone_book=[]
    fields = ['Фамилия',    'Имя',    'Телефон',    'Описание']
# line.split(',') = ['Питонов'‚    'Антон',    '777',    'знает Питон']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.split(',')))
           phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book): # Запись файла
    with open(filename,'w',encoding='utf-8') as phout:
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

        # print("\t" "Фамилия\t" "Имя\t" "Телефон\t" "Описание")
        # for i in range(len(phone_book)):
        # print(f"{i + 1}. {list(phone_book[i].values())}")
        #    print(f"{i + 1}. {phone_book[i]}")

    # Вывод заголовка таблицы
    print(
        " ",
        "Фамилия".ljust(20),
        # "|",
        "Имя".ljust(20),
        # "|",
        "Телефон".ljust(10),
        # "|",
        "Описание".ljust(20),
        # "|",
        sep=" |",
    )
    print(
        "═══════════════════════════════════════════════════════════════════════════════════════════"
    )
    # Вывод данных
    i = 0
    for item in phone_book:
        i = i + 1
        print(
            i,
            # "|",
            item["Фамилия"].ljust(20),
            # "|",
            item["Имя"].ljust(20),
            # "|",
            item["Телефон"].ljust(10),
            # "|",
            item["Описание"].ljust(20),
            # "|",
            sep=" |",
        )
    print(
        "═══════════════════════════════════════════════════════════════════════════════════════════"
    )
    input("Press Enter to continue...")
work_with_phonebook()

