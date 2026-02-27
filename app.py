from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(135deg, #c8facc, #a8e063, #87ceeb, #fff176);
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
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}
.streak {
    position: absolute;
    width: 3px;
    height: 60px;
    background: linear-gradient(to top, rgba(255,223,107,0.7), rgba(255,243,175,0.0));
    border-radius: 50%;
    animation: floatStreak 8s linear infinite;
}
@keyframes floatStreak {
    0% {transform: translateY(0) translateX(0) rotate(0deg);}
    50% {transform: translateY(-120vh) translateX(30px) rotate(10deg);}
    100% {transform: translateY(0) translateX(-30px) rotate(-10deg);}
}
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
.footer {
    position: absolute;
    bottom: 15px;
    right: 20px;
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    color: #000000;
}
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

<!-- Cinematic streaks -->
<div class="streak" style="bottom:0; left:10%; animation-delay:0s;"></div>
<div class="streak" style="bottom:0; left:25%; animation-delay:1s;"></div>
<div class="streak" style="bottom:0; left:40%; animation-delay:2s;"></div>
<div class="streak" style="bottom:0; left:55%; animation-delay:3s;"></div>
<div class="streak" style="bottom:0; left:70%; animation-delay:4s;"></div>
<div class="streak" style="bottom:0; left:85%; animation-delay:5s;"></div>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>हर किसान का डिजिटल साथी / Har Kisan Ka Digital Saathi</h2>

<button class="enter-btn" onclick="alert('Next screen loading...')">Enter App</button>

<div class="footer">Powered by PARTH'S</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
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

# ==========================
# Dashboard Screen
# ==========================
@app.route("/dashboard")
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI - Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: url('https://images.unsplash.com/photo-1500530855697-b586d89ba3ee') no-repeat center center fixed;
    background-size: cover;
    color:white;
    display:flex;
    justify-content:center;
    align-items:flex-start;
    flex-direction:column;
    min-height:100vh;
    text-align:center;
}
.overlay{
    background:rgba(0,0,0,0.4);
    padding:30px;
    width:100%;
}
h1{
    font-family:'Playfair Display', serif;
    font-size:48px;
    margin:0;
    padding:10px;
    text-shadow:2px 2px 8px rgba(0,0,0,0.4);
}
h2{
    font-size:24px;
    margin:0;
    padding:5px;
    text-shadow:1px 1px 6px rgba(0,0,0,0.3);
}
</style>
</head>
<body>
<div class="overlay">
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Dashboard / डैशबोर्ड</h2>
</div>
</body>
</html>
"""
@app.route("/dashboard")
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI - Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg, #a8e063, #fdd835); /* Colour background */
    color:white;
    display:flex;
    justify-content:center;
    align-items:flex-start;
    flex-direction:column;
    min-height:100vh;
    text-align:center;
}
.overlay{
    background:rgba(0,0,0,0.4);
    padding:30px;
    width:100%;
}
h1{ font-family:'Playfair Display', serif; font-size:48px; margin:0; padding:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.4); }
h2{ font-size:24px; margin:0; padding:5px; text-shadow:1px 1px 6px rgba(0,0,0,0.3); }

/* --- Category Buttons --- */
.cat-btn{
    margin:15px;
    padding:20px 40px;
    border-radius:25px;
    border:none;
    background:rgba(255,255,255,0.2);
    color:white;
    font-weight:bold;
    font-size:18px;
    cursor:pointer;
    text-shadow:1px 1px 3px rgba(0,0,0,0.4);
    transition:0.3s;
}
.cat-btn:hover{
    background:rgba(255,255,255,0.4);
    transform:scale(1.05);
}
.button-container{
    margin-top:50px;
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
}
</style>
</head>
<body>
<div class="overlay">
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Dashboard / डैशबोर्ड</h2>

<div class="button-container">
    <button class="cat-btn" onclick="alert('Category 1 – Crop Management / फ़सल प्रबंधन')">🌾 Crop Management / फ़सल प्रबंधन</button>
    <button class="cat-btn" onclick="alert('Category 2 – Irrigation Management / सिंचाई प्रबंधन')">💧 Irrigation Management / सिंचाई प्रबंधन</button>
    <button class="cat-btn" onclick="alert('Category 3 – Pest & Disease Control / कीट एवं रोग नियंत्रण')">🦠 Pest & Disease Control / कीट एवं रोग नियंत्रण</button>
    <button class="cat-btn" onclick="alert('Category 4 – Organic & AI Farming / ऑर्गेनिक & एआई खेती')">🌱 Organic & AI Farming / ऑर्गेनिक & एआई खेती</button>
    <button class="cat-btn" onclick="alert('Category 5 – Fertilizer Planning / उर्वरक योजना')">🧴 Fertilizer Planning / उर्वरक योजना</button>
    <button class="cat-btn" onclick="alert('Category 6 – Seed Management / बीज प्रबंधन')">🌾 Seed Management / बीज प्रबंधन</button>
</div>
</div>
</body>
</html>
"""
