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
    <html>
    <head>
        <title>AWS DevOps App</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
            }}
            .navbar {{
                background: #1e293b;
                padding: 15px;
                display: flex;
                justify-content: space-between;
            }}
            .logo {{
                font-weight: bold;
                font-size: 20px;
            }}
            .menu a {{
                color: white;
                margin: 0 15px;
                text-decoration: none;
            }}
            .container {{
                margin-top: 40px;
            }}
            .cards {{
                display: grid;
                grid-template-columns: repeat(5, 1fr);
                gap: 15px;
                padding: 20px;
            }}
            .card {{
                background: #1e293b;
                padding: 20px;
                border-radius: 10px;
                transition: 0.3s;
            }}
            .card:hover {{
                background: #334155;
                transform: scale(1.05);
            }}
        </style>
    </head>

    <body>

        <div class="navbar">
            <div class="logo">🚀 AWS DevOps App</div>
            <div class="menu">
                <a href="#">Home</a>
                <a href="#">Menu</a>
                <a href="#">Settings</a>
                <a href="#">Login</a>
            </div>
        </div>

        <div class="container">
            <h2>🔥 Hello World (Python)</h2>
            <p>Running on Port 5000</p>
            <p>Uptime: {elapsed()}</p>
        </div>

        <h3>☁️ AWS Services</h3>

        <div class="cards">
            <div class="card">EC2</div>
            <div class="card">S3</div>
            <div class="card">Lambda</div>
            <div class="card">RDS</div>
            <div class="card">CloudWatch</div>
            <div class="card">IAM</div>
            <div class="card">VPC</div>
            <div class="card">EKS</div>
            <div class="card">ECS</div>
            <div class="card">Route53</div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
