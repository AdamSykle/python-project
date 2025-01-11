from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, CI/CD Pipeline!"

@app.route('/time')
def current_time():
    now = datetime.now()
    return f"Current time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
