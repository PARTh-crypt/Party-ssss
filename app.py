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

# ================= DASHBOARD =================
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return """
    <h1>🌾 SAATHI Dashboard / डैशबोर्ड</h1>

    <a href="/category1">
        <button style="padding:10px;margin:10px;">
        🌾 Crop Management / फ़सल प्रबंधन
        </button>
    </a>

    <br><br>
    """

# ================= CATEGORY 1 =================
@app.route("/category1")
def category1():
    return """
    <h2>🌾 Crop Management Tools</h2>

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

    <a href='/dashboard'>⬅ Back</a>
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
                result = f"🌾 Estimated Yield: {round(area*seed*(rain/500),2)} quintals"

            elif tool_id == "2":
                ph = float(request.form.get("ph",0))
                if ph < 6:
                    result = "Soil acidic → Add Lime"
                elif ph > 7.5:
                    result = "Soil alkaline → Add Organic manure"
                else:
                    result = "Soil balanced"

            elif tool_id == "3":
                temp = float(request.form.get("temp",0))
                water = 6000
                if temp > 35: water *= 1.2
                if temp < 20: water *= 0.9
                result = f"Water Need: {round(water)} L/acre/day"

            elif tool_id == "4":
                soil = request.form.get("soil","").lower()
                if soil == "sandy":
                    result = "Irrigate every 4 days"
                elif soil == "clay":
                    result = "Irrigate every 8 days"
                else:
                    result = "Irrigate every 6 days"

            elif tool_id == "5":
                crop = request.form.get("crop","").lower()
                rotation = {
                    "wheat":"Plant legumes next",
                    "rice":"Plant maize next",
                    "maize":"Plant wheat next"
                }
                result = rotation.get(crop,"Plant legumes")

            elif tool_id == "6":
                hum = float(request.form.get("humidity",0))
                temp = float(request.form.get("temp",0))
                result = f"Pest Risk Score: {round((hum/100)*temp,2)}"

            elif tool_id == "7":
                age = int(request.form.get("age",0))
                if age < 30:
                    result = "Vegetative Stage"
                elif age < 60:
                    result = "Flowering Stage"
                else:
                    result = "Maturity Stage"

            elif tool_id == "8":
                crop = request.form.get("crop","").lower()
                age = int(request.form.get("age",0))
                if crop=="wheat" and age>=120:
                    result="Ready for harvest"
                elif crop=="rice" and age>=150:
                    result="Ready for harvest"
                else:
                    result="Not ready yet"

            elif tool_id == "9":
                fert = float(request.form.get("fert",0))
                yield_amt = float(request.form.get("yield",0))
                if fert>0:
                    result = f"Efficiency: {round((yield_amt/fert)*100,2)}%"
                else:
                    result = "Invalid fertilizer value"

            elif tool_id == "10":
                y = float(request.form.get("yield",0))
                price = float(request.form.get("price",0))
                cost = float(request.form.get("cost",0))
                result = f"Estimated Profit: ₹{round((y*price)-cost,2)}"

    except:
        result = "Invalid Input"

    forms = {
        "1": """<h3>Crop Yield Estimator</h3>
                <form method='post'>
                Area:<input name='area'><br>
                Seed:<input name='seed'><br>
                Rain:<input name='rain'><br>
                <button>Calculate</button></form>""",

        "2": """<h3>Soil Nutrient Balancer</h3>
                <form method='post'>
                Soil pH:<input name='ph'><br>
                <button>Check</button></form>""",

        "3": """<h3>Water Demand Calculator</h3>
                <form method='post'>
                Temp:<input name='temp'><br>
                <button>Calculate</button></form>""",

        "4": """<h3>Irrigation Interval</h3>
                <form method='post'>
                Soil:<input name='soil'><br>
                <button>Predict</button></form>""",

        "5": """<h3>Crop Rotation</h3>
                <form method='post'>
                Last Crop:<input name='crop'><br>
                <button>Suggest</button></form>""",

        "6": """<h3>Pest Risk</h3>
                <form method='post'>
                Humidity:<input name='humidity'><br>
                Temp:<input name='temp'><br>
                <button>Check</button></form>""",

        "7": """<h3>Growth Stage</h3>
                <form method='post'>
                Age:<input name='age'><br>
                <button>Check</button></form>""",

        "8": """<h3>Harvest Predictor</h3>
                <form method='post'>
                Crop:<input name='crop'><br>
                Age:<input name='age'><br>
                <button>Check</button></form>""",

        "9": """<h3>Fertilizer Efficiency</h3>
                <form method='post'>
                Fertilizer:<input name='fert'><br>
                Yield:<input name='yield'><br>
                <button>Check</button></form>""",

        "10": """<h3>Profit Forecast</h3>
                 <form method='post'>
                 Yield:<input name='yield'><br>
                 Price:<input name='price'><br>
                 Cost:<input name='cost'><br>
                 <button>Calculate</button></form>"""
    }

    return forms.get(tool_id,"Invalid Tool") + f"<br><h3 style='color:green'>{result}</h3><br><a href='/category1'>⬅ Back</a>"


if __name__ == "__main__":
    app.run(debug=True)
