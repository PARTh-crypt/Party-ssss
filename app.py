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
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* --- Cinematic Farm Light Streaks --- */
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

<!-- Cinematic farm streaks -->
<div class="streak" style="bottom:0; left:10%; animation-delay:0s;"></div>
<div class="streak" style="bottom:0; left:25%; animation-delay:1s;"></div>
<div class="streak" style="bottom:0; left:40%; animation-delay:2s;"></div>
<div class="streak" style="bottom:0; left:55%; animation-delay:3s;"></div>
<div class="streak" style="bottom:0; left:70%; animation-delay:4s;"></div>
<div class="streak" style="bottom:0; left:85%; animation-delay:5s;"></div>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi</h2>

<button class="enter-btn">Enter App</button>

<div class="footer">Powered by PARTH'S</div>

</body>
</html>
"""
from flask import Flask, render_template_string

app = Flask(__name__)

# --- Landing Page ---
@app.route("/")
def home():
    return render_template_string("""
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
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* --- Cinematic Farm Streaks Animation --- */
.streak {
    position: absolute;
    width: 3px;
    height: 60px;
    background: linear-gradient(to top, rgba(255,223,107,0.7), rgba(255,243,175,0));
    border-radius: 50%;
    animation: floatStreak 8s linear infinite;
}

@keyframes floatStreak {
    0% {transform: translateY(0) translateX(0) rotate(0deg);}
    50% {transform: translateY(-120vh) translateX(30px) rotate(10deg);}
    100% {transform: translateY(0) translateX(-30px) rotate(-10deg);}
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
    color: #000000; 
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

<!-- Cinematic farm streaks -->
<div class="streak" style="bottom:0; left:10%; animation-delay:0s;"></div>
<div class="streak" style="bottom:0; left:25%; animation-delay:1s;"></div>
<div class="streak" style="bottom:0; left:40%; animation-delay:2s;"></div>
<div class="streak" style="bottom:0; left:55%; animation-delay:3s;"></div>
<div class="streak" style="bottom:0; left:70%; animation-delay:4s;"></div>
<div class="streak" style="bottom:0; left:85%; animation-delay:5s;"></div>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi / Every Farmer's Digital Companion</h2>

<button class="enter-btn" onclick="location.href='/dashboard'">Enter App / ऐप में प्रवेश करें</button>

<div class="footer">Powered by PARTH'S</div>

</body>
</html>
""")

# --- Dashboard with Language Toggle ---
@app.route("/dashboard")
def dashboard():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN DASHBOARD</title>
<style>
body {font-family: Arial, sans-serif; text-align:center; background:#f0fff0; margin:0;}
h1 {font-size:40px; color:#2f6f2f; margin-top:30px;}
.tool-btn {padding:12px 30px; margin:15px; font-size:18px; border:none; border-radius:15px; background:#a8e063; cursor:pointer;}
.tool-btn:hover {background:#56ab2f; color:#fff; transform:scale(1.05);}
.lang-btn {position:absolute; top:15px; right:20px; padding:8px 15px; cursor:pointer; border-radius:10px; background:#fdd835; font-weight:bold;}
</style>

<script>
function setLanguage(lang){
    const labels = {
        'title': {'en':'PARTH\'S KISAN SAATHI - Dashboard', 'hi':'पार्थ का किसान साथी - डैशबोर्ड'},
        'weather': {'en':'🌤 Weather Info', 'hi':'🌤 मौसम जानकारी'},
        'crop': {'en':'🌱 Crop Advice', 'hi':'🌱 फसल सलाह'},
        'bill': {'en':'🧾 Bill Maker', 'hi':'🧾 बिल बनाने वाला'},
        'voice': {'en':'🎤 Voice Commands', 'hi':'🎤 वॉइस कमांड'}
    };
    document.getElementById('title').innerText = labels.title[lang];
    document.getElementById('weather').innerText = labels.weather[lang];
    document.getElementById('crop').innerText = labels.crop[lang];
    document.getElementById('bill').innerText = labels.bill[lang];
    document.getElementById('voice').innerText = labels.voice[lang];
}
</script>
</head>
<body>

<h1 id="title">PARTH'S KISAN SAATHI - Dashboard</h1>

<button class="tool-btn" id="weather" onclick="alert('Weather tool coming soon / मौसम उपकरण जल्द आ रहा है')">🌤 Weather Info</button>
<button class="tool-btn" id="crop" onclick="alert('Crop Advice tool coming soon / फसल सलाह उपकरण जल्द आ रहा है')">🌱 Crop Advice</button>
<button class="tool-btn" id="bill" onclick="alert('Bill Maker tool coming soon / बिल बनाने वाला जल्द आ रहा है')">🧾 Bill Maker</button>
<button class="tool-btn" id="voice" onclick="alert('Voice Assistant coming soon / वॉइस असिस्टेंट जल्द आ रहा है')">🎤 Voice Commands</button>

<!-- Language Toggle -->
<button class="lang-btn" onclick="setLanguage('en')">English</button>
<button class="lang-btn" style="right:120px;" onclick="setLanguage('hi')">हिंदी</button>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- Landing Page ---
@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body {margin:0; height:100vh; background: linear-gradient(135deg,#c8facc,#a8e063,#87ceeb,#fff176); background-size:400% 400%; animation:bgMove 20s ease infinite; display:flex; justify-content:center; align-items:center; flex-direction:column; font-family:'Montserrat',sans-serif; text-align:center; color:#ffffff; overflow:hidden;}
@keyframes bgMove {0%{background-position:0% 50%;}50%{background-position:100% 50%;}100%{background-position:0% 50%;}}
.streak{position:absolute;width:3px;height:60px;background:linear-gradient(to top,rgba(255,223,107,0.7),rgba(255,243,175,0));border-radius:50%;animation:floatStreak 8s linear infinite;}
@keyframes floatStreak {0%{transform:translateY(0) translateX(0) rotate(0deg);}50%{transform:translateY(-120vh) translateX(30px) rotate(10deg);}100%{transform:translateY(0) translateX(-30px) rotate(-10deg);}}
h1{font-family:'Playfair Display',serif;font-size:56px;margin-top:20px;font-weight:700;text-shadow:2px 2px 8px rgba(0,0,0,0.3);}
h2{font-family:'Montserrat',sans-serif;font-size:28px;margin-top:8px;opacity:0.95;text-shadow:1px 1px 4px rgba(0,0,0,0.25);}
.footer{position:absolute;bottom:15px;right:20px;font-family:'Playfair Display',serif;font-size:16px;color:#000000;}
.enter-btn{margin-top:40px;padding:14px 50px;border-radius:30px;border:none;background:linear-gradient(45deg,#fdd835,#fbc02d);color:#2f6f2f;font-weight:bold;cursor:pointer;box-shadow:0 4px 15px rgba(0,0,0,0.2);transition:0.3s;}
.enter-btn:hover{transform:scale(1.08);box-shadow:0 6px 20px rgba(0,0,0,0.3);}
</style>
</head>
<body>
<div class="streak" style="bottom:0; left:10%; animation-delay:0s;"></div>
<div class="streak" style="bottom:0; left:25%; animation-delay:1s;"></div>
<div class="streak" style="bottom:0; left:40%; animation-delay:2s;"></div>
<div class="streak" style="bottom:0; left:55%; animation-delay:3s;"></div>
<div class="streak" style="bottom:0; left:70%; animation-delay:4s;"></div>
<div class="streak" style="bottom:0; left:85%; animation-delay:5s;"></div>
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi / Every Farmer's Digital Companion</h2>
<button class="enter-btn" onclick="location.href='/dashboard'">Enter App / ऐप में प्रवेश करें</button>
<div class="footer">Powered by PARTH'S INDUSTRIES</div>
</body>
</html>
""")

# --- Dashboard with Farmer Tools & Language Toggle ---
@app.route("/dashboard")
def dashboard():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN DASHBOARD</title>
<style>
body {font-family: Arial, sans-serif; text-align:center; background:#f0fff0; margin:0;}
h1 {font-size:40px; color:#2f6f2f; margin-top:30px;}
.tool-btn {padding:12px 30px; margin:15px; font-size:18px; border:none; border-radius:15px; background:#a8e063; cursor:pointer;}
.tool-btn:hover {background:#56ab2f; color:#fff; transform:scale(1.05);}
.lang-btn {position:absolute; top:15px; right:20px; padding:8px 15px; cursor:pointer; border-radius:10px; background:#fdd835; font-weight:bold;}
</style>
<script>
function setLanguage(lang){
    const labels = {
        'title': {'en':'PARTH\'S KISAN SAATHI - Dashboard', 'hi':'पार्थ का किसान साथी - डैशबोर्ड'},
        'weather': {'en':'🌤 Weather Info', 'hi':'🌤 मौसम जानकारी'},
        'crop': {'en':'🌱 Crop Advice', 'hi':'🌱 फसल सलाह'},
        'bill': {'en':'🧾 Bill Maker', 'hi':'🧾 बिल बनाने वाला'},
        'voice': {'en':'🎤 Voice Commands', 'hi':'🎤 वॉइस कमांड'}
    };
    document.getElementById('title').innerText = labels.title[lang];
    document.getElementById('weather').innerText = labels.weather[lang];
    document.getElementById('crop').innerText = labels.crop[lang];
    document.getElementById('bill').innerText = labels.bill[lang];
    document.getElementById('voice').innerText = labels.voice[lang];
}
function voiceCommand() {
    alert("Voice Assistant coming soon / वॉइस असिस्टेंट जल्द आ रहा है");
}
</script>
</head>
<body>
<h1 id="title">PARTH'S KISAN SAATHI - Dashboard</h1>
<button class="tool-btn" id="weather" onclick="alert('Weather tool coming soon / मौसम उपकरण जल्द आ रहा है')">🌤 Weather Info</button>
<button class="tool-btn" id="crop" onclick="alert('Crop Advice tool coming soon / फसल सलाह उपकरण जल्द आ रहा है')">🌱 Crop Advice</button>
<button class="tool-btn" id="bill" onclick="alert('Bill Maker tool coming soon / बिल बनाने वाला जल्द आ रहा है')">🧾 Bill Maker</button>
<button class="tool-btn" id="voice" onclick="voiceCommand()">🎤 Voice Commands</button>
<button class="lang-btn" onclick="setLanguage('en')">English</button>
<button class="lang-btn" style="right:120px;" onclick="setLanguage('hi')">हिंदी</button>
</body>
</html>
""")
    from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ------------------- Dashboard -------------------
@app.route("/dashboard")
def dashboard():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN DASHBOARD</title>
<style>
body {font-family:Arial,sans-serif; text-align:center; background:#f0fff0; margin:0; padding:50px;}
h1 {font-size:36px; color:#2f6f2f;}
button {margin:12px; padding:14px 32px; border-radius:20px; border:none; font-size:18px; cursor:pointer; font-weight:bold; color:#fff; transition:0.3s;}
button:hover {transform:scale(1.05);}
#weather-btn{background:linear-gradient(45deg,#4fc3f7,#0288d1);}
#crop-btn{background:linear-gradient(45deg,#aed581,#7cb342);}
#bill-btn{background:linear-gradient(45deg,#ffd54f,#ffa000);}
#voice-btn{background:linear-gradient(45deg,#ff8a65,#d84315);}
</style>
</head>
<body>
<h1>PARTH'S KISAN DASHBOARD</h1>

<button id="weather-btn" onclick="getWeather()">🌤️ Weather</button>
<button id="crop-btn" onclick="getCropAdvice()">🌱 Crop Advice</button>
<button id="bill-btn" onclick="getBill()">🧾 Bill Maker</button>
<button id="voice-btn" onclick="voiceAssistant()">🎙️ Voice</button>

<script>
function getWeather(){
    fetch('/weather-api')
    .then(res=>res.json())
    .then(data=>alert("Temperature: "+data.temp+"°C\\nCondition: "+data.condition))
    .catch(()=>alert("Weather info not available"));
}

function getCropAdvice(){
    fetch('/crop-api')
    .then(res=>res.json())
    .then(data=>alert(data.advice))
    .catch(()=>alert("Crop advice not available"));
}

function getBill(){
    fetch('/bill-api')
    .then(res=>res.json())
    .then(data=>alert("Total Bill: ₹"+data.total))
    .catch(()=>alert("Bill calculation failed"));
}

function voiceAssistant(){
    let cmd = prompt("Enter your command / अपना कमांड लिखें");
    if(!cmd) return;
    fetch('/voice-api',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({command:cmd})
    })
    .then(res=>res.json())
    .then(data=>alert(data.response))
    .catch(()=>alert("Voice assistant not available"));
}
</script>
</body>
</html>
""")

# ------------------- Flask routes for buttons -------------------
@app.route("/weather-api")
def weather_api():
    return {"temp":32, "condition":"Sunny / धूप"}

@app.route("/crop-api")
def crop_api():
    return {"advice":"Recommended Crops: Rice, Wheat, Maize / सुझाई गई फसलें: धान, गेहूं, मक्का"}

@app.route("/bill-api")
def bill_api():
    items = [{"item":"Seed","qty":2,"price":50},{"item":"Fertilizer","qty":1,"price":100}]
    total = sum(item['qty']*item['price'] for item in items)
    return {"total": total}

@app.route("/voice-api", methods=["POST"])
def voice_api():
    command = request.json.get("command","").lower()
    if "weather" in command:
        return {"response":"Weather info: Sunny / धूप"}
    elif "crop" in command:
        return {"response":"Crop Advice: Rice / धान"}
    elif "bill" in command:
        return {"response":"Total Bill: ₹200"}
    else:
        return {"response":"Command not recognized / कमांड समझ नहीं आई"}

# ------------------- Run server -------------------
if __name__=="__main__":
    app.run(debug=True)
