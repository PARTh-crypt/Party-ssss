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
    from flask import Flask

app = Flask(__name__)

# ==========================
# Dashboard
# ==========================
@app.route("/dashboard")
def dashboard():
    return """
    <html>
    <head>
    <style>
    body{
        margin:0;
        font-family:Montserrat,sans-serif;
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
        background-size: 400% 400%;
        animation: gradientMove 15s ease infinite;
        color:white;
        text-align:center;
    }
    @keyframes gradientMove{
        0%{background-position:0% 50%;}
        50%{background-position:100% 50%;}
        100%{background-position:0% 50%;}
    }
    h1{
        padding-top:40px;
        font-size:48px;
        text-shadow:2px 2px 6px rgba(0,0,0,0.3);
    }
    .card{
        width:80%;
        margin:20px auto;
        padding:25px;
        border-radius:20px;
        background:rgba(255,255,255,0.2);
        font-size:24px;
        cursor:pointer;
        transition:0.3s;
    }
    .card:hover{
        transform:scale(1.05);
        background:rgba(255,255,255,0.35);
    }
    a{text-decoration:none;color:white;}
    </style>
    </head>
    <body>
    <h1>PARTH'S KISAN SAATHI<br>किसान डैशबोर्ड</h1>

    <a href="/crop">
        <div class="card">🌾 Crop Management<br>फसल प्रबंधन</div>
    </a>
    </body>
    </html>
    """

# ==========================
# Crop Management Tools Menu
# ==========================
@app.route("/crop")
def crop_menu():
    return """
    <html>
    <head>
    <style>
    body{
        margin:0;
        font-family:Montserrat,sans-serif;
        background: linear-gradient(135deg, #43cea2, #185a9d, #ff6a00, #ee0979);
        background-size:400% 400%;
        animation: gradientMove 15s ease infinite;
        color:white;
        text-align:center;
    }
    @keyframes gradientMove{
        0%{background-position:0% 50%;}
        50%{background-position:100% 50%;}
        100%{background-position:0% 50%;}
    }
    h1{padding-top:30px;}
    .tool-card{
        width:85%;
        margin:15px auto;
        padding:20px;
        border-radius:20px;
        background:rgba(255,255,255,0.2);
        font-size:22px;
        cursor:pointer;
        transition:0.3s;
    }
    .tool-card:hover{
        transform:scale(1.05);
        background:rgba(255,255,255,0.35);
    }
    a{text-decoration:none;color:white;}
    </style>
    </head>
    <body>
    <h1>🌾 Crop Management Tools<br>फसल प्रबंधन टूल्स</h1>

    <a href="/tool/1"><div class="tool-card">1️⃣ Crop Yield Estimator / उत्पादन अनुमान</div></a>
    <a href="/tool/2"><div class="tool-card">2️⃣ Soil Nutrient Balancer / मिट्टी पोषण संतुलन</div></a>
    <a href="/tool/3"><div class="tool-card">3️⃣ Water Demand Calculator / जल आवश्यकता कैलकुलेटर</div></a>
    <a href="/tool/4"><div class="tool-card">4️⃣ Irrigation Interval Predictor / सिंचाई अंतराल भविष्यवक्ता</div></a>
    <a href="/tool/5"><div class="tool-card">5️⃣ Crop Rotation Planner / फ़सल रोटेशन योजना</div></a>
    <a href="/tool/6"><div class="tool-card">6️⃣ Pest Risk Score / कीट जोखिम स्कोर</div></a>
    <a href="/tool/7"><div class="tool-card">7️⃣ Growth Stage Advisor / विकास चरण सलाहकार</div></a>
    <a href="/tool/8"><div class="tool-card">8️⃣ Harvest Time Predictor / कटाई समय पूर्वानुमान</div></a>
    <a href="/tool/9"><div class="tool-card">9️⃣ Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच</div></a>
    <a href="/tool/10"><div class="tool-card">🔟 Profit Forecast Tool / लाभ पूर्वानुमान</div></a>

    <a href="/dashboard"><div class="tool-card">⬅ Back to Dashboard / डैशबोर्ड पर वापस</div></a>
    </body>
    </html>
    """

# ==========================
# Tools Engine
# ==========================
@app.route("/tool/<int:id>")
def tool_engine(id):
    if id == 1:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#f7971e,#ffd200,#ff512f,#dd2476);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>🌾 Crop Yield Estimator / उत्पादन अनुमान</h2>
        <p>Theory: Estimates yield based on area, seed rate & rainfall.<br>थ्योरी: क्षेत्रफल, बीज दर और वर्षा के आधार पर अनुमान लगाता है।</p>
        Area (acres): 
        <button onclick="alert('2 acres')">2</button> 
        <button onclick="alert('5 acres')">5</button><br><br>
        Seed rate (kg/acre): 
        <button onclick="alert('20 kg')">20</button> 
        <button onclick="alert('50 kg')">50</button><br><br>
        Rainfall (mm): 
        <button onclick="alert('200 mm')">200</button> 
        <button onclick="alert('500 mm')">500</button><br><br>
        <button onclick="alert('Estimated Yield: 40 quintals / अनुमानित उत्पादन: 40 क्विंटल')">Calculate / गणना</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 2:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#36d1dc,#5b86e5,#f093fb,#f5576c);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>🧪 Soil Nutrient Balancer / मिट्टी पोषण संतुलन</h2>
        <p>Theory: Adjusts nutrient need based on soil pH.<br>थ्योरी: मिट्टी के pH के आधार पर पोषण आवश्यकताएं समायोजित करता है।</p>
        Soil type: 
        <button onclick="alert('Acidic → Add Lime + Compost / अम्लीय → चूना + कंपोस्ट डालें')">Acidic / अम्लीय</button>
        <button onclick="alert('Alkaline → Add Organic manure / क्षारीय → जैविक खाद डालें')">Alkaline / क्षारीय</button>
        <button onclick="alert('Balanced → Standard fertilizer / संतुलित → मानक उर्वरक')">Balanced / संतुलित</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 3:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#ff512f,#dd2476,#f7971e,#ffd200);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>💧 Water Demand Calculator / जल आवश्यकता कैलकुलेटर</h2>
        <p>Theory: Calculates water need based on crop & rainfall.<br>थ्योरी: फ़सल और वर्षा के आधार पर जल आवश्यकता की गणना।</p>
        <button onclick="alert('Low → 2000 liters / कम → 2000 लीटर')">Low / कम</button>
        <button onclick="alert('Medium → 4000 liters / मध्यम → 4000 लीटर')">Medium / मध्यम</button>
        <button onclick="alert('High → 6000 liters / अधिक → 6000 लीटर')">High / अधिक</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 4:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#11998e,#38ef7d,#ee0979,#ff6a00);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>📅 Irrigation Interval Predictor / सिंचाई अंतराल पूर्वानुमान</h2>
        <p>Theory: Suggests irrigation frequency based on soil type.<br>थ्योरी: मिट्टी के प्रकार के आधार पर सिंचाई अंतराल सुझाव।</p>
        <button onclick="alert('Sandy → Every 4 days / रेतीली → हर 4 दिन')">Sandy / रेतीली</button>
        <button onclick="alert('Loamy → Every 6 days / दोमट → हर 6 दिन')">Loamy / दोमट</button>
        <button onclick="alert('Clay → Every 8 days / चिकनी → हर 8 दिन')">Clay / चिकनी</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 5:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#f7971e,#ffd200,#ff512f,#dd2476);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>🌿 Crop Rotation Planner / फ़सल रोटेशन योजना</h2>
        <p>Theory: Suggests next crop.<br>थ्योरी: अगले फ़सल के लिए सुझाव।</p>
        <button onclick="alert('Wheat → Legumes / गेहूं → दलहन')">Wheat / गेहूं</button>
        <button onclick="alert('Rice → Maize / धान → मक्का')">Rice / धान</button>
        <button onclick="alert('Maize → Wheat / मक्का → गेहूं')">Maize / मक्का</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 6:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#36d1dc,#5b86e5,#f093fb,#f5576c);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>🦠 Pest Risk Score / कीट जोखिम स्कोर</h2>
        <p>Theory: Estimates pest risk based on humidity.<br>थ्योरी: आर्द्रता के आधार पर कीट जोखिम का अनुमान।</p>
        <button onclick="alert('Low / कम')">Low / कम</button>
        <button onclick="alert('Medium / मध्यम')">Medium / मध्यम</button>
        <button onclick="alert('High / उच्च')">High / उच्च</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 7:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#ff6a00,#ee0979,#f7971e,#ffd200);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>🌾 Growth Stage Advisor / विकास चरण सलाहकार</h2>
        <p>Theory: Advises based on crop age.<br>थ्योरी: फ़सल की उम्र के आधार पर सलाह।</p>
        <button onclick="alert('Vegetative / विकासशील')">Vegetative / विकासशील</button>
        <button onclick="alert('Flowering / फूल आना')">Flowering / फूल आना</button>
        <button onclick="alert('Maturity / परिपक्वता')">Maturity / परिपक्वता</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 8:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#43cea2,#185a9d,#ff6a00,#ee0979);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>🌾 Harvest Time Predictor / कटाई समय पूर्वानुमान</h2>
        <p>Theory: Suggests if crop is ready.<br>थ्योरी: फ़सल कटाई के लिए तैयार है या नहीं।</p>
        <button onclick="alert('Ready / तैयार')">Ready / तैयार</button>
        <button onclick="alert('Not Ready / तैयार नहीं')">Not Ready / तैयार नहीं</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 9:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#f093fb,#f5576c,#36d1dc,#5b86e5);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच</h2>
        <p>Theory: Measures output per fertilizer input.<br>थ्योरी: उर्वरक इनपुट के अनुसार उत्पादन मापता है।</p>
        <button onclick="alert('High / उच्च')">High / उच्च</button>
        <button onclick="alert('Medium / मध्यम')">Medium / मध्यम</button>
        <button onclick="alert('Low / कम')">Low / कम</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    elif id == 10:
        return """
        <html><body style='font-family:Montserrat;text-align:center;background:linear-gradient(135deg,#36d1dc,#5b86e5,#f093fb,#f5576c);background-size:400% 400%;animation:gradientMove 15s ease infinite;color:white;'>
        <h2>💰 Profit Forecast Tool / लाभ पूर्वानुमान</h2>
        <p>Theory: Predicts profit based on yield & price.<br>थ्योरी: उत्पादन और कीमत के आधार पर लाभ अनुमानित करता है।</p>
        <button onclick="alert('Profit High / लाभ उच्च')">High / उच्च</button>
        <button onclick="alert('Profit Medium / लाभ मध्यम')">Medium / मध्यम</button>
        <button onclick="alert('Profit Low / लाभ कम')">Low / कम</button><br><br>
        <a href='/crop' style='color:white;'>⬅ Back</a>
        </body></html>
        """
    else:
        return "<h2>Tool coming soon...</h2><a href='/crop'>⬅ Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
