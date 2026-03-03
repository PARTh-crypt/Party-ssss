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
from flask import Flask, request

app = Flask(__name__)

# ==========================
# Dashboard
# ==========================
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
    background: linear-gradient(135deg,#1e3c72,#2a5298,#6dd5ed,#2193b0);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white;
    text-align:center;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1{margin-top:30px; font-family:'Playfair Display', serif;}
.card{
    width:80%;
    margin:20px auto;
    padding:25px;
    border-radius:20px;
    background:rgba(255,255,255,0.2);
    font-size:22px;
    cursor:pointer;
    transition:0.3s;
}
.card:hover{background:rgba(255,255,255,0.35); transform:scale(1.03);}
</style>
</head>
<body>
<h1>Dashboard / डैशबोर्ड</h1>
<a href="/crop">
    <div class="card">🌾 Crop Management / फ़सल प्रबंधन</div>
</a>
</body>
</html>
"""

# ==========================
# Crop Management Category
# ==========================
@app.route("/crop")
def crop():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Crop Management Tools</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg,#11998e,#38ef7d,#30cfd0,#330867);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white;
    text-align:center;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1{margin-top:20px; font-family:'Playfair Display', serif;}
.card{
    width:90%;
    margin:15px auto;
    padding:20px;
    border-radius:20px;
    background:rgba(0,0,0,0.35);
    font-size:20px;
    cursor:pointer;
    transition:0.3s;
}
.card:hover{background:rgba(0,0,0,0.5); transform:scale(1.02);}
a{text-decoration:none;color:white;}
</style>
</head>
<body>
<h1>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h1>
""" + "\n".join([f"<a href='/tool/{i}'><div class='card'>{i}️⃣ {title}</div></a>" for i, title in enumerate([
    "Crop Yield Estimator / फ़सल अनुमान",
    "Soil Nutrient Balancer / मिट्टी पोषण संतुलन",
    "Water Demand Calculator / जल आवश्यकता कैलकुलेटर",
    "Irrigation Interval Predictor / सिंचाई अंतराल पूर्वानुमान",
    "Crop Rotation Planner / फ़सल चक्र योजना",
    "Pest Risk Score / कीट जोखिम मूल्यांकन",
    "Growth Stage Advisor / विकास अवस्था सलाहकार",
    "Harvest Time Predictor / कटाई समय पूर्वानुमान",
    "Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच",
    "Profit Forecast Tool / लाभ पूर्वानुमान"
], start=1)]) + """
<a href="/dashboard"><div class="card">⬅ Back to Dashboard / डैशबोर्ड पर वापस</div></a>
</body>
</html>
"""

# ==========================
# Tool Engine
# ==========================
@app.route("/tool/<tool_id>", methods=["GET","POST"])
def tool(tool_id):
    result = ""
    forms = {
        "1": """<h2>🌾 Crop Yield Estimator</h2>
<p>Theory: Estimates yield based on area, seed rate & rainfall.</p>
<form method='post'>
Area (acres): <input name='area'><br><br>
Seed rate (kg/acre): <input name='seed'><br><br>
Rainfall (mm): <input name='rain'><br><br>
<button type='submit'>Calculate</button>
</form>""",
        "2": """<h2>🧪 Soil Nutrient Balancer</h2>
<p>Theory: Adjusts nutrients based on soil pH.</p>
<form method='post'>
Soil pH: <input name='ph'><br><br>
<button type='submit'>Check</button>
</form>""",
        "3": """<h2>💧 Water Demand Calculator</h2>
<p>Theory: Calculates water need based on temperature.</p>
<form method='post'>
Temperature °C: <input name='temp'><br><br>
<button type='submit'>Calculate</button>
</form>""",
        "4": """<h2>📅 Irrigation Interval Predictor</h2>
<p>Theory: Determines irrigation frequency based on soil type.</p>
<form method='post'>
Soil (sandy/loamy/clay): <input name='soil'><br><br>
<button type='submit'>Predict</button>
</form>""",
        "5": """<h2>🌿 Crop Rotation Planner</h2>
<p>Theory: Suggests next crop to maintain soil fertility.</p>
<form method='post'>
Last Crop: <input name='crop'><br><br>
<button type='submit'>Suggest</button>
</form>""",
        "6": """<h2>🦠 Pest Risk Score</h2>
<p>Theory: Estimates pest attack probability based on humidity & temperature.</p>
<form method='post'>
Humidity %: <input name='humidity'><br><br>
Temperature °C: <input name='temp'><br><br>
<button type='submit'>Check</button>
</form>""",
        "7": """<h2>🌾 Growth Stage Advisor</h2>
<p>Theory: Advises action based on crop age.</p>
<form method='post'>
Crop age (days): <input name='age'><br><br>
<button type='submit'>Check</button>
</form>""",
        "8": """<h2>🌾 Harvest Time Predictor</h2>
<p>Theory: Suggests if crop is ready for harvest.</p>
<form method='post'>
Crop type: <input name='crop'><br><br>
Crop age (days): <input name='age'><br><br>
<button type='submit'>Check</button>
</form>""",
        "9": """<h2>🧪 Fertilizer Efficiency Checker</h2>
<p>Theory: Measures output yield per fertilizer input.</p>
<form method='post'>
Fertilizer (kg): <input name='fert'><br><br>
Yield (quintal): <input name='yield'><br><br>
<button type='submit'>Check</button>
</form>""",
        "10": """<h2>💰 Profit Forecast Tool</h2>
<p>Theory: Predicts profit based on yield & market price.</p>
<form method='post'>
Yield (quintal): <input name='yield'><br><br>
Price per quintal ₹: <input name='price'><br><br>
Total cost ₹: <input name='cost'><br><br>
<button type='submit'>Calculate</button>
</form>"""
    }

    if request.method=="POST":
        # calculation logic here
        try:
            if tool_id=="1":
                area=float(request.form["area"])
                seed=float(request.form["seed"])
                rain=float(request.form["rain"])
                result=f"<h3>Estimated Yield / अनुमानित उत्पादन: {round(area*seed*(rain/500),2)} quintals</h3>"
            elif tool_id=="2":
                ph=float(request.form["ph"])
                if ph<6: r="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कम्पोस्ट डालें"
                elif ph>7.5: r="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → कार्बनिक खाद डालें"
                else: r="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → सामान्य उर्वरक"
                result=f"<h3>{r}</h3>"
            elif tool_id=="3":
                temp=float(request.form["temp"])
                base=6000
                if temp>35: base*=1.2
                elif temp<20: base*=0.9
                result=f"<h3>Water Requirement / जल आवश्यकता: {round(base)} liters/acre/day</h3>"
            elif tool_id=="4":
                soil=request.form["soil"].lower()
                if soil=="sandy": r="Irrigate every 4 days / हर 4 दिन सिंचाई करें"
                elif soil=="clay": r="Irrigate every 8 days / हर 8 दिन सिंचाई करें"
                else: r="Irrigate every 6 days / हर 6 दिन सिंचाई करें"
                result=f"<h3>{r}</h3>"
            elif tool_id=="5":
                last=request.form["crop"].lower()
                rotation={"wheat":"Plant legumes next / अगली फसल दलहनी", "rice":"Plant maize next / अगली फसल मक्का","maize":"Plant wheat next / अगली फसल गेहूं"}
                r=rotation.get(last,"Plant legumes for soil recovery / मिट्टी सुधार के लिए दलहनी लगाएं")
                result=f"<h3>{r}</h3>"
            elif tool_id=="6":
                hum=float(request.form["humidity"])
                temp=float(request.form["temp"])
                risk=(hum/100)*temp
                if risk>25: r="⚠ High Pest Risk / उच्च कीट जोखिम"
                else: r="Low to Moderate Risk / कम या मध्यम जोखिम"
                result=f"<h3>Pest Risk Score / कीट जोखिम स्कोर: {round(risk,2)}<br>{r}</h3>"
            elif tool_id=="7":
                age=int(request.form["age"])
                if age<30: r="Vegetative Stage → Focus on nitrogen / पौधे की वृद्धि चरण → नाइट्रोजन पर ध्यान दें"
                elif age<60: r="Flowering Stage → Balanced nutrients / फूल आने का चरण → संतुलित पोषण"
                else: r="Maturity Stage → Reduce irrigation / परिपक्वता चरण → सिंचाई कम करें"
                result=f"<h3>{r}</h3>"
            elif tool_id=="8":
                crop=request.form["crop"].lower()
                age=int(request.form["age"])
                if (crop=="wheat" and age>=120) or (crop=="rice" and age>=150): r="Ready for harvest / कटाई के लिए तैयार"
                else: r="Not ready yet / अभी तैयार नहीं"
                result=f"<h3>{r}</h3>"
            elif tool_id=="9":
                fert=float(request.form["fert"])
                yield_amt=float(request.form["yield"])
                eff=(yield_amt/fert)*100
                result=f"<h3>Efficiency / दक्षता: {round(eff,2)}%</h3>"
            elif tool_id=="10":
                yield_amt=float(request.form["yield"])
                price=float(request.form["price"])
                cost=float(request.form["cost"])
                profit=(yield_amt*price)-cost
                result=f"<h3>Estimated Profit / अनुमानित लाभ: ₹{round(profit,2)}</h3>"
        except:
            result="<h3>Error: Invalid input / त्रुटि: अमान्य इनपुट</h3>"

    return f"""
<html>
<head>
<title>Tool {tool_id}</title>
<style>
body{{margin:0; font-family:'Montserrat',sans-serif; background: linear-gradient(135deg,#11998e,#38ef7d,#30cfd0,#330867); background-size:400% 400%; animation:bgMove 20s ease infinite; color:white; text-align:center;}}
@keyframes bgMove{{0%{{background-position:0% 50%;}}50%{{background-position:100% 50%;}}100%{{background-position:0% 50%;}}}}
h2{{margin-top:20px;}}
form{{margin-top:20px;}}
input{{padding:5px; margin:5px; border-radius:5px;}}
button{{padding:8px 20px; margin-top:10px; border-radius:8px; background:linear-gradient(45deg,#fdd835,#fbc02d); border:none; color:#2f6f2f; font-weight:bold; cursor:pointer;}}
button:hover{{transform:scale(1.05);}}
</style>
</head>
<body>
{forms.get(tool_id,"Invalid Tool")}
{result}
<br><br>
<a href='/crop'>⬅ Back to Crop Tools / फ़सल टूल्स पर वापस</a>
</body>
</html>
"""
