from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>

<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Poppins:wght@300;500&display=swap" rel="stylesheet">

<style>

body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(135deg, #1e1e2f, #2b2b45, #3a3a5f);
    background-size: 300% 300%;
    animation: bgMove 10s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    color: #e8d8b9;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1 {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    letter-spacing: 3px;
    margin: 0;
    text-align: center;
}

p {
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    margin-top: 15px;
    opacity: 0.8;
}

.enter-btn {
    margin-top: 40px;
    padding: 14px 35px;
    border: none;
    border-radius: 30px;
    background: #c5a46d;
    color: #1e1e2f;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s ease;
}

.enter-btn:hover {
    background: #e8d8b9;
    transform: scale(1.05);
}

</style>
</head>

<body>

<h1>PARTH'S KISAN SAATHI</h1>
<p>Royal Farming Intelligence System</p>

<button class="enter-btn">Enter Platform</button>

</body>
</html>
"""
