from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
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
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}
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
.footer {
    position: absolute;
    bottom: 15px;
    right: 20px;
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    color: #000000;
}
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

<!-- Cinematic streaks -->
<div class="streak" style="bottom:0; left:10%; animation-delay:0s;"></div>
<div class="streak" style="bottom:0; left:25%; animation-delay:1s;"></div>
<div class="streak" style="bottom:0; left:40%; animation-delay:2s;"></div>
<div class="streak" style="bottom:0; left:55%; animation-delay:3s;"></div>
<div class="streak" style="bottom:0; left:70%; animation-delay:4s;"></div>
<div class="streak" style="bottom:0; left:85%; animation-delay:5s;"></div>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>हर किसान का डिजिटल साथी / Har Kisan Ka Digital Saathi</h2>

<button class="enter-btn" onclick="alert('Next screen loading...')">Enter App</button>

<div class="footer">Powered by PARTH'S</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, render_template_string

app = Flask(__name__)

# ==============================
# CATEGORY 1 – 🌾 CROP MANAGEMENT TOOLS
# ==============================

def soil_type_checker():
    return "🌱 Soil Type Checker / मिट्टी का प्रकार जानें\n- Choose color: Red/Black/Yellow\n- Loamy, Clayey, Sandy detected"

def crop_suggestion():
    return "🌾 Crop Suggestion / फ़सल सुझाव\n- Based on soil: Wheat, Maize, Rice, Groundnut"

def sowing_time_advisor():
    return "⏰ Sowing Time Advisor / बुवाई समय सलाहकार\n- Wheat: Oct-Nov\n- Rice: Jun-Jul\n- Maize: Jun-Jul"

def fertilizer_recommendation():
    return "💊 Fertilizer Recommendation / उर्वरक सुझाव\n- Loamy: NPK 10:10:10\n- Clayey: Urea 50kg/acre"

def irrigation_planner():
    return "💧 Irrigation Planner / सिंचाई योजना\n- Wheat: every 15 days\n- Rice: every 7 days"

def pest_early_warning():
    return "🐛 Pest Early Warning / कीट चेतावनी\n- Holes: Caterpillar\n- Yellow leaves: Aphids"

def crop_health_checker():
    return "📷 Crop Health Checker / फ़सल स्वास्थ्य जांच\n- Camera optional\n- Observe leaves, spots, color"

def harvest_time_advisor():
    return "⏳ Harvest Time Advisor / कटाई समय सलाहकार\n- Wheat: Apr-May\n- Rice: Oct-Nov"

def seed_quality_checker():
    return "🌰 Seed Quality Checker / बीज गुणवत्ता जाँच\n- Good: uniform color, no cracks\n- Poor: discolored or broken"

def crop_rotation_planner():
    return "🔄 Crop Rotation Planner / फ़सल रोटेशन योजना\n- Example: Wheat -> Rice -> Maize\n- Prevents soil nutrient loss"

# Category tools dictionary
categories = {
    "1": {
        "name": "🌾 Crop Management",
        "tools": [
            soil_type_checker,
            crop_suggestion,
            sowing_time_advisor,
            fertilizer_recommendation,
            irrigation_planner,
            pest_early_warning,
            crop_health_checker,
            harvest_time_advisor,
            seed_quality_checker,
            crop_rotation_planner
        ]
    }
}

# ==============================
# HOME PAGE
# ==============================
@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body {
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: url('https://images.unsplash.com/photo-1500382017468-9049fed747ef') no-repeat center center fixed;
    background-size: cover;
    color:white;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    height:100vh;
    text-align:center;
}
.overlay{
    background:rgba(0,0,0,0.5);
    padding:40px;
    border-radius:25px;
}
button{
    margin:10px;
    padding:15px 30px;
    border:none;
    border-radius:25px;
    font-size:16px;
    cursor:pointer;
    font-weight:bold;
    background: linear-gradient(45deg,#fdd835,#fbc02d);
    color:#2f6f2f;
    transition:0.3s;
}
button:hover{
    transform:scale(1.05);
}
.tool-box{
    margin-top:20px;
    text-align:left;
    max-width:500px;
    background:rgba(255,255,255,0.2);
    padding:15px;
    border-radius:15px;
}
</style>
</head>
<body>

<div class="overlay">
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi</h2>

<h3>Categories / श्रेणियाँ</h3>
<button onclick="showTools('1')">{{categories['1']['name']}}</button>

<div id="tools" class="tool-box" style="display:none;"></div>
</div>

<script>
const categories = {{categories | tojson}};

function showTools(catId){
    const toolsDiv = document.getElementById('tools');
    toolsDiv.innerHTML = '';
    categories[catId].tools.forEach((tool, idx) => {
        let toolName = tool(); // call function
        let p = document.createElement('p');
        p.innerText = (idx+1) + '. ' + toolName;
        toolsDiv.appendChild(p);
    });
    toolsDiv.style.display='block';
}
</script>

</body>
</html>
""", categories=categories)

# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    app.run(debug=True)
