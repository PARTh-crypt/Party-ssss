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
# Dashboard
# ==========================
@app.route("/dashboard")
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
<style>
body{
    margin:0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(135deg,#4facfe,#43e97b);
    text-align:center;
    color:white;
}
h1{
    padding-top:30px;
}
.category-btn{
    width:80%;
    padding:20px;
    margin:25px;
    font-size:22px;
    border:none;
    border-radius:18px;
    background:white;
    color:#2f6f2f;
    font-weight:bold;
    cursor:pointer;
}
.category-btn:hover{
    transform:scale(1.05);
}
</style>
</head>
<body>

<h1>Dashboard / डैशबोर्ड</h1>

<button class="category-btn" onclick="window.location.href='/crop'">
🌾 Crop Management / फसल प्रबंधन
</button>

</body>
</html>
"""
    # ==========================
# Crop Management
# ==========================
@app.route("/crop")
def crop():
    return """
<!DOCTYPE html>
<html>
<head>
<style>
body{
    margin:0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(135deg,#11998e,#38ef7d);
    text-align:center;
    color:white;
}
h2{
    padding-top:20px;
}
.tool-btn{
    width:85%;
    padding:18px;
    margin:12px;
    font-size:18px;
    border:none;
    border-radius:15px;
    background:#fff176;
    color:#2f6f2f;
    font-weight:bold;
    cursor:pointer;
}
.tool-btn:hover{
    transform:scale(1.05);
}
</style>
</head>
<body>

<h2>Crop Tools / फसल उपकरण</h2>

<button class="tool-btn" onclick="window.location.href='/tool/1'">🌧 Rain Check / बारिश जांच</button>
<button class="tool-btn" onclick="window.location.href='/tool/2'">🌱 Plant Health / पौधा स्थिति</button>
<button class="tool-btn" onclick="window.location.href='/tool/3'">🐛 Pest Problem / कीट समस्या</button>
<button class="tool-btn" onclick="window.location.href='/tool/4'">💧 Water Need / पानी जरूरत</button>
<button class="tool-btn" onclick="window.location.href='/tool/5'">🌾 Harvest Time / कटाई समय</button>
<button class="tool-btn" onclick="window.location.href='/tool/6'">🌡 Temperature Effect / तापमान प्रभाव</button>
<button class="tool-btn" onclick="window.location.href='/tool/7'">🌤 Weather Advice / मौसम सलाह</button>
<button class="tool-btn" onclick="window.location.href='/tool/8'">🧪 Fertilizer Need / खाद जरूरत</button>
<button class="tool-btn" onclick="window.location.href='/tool/9'">🌿 Leaf Color Check / पत्ते रंग जांच</button>
<button class="tool-btn" onclick="window.location.href='/tool/10'">📦 Storage Advice / भंडारण सलाह</button>

</body>
</html>
"""
    # ==========================
# Tools Logic
# ==========================
@app.route("/tool/<int:id>")
def tool(id):

    questions = {
        1:"क्या बारिश हो रही है? / Is it raining?",
        2:"पौधा हरा दिख रहा है? / Plant green?",
        3:"कीड़े दिख रहे हैं? / Pests visible?",
        4:"खेत सूखा है? / Field dry?",
        5:"दाने सख्त हो गए? / Grains hard?",
        6:"बहुत गर्मी है? / Too hot?",
        7:"आसमान बादल है? / Cloudy sky?",
        8:"खाद डाली है? / Added fertilizer?",
        9:"पत्ते पीले हैं? / Leaves yellow?",
        10:"फसल सूखी है? / Crop dry?"
    }

    yes_ans = {
        1:"अच्छा है 🌾 / Good for crop",
        2:"फसल स्वस्थ 👍 / Crop healthy",
        3:"स्प्रे करें 🧴 / Spray medicine",
        4:"पानी दें 💧 / Irrigate",
        5:"कटाई करें ✂ / Harvest now",
        6:"पानी बढ़ाएं 💧 / Increase irrigation",
        7:"बारिश हो सकती है 🌧 / Rain possible",
        8:"अच्छा 👍 / Good",
        9:"खाद दें 🌱 / Add fertilizer",
        10:"भंडारण करें 📦 / Store now"
    }

    no_ans = {
        1:"सिंचाई करें 💧 / Irrigate",
        2:"खाद दें 🌱 / Add fertilizer",
        3:"फसल सुरक्षित 👍 / Crop safe",
        4:"अभी जरूरत नहीं / Not needed",
        5:"अभी इंतजार करें ⏳ / Wait",
        6:"ठीक है 👍 / Normal",
        7:"सिंचाई करें 💧 / Irrigate",
        8:"खाद डालें 🌱 / Add fertilizer",
        9:"ठीक है 👍 / Normal",
        10:"अभी इंतजार करें ⏳ / Wait"
    }

    return f"""
    <html>
    <head>
    <style>
    body{{
        margin:0;
        font-family:Montserrat;
        background: linear-gradient(135deg,#0f2027,#2c5364);
        text-align:center;
        color:white;
    }}
    h2{{padding-top:40px;}}
    .btn{{
        width:70%;
        padding:18px;
        margin:15px;
        font-size:20px;
        border:none;
        border-radius:15px;
        background:#00ffcc;
        cursor:pointer;
    }}
    </style>
    </head>
    <body>

    <h2>{questions.get(id,"Question")}</h2>

    <button class="btn" onclick="alert('{yes_ans.get(id,"")}')">हाँ / Yes</button>
    <button class="btn" onclick="alert('{no_ans.get(id,"")}')">नहीं / No</button>

    <br><br>
    <a href="/crop" style="color:white;">⬅ Back</a>

    </body>
    </html>
    """
