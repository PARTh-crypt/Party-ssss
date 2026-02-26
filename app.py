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
    background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
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
    bottom: 12%;
    left: 50%;
    transform: translateX(-50%);
    width: 160px;
}

.arrow {
    position: absolute;
    bottom: 20%;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    animation: shoot 2.2s ease forwards;
}

@keyframes shoot {
    0% { bottom: 20%; opacity: 1; }
    90% { opacity: 1; }
    100% { bottom: 120%; opacity: 0; }
}

/* --- Headings & Text --- */
h1 {
    font-size: 52px;
    margin-top: 20px;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
}

p {
    margin-top: 12px;
    font-size: 20px;
    opacity: 0.9;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.2);
}

/* --- Button --- */
.enter-btn {
    margin-top: 40px;
    padding: 14px 45px;
    border-radius: 30px;
    border: none;
    background: linear-gradient(45deg, #ff9a9e, #fad0c4);
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

<!-- Ready-to-use bow + arrow placeholders -->
<img class="bow" src="https://i.imgur.com/ZlO3lMa.png" alt="Bow">
<img class="arrow" src="https://i.imgur.com/5v4g2NW.png" alt="Arrow">

<h1>PARTH'S KISAN SAATHI</h1>
<p>Smart Farming. Better Future.</p>

<button class="enter-btn">Enter App</button>

</body>
</html>
"""
