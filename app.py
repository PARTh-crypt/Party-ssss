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
    background: linear-gradient(180deg, #a8e063, #87ceeb, #ffffff, #fff176);
    background-size: 400% 400%;
    animation: bgMove 25s ease infinite;
    color:white;
    display:flex;
    justify-content:flex-start;
    align-items:center;
    flex-direction:column;
    min-height:100vh;
    text-align:center;
    overflow-x:hidden;
}

@keyframes bgMove {
    0% {background-position: 0% 0%;}
    50% {background-position: 0% 100%;}
    100% {background-position: 0% 0%;}
}

.overlay{
    background:rgba(0,0,0,0.3);
    padding:30px;
    width:90%;
    max-width:500px;
    border-radius:20px;
    margin-top:20px;
}

/* Headings */
h1{ font-family:'Playfair Display', serif; font-size:48px; margin:0; padding:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.4); }
h2{ font-size:24px; margin:0; padding:5px; text-shadow:1px 1px 6px rgba(0,0,0,0.3); }

/* Buttons */
.cat-btn{
    margin:12px auto;
    padding:18px 30px;
    border-radius:25px;
    border:none;
    background:rgba(255,255,255,0.25);
    color:white;
    font-weight:bold;
    font-size:20px;
    cursor:pointer;
    text-shadow:1px 1px 3px rgba(0,0,0,0.4);
    transition:0.3s;
    width:80%;
}
.cat-btn:hover{
    background:rgba(255,255,255,0.45);
    transform:scale(1.05);
}

.button-container{
    margin-top:30px;
    display:flex;
    flex-direction:column;
    justify-content:center;
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
    <button class="cat-btn" onclick="alert('Category 9 – Harvesting & Post-Harvest Planning / कटाई और पोस्ट-हार्वेस्ट योजना')">🌾 Harvesting / कटाई</button>
    <button class="cat-btn" onclick="alert('Category 10 – Essential Farm Operations / जरूरी खेत संचालन')">🛠️ Farm Operations / खेत संचालन</button>
    <button class="cat-btn" onclick="alert('Category 11 – Reminders & Notes / रिमाइंडर & नोट्स')">📌 Reminders & Notes / रिमाइंडर & नोट्स</button>
</div>
</div>
</body>
</html>
"""
    from flask import Flask, render_template_string, request

app = Flask(__name__)

# ------------------ CATEGORY 1 DATA ------------------
category1_tools = [
    {
        "name": "🌾 Soil Type Analyzer / मिट्टी प्रकार विश्लेषक",
        "theory": "Soil type affects crop growth. Sandy soil drains quickly, clay retains water, loamy is ideal.",
        "practical": "Upload soil photo to identify texture.",
    },
    {
        "name": "💧 Moisture Detector / नमी पता लगाने वाला",
        "theory": "Soil moisture determines irrigation need. Overwatering harms crops.",
        "practical": "Enter soil moisture % or attach photo of soil surface.",
    },
    {
        "name": "🌤 Sunlight Checker / धूप मापने वाला",
        "theory": "Crops need sunlight. Too little sunlight reduces yield.",
        "practical": "Check sunlight hours at field; use camera photo of field shadow.",
    },
    {
        "name": "🌱 Germination Helper / अंकुरण सहायता",
        "theory": "Seeds require optimum water, soil and temperature to germinate.",
        "practical": "Enter seed type & moisture; app advises best method.",
    },
    {
        "name": "🧴 Fertilizer Advisor / उर्वरक सलाहकार",
        "theory": "Proper fertilizer improves yield; excess harms soil.",
        "practical": "Enter crop type & soil condition; app recommends fertilizer.",
    },
    {
        "name": "🛠️ Crop Maintenance Tips / फसल रखरखाव सुझाव",
        "theory": "Regular weeding, pruning, pest checks improve growth.",
        "practical": "Upload field photo; app highlights areas to care.",
    },
    {
        "name": "🚜 Planting Scheduler / रोपाई समय सारणी",
        "theory": "Planting at right season increases yield.",
        "practical": "Enter crop & local season; app suggests sowing date.",
    },
    {
        "name": "📝 Growth Tracker / विकास ट्रैकर",
        "theory": "Track plant height, leaf color for healthy growth.",
        "practical": "Enter weekly observations; app advises interventions.",
    },
    {
        "name": "💨 Wind Exposure Advisor / हवा के प्रभाव की सलाह",
        "theory": "Wind can damage crops; use shelter or fencing.",
        "practical": "Enter location & crop; app suggests precautions.",
    },
    {
        "name": "🌾 Harvesting Guide / फसल कटाई मार्गदर्शक",
        "theory": "Harvest at peak maturity for best yield.",
        "practical": "Enter crop type & visual photo; app advises harvest time.",
    },
]

# ------------------ DASHBOARD ------------------
@app.route("/")
def dashboard():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI - Dashboard</title>
<style>
body{
    font-family:sans-serif;
    margin:0; padding:0;
    background: linear-gradient(135deg,#87ceeb,#a8e063,#ffffff,#fff176);
    min-height:100vh;
    display:flex; justify-content:center; align-items:flex-start;
}
.overlay{
    background:rgba(0,0,0,0.3); padding:20px; width:90%; margin-top:20px;
}
h1,h2{text-align:center;color:white;text-shadow:1px 1px 4px #000;}
.button-container{
    display:flex; flex-direction:column; align-items:center; gap:12px; margin-top:20px;
}
.cat-btn{
    width:80%; padding:15px; font-size:18px; border:none; border-radius:20px;
    background:rgba(255,255,255,0.25); color:white; cursor:pointer;
    text-align:left; transition:0.3s;
}
.cat-btn:hover{background:rgba(255,255,255,0.45); transform:scale(1.03);}
</style>
<script>
function openCategory(url){
    window.location.href = url;
}
</script>
</head>
<body>
<div class="overlay">
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Dashboard / डैशबोर्ड</h2>
<div class="button-container">
    <button class="cat-btn" onclick="openCategory('/category1')">🌾 Category 1 – Crop Management / फ़सल प्रबंधन</button>
    <button class="cat-btn" onclick="alert('Category 2 – Irrigation Management / सिंचाई प्रबंधन')">💧 Category 2</button>
    <button class="cat-btn" onclick="alert('Category 3 – Pest & Disease Control / कीट एवं रोग नियंत्रण')">🦠 Category 3</button>
    <button class="cat-btn" onclick="alert('Category 4 – Organic & AI Farming / ऑर्गेनिक & एआई खेती')">🌱 Category 4</button>
    <button class="cat-btn" onclick="alert('Category 5 – Fertilizer Planning / उर्वरक योजना')">🧴 Category 5</button>
    <button class="cat-btn" onclick="alert('Category 6 – Seed Management / बीज प्रबंधन')">🌾 Category 6</button>
    <button class="cat-btn" onclick="alert('Category 7 – Profit & Yield Tracking / लाभ & उत्पादन ट्रैकिंग')">📊 Category 7</button>
    <button class="cat-btn" onclick="alert('Category 8 – Smart Farming Tools / स्मार्ट खेती उपकरण')">💻 Category 8</button>
    <button class="cat-btn" onclick="alert('Category 9 – Crop Calendar / फ़सल कैलेंडर')">📅 Category 9</button>
    <button class="cat-btn" onclick="alert('Category 10 – Farm Maintenance / खेत रखरखाव')">🛠️ Category 10</button>
    <button class="cat-btn" onclick="alert('Category 11 – Reminders & Notes / रिमाइंडर & नोट्स')">📌 Category 11</button>
</div>
</div>
</body>
</html>
""")

# ------------------ CATEGORY 1 PAGE ------------------
@app.route("/category1", methods=["GET", "POST"])
def category1():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>Category 1 – Crop Management</title>
<style>
body{font-family:sans-serif; margin:0; padding:0; background:#87ceeb; color:#000;}
.container{padding:20px; max-width:900px; margin:auto;}
h1,h2{text-align:center;}
.tool-card{background:rgba(255,255,255,0.8); padding:15px; margin:15px 0; border-radius:15px;}
textarea,input{width:100%; padding:8px; margin:5px 0; border-radius:8px;}
button{padding:10px 20px; border:none; border-radius:15px; background:#4caf50; color:white; cursor:pointer;}
</style>
</head>
<body>
<div class="container">
<h1>🌾 Category 1 – Crop Management / फ़सल प्रबंधन</h1>
<h2>Select a tool / टूल चुनें</h2>
{% for tool in tools %}
<div class="tool-card">
<h3>{{tool.name}}</h3>
<p><b>Theory / सिद्धांत:</b> {{tool.theory}}</p>
<p><b>Practical / व्यावहारिक:</b> {{tool.practical}}</p>
</div>
{% endfor %}
</div>
</body>
</html>
""", tools=category1_tools)

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)
