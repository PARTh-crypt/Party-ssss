from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">

<style>

/* --- Body & Gradient Background --- */
body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(135deg, #a8e063, #56ab2f, #87ceeb, #fff176);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-family: 'Montserrat', sans-serif;
    text-align: center;
    overflow: hidden;
    color: #ffffff;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* --- Cinematic Light Streak Animation --- */
.light-streak {
    position: absolute;
    width: 200%;
    height: 4px;
    background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.4) 50%, rgba(255,255,255,0) 100%);
    top: 30%;
    left: -100%;
    transform: rotate(25deg);
    animation: streakMove 5s linear infinite;
}

@keyframes streakMove {
    0% {left: -100%;}
    100% {left: 100%;}
}

/* --- Headings & Text --- */
h1 {
    font-family: 'Playfair Display', serif;
    font-size: 56px;
    margin-top: 20px;
    font-weight: 700;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}

h2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 28px;
    margin-top: 8px;
    opacity: 0.95;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.25);
}

/* --- Footer --- */
.footer {
    position: absolute;
    bottom: 15px;
    right: 20px;
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    color: #000000; /* black royal */
}

/* --- Button --- */
.enter-btn {
    margin-top: 40px;
    padding: 14px 50px;
    border-radius: 30px;
    border: none;
    background: linear-gradient(45deg, #fdd835, #fbc02d);
    color: #2f6f2f;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transition: 0.3s;
}

.enter-btn:hover {
    transform: scale(1.08);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

</style>
</head>

<body>

<!-- Cinematic Light Streak -->
<div class="light-streak"></div>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi</h2>

<button class="enter-btn">Enter App</button>

<div class="footer">Powered by PARTH'S INDUSTRIES</div>

</body>
</html>
"""
