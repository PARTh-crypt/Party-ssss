from flask import Flask, request

app = Flask(__name__)

# ==========================
# Starting Screen (Already Given)
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
h1{
font-family: 'Playfair Display', serif;
font-size:56px;
margin:10px;
text-shadow:2px 2px 8px rgba(0,0,0,0.3);
}
h2{
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
# Tool Engine
# ==========================
@app.route("/tool/<tool_id>", methods=["GET","POST"])
def tool(tool_id):
    result = ""
    form_html = ""
    
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
    
    # ====== TODO: Implement other tools similarly ======
    # For brevity, you can add tool 3-10 in the same style

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
