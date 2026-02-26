from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTHS KISAN SAATHI</title>
<style>
body {
    margin: 0;
    background: #111;
    font-family: Georgia, serif;
    color: #d6c2a5;
    overflow: hidden;
}

.bow {
    position: absolute;
    bottom: 12%;
    left: 50%;
    transform: translateX(-50%);
    font-size: 60px;
}

.arrow {
    position: absolute;
    bottom: 18%;
    left: 50%;
    transform: translateX(-50%);
    font-size: 30px;
    animation: shoot 2s ease forwards;
}

@keyframes shoot {
    from { bottom: 18%; opacity: 1; }
    to { bottom: 110%; opacity: 0; }
}

.title {
    position: absolute;
    width: 100%;
    top: 45%;
    text-align: center;
    opacity: 0;
    animation: fade 2s forwards 2s;
}

@keyframes fade {
    to { opacity: 1; }
}
</style>
</head>

<body>

<div class="bow">V</div>
<div class="arrow">|</div>

<div class="title">
    <h1>PARTHS KISAN SAATHI</h1>
    <p>Royal Farming Intelligence</p>
</div>

</body>
</html>
"""
