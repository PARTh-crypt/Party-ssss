from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">

<style>

/* --- Body & Gradient Background --- */
body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(135deg, #c8facc, #a8e063, #87ceeb, #fff176);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-family: 'Montserrat', sans-serif;
    text-align: center;
    overflow: hidden;
    color: #ffffff;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* --- Cinematic Farm Light Streaks --- */
.streak {
    position: absolute;
    width: 3px;
    height: 60px;
    background: linear-gradient(to top, rgba(255,223,107,0.7), rgba(255,243,175,0.0));
    border-radius: 50%;
    animation: floatStreak 8s linear infinite;
}

@keyframes floatStreak {
    0% {transform: translateY(0) translateX(0) rotate(0deg);}
    50% {transform: translateY(-120vh) translateX(30px) rotate(10deg);}
    100% {transform: translateY(0) translateX(-30px) rotate(-10deg);}
}

/* --- Headings & Text --- */
h1 {
    font-family: 'Playfair Display', serif;
    font-size: 56px;
    margin-top: 20px;
    font-weight: 700;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}

h2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 28px;
    margin-top: 8px;
    opacity: 0.95;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.25);
}

/* --- Footer --- */
.footer {
    position: absolute;
    bottom: 15px;
    right: 20px;
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    color: #000000; /* black royal */
}

/* --- Button --- */
.enter-btn {
    margin-top: 40px;
    padding: 14px 50px;
    border-radius: 30px;
    border: none;
    background: linear-gradient(45deg, #fdd835, #fbc02d);
    color: #2f6f2f;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transition: 0.3s;
}

.enter-btn:hover {
    transform: scale(1.08);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

</style>
</head>

<body>

<!-- Cinematic farm streaks -->
<div class="streak" style="bottom:0; left:10%; animation-delay:0s;"></div>
<div class="streak" style="bottom:0; left:25%; animation-delay:1s;"></div>
<div class="streak" style="bottom:0; left:40%; animation-delay:2s;"></div>
<div class="streak" style="bottom:0; left:55%; animation-delay:3s;"></div>
<div class="streak" style="bottom:0; left:70%; animation-delay:4s;"></div>
<div class="streak" style="bottom:0; left:85%; animation-delay:5s;"></div>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi</h2>

<button class="enter-btn">Enter App</button>

<div class="footer">Powered by PARTH'S INDUSTRIES</div>

</body>
</html>
"""
from flask import Flask

app = Flask(__name__)

# =====================
# CATEGORY 1: CROP MANAGEMENT TOOLS
# =====================
def crop_management_tools():
    tools_output = []

    # 1️⃣ Crop Planner
    crop_name = 'गेहूं / Wheat'
    field_area = 2  # acres example
    water_needed = field_area * 1500  # liters approx
    fertilizer = 'NPK 20:20:20'
    tools_output.append(f"🌾 Crop Planner / फसल योजना:\nCrop / फसल: {crop_name}\nArea / क्षेत्रफल: {field_area} acres\nWater / पानी: {water_needed} liters\nFertilizer / उर्वरक: {fertilizer}")

    # 2️⃣ Soil Health Checker
    soil_moisture = 40  # % example
    ph_level = 6.5
    nutrients = 'Medium / मध्यम'
    tools_output.append(f"🌱 Soil Health Check / मिट्टी स्वास्थ्य:\nMoisture / नमी: {soil_moisture}%\nPH / पीएच: {ph_level}\nNutrients / पोषक तत्व: {nutrients}")

    # 3️⃣ Fertilizer Calculator
    soil_type = 'Loamy / दोमट'
    recommended_fert = 'Urea 46%'
    tools_output.append(f"🧴 Fertilizer Calculator / उर्वरक कैलकुलेटर:\nSoil Type / मिट्टी प्रकार: {soil_type}\nRecommended / सुझाव: {recommended_fert}")

    # 4️⃣ Seed Calculator
    seeds_needed = field_area * 8  # kg approx
    tools_output.append(f"🌱 Seed Calculator / बीज कैलकुलेटर:\nEstimated Seeds / अनुमानित बीज: {seeds_needed} kg")

    # 5️⃣ Irrigation Scheduler
    irrigation_freq = 'Every 3 days / हर 3 दिन'
    tools_output.append(f"💧 Irrigation Scheduler / सिंचाई समय सारणी:\nRecommended Frequency / सुझाई गई बार: {irrigation_freq}")

    # 6️⃣ Crop Rotation Advisor
    last_crop = 'मक्का / Maize'
    next_crop = 'दलहनी / Legumes'
    tools_output.append(f"🔄 Crop Rotation / फसल चक्रीकरण:\nLast Crop / पिछली फसल: {last_crop}\nRecommended Next Crop / अगली फसल: {next_crop}")

    # 7️⃣ Pest & Disease Guide
    pest_found = True
    pest_name = 'Aphids / एफिड्स' if pest_found else 'None / कोई नहीं'
    tools_output.append(f"🦠 Pest & Disease Guide / कीट और रोग मार्गदर्शिका:\nDetected / पता चला कीट: {pest_name}")

    # 8️⃣ Organic Tips
    organic_tip = 'Use compost instead of chemical fertilizer / रासायनिक उर्वरक की जगह कम्पोस्ट का प्रयोग करें'
    tools_output.append(f"🌱 Organic Tips / जैविक खेती सुझाव:\nTip / सुझाव: {organic_tip}")

    # 9️⃣ AI Farming Tips
    ai_tip = 'Use drone images to monitor crop health / ड्रोन इमेजरी से फसल स्वास्थ्य मॉनिटर करें'
    tools_output.append(f"🤖 AI Farming Tips / AI खेती सुझाव:\nTip / सुझाव: {ai_tip}")

    # 🔟 Crop Insurance Guide
    insurance_plan = 'Standard Plan / स्टैंडर्ड योजना'
    tools_output.append(f"📋 Crop Insurance Guide / फसल बीमा:\nRecommended Plan / सुझाई गई योजना: {insurance_plan}")

    return "\n\n".join(tools_output)

# Flask routes
@app.route("/")
def home():
    return """
    <h1>🌾 Kisan Saathi - Crop Management</h1>
    <a href='/tools'>Show Tools</a>
    """

@app.route("/tools")
def show_tools():
    return f"<pre>{crop_management_tools()}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
