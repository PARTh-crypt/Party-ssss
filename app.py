from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>PARTH KISAN SAATHI</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298, #43e97b, #38f9d7);
                background-size: 400% 400%;
                animation: gradient 12s ease infinite;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
                text-align: center;
            }

            @keyframes gradient {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            .box {
                background: rgba(0,0,0,0.4);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
            }

            h1 {
                font-size: 38px;
                margin-bottom: 10px;
            }

            p {
                font-size: 18px;
                margin-bottom: 20px;
            }

            button {
                padding: 12px 25px;
                border: none;
                border-radius: 25px;
                font-size: 16px;
                cursor: pointer;
                background: #00ffcc;
                color: black;
                font-weight: bold;
            }

            button:hover {
                background: white;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🌾 PARTH KISAN SAATHI</h1>
            <p>AI Powered Farming Assistant for Smart Farmers</p>
            <button onclick="alert('AI Panel Coming Soon 🚀')">Enter App</button>
        </div>
    </body>
    </html>
    """
