from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>

<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&display=swap" rel="stylesheet">

<style>

body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(135deg, #56ab2f, #a8e063, #87ceeb);
    background-size: 300% 300%;
    animation: bgMove 12s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
    text-align: center;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.logo {
    font-size: 60px;
    margin-bottom: 20px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

h1 {
    font-size: 48px;
    margin: 0;
}

p {
    margin-top: 15px;
    font-size: 18px;
    opacity: 0.9;
}

.enter-btn {
    margin-top: 40px;
    padding: 14px 40px;
    border-radius: 30px;
    border: none;
    background: white;
    color: #2f6f2f;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

.enter-btn:hover {
    background: #f1f1f1;
    transform: scale(1.05);
}

</style>
</head>

<body>

<div class="logo">🏹</div>

<h1>PARTH'S KISAN SAATHI</h1>
<p>Smart Farming. Better Future.</p>

<button class="enter-btn">Enter App</button>

</body>
</html>
"""
