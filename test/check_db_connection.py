import mysql.connector


connection = mysql.connector.connect(host="94.125.123.247", database="addressbook2", user="super", password="Tyco12345!")


try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()