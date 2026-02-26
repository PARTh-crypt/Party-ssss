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
    background: linear-gradient(135deg, #a8e063, #56ab2f, #87ceeb, #fff59d);
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

/* Bow + Arrow */
.bow {
    position: absolute;
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    width: 150px;
}

.arrow {
    position: absolute;
    bottom: 18%;
    left: 50%;
    transform: translateX(-50%);
    width: 70px;
    animation: shoot 2.2s ease forwards;
}

@keyframes shoot {
    0% { bottom: 18%; opacity: 1; }
    90% { opacity: 1; }
    100% { bottom: 120%; opacity: 0; }
}

h1 {
    font-size: 50px;
    margin-top: 20px;
}

p {
    margin-top: 10px;
    font-size: 18px;
    opacity: 0.9;
}

.enter-btn {
    margin-top: 35px;
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

<!-- Replace these URLs with your actual Gandiv bow and arrow PNG images -->
<img class="bow" src="https://i.imgur.com/your_bow_image.png" alt="Bow">
<img class="arrow" src="https://i.imgur.com/your_arrow_image.png" alt="Arrow">

<h1>PARTH'S KISAN SAATHI</h1>
<p>Smart Farming. Better Future.</p>

<button class="enter-btn">Enter App</button>

</body>
</html>
"""
