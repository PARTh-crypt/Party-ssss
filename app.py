        from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>PARTH'S KISAN SAATHI</title>

        <style>
            body {
                margin: 0;
                background: linear-gradient(to bottom, #0f0f0f, #1c1c1c, #0a0a0a);
                font-family: 'Times New Roman', serif;
                overflow: hidden;
                color: #e0d3b8;
            }

            .center-text {
                position: absolute;
                width: 100%;
                text-align: center;
                top: 45%;
                opacity: 0;
                animation: fadeIn 2s ease forwards 2s;
            }

            h1 {
                font-size: 50px;
                letter-spacing: 4px;
                margin: 0;
            }

            p {
                font-size: 18px;
                margin-top: 15px;
                color: #bfae90;
            }

            .bow {
                position: absolute;
                bottom: 10%;
                left: 50%;
                transform: translateX(-50%);
                font-size: 80px;
                color: #bfa46f;
            }

            .arrow {
                position: absolute;
                bottom: 18%;
                left: 50%;
                transform: translateX(-50%);
                font-size: 40px;
                color: #d4b77d;
                animation: shootUp 2s ease forwards;
            }

            @keyframes shootUp {
                0% { bottom: 18%; opacity: 1; }
                90% { opacity: 1; }
                100% { bottom: 110%; opacity: 0; }
            }

            @keyframes fadeIn {
                to { opacity: 1; }
            }

        </style>
    </head>

    <body>

        <div class="bow">🏹</div>
        <div class="arrow">➶</div>

        <div class="center-text">
            <h1>PARTH'S KISAN SAATHI</h1>
            <p>Royal Farming Intelligence System</p>
        </div>

    </body>
    </html>
    """
