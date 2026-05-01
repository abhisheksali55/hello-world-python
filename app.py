import time
from flask import Flask

app = Flask(__name__)

START = time.time()

def elapsed():
    running = int(time.time() - START)
    hours = running // 3600
    minutes = (running % 3600) // 60
    seconds = running % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"

@app.route('/')
def home():
    return f"""
    <h2>🚀 Hello World (Python)</h2>
    <p>App is running on port 5000</p>
    <p>Uptime: {elapsed()}</p>
    """

if __name__ == "__main__":
    # 👇 Only port 5000
    app.run(host="0.0.0.0", port=5000)
