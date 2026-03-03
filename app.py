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
# ================= CROP MANAGEMENT (FINAL) =================

@app.route("/category1")
def category1():
    return """
    <style>
    body{
        background: linear-gradient(135deg,#1d976c,#93f9b9);
        font-family: Arial;
        text-align:center;
        color:white;
    }
    h2{margin-top:20px;}
    .card{
        background: rgba(255,255,255,0.15);
        margin:12px;
        padding:18px;
        border-radius:15px;
    }
    button{
        padding:14px 20px;
        margin:6px;
        border:none;
        border-radius:10px;
        font-size:15px;
        cursor:pointer;
        background:#ffeb3b;
    }
    a{color:white;text-decoration:none;}
    </style>

    <h2>🌾 Crop Management / फसल प्रबंधन</h2>

    <div class='card'>
        <a href='/tool/1'><button>🌧 Rain Help / बारिश सलाह</button></a>
        <a href='/tool/2'><button>🌡 Weather Help / मौसम सलाह</button></a>
        <a href='/tool/3'><button>🌱 Soil Check / मिट्टी जांच</button></a>
        <a href='/tool/4'><button>🐛 Pest Help / कीट सलाह</button></a>
        <a href='/tool/5'><button>🌾 Harvest Time / कटाई समय</button></a>
        <a href='/tool/6'><button>💧 Water Advice / पानी सलाह</button></a>
        <a href='/tool/7'><button>🌿 Next Crop / अगली फसल</button></a>
        <a href='/tool/8'><button>🧴 Fertilizer Help / खाद सलाह</button></a>
        <a href='/tool/9'><button>💰 Sell or Wait / बेचें या रोकें</button></a>
        <a href='/tool/10'><button>🌱 Plant Health / पौधा स्थिति</button></a>
    </div>
    """


@app.route("/tool/<tool_id>")
def tool(tool_id):

    theme = """
    <style>
    body{
        background: linear-gradient(135deg,#0f2027,#2c5364);
        font-family: Arial;
        text-align:center;
        color:white;
    }
    button{
        padding:15px 25px;
        margin:10px;
        border:none;
        border-radius:12px;
        font-size:16px;
        cursor:pointer;
        background:#00ffcc;
    }
    a{color:white;text-decoration:none;}
    </style>
    """

    tools = {
        "1": "🌧 क्या बारिश हो रही है? / Is it raining?",
        "2": "🌡 क्या बहुत गर्मी है? / Is it very hot?",
        "3": "🌱 मिट्टी सूखी लग रही है? / Soil looks dry?",
        "4": "🐛 क्या कीड़े दिख रहे हैं? / Seeing pests?",
        "5": "🌾 दाने सख्त हो गए? / Grains hard?",
        "6": "💧 खेत सूखा है? / Field dry?",
        "7": "🌿 पिछली फसल गेहूं थी? / Last crop wheat?",
        "8": "🧴 पत्ते पीले हैं? / Leaves yellow?",
        "9": "💰 बाजार भाव अच्छा है? / Market price good?",
        "10": "🌱 पौधा हरा दिख रहा है? / Plant looks green?"
    }

    yes_answer = {
        "1": "अच्छी पैदावार होगी 🌾 / Good yield",
        "2": "ज्यादा पानी दें 💦 / Give more water",
        "3": "आज पानी दें 💧 / Irrigate today",
        "4": "जैविक स्प्रे करें 🌿 / Spray organic",
        "5": "कटाई करें ✂ / Harvest now",
        "6": "पानी दें 💦 / Irrigate",
        "7": "अब दाल बोएं 🌱 / Grow pulses",
        "8": "नाइट्रोजन खाद दें / Add nitrogen",
        "9": "अभी बेचें 💵 / Sell now",
        "10": "फसल स्वस्थ 👍 / Crop healthy"
    }

    no_answer = {
        "1": "सिंचाई करें 💧 / Irrigate",
        "2": "सामान्य देखभाल करें 👍 / Normal care",
        "3": "अभी जरूरत नहीं / No need now",
        "4": "फसल सुरक्षित 👍 / Crop safe",
        "5": "अभी इंतजार करें ⏳ / Wait",
        "6": "अभी जरूरत नहीं / Not needed",
        "7": "मक्का बोएं 🌽 / Grow maize",
        "8": "सब ठीक 👍 / All good",
        "9": "रोक कर रखें ⏳ / Wait to sell",
        "10": "खाद/पानी जांचें 💧 / Check fertilizer"
    }

    if tool_id in tools:
        return theme + f"""
        <h2>{tools[tool_id]}</h2>
        <button onclick="alert('{yes_answer[tool_id]}')">हाँ / Yes</button>
        <button onclick="alert('{no_answer[tool_id]}')">नहीं / No</button>
        <br><br>
        <a href='/category1'>⬅ Back</a>
        """

    return "Invalid Tool"
    
