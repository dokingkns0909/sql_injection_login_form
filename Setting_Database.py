import sqlite3

conn = sqlite3.connect('webhacking.db')  # users.db 파일을ㄹ생성하거나 연결합니다.
cursor = conn.cursor()

# users 테이블을 생성합니다. 이미 존재한다면 아무런 작업도 수행하지 않습니다.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
''')

# 예시 사용자를 추가합니다. 이번에는 username과 password를 admin과 admin1로 설정했습니다.
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin1'))

conn.commit()  # 변경 사항을 커밋(저장)합니다.
conn.close()  # 연결을 닫습니다.
