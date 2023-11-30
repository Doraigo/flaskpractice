from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'contrasena123',
    'database': 'flask',
}

def user_exists(cursor, name):
    cursor.execute("SELECT 1 FROM users WHERE name = %s", (name,))
    return cursor.fetchone() is not None

@app.route('/')
def index():

    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', users=users)

if __name__ == '__main__':

    setup_conn = mysql.connector.connect(**mysql_config)
    setup_cursor = setup_conn.cursor()

    setup_cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    setup_conn.commit()

    if not user_exists(setup_cursor, 'Sahid'):
        setup_cursor.execute("INSERT INTO users (name) VALUES ('Sahid')")

    if not user_exists(setup_cursor, 'Aldahir'):
        setup_cursor.execute("INSERT INTO users (name) VALUES ('Aldahir')")
    
    if not user_exists(setup_cursor, 'Oliver'):
        setup_cursor.execute("INSERT INTO users (name) VALUES ('Oliver')")
    
    if not user_exists(setup_cursor, 'Victor'):
        setup_cursor.execute("INSERT INTO users (name) VALUES ('Victor')")

    setup_conn.commit()

    setup_cursor.close()
    setup_conn.close()

    app.run(debug=True)