from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = "YOU ARE NOT ADMIN ~_~"  # Default message
    username = ""
    password = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        conn.set_trace_callback(print)
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        print(f"Executing query: {query}") 

        try:
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                message = "HELLO ADMIN!"
        except sqlite3.OperationalError as e:
            print(f"SQLite error: {e}")
        finally:
            cursor.close()
            conn.close()

    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Login</title>
  <style>
      /* Add your CSS here */
      body {
          background: #0e0e0e;
          font-family: Courier New;
          color: #00ff00;
      }
      .container {
          display: flex;
          flex-direction: column;
          align-items: center;
          height: 100vh;
      }
      .card {
         width: 600px;
         padding: 20px;
         border-radius: 12px;
         background-color: #222;
         box-shadow: 0px 2px 5px rgba(0, 255, 0, .2);
     }
     pre {
         color: #00ff00;
     }
     label {
         color: #00ff00;
     }
     input[type=text], input[type=password] {
       border: none;
       outline: none;
       background-color: #333;
       color: #00ff00;
       padding: 10px;
       margin-bottom: 10px;
   }
   button[type=submit] {
    background-color: #333;
    color: #00ff00;
    outline: none;
    border: none;
    padding: 10px;
   }
   .message {
    color: #ff0000;
    margin-top: 10px;
   }
   .admin-message {
    color: #00ff00;
    margin-top: 10px;
   }
</style>
</head>
<body>
<div class="container">
   <!-- SQL Query -->
   <pre>SELECT * FROM users WHERE username='{{username}}' AND password='{{password}}'</pre>

   <!-- Login Form -->
   <div class="card">
      <!-- Message -->
      {% if message %}
        <div class="{% if 'ADMIN' in message %}admin-message{% else %}message{% endif %}">
          {{ message }}
        </div>
      {% endif %}

      <!-- Form -->
      <form method="post">
          <!-- Username Field -->
          <label for="username">Username</label>
          <input type="text" id="username" name="username" placeholder="Username" autocomplete="off">

          <!-- Password Field -->
          <label for="password">Password</label>
          <input type="password" id="password" name="password" placeholder="Password" autocomplete="off">

          <!-- Submit Button -->
          <button type="submit">Login</button>
      </form>
   </div>
</div>
</body>
</html>
""", message=message, username=username, password=password)

if __name__ == "__main__":
    app.run(debug=True)

