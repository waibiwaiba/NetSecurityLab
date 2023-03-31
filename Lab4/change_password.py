import mysql.connector
import os

import scheme

if __name__ == '__main__':

    db = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='toor'
    )

    cur = db.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS lab5')
    cur.execute('USE lab5')
    # cur.execute('DROP TABLE user')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS user (
        username VARCHAR(32),
        password VARCHAR(128)
    )
    '''.strip())
    # cur.execute('DELETE * FROM user')
    username = input('Username:')
    password = input('Password:')
    password = scheme.sha512(username + password)
    cur.execute("SELECT password FROM user WHERE username = %s", (username,))
    result = cur.fetchone()

    # 检查输入的密码是否与数据库中存储的密码匹配
    if result and password == result[0]:
        # 提示用户输入新密码
        new_password = input('Enter new password:')
        # 对新密码进行哈希处理
        hashed_new_password = scheme.sha512(username + new_password)
        # 更新数据库中存储的密码
        cur.execute("UPDATE user SET password = %s WHERE username = %s", (hashed_new_password, username))
        db.commit()
        print("Password updated successfully!")
    else:
        print("Invalid username or password.")
        # cur.execute(f'INSERT INTO user (username, password) VALUES ("{username}", "{password}")')
        # db.commit()
