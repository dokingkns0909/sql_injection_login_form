from flask import Flask, request
import sqlite3

app = Flask(__name__)

# 데이터베이스 연결 함수
def connect_db():
    return sqlite3.connect('users.db')

# 로그인 엔드포인트
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        cursor = conn.cursor()

        # WARNING: Do not use this in real applications.
        # This is vulnerable to SQL Injection attacks.
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
       # URL 파라미터를 통해 데이터베이스에 데이터를 요청하는 코드
       username = request.args.get('username')
       password = request.args.get('password')

       conn=connect_db()
       cursor=conn.cursor()

      # WARNING: Do not use this in real applications.
      # This is vulnerable to SQL Injection attacks.
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
