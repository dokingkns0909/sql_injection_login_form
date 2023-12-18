from flask import Flask, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('users.db')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        
        cursor.execute(query)

        user = cursor.fetchone()

        conn.close()

        if user:
            message="HELLO ADMIN!"
            return f"""
                <html>
                <body style='background-color:black; color:lime; font-family: Courier New'>
                    <h1>{message}</h1>
                    <p>Executed query:</p>
                    <pre>{query}</pre>
                </body>
                </html>"""
            
    else:
       username = request.args.get('username')
       password = request.args.get('password')

       conn=connect_db()
       cursor=conn.cursor()

    query=f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
       
    cursor.execute(query)

    user=cursor.fetchone()

    conn.close()

    if user:
         message="HELLO ADMIN!"
    else:
         message="YOU ARE NOT ADMIN ~_~"

    return f"""
             <html>
             <body style='background-color:black; color:lime; font-family: Courier New'>
                 <h1>{message}</h1>
                 <p>Executed query:</p>
                 <pre>{query}</pre>
             </body>
             </html>"""

if __name__ == '__main__':
   app.run(debug=True)
