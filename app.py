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
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ==============================
# Category 1 – Crop Management Tools
# ==============================

# 1️⃣ Soil Type Identifier
soil_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🌱 Soil Type Identifier / मिट्टी प्रकार पहचान</h3>
<p><b>Theory / सिद्धांत:</b> मिट्टी की पहचान से फ़सल और उर्वरक का सही चयन आसान होता है।</p>
<p><b>Practical / प्रयोग:</b> खेत से मिट्टी की फोटो लें और नीचे upload करें। App बताएगा मिट्टी का type।</p>
<form action="/analyze_soil" method="post" enctype="multipart/form-data">
<input type="file" name="soil_photo" accept="image/*" required>
<button type="submit">Analyze / विश्लेषण करें</button>
</form>
</div>
"""

# 2️⃣ Water Requirement Checker
water_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>💧 Water Requirement Checker / पानी की आवश्यकता जांच</h3>
<p><b>Theory / सिद्धांत:</b> फ़सल को सही मात्रा में पानी देने से उत्पादन बेहतर होता है।</p>
<p><b>Practical / प्रयोग:</b> खेत की फोटो या नमी देखकर input दें। App बताएगा पानी की आवश्यकता।</p>
<form method="post" action="/check_water">
<label>Soil Moisture % / मिट्टी नमी %:</label>
<input type="number" name="moisture" min="0" max="100" required>
<button type="submit">Check / जाँच करें</button>
</form>
</div>
"""

# 3️⃣ Fertilizer Suggestion
fert_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🧴 Fertilizer Suggestion / उर्वरक सुझाव</h3>
<p><b>Theory / सिद्धांत:</b> सही उर्वरक से फ़सल उत्पादन बढ़ता है।</p>
<p><b>Practical / प्रयोग:</b> फ़सल का नाम डालें और App बताएगा recommended fertilizer।</p>
<form method="post" action="/fert_suggest">
<label>Crop Name / फ़सल का नाम:</label>
<input type="text" name="crop" required>
<button type="submit">Get Suggestion / सुझाव देखें</button>
</form>
</div>
"""

# 4️⃣ Pest Identifier
pest_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🐛 Pest Identifier / कीट पहचान</h3>
<p><b>Theory / सिद्धांत:</b> फ़सल में कीट का समय पर पता लगाने से नुकसान कम होता है।</p>
<p><b>Practical / प्रयोग:</b> पौधे की फोटो upload करें। App बताएगा कीट का नाम और नियंत्रण।</p>
<form action="/analyze_pest" method="post" enctype="multipart/form-data">
<input type="file" name="pest_photo" accept="image/*" required>
<button type="submit">Analyze / विश्लेषण करें</button>
</form>
</div>
"""

# 5️⃣ Growth Stage Tracker
growth_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🌿 Growth Stage Tracker / वृद्धि चरण ट्रैकर</h3>
<p><b>Theory / सिद्धांत:</b> फ़सल की वृद्धि चरण जानना फ़सल प्रबंधन के लिए जरूरी है।</p>
<p><b>Practical / प्रयोग:</b> पौधे की फोटो भेजें, App बताएगा stage और next steps।</p>
<form action="/analyze_growth" method="post" enctype="multipart/form-data">
<input type="file" name="growth_photo" accept="image/*" required>
<button type="submit">Analyze / विश्लेषण करें</button>
</form>
</div>
"""

# 6️⃣ Harvest Time Predictor
harvest_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🌾 Harvest Time Predictor / कटाई समय अनुमान</h3>
<p><b>Theory / सिद्धांत:</b> सही समय पर कटाई से गुणवत्ता और उत्पादन बेहतर होता है।</p>
<p><b>Practical / प्रयोग:</b> फ़सल की फोटो upload करें। App बताएगा कटाई का समय।</p>
<form action="/analyze_harvest" method="post" enctype="multipart/form-data">
<input type="file" name="harvest_photo" accept="image/*" required>
<button type="submit">Analyze / विश्लेषण करें</button>
</form>
</div>
"""

# 7️⃣ Soil PH Checker
ph_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🧪 Soil PH Checker / मिट्टी पीएच जांच</h3>
<p><b>Theory / सिद्धांत:</b> पीएच संतुलन से फ़सल की वृद्धि और उर्वरक प्रभाव बढ़ता है।</p>
<p><b>Practical / प्रयोग:</b> मिट्टी की फोटो या manual input दें। App बताएगा PH level।</p>
<form method="post" action="/check_ph">
<label>PH Value / पीएच मान:</label>
<input type="number" name="ph" step="0.1" required>
<button type="submit">Check / जाँच करें</button>
</form>
</div>
"""

# 8️⃣ Sunlight Requirement
sun_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>☀ Sunlight Requirement / धूप की आवश्यकता</h3>
<p><b>Theory / सिद्धांत:</b> फ़सल की सही धूप से वृद्धि बेहतर होती है।</p>
<p><b>Practical / प्रयोग:</b> खेत की फोटो भेजें। App बताएगा sunlight adequacy।</p>
<form action="/check_sunlight" method="post" enctype="multipart/form-data">
<input type="file" name="sun_photo" accept="image/*" required>
<button type="submit">Analyze / विश्लेषण करें</button>
</form>
</div>
"""

# 9️⃣ Weed Detection
weed_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🌾 Weed Detection / खरपतवार पहचान</h3>
<p><b>Theory / सिद्धांत:</b> खेत से खरपतवार हटाने से फ़सल सुरक्षित रहती है।</p>
<p><b>Practical / प्रयोग:</b> खेत की फोटो upload करें। App बताएगा weeds और control।</p>
<form action="/analyze_weed" method="post" enctype="multipart/form-data">
<input type="file" name="weed_photo" accept="image/*" required>
<button type="submit">Analyze / विश्लेषण करें</button>
</form>
</div>
"""

# 🔟 Crop Disease Checker
disease_tool_html = """
<div style='margin:15px;padding:15px;background:rgba(255,255,255,0.15);border-radius:15px;text-align:left;'>
<h3>🦠 Crop Disease Checker / फ़सल रोग जांच</h3>
<p><b>Theory / सिद्धांत:</b> रोग पहचान से फ़सल की सुरक्षा सुनिश्चित होती है।</p>
<p><b>Practical / प्रयोग:</b> पौधे की फोटो upload करें। App बताएगा रोग और नियंत्रण।</p>
<form action="/analyze_disease" method="post" enctype="multipart/form-data">
<input type="file" name="disease_photo" accept="image/*" required>
<button type="submit">Analyze / विश्लेषण करें</button>
</form>
</div>
"""

# Combine all tools
tools_html = soil_tool_html + water_tool_html + fert_tool_html + pest_tool_html + growth_tool_html + harvest_tool_html + ph_tool_html + sun_tool_html + weed_tool_html + disease_tool_html

@app.route("/category1")
def category1():
    return render_template_string("""
<html>
<head><title>Category 1 – Crop Management</title></head>
<body style="font-family:Arial;background:#87ceeb;padding:20px;">
<h1>🌾 Crop Management / फ़सल प्रबंधन</h1>
{{ tools|safe }}
</body>
</html>
""", tools=tools_html)


# ==============================
# Example server-side logic for placeholder analysis
# ==============================
@app.route("/analyze_soil", methods=["POST"])
def analyze_soil():
    return "<h2>Soil Type: Loamy / दोमट मिट्टी</h2><a href='/category1'>⬅ Back</a>"

@app.route("/check_water", methods=["POST"])
def check_water():
    moisture = int(request.form.get("moisture",0))
    if moisture < 40:
        msg = "Water Needed / पानी चाहिए"
    else:
        msg = "Water Sufficient / पानी पर्याप्त है"
    return f"<h2>{msg}</h2><a href='/category1'>⬅ Back</a>"

@app.route("/fert_suggest", methods=["POST"])
def fert_suggest():
    crop = request.form.get("crop","Unknown")
    return f"<h2>Recommended Fertilizer for {crop}: Nitrogen-based / {crop} के लिए नाइट्रोजन आधारित उर्वरक</h2><a href='/category1'>⬅ Back</a>"

@app.route("/analyze_pest", methods=["POST"])
def analyze_pest():
    return "<h2>Pest Identified: Aphids / कीट: एफिड्स</h2><a href='/category1'>⬅ Back</a>"

@app.route("/analyze_growth", methods=["POST"])
def analyze_growth():
    return "<h2>Growth Stage: Vegetative / वृद्धि चरण: पत्तेदार</h2><a href='/category1'>⬅ Back</a>"

@app.route("/analyze_harvest", methods=["POST"])
def analyze_harvest():
    return "<h2>Harvest Time: 5-7 days / कटाई का समय: 5-7 दिन</h2><a href='/category1'>⬅ Back</a>"

@app.route("/check_ph", methods=["POST"])
def check_ph():
    ph = float(request.form.get("ph",7))
    return f"<h2>Soil PH: {ph}</h2><a href='/category1'>⬅ Back</a>"

@app.route("/check_sunlight", methods=["POST"])
def check_sunlight():
    return "<h2>Sunlight Adequacy: Sufficient / धूप पर्याप्त है</h2><a href='/category1'>⬅ Back</a>"

@app.route("/analyze_weed", methods=["POST"])
def analyze_weed():
    return "<h2>Weeds Detected / खरपतवार पाया गया</h2><a href='/category1'>⬅ Back</a>"

@app.route("/analyze_disease", methods=["POST"])
def analyze_disease():
    return "<h2>Disease Detected: Fungal / रोग: फंगल</h2><a href='/category1'>⬅ Back</a>"
