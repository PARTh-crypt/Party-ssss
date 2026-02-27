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
from flask import Flask

app = Flask(__name__)

# =============================
# Category 1 Tools – Crop Management
# =============================
category1_tools = [
    {"name": "Soil Type / मिट्टी का प्रकार", "theory": "Soil type affects crop growth. / मिट्टी का प्रकार फ़सल की वृद्धि को प्रभावित करता है।", "practical": "Take a soil sample photo and send. / मिट्टी का नमूना फोटो खींच कर भेजें।"},
    {"name": "Crop Rotation / फ़सल चक्र", "theory": "Rotate crops to improve soil fertility. / मिट्टी की उर्वरता बढ़ाने के लिए फ़सल बदलें।", "practical": "Select crops to rotate. / बदलने के लिए फ़सल चुनें।"},
    {"name": "Planting Time / रोपाई का समय", "theory": "Plant crops at the right season. / सही मौसम में फ़सल लगाएँ।", "practical": "Select crop and season. / फ़सल और मौसम चुनें।"},
    {"name": "Fertilizer Use / उर्वरक का उपयोग", "theory": "Use proper fertilizers for crops. / फ़सल के लिए सही उर्वरक का उपयोग करें।", "practical": "Upload soil report photo. / मिट्टी रिपोर्ट फोटो अपलोड करें।"},
    {"name": "Pest Monitoring / कीट निगरानी", "theory": "Monitor pests regularly. / कीटों की निगरानी करें।", "practical": "Upload pest affected plant photo. / प्रभावित पौधे का फोटो भेजें।"},
    {"name": "Irrigation Schedule / सिंचाई कार्यक्रम", "theory": "Maintain proper irrigation. / सही सिंचाई करें।", "practical": "Select field and water schedule. / खेत और पानी का समय चुनें।"},
    {"name": "Seed Selection / बीज चयन", "theory": "Choose high-quality seeds. / उच्च गुणवत्ता वाले बीज चुनें।", "practical": "Upload seed package photo. / बीज पैकेज का फोटो भेजें।"},
    {"name": "Harvesting Time / कटाई का समय", "theory": "Harvest at peak maturity. / फ़सल पकने पर काटें।", "practical": "Select crop and harvest date. / फ़सल और कटाई तारीख चुनें।"},
    {"name": "Weed Control / खरपतवार नियंत्रण", "theory": "Remove weeds regularly. / खरपतवार नियमित रूप से निकालें।", "practical": "Upload field photo. / खेत का फोटो भेजें।"},
    {"name": "Yield Prediction / उत्पादन अनुमान", "theory": "Estimate expected crop yield. / फ़सल की अनुमानित पैदावार का आकलन करें।", "practical": "Enter crop area & conditions. / फ़सल क्षेत्र और स्थिति दर्ज करें।"}
]
