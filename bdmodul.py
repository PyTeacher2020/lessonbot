import csv
data = []
lid = 0
access_level = 1
log1 = ''




def open_file():  # Запись информации из базы данных в список
    try:
        data.clear()
        with open('books.csv') as database:
            for i in database:
                data.append(i)
    except IOError:
        print('Input or Output error')


def login():  # Авторизация
    global access_level, log1
    accs = []
    log = input('Enter login\n')
    password = input('Enter password\n')
    with open('accounts.csv') as accounts:
        for i in accounts:
            accs.append(i)
    accs.pop(0)
    k = 0
    for i in accs:
        s = i.split(', ')
        print(log)
        print(s)
        print(password)
        if log == s[1] and password == s[2]:
            log1 = log
            access_level = int(s[3])
            print('Success\n')
            k = 1
            break
    if k == 0:
        print('Wrong login or password!\n')


def bad_symbols_check(text):  # Проверка запрещённых символов в тексте
    ret = False
    for i in text:
        if ord(i) in range(48, 57) or ord(i) in range(65, 90) or ord(i) in range(97, 122):
            ret = True
        else:
            ret = False
            break
    return ret


def register():  # Регистрация
    accs = []
    log_chk = []
    if access_level <= 1:
        logi = 1
        with open('accounts.csv') as log_check:
            for i in log_check:
                log_chk.append(i.split(', ')[1])
        while logi == 1:
            log = input('Enter login(from 3 to 12 symbols(numbers and letters))\n')
            if 3 <= len(log) <= 12 and not log.isspace() and bad_symbols_check(log) and log not in log_chk:
                logi = 0
        while True:
            password = input('Enter password(from 6 to 12 symbols(numbers and letters))\n')
            if 6 <= len(password) <= 12 and not password.isspace() and bad_symbols_check(password):
                break
        with open('accounts.csv') as accounts:
            for i in accounts:
                accs.append(i)
        accs.reverse()
        pid = str(int(accs[0].split(', ')[0]) + 1)
        file = open('accounts.csv', 'a')
        file.write(pid + ', ' + log + ', ' + password + ', ' + '2\n')
    else:
        print('You already have an account')


def set_access():  # Выдача уровня доступа аккаунту
    accs = []
    x = 0
    with open('accounts.csv') as accounts:
        for i in accounts:
            print(i)
            accs.append(i)
            x += 1
    ask = input('Enter account id\n')
    acc = input('Enter new access\n')
    for i in range(x):
        s = accs[i].split(', ')
        if s[0] == ask:
            s[3] = acc
            accs[i] = ', '.join(s) + '\n'
            break
    file = open('accounts.csv', 'w')
    for i in accs:
        file.write(i)
    file.close()


def id_sort(fil):  # Сортировка ID в базе данных (Только если ID находится первым в ряду)
    x = 0
    olist = []
    flist = []
    with open(fil) as file:
        for i in file:
            x += 1
            olist.append(i)
    flist.append(olist[0])
    olist.pop(0)
    for i in range(0, x - 1):
        s = olist[i].split(',')
        s[0] = str((i + 1))
        flist.append(','.join(s))
    file2 = open(fil, 'w')
    for i in flist:
        file2.write(i)
    file2.close()


def delete_account():  # Удаление аккаунта
    accs = []
    x = 0
    with open('accounts.csv') as accounts:
        for i in accounts:
            print(i)
            accs.append(i)
            x += 1
    ask = input('Enter account id\n')
    for i in range(x):
        s = accs[i].split(', ')
        if s[0] == ask:
            accs.pop(i)
            break
    file = open('accounts.csv', 'w')
    for i in accs:
        file.write(i)
    file.close()
    id_sort('accounts.csv')


def comma_check(word):  # Проверка запятых в слове (Для записи текста в базу данных)
    if ',' in word:
        word = '"' + word + '"'
    return word


def list_to_csv():  # Записывает список data в базу данных книжек
    file = open('test.csv', 'w')
    for i in data:
        file.write(i)
    file.close()


def empty_check(text):  # Проверка пустого текста
    if text.isspace() or text == '':
        return 'Empty'
    else:
        return text


def get_book(bid):  # Выдая книги по её ID
    s = []
    for i in data:
        s = i.split(',')
        if bid in s:
            return s
    print('There is no book with that id')
    return 0


def get_lid():  # Выдаёт самый маленький свободный ID
     data2 = data
     data2.reverse()
     s = data2[0].split(',')
     try:
        ret = int(s[0])
        return ret + 1
     except ValueError:
         print('There is any books in database')


def show_all():  # Отображает все книги
    for i in data:
        slist = i.split(',')
    return slist


def new_book():  # Добаление новой книги
    ask = 2
    book = []
    while ask == 2:
        book = []
        book.append(input('Name: '))
        book.append(input('Author: '))
        book.append(input('Year of issue: '))
        book.append(input('Date: '))
        book.append(input('Comment: '))
        print(book)
        for i in range(5):
            book[i] = comma_check(book[i])
            book[i] = empty_check(book[i])
        try:
            ask2 = int(input('1 - Yes, 2 - No, 0 - Exit'))
            if ask == 1 or ask == 2 or ask == 3:
                ask = ask2
            else:
                print('Enter only 1, 2 or 0')
        except ValueError:
            print('Enter only 1, 2 or 0')
    if ask == 1:
        book.reverse()
        book.append(str(lid))
        book[0] = book[0] + '\n'
        book.reverse()
        data.append(', '.join(book))
        list_to_csv()


def edit():  # Редактирование уже записанной книги
    try:
        eid = input('Enter book ID')
        fin_book = []
        if eid.isalnum():
            book = get_book(eid)
            stbook = ''
            for i in book:
                stbook = stbook + ' ' + i
            print(stbook)
            fin_book.append(input('New name: '))
            fin_book.append(input('New author: '))
            fin_book.append(input('New year of issue: '))
            fin_book.append(input('New date: '))
            fin_book.append(input('New comment: '))
            for i in range(5):
                fin_book[i] = comma_check(fin_book[i])
                fin_book[i] = empty_check(fin_book[i])
            fin = eid + ', ' + ', '.join(fin_book) + '\n'
            data[int(eid)] = fin
            list_to_csv()
        else:
            print('Enter only numbers!!!')
    except TypeError:
        print('Enter only numbers!!!')


def back_database():  # Запись из основной базы данных (books.csv) в промежуточную (test.csv)
    file = open('books.csv', 'r')
    dat = open('test.csv', 'w')
    dat.write(file.read())
    file.close()
    dat.close()


def save_database():  # Запись из промежуточной базы данных (test.csv) в основную (books.csv)
    file = open('test.csv', 'r')
    dat = open('books.csv', 'w')
    dat.write(file.read())
    file.close()
    dat.close()


def delete():  # Удаление книги
    try:
        eid = input('Enter book ID')
        if eid.isalnum():
            data.remove(','.join(get_book(eid)))
            list_to_csv()
        else:
            print('Enter only numbers!!!')
    except TypeError:
        print('Enter only numbers!!!')


def menu():  # Меню вызова функций
    global access_level, log1
    while True:
        print('1-Account')
        print('2-Show all books')
        print('3-Add new book')
        print('4-Edit')
        print('5-Delete')
        print('6-Back to save')
        print('0-Exit')
        try:
            ask = int(input(''))
            open_file()
            if ask == 1:
                if access_level <= 1:
                    print('1-Login')
                    print('2-Register')
                    ask2 = int(input())
                    if ask2 == 1:
                        login()
                    elif ask2 == 2:
                        register()
                else:
                    print('You logged as ' + str(log1))
                    print('Your access level is ' + str(access_level))
                    print('1-Exit from account')
                    print('Any other number to exit from menu')
                    if access_level >= 5:  # Админ-панель
                        print('513-Admin Panel')
                    ask3 = int(input())
                    if ask3 == 1:
                        access_level = 1
                        log1 = ''
                    if access_level >= 5 and ask3 == 513:
                        print('1-Set an access to account')
                        print('2-Delete account')
                        ask4 = int(input())
                        if ask4 == 1:
                            set_access()
                        if ask4 == 2:
                            delete_account()
            if ask == 2:
                if access_level >= 1:
                    show_all()
                else:
                    print('Required access level: 1. Your access level: ' + str(access_level))
            if ask == 3:
                if access_level >= 2:
                    new_book()
                else:
                    print('Required access level: 2. Your access level: ' + str(access_level))
            if ask == 4:
                if access_level >= 3:
                    edit()
                else:
                    print('Required access level: 3. Your access level: ' + str(access_level))
            if ask == 5:
                if access_level >= 4:
                    delete()
                else:
                    print('Required access level: 4. Your access level: ' + str(access_level))
            if ask == 6:
                if access_level >= 4:
                    back_database()
                else:
                    print('Required access level: 4. Your access level: ' + str(access_level))
            if ask == 0:
                save_database()
                break
            open_file()
            id_sort('test.csv')
        except ValueError:
            print('Enter only numbers!!')
