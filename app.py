from flask import Flask

app = Flask(__name__)

# ==========================
# Starting Screen
# ==========================
@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    height:100vh;
    background: url('https://images.unsplash.com/photo-1500382017468-9049fed747ef') no-repeat center center fixed;
    background-size: cover;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    font-family: 'Montserrat', sans-serif;
    text-align:center;
    color:white;
}

h1 {
    font-family: 'Playfair Display', serif;
    font-size:56px;
    margin:10px;
    text-shadow:2px 2px 8px rgba(0,0,0,0.3);
}

h2 {
    font-size:28px;
    margin:5px;
    text-shadow:1px 1px 4px rgba(0,0,0,0.25);
}

.enter-btn{
    margin-top:30px;
    padding:14px 40px;
    border-radius:25px;
    border:none;
    background:linear-gradient(45deg,#fdd835,#fbc02d);
    color:#2f6f2f;
    font-weight:bold;
    cursor:pointer;
}
.enter-btn:hover{
    transform:scale(1.05);
}
</style>
</head>
<body>
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi</h2>
<button class="enter-btn" onclick="window.location.href='/dashboard'">Enter App / ऐप में प्रवेश करें</button>
</body>
</html> 
"""
@app.route("/dashboard")
def dashboard():
    return """
    <html>
    <head>
    <style>
    body{
        margin:0;
        font-family:Montserrat;
        background: linear-gradient(135deg,#1e3c72,#2a5298);
        color:white;
        text-align:center;
    }
    h1{
        padding-top:40px;
    }
    .card{
        width:80%;
        margin:30px auto;
        padding:30px;
        border-radius:15px;
        background:rgba(255,255,255,0.2);
        font-size:22px;
        cursor:pointer;
    }
    a{
        text-decoration:none;
        color:white;
    }
    </style>
    </head>
    <body>

    <h1>Farmer Dashboard<br>किसान डैशबोर्ड</h1>

    <a href="/crop">
        <div class="card">
            🌾 Crop Management<br>
            फसल प्रबंधन
        </div>
    </a>

    </body>
    </html>
    """
