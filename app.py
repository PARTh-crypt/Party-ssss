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
    <html>
    <head>
    <style>
    body{
        margin:0;
        font-family:Montserrat;
        background: linear-gradient(135deg,#1e3c72,#2a5298);
        color:white;
        text-align:center;
    }
    h1{
        padding-top:40px;
    }
    .card{
        width:80%;
        margin:30px auto;
        padding:30px;
        border-radius:15px;
        background:rgba(255,255,255,0.2);
        font-size:22px;
        cursor:pointer;
    }
    a{
        text-decoration:none;
        color:white;
    }
    </style>
    </head>
    <body>

    <h1>Farmer Dashboard<br>किसान डैशबोर्ड</h1>

    <a href="/crop">
        <div class="card">
            🌾 Crop Management<br>
            फसल प्रबंधन
        </div>
    </a>

    </body>
    </html>
    """
from flask import Flask, request
app = Flask(__name__)

@app.route("/tools", methods=["GET","POST"])
def tools():

    result = ""

    if request.method == "POST":
        tool = request.form.get("tool")

        # Temperature
        if tool == "temperature":
            temp = float(request.form.get("value"))
            if temp > 35:
                result = "⚠ High temperature! Increase irrigation."
            elif temp < 10:
                result = "⚠ Very cold! Protect crop."
            else:
                result = "✅ Temperature normal."

        # Soil
        elif tool == "soil":
            level = request.form.get("value")
            if level == "dry":
                result = "💧 Soil dry. Irrigate immediately."
            elif level == "wet":
                result = "⚠ Too wet. Stop watering."
            else:
                result = "✅ Moisture good."

        # Rain
        elif tool == "rain":
            level = request.form.get("value")
            if level == "yes":
                result = "🌧 Do not irrigate today."
            else:
                result = "💧 Light irrigation recommended."

        # Leaf
        elif tool == "leaf":
            color = request.form.get("value")
            if color == "yellow":
                result = "🍂 Nitrogen deficiency. Add urea."
            elif color == "brown":
                result = "⚠ Disease possible."
            else:
                result = "✅ Crop healthy."

        # Pest
        elif tool == "pest":
            level = request.form.get("value")
            if level == "high":
                result = "🐛 Spray immediately."
            elif level == "medium":
                result = "⚠ Monitor crop."
            else:
                result = "✅ No major issue."

        # Fertilizer
        elif tool == "fertilizer":
            result = "🧪 Use balanced NPK. Do not overuse."

        # Harvest
        elif tool == "harvest":
            result = "🌾 If grains hard and yellow → Harvest time."

        # Storage
        elif tool == "storage":
            result = "🏪 Dry crop fully before storage."

        # Irrigation
        elif tool == "irrigation":
            result = "🚿 Best time: Morning or evening."

        # Disease
        elif tool == "disease":
            result = "🦠 Spots on leaves? Use fungicide."

    return f"""
    <html>
    <body style="font-family:Arial;text-align:center;">

    <h2>🌾 Smart Farmer Tool</h2>

    <form method="POST">

    <select name="tool">
        <option value="temperature">Temperature</option>
        <option value="soil">Soil Moisture</option>
        <option value="rain">Rain</option>
        <option value="leaf">Leaf Color</option>
        <option value="pest">Pest Level</option>
        <option value="fertilizer">Fertilizer Guide</option>
        <option value="harvest">Harvest</option>
        <option value="storage">Storage</option>
        <option value="irrigation">Irrigation</option>
        <option value="disease">Disease Check</option>
    </select>

    <br><br>

    <input type="text" name="value" placeholder="Enter value if needed">

    <br><br>

    <button type="submit">Check</button>
    </form>

    <h3>{result}</h3>

    <br><a href="/dashboard">Back</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
    
