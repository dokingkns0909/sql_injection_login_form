from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    return f'<h1>Welcome, {name}!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
