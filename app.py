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
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(135deg, #f093fb, #f5576c, #4facfe, #00f2fe);
        background-size: 400% 400%;
        animation: bgMove 15s ease infinite;
        color:white;
        text-align:center;
    }
    @keyframes bgMove{
        0%{background-position:0% 50%;}
        50%{background-position:100% 50%;}
        100%{background-position:0% 50%;}
    }
    h1{
        padding-top:40px;
        font-family:'Playfair Display', serif;
        font-size:48px;
        text-shadow:2px 2px 8px rgba(0,0,0,0.4);
    }
    .card{
        width:80%;
        margin:20px auto;
        padding:25px;
        border-radius:20px;
        background: rgba(255,255,255,0.2);
        font-size:22px;
        cursor:pointer;
        transition:0.3s;
    }
    .card:hover{
        background: rgba(255,255,255,0.35);
        transform:scale(1.05);
    }
    a{
        text-decoration:none;
        color:white;
    }
    </style>
    </head>
    <body>
    <h1>PARTH'S KISAN SAATHI<br>किसान का डिजिटल साथी</h1>
    <a href="/crop">
        <div class="card">
            🌾 Crop Management / फ़सल प्रबंधन
        </div>
    </a>
    </body>
    </html>
    """

# ==========================
# Crop Management Tools Page
# ==========================
@app.route("/crop")
def crop():
    tools = [
        "1️⃣ Crop Yield Estimator / अनुमानित उत्पादन",
        "2️⃣ Soil Nutrient Balancer / मिट्टी पोषण संतुलक",
        "3️⃣ Water Demand Calculator / पानी की आवश्यकता",
        "4️⃣ Irrigation Interval Predictor / सिंचाई अंतराल",
        "5️⃣ Crop Rotation Planner / फसल चक्रीकरण",
        "6️⃣ Pest Risk Score / कीट जोखिम",
        "7️⃣ Growth Stage Advisor / विकास चरण सलाह",
        "8️⃣ Harvest Time Predictor / कटाई समय",
        "9️⃣ Fertilizer Efficiency Checker / उर्वरक दक्षता",
        "🔟 Profit Forecast Tool / लाभ पूर्वानुमान"
    ]
    html_tools=""
    for i,t in enumerate(tools):
        html_tools+=f"<a href='/tool/{i+1}'><div class='tool'>{t}</div></a>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Crop Management Tools</title>
    <style>
    body{{font-family:Montserrat; text-align:center; background: linear-gradient(135deg,#fdfbfb,#ebedee);}}
    h2{{margin-top:30px;}}
    .tool{{
        margin:15px auto;
        padding:20px;
        width:80%;
        border-radius:15px;
        background: linear-gradient(to right,#00f2fe,#4facfe);
        color:white;
        font-size:20px;
        cursor:pointer;
        transition:0.3s;
    }}
    .tool:hover{{transform:scale(1.05);}}
    </style>
    </head>
    <body>
    <h2>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h2>
    {html_tools}
    <a href='/dashboard'><div class='tool' style='background:#ff6a00;'>⬅ Back / वापस</div></a>
    </body>
    </html>
    """

# ==========================
# Tool Engine - All 10 Tools Practical + Theory
# ==========================
@app.route("/tool/<int:id>", methods=["GET","POST"])
def tool(id):
    result=""
    form_html=""
    
    # Tool Forms & Theory
    if id==1:
        form_html="""
        <h2>🌾 Crop Yield Estimator / अनुमानित उत्पादन</h2>
        <p>Theory: Estimates yield based on area, seed rate & rainfall.<br>सिद्धांत: क्षेत्रफल, बीज और वर्षा के आधार पर उत्पादन अनुमान।</p>
        <form method='post'>
        Area (acres / एकड़): <input name='area' type='number' step='0.01'><br><br>
        Seed rate (kg/acre / बीज दर): <input name='seed' type='number' step='0.01'><br><br>
        Rainfall (mm / वर्षा): <input name='rain' type='number' step='0.01'><br><br>
        <button type='submit'>Calculate / गणना करें</button>
        </form>
        """
    elif id==2:
        form_html="""
        <h2>🧪 Soil Nutrient Balancer / मिट्टी पोषण संतुलक</h2>
        <p>Theory: Adjusts nutrients based on soil pH.<br>सिद्धांत: मिट्टी के पीएच के आधार पर पोषक तत्व संतुलित करता है।</p>
        <form method='post'>
        Soil pH / मिट्टी pH: <input name='ph' type='number' step='0.1'><br><br>
        <button type='submit'>Check / जाँच करें</button>
        </form>
        """
    elif id==3:
        form_html="""
        <h2>💧 Water Demand Calculator / पानी की आवश्यकता</h2>
        <p>Theory: Calculates water requirement based on temperature.<br>सिद्धांत: तापमान के आधार पर पानी की आवश्यकता।</p>
        <form method='post'>
        Temperature °C / तापमान: <input name='temp' type='number' step='0.1'><br><br>
        <button type='submit'>Calculate / गणना करें</button>
        </form>
        """
    elif id==4:
        form_html="""
        <h2>📅 Irrigation Interval Predictor / सिंचाई अंतराल</h2>
        <p>Theory: Determines irrigation frequency based on soil type.<br>सिद्धांत: मिट्टी के प्रकार के आधार पर सिंचाई अंतराल।</p>
        <form method='post'>
        Soil Type (sandy/loamy/clay / मिट्टी प्रकार): <select name='soil'>
            <option value='sandy'>Sandy / बालू</option>
            <option value='loamy'>Loamy / दोमट</option>
            <option value='clay'>Clay / मिट्टी</option>
        </select><br><br>
        <button type='submit'>Predict / अनुमान लगाएँ</button>
        </form>
        """
    elif id==5:
        form_html="""
        <h2>🌿 Crop Rotation Planner / फसल चक्रीकरण</h2>
        <p>Theory: Suggests next crop for soil health.<br>सिद्धांत: मिट्टी की उर्वरता के लिए अगली फसल सुझाव।</p>
        <form method='post'>
        Last Crop / पिछली फसल: <input name='crop' type='text'><br><br>
        <button type='submit'>Suggest / सुझाव दें</button>
        </form>
        """
    elif id==6:
        form_html="""
        <h2>🦠 Pest Risk Score / कीट जोखिम</h2>
        <p>Theory: Estimates pest attack probability.<br>सिद्धांत: कीट हमले की संभावना का अनुमान।</p>
        <form method='post'>
        Humidity % / नमी %: <input name='humidity' type='number' step='0.1'><br><br>
        Temperature °C / तापमान: <input name='temp' type='number' step='0.1'><br><br>
        <button type='submit'>Check / जाँच करें</button>
        </form>
        """
    elif id==7:
        form_html="""
        <h2>🌾 Growth Stage Advisor / विकास चरण सलाह</h2>
        <p>Theory: Advises based on crop age.<br>सिद्धांत: फसल की उम्र के आधार पर सलाह।</p>
        <form method='post'>
        Crop Age (days / दिन): <input name='age' type='number'><br><br>
        <button type='submit'>Check / जाँच करें</button>
        </form>
        """
    elif id==8:
        form_html="""
        <h2>🌾 Harvest Time Predictor / कटाई समय</h2>
        <p>Theory: Suggests if crop ready for harvest.<br>सिद्धांत: फसल की कटाई के लिए तैयार है या नहीं।</p>
        <form method='post'>
        Crop Type / फसल: <input name='crop' type='text'><br><br>
        Crop Age (days / दिन): <input name='age' type='number'><br><br>
        <button type='submit'>Check / जाँच करें</button>
        </form>
        """
    elif id==9:
        form_html="""
        <h2>🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता</h2>
        <p>Theory: Measures output per fertilizer input.<br>सिद्धांत: उर्वरक के अनुसार उत्पादन।</p>
        <form method='post'>
        Fertilizer (kg / किलोग्राम): <input name='fert' type='number' step='0.1'><br><br>
        Yield (quintal / क्विंटल): <input name='yield' type='number' step='0.1'><br><br>
        <button type='submit'>Check / जाँच करें</button>
        </form>
        """
    elif id==10:
        form_html="""
        <h2>💰 Profit Forecast Tool / लाभ पूर्वानुमान</h2>
        <p>Theory: Predicts profit based on yield & market price.<br>सिद्धांत: उत्पादन और बाजार मूल्य के आधार पर लाभ।</p>
        <form method='post'>
        Yield (quintal / क्विंटल): <input name='yield' type='number' step='0.1'><br><br>
        Price per quintal ₹ / बाजार मूल्य: <input name='price' type='number' step='0.1'><br><br>
        Total Cost ₹ / कुल लागत: <input name='cost' type='number' step='0.1'><br><br>
        <button type='submit'>Calculate / गणना करें</button>
        </form>
        """

    # Tool Calculations
    if request.method=="POST":
        if id==1:
            area=float(request.form.get("area",0))
            seed=float(request.form.get("seed",0))
            rain=float(request.form.get("rain",0))
            yield_est=area*seed*(rain/500)
            result=f"<h3>Estimated Yield / अनुमानित उत्पादन: {round(yield_est,2)} quintals / क्विंटल</h3>"
        elif id==2:
            ph=float(request.form.get("ph",7))
            if ph<6: result="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कंपोस्ट डालें"
            elif ph>7.5: result="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → जैविक खाद डालें"
            else: result="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → सामान्य उर्वरक"
        elif id==3:
            temp=float(request.form.get("temp",25))
            base=6000
            if temp>35: base*=1.2
            elif temp<20: base*=0.9
            result=f"Water Requirement / पानी की आवश्यकता: {round(base)} liters/acre/day"
        elif id==4:
            soil=request.form.get("soil","loamy").lower()
            if soil=="sandy": result="Irrigate every 4 days / हर 4 दिन सिंचाई करें"
            elif soil=="clay": result="Irrigate every 8 days / हर 8 दिन सिंचाई करें"
            else: result="Irrigate every 6 days / हर 6 दिन सिंचाई करें"
        elif id==5:
            last=request.form.get("crop","").lower()
            rotation={"wheat":"Plant legumes next / अगली फसल लेग्यूम्स", "rice":"Plant maize next / अगली फसल मक्का", "maize":"Plant wheat next / अगली फसल गेहूँ"}
            result=rotation.get(last,"Plant legumes for soil recovery / मिट्टी सुधार के लिए लेग्यूम्स")
        elif id==6:
            hum=float(request.form.get("humidity",50))
            temp=float(request.form.get("temp",25))
            risk=(hum/100)*temp
            if risk>25: result=f"Pest Risk Score / कीट जोखिम: {round(risk,2)} ⚠ High / उच्च"
            else: result=f"Pest Risk Score / कीट जोखिम: {round(risk,2)} Low / कम"
        elif id==7:
            age=int(request.form.get("age",30))
            if age<30: result="Vegetative Stage → Focus on nitrogen / अंकुरण चरण → नाइट्रोजन पर ध्यान दें"
            elif age<60: result="Flowering Stage → Balanced nutrients / फूलने का चरण → संतुलित पोषक"
            else: result="Maturity Stage → Reduce irrigation / परिपक्वता चरण → सिंचाई कम करें"
        elif id==8:
            crop=request.form.get("crop","").lower()
            age=int(request.form.get("age",0))
            if crop=="wheat" and age>=120: result="Ready for harvest / कटाई के लिए तैयार"
            elif crop=="rice" and age>=150: result="Ready for harvest / कटाई के लिए तैयार"
            else: result="Not ready yet / अभी तैयार नहीं"
        elif id==9:
            fert=float(request.form.get("fert",0))
            yield_amt=float(request.form.get("yield",0))
            eff=(yield_amt/fert)*100 if fert>0 else 0
            result=f"Efficiency / दक्षता: {round(eff,2)}%"
        elif id==10:
            yield_amt=float(request.form.get("yield",0))
            price=float(request.form.get("price",0))
            cost=float(request.form.get("cost",0))
            profit=(yield_amt*price)-cost
            result=f"Estimated Profit / अनुमानित लाभ: ₹{round(profit,2)}"

    return f"""
    <html>
    <head><title>Tool</title></head>
    <body style='font-family:Montserrat;text-align:center;'>
    {form_html}
    {result}
    <br><a href='/crop'>⬅ Back to Tools / टूल्स पर वापस</a>
    </body>
    </html>
    """

if __name__=="__main__":
    app.run(debug=True)
