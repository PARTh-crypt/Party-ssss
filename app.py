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

/* --- Body & Background --- */
body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(135deg, #a8e063, #56ab2f, #87ceeb, #fff176);
    background-size: 400% 400%;
    animation: bgMove 15s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
    text-align: center;
    overflow: hidden;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* --- Bow + Arrow --- */
.bow {
    position: absolute;
    bottom: 15%;
    left: 50%;
    transform: translateX(-50%);
    width: 180px;
    height: auto;
}

.arrow {
    position: absolute;
    bottom: 22%;
    left: 50%;
    transform: translateX(-50%);
    width: 16px;
    height: 120px;
    background: linear-gradient(to top, #ffb74d, #ffd54f);
    clip-path: polygon(50% 0%, 60% 10%, 55% 10%, 60% 20%, 55% 20%, 50% 30%, 45% 20%, 40% 20%, 45% 10%, 40% 10%);
    animation: shoot 2.2s ease forwards;
}

@keyframes shoot {
    0% { bottom: 22%; opacity: 1; }
    90% { opacity: 1; }
    100% { bottom: 130%; opacity: 0; }
}

/* --- Headings & Text --- */
h1 {
    font-size: 56px;
    margin-top: 20px;
    font-weight: 700;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}

h2 {
    font-size: 28px;
    margin-top: 8px;
    opacity: 0.9;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.2);
}

/* --- Footer --- */
.footer {
    position: absolute;
    bottom: 15px;
    right: 20px;
    font-size: 14px;
    color: #ffffffcc;
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

<!-- Bow placeholder (CSS/SVG could be enhanced later) -->
<img class="bow" src="https://i.imgur.com/ZlO3lMa.png" alt="Bow">

<!-- Animated arrow -->
<div class="arrow"></div>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>Sabka Smart Saathi</h2>

<button class="enter-btn">Enter App</button>

<div class="footer">Powered by PARTH'S INDUSTRIES</div>

</body>
</html>
"""
