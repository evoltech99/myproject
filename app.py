from flask import Flask
import subprocess

app = Flask(__name__)

def fetch_google():
    result = subprocess.run(['curl', 'https://www.google.com'], capture_output=True, text=True)
    return result.stdout

@app.route('/')
def index():
    content = fetch_google()
    return content

if __name__ == "__main__":
    app.run(debug=True)
