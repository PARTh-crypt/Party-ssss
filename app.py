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
from flask import Flask, render_template_string, request

app = Flask(name)

==========================

DASHBOARD

==========================

@app.route('/dashboard') def dashboard(): return render_template_string(""" <!DOCTYPE html> <html> <head> <title>PARTH'S KISAN SAATHI - Dashboard</title> <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet"> <style> body{ margin:0; font-family:'Montserrat',sans-serif; background: linear-gradient(135deg,#1e3c72,#2a5298,#6dd5ed,#2193b0); background-size: 400% 400%; animation: gradientBG 15s ease infinite; color:white; text-align:center; min-height:100vh; }

@keyframes gradientBG {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}

h1{margin-top:40px;font-family:'Playfair Display', serif;font-size:48px;}
h2{font-size:24px;margin:10px;}

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
.card:hover{background:rgba(255,255,255,0.35); transform:scale(1.05);}
a{text-decoration:none;color:white;}
</style>
</head>
<body>
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Farmer Dashboard / किसान डैशबोर्ड</h2>

<a href="/crop"><div class="card">🌾 Crop Management / फ़सल प्रबंधन</div></a>
</body>
</html>
""")

==========================

CATEGORY 1 – CROP MANAGEMENT TOOLS

==========================

@app.route('/crop', methods=['GET','POST']) def crop_tools(): result = ""

tool_id = request.args.get('tool')

# Tool logic
if request.method=='POST':
    if tool_id=='1':  # Crop Yield Estimator
        area = float(request.form['area'])
        seed = float(request.form['seed'])
        rain = float(request.form['rain'])
        yield_est = area * seed * (rain/500)
        result = f"Estimated Yield / अनुमानित उत्पादन: {round(yield_est,2)} quintals"
    elif tool_id=='2':  # Soil Nutrient Balancer
        ph = float(request.form['ph'])
        if ph<6:
            result="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कम्पोस्ट डालें"
        elif ph>7.5:
            result="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → जैविक खाद डालें"
        else:
            result="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → सामान्य उर्वरक"
    elif tool_id=='3':  # Water Demand Calculator
        temp = float(request.form['temp'])
        base = 6000
        if temp>35: base*=1.2
        elif temp<20: base*=0.9
        result=f"Water Requirement / जल आवश्यकता: {round(base)} liters/acre/day"
    elif tool_id=='4':  # Irrigation Interval Predictor
        soil = request.form['soil'].lower()
        if soil=='sandy': result="Irrigate every 4 days / हर 4 दिन सिंचाई करें"
        elif soil=='clay': result="Irrigate every 8 days / हर 8 दिन सिंचाई करें"
        else: result="Irrigate every 6 days / हर 6 दिन सिंचाई करें"
    elif tool_id=='5':  # Crop Rotation Planner
        last_crop = request.form['crop'].lower()
        rotation = {'wheat':'Plant legumes next / अगली फसल: दलहन','rice':'Plant maize next / अगली फसल: मक्का','maize':'Plant wheat next / अगली फसल: गेहूं'}
        result = rotation.get(last_crop,'Plant legumes for soil recovery / मिट्टी सुधार के लिए दलहन लगाएं')
    elif tool_id=='6':  # Pest Risk Score
        hum = float(request.form['humidity'])
        temp = float(request.form['temp'])
        risk=(hum/100)*temp
        result=f"Pest Risk Score / कीट जोखिम: {round(risk,2)} (Low/Medium/High)"
    elif tool_id=='7':  # Growth Stage Advisor
        age=int(request.form['age'])
        if age<30: result="Vegetative Stage → Focus on nitrogen / पत्तेदार अवस्था → नाइट्रोजन पर ध्यान दें"
        elif age<60: result="Flowering Stage → Balanced nutrients / फूल आने की अवस्था → संतुलित पोषण"
        else: result="Maturity Stage → Reduce irrigation / पकने की अवस्था → सिंचाई कम करें"
    elif tool_id=='8':  # Harvest Time Predictor
        crop=request.form['crop'].lower()
        age=int(request.form['age'])
        if crop=='wheat' and age>=120: result="Ready for harvest / कटाई के लिए तैयार"
        elif crop=='rice' and age>=150: result="Ready for harvest / कटाई के लिए तैयार"
        else: result="Not ready yet / अभी तैयार नहीं"
    elif tool_id=='9':  # Fertilizer Efficiency Checker
        fert=float(request.form['fert'])
        yield_amt=float(request.form['yield'])
        efficiency=(yield_amt/fert)*100
        result=f"Efficiency / दक्षता: {round(efficiency,2)}%"
    elif tool_id=='10':  # Profit Forecast Tool
        yield_amt=float(request.form['yield'])
        price=float(request.form['price'])
        cost=float(request.form['cost'])
        profit=(yield_amt*price)-cost
        result=f"Estimated Profit / अनुमानित लाभ: ₹{round(profit,2)}"

# HTML FORM
forms = {
    '1':"""
    <h3>🌾 Crop Yield Estimator / अनुमानित उत्पादन</h3>
    <p>Tap values / मान टैप करें</p>
    <form method='post'>
    Area (acres) / क्षेत्र (एकड़): <input name='area' type='number' step='0.1'><br><br>
    Seed rate (kg/acre) / बीज दर (किग्रा/एकड़): <input name='seed' type='number' step='0.1'><br><br>
    Rainfall (mm) / वर्षा (मिमी): <input name='rain' type='number' step='0.1'><br><br>
    <button type='submit'>Calculate / गणना करें</button>
    </form>
    """,
    '2':"""
    <h3>🧪 Soil Nutrient Balancer / मिट्टी पोषण संतुलन</h3>
    <form method='post'>
    Soil pH / मिट्टी pH: <input name='ph' type='number' step='0.1'><br><br>
    <button type='submit'>Check / जाँचें</button>
    </form>
    """,
    '3':"""
    <h3>💧 Water Demand Calculator / पानी की आवश्यकता</h3>
    <form method='post'>
    Temperature °C / तापमान °C: <input name='temp' type='number' step='0.1'><br><br>
    <button type='submit'>Calculate / गणना करें</button>
    </form>
    """,
    '4':"""
    <h3>📅 Irrigation Interval Predictor / सिंचाई अंतराल</h3>
    <form method='post'>
    Soil type / मिट्टी प्रकार (sandy/loamy/clay): <input name='soil'><br><br>
    <button type='submit'>Predict / भविष्यवाणी करें</button>
    </form>
    """,
    '5':"""
    <h3>🌿 Crop Rotation Planner / फसल चक्रीकरण</h3>
    <form method='post'>
    Last Crop / पिछली फसल: <input name='crop'><br><br>
    <button type='submit'>Suggest / सुझाव दें</button>
    </form>
    """,
    '6':"""
    <h3>🦠 Pest Risk Score / कीट जोखिम</h3>
    <form method='post'>
    Humidity % / आर्द्रता %: <input name='humidity'><br>
    Temperature °C / तापमान °C: <input name='temp'><br><br>
    <button type='submit'>Check / जाँचें</button>
    </form>
    """,
    '7':"""
    <h3>🌾 Growth Stage Advisor / विकास अवस्था सलाहकार</h3>
    <form method='post'>
    Crop Age (days) / फसल उम्र (दिन): <input name='age' type='number'><br><br>
    <button type='submit'>Check / जाँचें</button>
    </form>
    """,
    '8':"""
    <h3>🌾 Harvest Time Predictor / कटाई समय पूर्वानुमान</h3>
    <form method='post'>
    Crop type / फसल प्रकार: <input name='crop'><br>
    Crop age / फसल उम्र (दिन): <input name='age' type='number'><br><br>
    <button type='submit'>Check / जाँचें</button>
    </form>
    """,
    '9':"""
    <h3>🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच</h3>
    <form method='post'>
    Fertilizer (kg) / उर्वरक (किग्रा): <input name='fert' type='number'><br>
    Yield (quintal) / उत्पादन (क्विंटल): <input name='yield' type='number'><br><br>
    <button type='submit'>Check / जाँचें</button>
    </form>
    """,
    '10':"""
    <h3>💰 Profit Forecast Tool / लाभ पूर्वानुमान</h3>
    <form method='post'>
    Yield (quintal) / उत्पादन (क्विंटल): <input name='yield' type='number'><br>
    Price per quintal ₹ / कीमत प्रति क्विंटल ₹: <input name='price' type='number'><br>
    Total cost ₹ / कुल लागत ₹: <input name='cost' type='number'><br><br>
    <button type='submit'>Calculate / गणना करें</button>
    </form>
    """
}

tool_html = forms.get(tool_id,'')

all_tools_html = """
<h2>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h2>
<p>Tap a tool below to open / नीचे टैप करें:</p>
<div style='display:flex;flex-direction:column;align-items:center;'>
"""
for i in range(1,11):
    all_tools_html+=f"<a href='/crop?tool={i}'><div class='card'>{i}️⃣ Tool / टूल {i}</div></a>"
all_tools_html+="</div>"

return render_template_string(f"""
<!DOCTYPE html>
<html>
<head>
<title>Crop Management Tools</title>
<style>
body{{margin:0;font-family:Montserrat;background:linear-gradient(135deg,#11998e,#38ef7d,#30cfd0,#330867);color:white;text-align:center;min-height:100vh;}}
.card{{width:80%;margin:15px auto;padding:20px;border-radius:15px;background:rgba(255,255,255,0.2);cursor:pointer;transition:0.3s;font-size:20px;}}
.card:hover{{background:rgba(255,255,255,0.35);transform:scale(1.05);}}
a{{text-decoration:none;color:white;}}
</style>
</head>
<body>
{all_tools_html}
<hr>
{tool_html}
<h3>{result}</h3>
<a href='/dashboard'>⬅ Back to Dashboard / डैशबोर्ड पर वापस जाएँ</a>
</body>
</html>
""")

if name=='main': app.run(debug=True)
