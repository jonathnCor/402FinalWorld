import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Spdude77@', db='menagerie')
c = conn.cursor()


def display_data():
    c.execute('SELECT name, birth, MONTH(birth) FROM pet')
    databases = c.fetchall()
    for database in databases:
        print(database)


def main():
    display_data()


main()
