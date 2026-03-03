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
# ================= CATEGORY 1 – 10 REAL WORKING TOOLS (SAFE VERSION) =================
from flask import request

@app.route("/category1")
def category1():
    return """
    <h2>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h2>
    <a href='/tool/1'>1️⃣ Crop Yield Estimator</a><br><br>
    <a href='/tool/2'>2️⃣ Soil Nutrient Balancer</a><br><br>
    <a href='/tool/3'>3️⃣ Water Demand Calculator</a><br><br>
    <a href='/tool/4'>4️⃣ Irrigation Interval Predictor</a><br><br>
    <a href='/tool/5'>5️⃣ Crop Rotation Planner</a><br><br>
    <a href='/tool/6'>6️⃣ Pest Risk Score</a><br><br>
    <a href='/tool/7'>7️⃣ Growth Stage Advisor</a><br><br>
    <a href='/tool/8'>8️⃣ Harvest Time Predictor</a><br><br>
    <a href='/tool/9'>9️⃣ Fertilizer Efficiency Checker</a><br><br>
    <a href='/tool/10'>🔟 Profit Forecast Tool</a><br><br>
    <a href='/dashboard'>⬅ Back to Dashboard</a>
    """

# ================= TOOL ENGINE =================
@app.route("/tool/<tool_id>", methods=["GET","POST"])
def tools(tool_id):

    result = ""

    try:
        if request.method == "POST":

            if tool_id == "1":
                area = float(request.form.get("area",0))
                seed = float(request.form.get("seed",0))
                rain = float(request.form.get("rain",0))
                yield_est = area * seed * (rain / 500)
                result = f"🌾 Estimated Yield: {round(yield_est,2)} quintals"

            elif tool_id == "2":
                ph = float(request.form.get("ph",0))
                if ph < 6:
                    result = "🧪 Soil acidic → Add Lime + Compost"
                elif ph > 7.5:
                    result = "🧪 Soil alkaline → Add Organic manure"
                else:
                    result = "🧪 Soil balanced → Standard fertilizer dose"

            elif tool_id == "3":
                temp = float(request.form.get("temp",0))
                base = 6000
                if temp > 35:
                    base *= 1.2
                elif temp < 20:
                    base *= 0.9
                result = f"💧 Water Requirement: {round(base)} liters/acre/day"

            elif tool_id == "4":
                soil = request.form.get("soil","").lower()
                if soil == "sandy":
                    result = "📅 Irrigate every 4 days"
                elif soil == "clay":
                    result = "📅 Irrigate every 8 days"
                else:
                    result = "📅 Irrigate every 6 days"

            elif tool_id == "5":
                last = request.form.get("crop","").lower()
                rotation = {
                    "wheat":"🌿 Plant legumes next",
                    "rice":"🌿 Plant maize next",
                    "maize":"🌿 Plant wheat next"
                }
                result = rotation.get(last,"🌿 Plant legumes for soil recovery")

            elif tool_id == "6":
                hum = float(request.form.get("humidity",0))
                temp = float(request.form.get("temp",0))
                risk = (hum/100) * temp
                result = f"🦠 Pest Risk Score: {round(risk,2)}"

            elif tool_id == "7":
                age = int(request.form.get("age",0))
                if age < 30:
                    result = "🌾 Vegetative Stage → Focus on nitrogen"
                elif age < 60:
                    result = "🌾 Flowering Stage → Balanced nutrients"
                else:
                    result = "🌾 Maturity Stage → Reduce irrigation"

            elif tool_id == "8":
                crop = request.form.get("crop","").lower()
                age = int(request.form.get("age",0))
                if crop=="wheat" and age>=120:
                    result="🌾 Ready for harvest"
                elif crop=="rice" and age>=150:
                    result="🌾 Ready for harvest"
                else:
                    result="🌾 Not ready yet"

            elif tool_id == "9":
                fert = float(request.form.get("fert",0))
                yield_amt = float(request.form.get("yield",0))
                if fert > 0:
                    efficiency = (yield_amt/fert)*100
                    result = f"🧪 Efficiency: {round(efficiency,2)}%"
                else:
                    result = "Invalid fertilizer value"

            elif tool_id == "10":
                yield_amt = float(request.form.get("yield",0))
                price = float(request.form.get("price",0))
                cost = float(request.form.get("cost",0))
                profit = (yield_amt*price)-cost
                result = f"💰 Estimated Profit: ₹{round(profit,2)}"

    except:
        result = "⚠ Invalid input. Please enter correct numbers."

    # ================= FORMS =================
    forms = {
        "1": """<h3>🌾 Crop Yield Estimator</h3>
        <p><b>Theory:</b> Estimates yield based on area, seed rate & rainfall.</p>
        <form method='post'>
        Area: <input name='area' required><br><br>
        Seed rate: <input name='seed' required><br><br>
        Rainfall: <input name='rain' required><br><br>
        <button type='submit'>Calculate</button>
        </form>""",

        "2": """<h3>🧪 Soil Nutrient Balancer</h3>
        <p><b>Theory:</b> Adjust nutrients based on soil pH.</p>
        <form method='post'>
        Soil pH: <input name='ph' required><br><br>
        <button type='submit'>Check</button>
        </form>""",

        "3": """<h3>💧 Water Demand Calculator</h3>
        <form method='post'>
        Temperature °C: <input name='temp' required><br><br>
        <button type='submit'>Calculate</button>
        </form>""",

        "4": """<h3>📅 Irrigation Interval Predictor</h3>
        <form method='post'>
        Soil (sandy/loamy/clay): <input name='soil' required><br><br>
        <button type='submit'>Predict</button>
        </form>""",

        "5": """<h3>🌿 Crop Rotation Planner</h3>
        <form method='post'>
        Last Crop: <input name='crop' required><br><br>
        <button type='submit'>Suggest</button>
        </form>""",

        "6": """<h3>🦠 Pest Risk Score</h3>
        <form method='post'>
        Humidity %: <input name='humidity' required><br><br>
        Temperature °C: <input name='temp' required><br><br>
        <button type='submit'>Check</button>
        </form>""",

        "7": """<h3>🌾 Growth Stage Advisor</h3>
        <form method='post'>
        Crop Age (days): <input name='age' required><br><br>
        <button type='submit'>Check</button>
        </form>""",

        "8": """<h3>🌾 Harvest Time Predictor</h3>
        <form method='post'>
        Crop type: <input name='crop' required><br><br>
        Crop age: <input name='age' required><br><br>
        <button type='submit'>Check</button>
        </form>""",

        "9": """<h3>🧪 Fertilizer Efficiency Checker</h3>
        <form method='post'>
        Fertilizer (kg): <input name='fert' required><br><br>
        Yield (quintal): <input name='yield' required><br><br>
        <button type='submit'>Check</button>
        </form>""",

        "10": """<h3>💰 Profit Forecast Tool</h3>
        <form method='post'>
        Yield (quintal): <input name='yield' required><br><br>
        Price ₹: <input name='price' required><br><br>
        Cost ₹: <input name='cost' required><br><br>
        <button type='submit'>Calculate</button>
        </form>"""
    }

    return forms.get(tool_id,"Invalid Tool") + f"<br><br><h3 style='color:green;'>{result}</h3><br><a href='/category1'>⬅ Back</a>"
