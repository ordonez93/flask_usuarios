import mysql.connector
DB = mysql.connector.connect(
    host='localhost',
    user ='root',
    password='12523',
    database='encuestas',
    port=3306
)
def getAllUsers():
    cursor = DB.cursor(dictionary=True)
    cursor.execute('select * from usuarios')
    return cursor.fetchall()
