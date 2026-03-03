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
<title>Farmer Dashboard / किसान डैशबोर्ड</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body {
    margin:0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(135deg,#1e3c72,#2a5298,#00c6ff,#5ee7df);
    color:white;
    text-align:center;
}
h1 {
    padding-top:30px;
    font-family:'Playfair Display', serif;
    font-size:48px;
}
.card {
    width:80%;
    margin:20px auto;
    padding:20px;
    border-radius:15px;
    background: rgba(255,255,255,0.2);
    font-size:22px;
    cursor:pointer;
    transition:0.3s;
}
.card:hover{
    transform:scale(1.05);
    background: rgba(255,255,255,0.35);
}
</style>
</head>
<body>
<h1>Farmer Dashboard / किसान डैशबोर्ड</h1>
<a href="/category1"><div class="card">🌾 Crop Management / फ़सल प्रबंधन</div></a>
</body>
</html>
"""

# ==========================
# Category 1 – Crop Management Tools
# ==========================
@app.route("/category1")
def category1():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Crop Management Tools</title>
<style>
body { font-family:Montserrat; background: linear-gradient(135deg,#11998e,#38ef7d,#fbc2eb,#a6c0fe); color:white; text-align:center;}
h1{padding-top:20px; font-family: 'Playfair Display', serif;}
.button {padding:15px 25px; margin:10px; border-radius:20px; border:none; background: rgba(255,255,255,0.2); color:white; cursor:pointer; font-size:18px; transition:0.3s;}
.button:hover {background: rgba(255,255,255,0.35); transform:scale(1.05);}
</style>
</head>
<body>
<h1>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h1>
<a href="/tool/1"><button class="button">1️⃣ Crop Yield Estimator / उत्पादन अनुमान</button></a><br>
<a href="/tool/2"><button class="button">2️⃣ Soil Nutrient Balancer / मिट्टी पोषण संतुलक</button></a><br>
<a href="/tool/3"><button class="button">3️⃣ Water Demand Calculator / पानी की आवश्यकता</button></a><br>
<a href="/tool/4"><button class="button">4️⃣ Irrigation Interval Predictor / सिंचाई अंतराल</button></a><br>
<a href="/tool/5"><button class="button">5️⃣ Crop Rotation Planner / फसल परिवर्तन योजना</button></a><br>
<a href="/tool/6"><button class="button">6️⃣ Pest Risk Score / कीट जोखिम</button></a><br>
<a href="/tool/7"><button class="button">7️⃣ Growth Stage Advisor / विकास चरण सलाहकार</button></a><br>
<a href="/tool/8"><button class="button">8️⃣ Harvest Time Predictor / फसल कटाई समय</button></a><br>
<a href="/tool/9"><button class="button">9️⃣ Fertilizer Efficiency Checker / उर्वरक दक्षता</button></a><br>
<a href="/tool/10"><button class="button">🔟 Profit Forecast Tool / लाभ पूर्वानुमान</button></a><br>
<a href="/dashboard"><button class="button">⬅ Back to Dashboard / डैशबोर्ड</button></a>
</body>
</html>
"""

# ==========================
# Tool Engine – 10 Full Tools
# ==========================
@app.route("/tool/<tool_id>", methods=["GET","POST"])
def tool(tool_id):
    result = ""
    form_html = ""
    
    # ----- 1️⃣ Crop Yield Estimator -----
    if tool_id=="1":
        form_html = """
        <h2>🌾 Crop Yield Estimator / उत्पादन अनुमान</h2>
        <p>Theory: Estimates yield based on area, seed & rainfall / क्षेत्र, बीज और वर्षा पर अनुमानित उत्पादन।</p>
        <form method="post">
            Area (acres / एकड़): <input name="area" type="number" step="0.01"><br><br>
            Seed (kg / किलोग्राम): <input name="seed" type="number" step="0.01"><br><br>
            Rainfall (mm / मिलीमीटर): <input name="rain" type="number" step="0.01"><br><br>
            <button type="submit">Calculate / गणना करें</button>
        </form>
        """
        if request.method=="POST":
            area = float(request.form["area"])
            seed = float(request.form["seed"])
            rain = float(request.form["rain"])
            yield_est = area * seed * (rain / 500)
            result = f"<h3>Estimated Yield / अनुमानित उत्पादन: {round(yield_est,2)} quintals / क्विंटल</h3>"
    
    # ----- 2️⃣ Soil Nutrient Balancer -----
    elif tool_id=="2":
        form_html = """
        <h2>🧪 Soil Nutrient Balancer / मिट्टी पोषण संतुलक</h2>
        <p>Theory: Adjust nutrients based on soil pH / मिट्टी के पीएच के आधार पर पोषक तत्व संतुलन।</p>
        <form method="post">
            Soil pH / मिट्टी पीएच: <input name="ph" type="number" step="0.01"><br><br>
            <button type="submit">Check / जाँच करें</button>
        </form>
        """
        if request.method=="POST":
            ph = float(request.form["ph"])
            if ph<6:
                result="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कंपोस्ट डालें"
            elif ph>7.5:
                result="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → कार्बनिक खाद डालें"
            else:
                result="Soil balanced → Standard fertilizer / मिट्टी संतुलित → सामान्य उर्वरक"
            result = f"<h3>{result}</h3>"

    # ----- 3️⃣ Water Demand Calculator -----
    elif tool_id=="3":
        form_html = """
        <h2>💧 Water Demand Calculator / पानी की आवश्यकता</h2>
        <p>Theory: Calculates water need based on temperature / तापमान के आधार पर पानी की आवश्यकता।</p>
        <form method="post">
            Temperature °C / तापमान: <input name="temp" type="number" step="0.1"><br><br>
            <button type="submit">Calculate / गणना करें</button>
        </form>
        """
        if request.method=="POST":
            temp = float(request.form["temp"])
            water = 6000
            if temp>35: water*=1.2
            elif temp<20: water*=0.9
            result = f"<h3>Water Requirement / पानी की आवश्यकता: {round(water)} liters/acre / लीटर/एकड़</h3>"

    # ----- 4️⃣ Irrigation Interval Predictor -----
    elif tool_id=="4":
        form_html = """
        <h2>📅 Irrigation Interval Predictor / सिंचाई अंतराल</h2>
        <p>Theory: Determines irrigation frequency based on soil / मिट्टी के आधार पर सिंचाई अंतराल।</p>
        <form method="post">
            Soil type (sandy/loamy/clay) / मिट्टी प्रकार: <input name="soil" type="text"><br><br>
            <button type="submit">Predict / भविष्यवाणी</button>
        </form>
        """
        if request.method=="POST":
            soil = request.form["soil"].lower()
            if soil=="sandy": result="Irrigate every 4 days / हर 4 दिन सिंचाई"
            elif soil=="clay": result="Irrigate every 8 days / हर 8 दिन सिंचाई"
            else: result="Irrigate every 6 days / हर 6 दिन सिंचाई"
            result=f"<h3>{result}</h3>"

    # ----- 5️⃣ Crop Rotation Planner -----
    elif tool_id=="5":
        form_html = """
        <h2>🌿 Crop Rotation Planner / फसल परिवर्तन योजना</h2>
        <p>Theory: Suggests next crop / अगली फसल सुझाएं।</p>
        <form method="post">
            Last Crop / पिछली फसल: <input name="crop" type="text"><br><br>
            <button type="submit">Suggest / सुझाव दें</button>
        </form>
        """
        if request.method=="POST":
            last = request.form["crop"].lower()
            rotation = {"wheat":"Plant legumes next / अगली फसल दलहन लगाएं",
                        "rice":"Plant maize next / अगली फसल मक्का लगाएं",
                        "maize":"Plant wheat next / अगली फसल गेहूं लगाएं"}
            result = f"<h3>{rotation.get(last,'Plant legumes for soil recovery / मिट्टी सुधार के लिए दलहन')} </h3>"

    # ----- 6️⃣ Pest Risk Score -----
    elif tool_id=="6":
        form_html = """
        <h2>🦠 Pest Risk Score / कीट जोखिम</h2>
        <p>Theory: Estimates pest attack probability based on humidity & temp / आर्द्रता और तापमान के आधार पर कीट जोखिम।</p>
        <form method="post">
            Humidity % / आर्द्रता %: <input name="humidity" type="number" step="0.1"><br><br>
            Temperature °C / तापमान: <input name="temp" type="number" step="0.1"><br><br>
            <button type="submit">Check / जाँच करें</button>
        </form>
        """
        if request.method=="POST":
            hum = float(request.form["humidity"])
            temp = float(request.form["temp"])
            risk = (hum/100)*temp
            status = "⚠ High Pest Risk / उच्च कीट जोखिम" if risk>25 else "Low to Moderate Risk / कम से मध्यम जोखिम"
            result=f"<h3>Pest Risk Score: {round(risk,2)} | {status}</h3>"

    # ----- 7️⃣ Growth Stage Advisor -----
    elif tool_id=="7":
        form_html = """
        <h2>🌾 Growth Stage Advisor / विकास चरण सलाहकार</h2>
        <p>Theory: Advises action based on crop age / फसल की आयु के आधार पर सुझाव।</p>
        <form method="post">
            Crop Age (days / दिन): <input name="age" type="number"><br><br>
            <button type="submit">Check / जाँच करें</button>
        </form>
        """
        if request.method=="POST":
            age = int(request.form["age"])
            if age<30: result="Vegetative Stage → Focus on nitrogen / पत्ते वाला चरण → नाइट्रोजन पर ध्यान दें"
            elif age<60: result="Flowering Stage → Balanced nutrients / फूलने का चरण → संतुलित पोषण"
            else: result="Maturity Stage → Reduce irrigation / परिपक्वता चरण → सिंचाई कम करें"
            result=f"<h3>{result}</h3>"

    # ----- 8️⃣ Harvest Time Predictor -----
    elif tool_id=="8":
        form_html = """
        <h2>🌾 Harvest Time Predictor / फसल कटाई समय</h2>
        <p>Theory: Suggests if crop ready / फसल कटाई के लिए तैयार है या नहीं।</p>
        <form method="post">
            Crop type / फसल प्रकार: <input name="crop" type="text"><br><br>
            Crop Age (days / आयु दिन): <input name="age" type="number"><br><br>
            <button type="submit">Check / जाँच करें</button>
        </form>
        """
        if request.method=="POST":
            crop = request.form["crop"].lower()
            age = int(request.form["age"])
            ready = False
            if crop=="wheat" and age>=120: ready=True
            elif crop=="rice" and age>=150: ready=True
            result=f"<h3>{'Ready for harvest / कटाई के लिए तैयार' if ready else 'Not ready yet / अभी तैयार नहीं'}</h3>"

    # ----- 9️⃣ Fertilizer Efficiency Checker -----
    elif tool_id=="9":
        form_html = """
        <h2>🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता</h2>
        <p>Theory: Measures output per fertilizer input / उर्वरक के अनुसार उत्पादन मापें।</p>
        <form method="post">
            Fertilizer (kg / किलोग्राम): <input name="fert" type="number" step="0.01"><br><br>
            Yield (quintal / क्विंटल): <input name="yield" type="number" step="0.01"><br><br>
            <button type="submit">Check / जाँच करें</button>
        </form>
        """
        if request.method=="POST":
            fert = float(request.form["fert"])
            yield_amt = float(request.form["yield"])
            efficiency = (yield_amt/fert)*100
            result=f"<h3>Efficiency / दक्षता: {round(efficiency,2)}% </h3>"

    # ----- 10️⃣ Profit Forecast Tool -----
    elif tool_id=="10":
        form_html = """
        <h2>💰 Profit Forecast Tool / लाभ पूर्वानुमान</h2>
        <p>Theory: Predicts profit based on yield & market price / उत्पादन और बाजार मूल्य के आधार पर लाभ का अनुमान।</p>
        <form method="post">
            Yield (quintal / क्विंटल): <input name="yield" type="number" step="0.01"><br><br>
            Price per quintal ₹ / कीमत प्रति क्विंटल: <input name="price" type="number" step="0.01"><br><br>
            Total cost ₹ / कुल लागत: <input name="cost" type="number" step="0.01"><br><br>
            <button type="submit">Calculate / गणना करें</button>
        </form>
        """
        if request.method=="POST":
            yield_amt = float(request.form["yield"])
            price = float(request.form["price"])
            cost = float(request.form["cost"])
            profit = (yield_amt*price)-cost
            result=f"<h3>Estimated Profit / अनुमानित लाभ: ₹{round(profit,2)}</h3>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Tool {tool_id}</title>
    <style>
    body {{ font-family:Montserrat; background: linear-gradient(135deg,#ff758c,#ff7eb3,#c2e59c,#64b3f4); color:white; text-align:center; }}
    input {{ padding:8px; margin:5px; border-radius:8px; border:none; }}
    button {{ padding:10px 20px; border-radius:15px; border:none; cursor:pointer; background: rgba(255,255,255,0.2); color:white; margin-top:10px; }}
    button:hover{{background: rgba(255,255,255,0.35); transform:scale(1.05);}}
    </style>
    </head>
    <body>
    {form_html}
    {result}
    <br><br><a href="/category1" style="color:white;">⬅ Back / वापस</a>
    </body>
    </html>
    """

if __name__=="__main__":
    app.run(debug=True)
