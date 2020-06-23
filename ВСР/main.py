import sqlite3
import functools

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called: 
            result = func(*args, **kwargs)
            inner.called = True # ? 
            print('called is changed')
        return result            
    inner.called = False 
    return inner 
@once
def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            connection = sqlite3.connect(
                'file:' + path_to_db + '?mode=rw', uri=True)
            # connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]

def get_users_from_table(conn, table):
    sql_query = "SELECT * FROM " + str(table)
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    users_lst = res.fetchall()
    #print(users_lst)

    return users_lst

def check(f):
    @functools.wraps(f)
    def wrapper():
    # он должен в себе содержать: 
    # ввод с клавиатуры или получения из другого источника 
    # логина и пароля 

    # получение из БД пользователя с тем логином, который был введен

    # сверка пароля введенного пользователем с паролем, хранящемся в БД

    # если успех и аутентификация прошла успешно, показываем 

    # если нет, то показать надпись пользователю о том, пользователя с таким паролем - нет
        login = input('Введите логин\n')
        pswd = input('Введите пароль\n')
        res = cur.execute("SELECT * FROM users where login = ?", (login,))
        login_check = res.fetchone()
        #print(login_check)
        if login_check:
            if login_check[1] == pswd:
                print(f())
                global user_role
                user_role = login_check[2]
                #return user_role
            else:
                print("You have entered the wrong password")
        else:
            print("No such user exists")
    return wrapper


@check
def private_zone_area():
    return "private_zone_area"


# 2 вариант
try:
    sql_query = '''CREATE TABLE users
             (login text, pass text, role int)'''
    cur.execute(sql_query)
except sqlite3.OperationalError as e:
    e_str = str(e)

    if ("already exists" in e_str):
        print(f' NOTICE: {e}. CONTINUE ')

        sql_query = '''INSERT INTO users VALUES (?, ?, ?)'''
        
        users_lst = [('root', '123', 0), ('admin', '789', 1), ('user', 'qwe', 2)]
        try:
            cur.executemany(sql_query, users_lst)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error with adding users to db. {e}')


users = get_users_from_table(conn, 'users')            

private_zone_area()
print(user_role)
conn.close()
cur, conn = None, None
