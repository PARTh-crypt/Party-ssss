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
 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PARTH'S KISAN SAATHI - Crop Management</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(135deg, #87ceeb, #a8e063, #fff176, #f5a623);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:#222;
    text-align:center;
    min-height:100vh;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1{
    font-family:'Playfair Display', serif;
    font-size:48px;
    margin-top:20px;
    text-shadow:2px 2px 8px rgba(0,0,0,0.4);
}
h2{
    font-size:24px;
    margin-bottom:10px;
    text-shadow:1px 1px 6px rgba(0,0,0,0.3);
}
.tool-btn{
    margin:10px;
    padding:20px 25px;
    font-size:18px;
    border:none;
    border-radius:15px;
    background:rgba(255,255,255,0.25);
    cursor:pointer;
    text-shadow:1px 1px 2px #000;
    transition:0.3s;
}
.tool-btn:hover{
    background:rgba(255,255,255,0.45);
    transform:scale(1.05);
}
.card{
    background: rgba(255,255,255,0.85);
    margin: 20px auto;
    padding: 20px;
    border-radius: 15px;
    width: 90%;
    max-width: 500px;
    text-align:left;
}
input, select{
    padding:8px;
    margin:5px 0 15px 0;
    width:90%;
    font-size:16px;
}
button.calc-btn{
    padding:10px 20px;
    font-size:16px;
    cursor:pointer;
    border:none;
    border-radius:10px;
    background: linear-gradient(45deg,#fdd835,#fbc02d);
}
.result{
    margin-top:15px;
    font-weight:bold;
    font-size:18px;
    color:#1e3c72;
}
</style>
</head>
<body>
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Crop Management / फ़सल प्रबंधन</h2>

<div id="tools">
    <button class="tool-btn" onclick="showTool(1)">1️⃣ Crop Yield Estimator</button>
    <button class="tool-btn" onclick="showTool(2)">2️⃣ Soil Nutrient Balancer</button>
    <button class="tool-btn" onclick="showTool(3)">3️⃣ Water Demand Calculator</button>
    <button class="tool-btn" onclick="showTool(4)">4️⃣ Irrigation Interval Predictor</button>
    <button class="tool-btn" onclick="showTool(5)">5️⃣ Crop Rotation Planner</button>
    <button class="tool-btn" onclick="showTool(6)">6️⃣ Pest Risk Score</button>
    <button class="tool-btn" onclick="showTool(7)">7️⃣ Growth Stage Advisor</button>
    <button class="tool-btn" onclick="showTool(8)">8️⃣ Harvest Time Predictor</button>
    <button class="tool-btn" onclick="showTool(9)">9️⃣ Fertilizer Efficiency Checker</button>
    <button class="tool-btn" onclick="showTool(10)">🔟 Profit Forecast Tool</button>
</div>

<div id="tool-card" class="card" style="display:none;"></div>

<script>
function showTool(id){
    const card = document.getElementById('tool-card');
    card.style.display='block';
    let html = '';
    if(id==1){
        html = `
        <h3>🌾 Crop Yield Estimator</h3>
        <p>Theory / सैद्धांतिक: Estimates yield based on area, seed & rainfall.</p>
        Area (acres / एकड़): <input id="area" type="number"><br>
        Seed rate (kg/acre / बीज दर): <input id="seed" type="number"><br>
        Rainfall (mm / वर्षा): <input id="rain" type="number"><br>
        <button class="calc-btn" onclick="calcYield()">Calculate / गणना</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==2){
        html = `
        <h3>🧪 Soil Nutrient Balancer</h3>
        <p>Theory / सैद्धांतिक: Adjust nutrients based on soil pH.</p>
        Soil pH / मिट्टी pH: <input id="ph" type="number"><br>
        <button class="calc-btn" onclick="calcSoil()">Check / जाँच</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==3){
        html = `
        <h3>💧 Water Demand Calculator</h3>
        <p>Theory / सैद्धांतिक: Calculates water need based on temperature.</p>
        Temperature °C / तापमान: <input id="temp" type="number"><br>
        <button class="calc-btn" onclick="calcWater()">Calculate / गणना</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==4){
        html = `
        <h3>📅 Irrigation Interval Predictor</h3>
        <p>Theory / सैद्धांतिक: Suggest irrigation frequency based on soil type.</p>
        Soil type / मिट्टी का प्रकार:
        <select id="soil">
            <option value="sandy">Sandy / रेतीली</option>
            <option value="loamy">Loamy / दोमट</option>
            <option value="clay">Clay / चिकनी</option>
        </select><br>
        <button class="calc-btn" onclick="calcIrrigation()">Predict / अनुमान</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==5){
        html = `
        <h3>🌿 Crop Rotation Planner</h3>
        <p>Theory / सैद्धांतिक: Suggests next crop for soil fertility.</p>
        Last crop / पिछली फसल:
        <select id="lastcrop">
            <option value="wheat">Wheat / गेहूँ</option>
            <option value="rice">Rice / चावल</option>
            <option value="maize">Maize / मक्का</option>
        </select><br>
        <button class="calc-btn" onclick="calcRotation()">Suggest / सुझाएँ</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==6){
        html = `
        <h3>🦠 Pest Risk Score</h3>
        <p>Theory / सैद्धांतिक: Risk based on humidity & temperature.</p>
        Humidity % / आर्द्रता %: <input id="hum" type="number"><br>
        Temperature °C / तापमान: <input id="temp2" type="number"><br>
        <button class="calc-btn" onclick="calcPest()">Check / जाँच</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==7){
        html = `
        <h3>🌾 Growth Stage Advisor</h3>
        <p>Theory / सैद्धांतिक: Advises action based on crop age.</p>
        Crop age (days / दिन): <input id="age" type="number"><br>
        <button class="calc-btn" onclick="calcGrowth()">Check / जाँच</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==8){
        html = `
        <h3>🌾 Harvest Time Predictor</h3>
        <p>Theory / सैद्धांतिक: Checks if crop ready for harvest.</p>
        Crop type / फसल: 
        <select id="crop">
            <option value="wheat">Wheat / गेहूँ</option>
            <option value="rice">Rice / चावल</option>
        </select><br>
        Crop age (days / दिन): <input id="age2" type="number"><br>
        <button class="calc-btn" onclick="calcHarvest()">Check / जाँच</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==9){
        html = `
        <h3>🧪 Fertilizer Efficiency Checker</h3>
        <p>Theory / सैद्धांतिक: Output per fertilizer input.</p>
        Fertilizer kg / उर्वरक: <input id="fert" type="number"><br>
        Yield quintal / उत्पादन: <input id="yield1" type="number"><br>
        <button class="calc-btn" onclick="calcFert()">Check / जाँच</button>
        <div class="result" id="res"></div>
        `;
    }
    else if(id==10){
        html = `
        <h3>💰 Profit Forecast Tool</h3>
        <p>Theory / सैद्धांतिक: Profit based on yield & market price.</p>
        Yield quintal / उत्पादन: <input id="yield2" type="number"><br>
        Price per quintal ₹ / कीमत: <input id="price" type="number"><br>
        Total cost ₹ / कुल खर्च: <input id="cost" type="number"><br>
        <button class="calc-btn" onclick="calcProfit()">Calculate / गणना</button>
        <div class="result" id="res"></div>
        `;
    }
    card.innerHTML = html;
}

// ================= JS Calculations =================
function calcYield(){
    let area=parseFloat(document.getElementById('area').value);
    let seed=parseFloat(document.getElementById('seed').value);
    let rain=parseFloat(document.getElementById('rain').value);
    let y=area*seed*(rain/500);
    document.getElementById('res').innerText='Estimated Yield / अनुमानित उत्पादन: '+y.toFixed(2)+' quintals';
}
function calcSoil(){
    let ph=parseFloat(document.getElementById('ph').value);
    let res='';
    if(ph<6) res='Soil acidic → Add Lime + Compost';
    else if(ph>7.5) res='Soil alkaline → Add Organic manure';
    else res='Soil balanced → Standard fertilizer dose';
    document.getElementById('res').innerText=res;
}
function calcWater(){
    let temp=parseFloat(document.getElementById('temp').value);
    let base=6000;
    if(temp>35) base*=1.2;
    else if(temp<20) base*=0.9;
    document.getElementById('res').innerText='Water Requirement: '+Math.round(base)+' liters/acre/day';
}
function calcIrrigation(){
    let soil=document.getElementById('soil').value;
    let res='';
    if(soil=='sandy') res='Irrigate every 4 days';
    else if(soil=='clay') res='Irrigate every 8 days';
    else res='Irrigate every 6 days';
    document.getElementById('res').innerText=res;
}
function calcRotation(){
    let crop=document.getElementById('lastcrop').value;
    let rotation={'wheat':'Plant legumes next','rice':'Plant maize next','maize':'Plant wheat next'};
    document.getElementById('res').innerText=rotation[crop];
}
function calcPest(){
    let hum=parseFloat(document.getElementById('hum').value);
    let temp=parseFloat(document.getElementById('temp2').value);
    let risk=(hum/100)*temp;
    let msg=risk>25?'⚠ High Pest Risk':'Low to Moderate Risk';
    document.getElementById('res').innerText='Pest Risk Score: '+risk.toFixed(2)+' → '+msg;
}
function calcGrowth(){
    let age=parseInt(document.getElementById('age').value);
    let stage='';
    if(age<30) stage='Vegetative Stage → Focus on nitrogen';
    else if(age<60) stage='Flowering Stage → Balanced nutrients';
    else stage='Maturity Stage → Reduce irrigation';
    document.getElementById('res').innerText=stage;
}
function calcHarvest(){
    let crop=document.getElementById('crop').value;
    let age=parseInt(document.getElementById('age2').value);
    let ready=false;
    if(crop=='wheat' && age>=120) ready=true;
    else if(crop=='rice' && age>=150) ready=true;
    document.getElementById('res').innerText=ready?'Ready for harvest / कटाई के लिए तैयार':'Not ready yet / अभी तैयार नहीं';
}
function calcFert(){
    let fert=parseFloat(document.getElementById('fert').value);
    let y=parseFloat(document.getElementById('yield1').value);
    let eff=(y/fert)*100;
    document.getElementById('res').innerText='Efficiency: '+eff.toFixed(2)+'%';
}
function calcProfit(){
    let y=parseFloat(document.getElementById('yield2').value);
    let p=parseFloat(document.getElementById('price').value);
    let c=parseFloat(document.getElementById('cost').value);
    let profit=(y*p)-c;
    document.getElementById('res').innerText='Estimated Profit / अनुमानित लाभ: ₹'+profit.toFixed(2);
}
</script>
</body>
</html>
