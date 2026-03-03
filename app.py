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
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI - Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg, #87ceeb, #a8e063, #fff176, #ffffff);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white;
    display:flex;
    justify-content:center;
    align-items:flex-start;
    flex-direction:column;
    min-height:100vh;
    text-align:center;
    padding-top:40px;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.overlay{
    background:rgba(0,0,0,0.35);
    padding:30px;
    width:100%;
    max-width:500px;
    margin:auto;
    border-radius:15px;
}

/* Headings */
h1{ font-family:'Playfair Display', serif; font-size:48px; margin:0; padding:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.4); }
h2{ font-size:24px; margin:0; padding:5px; text-shadow:1px 1px 6px rgba(0,0,0,0.3); }

/* Buttons vertical */
.cat-btn{
    margin:12px 0;
    padding:18px 30px;
    border-radius:25px;
    border:none;
    background:rgba(255,255,255,0.25);
    color:white;
    font-weight:bold;
    font-size:18px;
    cursor:pointer;
    text-shadow:1px 1px 3px rgba(0,0,0,0.4);
    transition:0.3s;
    width:100%;
}
.cat-btn:hover{
    background:rgba(255,255,255,0.45);
    transform:scale(1.03);
}

.button-container{
    margin-top:30px;
    display:flex;
    flex-direction:column;
    align-items:center;
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
    <button class="cat-btn" onclick="alert('Category 7 – Profit & Yield Tracking / लाभ & उत्पादन ट्रैकिंग')">📊 Profit & Yield Tracking / लाभ & उत्पादन ट्रैकिंग</button>
    <button class="cat-btn" onclick="alert('Category 8 – Smart Farming Tools / स्मार्ट खेती उपकरण')">💻 Smart Farming Tools / स्मार्ट खेती उपकरण</button>
    <button class="cat-btn" onclick="alert('Category 9 – Harvesting & Guidance / कटाई & मार्गदर्शन')">🌾 Harvesting & Guidance / कटाई & मार्गदर्शन</button>
    <button class="cat-btn" onclick="alert('Category 10 – Soil & Crop Care / मिट्टी & फ़सल देखभाल')">🛠️ Soil & Crop Care / मिट्टी & फ़सल देखभाल</button>
    <button class="cat-btn" onclick="alert('Category 11 – Reminders & Notes / रिमाइंडर & नोट्स')">📌 Reminders & Notes / रिमाइंडर & नोट्स</button>
</div>
</div>
</body>
</html>
"""
    @app.route("/category1")
def category1():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Crop Management / फ़सल प्रबंधन</title>
<style>
body{
margin:0;
font-family:Arial;
background: linear-gradient(135deg, #87ceeb, #a8e063, #fff176);
color:white;
text-align:center;
min-height:100vh;
padding-bottom:50px;
}
h1{margin-top:30px;}
.section{
background:rgba(0,0,0,0.35);
margin:20px auto;
padding:20px;
border-radius:20px;
width:85%;
}
button{
padding:12px 20px;
margin:10px;
border:none;
border-radius:25px;
cursor:pointer;
font-weight:bold;
background:white;
color:black;
}
button:hover{
background:#ddd;
}
.option-btn{
display:block;
width:80%;
margin:10px auto;
}
</style>

<script>
function showTheory(){
document.getElementById("content").innerHTML = `
<h3>Theory / सिद्धांत</h3>
<p><b>Soil Types / मिट्टी के प्रकार:</b></p>
<p>1. Sandy Soil – पानी जल्दी निकल जाता है / Water drains quickly</p>
<p>2. Clay Soil – पानी रुकता है / Holds water</p>
<p>3. Loamy Soil – खेती के लिए सबसे अच्छी / Best for farming</p>
`;
}

function showPractical(){
document.getElementById("content").innerHTML = `
<h3>Practical / प्रयोग</h3>
<p><b>Q1: आपकी मिट्टी कैसी लगती है?</b></p>
<p><b>How does your soil feel?</b></p>

<button class="option-btn" onclick="answer1('sandy')">
रेतीली (Sandy)
</button>

<button class="option-btn" onclick="answer1('clay')">
चिकनी (Clay)
</button>

<button class="option-btn" onclick="answer1('loamy')">
मिश्रित (Loamy)
</button>
`;
}

function answer1(type){
if(type=="sandy"){
document.getElementById("content").innerHTML =
"<h3>Result</h3><p>आपकी मिट्टी रेतीली है। मूंगफली, तरबूज उगा सकते हैं।</p><p>Your soil is Sandy. Groundnut, Watermelon are suitable.</p>";
}
if(type=="clay"){
document.getElementById("content").innerHTML =
"<h3>Result</h3><p>आपकी मिट्टी चिकनी है। धान, गेहूं उगा सकते हैं।</p><p>Your soil is Clay. Rice, Wheat are suitable.</p>";
}
if(type=="loamy"){
document.getElementById("content").innerHTML =
"<h3>Result</h3><p>आपकी मिट्टी दोमट है। अधिकतर फसलें उग सकती हैं।</p><p>Your soil is Loamy. Most crops grow well.</p>";
}
}
</script>

</head>
<body>

<h1>🌾 Crop Management / फ़सल प्रबंधन</h1>

<div class="section">
<h2>Tool 1: Soil Type Identification / मिट्टी पहचान</h2>

<button onclick="showTheory()">Theory / सिद्धांत</button>
<button onclick="showPractical()">Practical / प्रयोग</button>

<div id="content"></div>

</div>

</body>
</html>
"""
