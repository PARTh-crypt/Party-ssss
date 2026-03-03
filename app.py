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
from flask import Flask, request

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return """
    <h1>🌾 PARTH'S KISAN SAATHI</h1>
    <a href='/dashboard'><button>Enter App</button></a>
    """

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    return """
    <h2>Dashboard / डैशबोर्ड</h2>
    <a href='/category1'><button>🌾 Crop Management</button></a>
    """

# ---------------- CATEGORY 1 ----------------
@app.route("/category1")
def category1():
    return """
    <h2>Crop Management / फ़सल प्रबंधन</h2>

    <h3>Tool 1: Soil Type Identification</h3>

    <a href='/theory1'><button>Theory / सिद्धांत</button></a>
    <a href='/practical1'><button>Practical / प्रयोग</button></a>
    """

# ---------------- THEORY ----------------
@app.route("/theory1")
def theory1():
    return """
    <h3>Theory / सिद्धांत</h3>

    <p>Sandy Soil – पानी जल्दी निकलता है</p>
    <p>Clay Soil – पानी रुकता है</p>
    <p>Loamy Soil – खेती के लिए सर्वोत्तम</p>

    <a href='/category1'><button>Back</button></a>
    """

# ---------------- PRACTICAL ----------------
@app.route("/practical1")
def practical1():
    return """
    <h3>Practical Question</h3>
    <p>How does your soil feel?</p>

    <a href='/result1?type=sandy'><button>रेतीली / Sandy</button></a>
    <a href='/result1?type=clay'><button>चिकनी / Clay</button></a>
    <a href='/result1?type=loamy'><button>दोमट / Loamy</button></a>
    """

# ---------------- RESULT ----------------
@app.route("/result1")
def result1():
    soil = request.args.get("type")

    if soil == "sandy":
        msg = "Sandy Soil: Groundnut, Watermelon suitable."
    elif soil == "clay":
        msg = "Clay Soil: Rice, Wheat suitable."
    elif soil == "loamy":
        msg = "Loamy Soil: Most crops suitable."
    else:
        msg = "Invalid selection."

    return f"""
    <h3>Result</h3>
    <p>{msg}</p>
    <a href='/category1'><button>Back</button></a>
    """

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run()
