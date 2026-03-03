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
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg,#1e3c72,#2a5298,#ff7e5f,#feb47b);
    background-size: 400% 400%;
    animation:bgMove 20s ease infinite;
    color:white;
    text-align:center;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1,h2{margin:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.5);}
h2{font-size:24px;}
.button{
    margin:10px;
    padding:15px 25px;
    font-size:18px;
    border:none;
    border-radius:20px;
    cursor:pointer;
    background:rgba(255,255,255,0.25);
    color:white;
    text-shadow:1px 1px 3px rgba(0,0,0,0.4);
    transition:0.3s;
}
.button:hover{background:rgba(255,255,255,0.45); transform:scale(1.05);}
.tool-container{display:none; margin-top:20px;}
.tool{background:rgba(0,0,0,0.35); padding:20px; margin:15px auto; border-radius:15px; width:80%;}
input[type=number]{padding:8px; border-radius:8px; border:none; margin:5px 0; width:80px;}
select{padding:8px; border-radius:8px; border:none; margin:5px;}
.result{margin-top:10px; font-weight:bold;}
</style>
</head>
<body>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>किसान डैशबोर्ड / Farmer Dashboard</h2>

<div id="dashboard">
    <button class="button" onclick="openCategory()">🌾 Crop Management / फ़सल प्रबंधन</button>
</div>

<div id="category1" class="tool-container">
    <h2>Crop Management Tools / फ़सल प्रबंधन टूल्स</h2>
    <div class="tool">
        <h3>1️⃣ Crop Yield Estimator</h3>
        <p>Theory: Estimates yield based on area, seed rate & rainfall.</p>
        Area (acres): <input type="number" id="area1"><br>
        Seed rate (kg/acre): <input type="number" id="seed1"><br>
        Rainfall (mm): <input type="number" id="rain1"><br>
        <button class="button" onclick="calcYield()">Calculate / अनुमानित उत्पादन</button>
        <div class="result" id="res1"></div>
    </div>

    <div class="tool">
        <h3>2️⃣ Soil Nutrient Balancer</h3>
        <p>Theory: Adjusts nutrient based on soil pH.</p>
        Soil pH: <input type="number" step="0.1" id="ph2"><br>
        <button class="button" onclick="checkSoil()">Check / जाँचें</button>
        <div class="result" id="res2"></div>
    </div>

    <div class="tool">
        <h3>3️⃣ Water Demand Calculator</h3>
        <p>Theory: Calculates water need based on temperature.</p>
        Temperature °C: <input type="number" id="temp3"><br>
        <button class="button" onclick="calcWater()">Calculate / पानी आवश्यकता</button>
        <div class="result" id="res3"></div>
    </div>

    <div class="tool">
        <h3>4️⃣ Irrigation Interval Predictor</h3>
        <p>Theory: Suggests irrigation frequency based on soil type.</p>
        Soil Type: 
        <select id="soil4">
            <option value="sandy">Sandy / रेतीला</option>
            <option value="loamy">Loamy / दोमट</option>
            <option value="clay">Clay / चिकनी मिट्टी</option>
        </select><br>
        <button class="button" onclick="irrigate()">Predict / सिंचाई अंतराल</button>
        <div class="result" id="res4"></div>
    </div>

    <div class="tool">
        <h3>5️⃣ Crop Rotation Planner</h3>
        <p>Theory: Suggests next crop for soil fertility.</p>
        Last Crop: 
        <select id="crop5">
            <option value="wheat">Wheat / गेहूँ</option>
            <option value="rice">Rice / चावल</option>
            <option value="maize">Maize / मक्का</option>
        </select><br>
        <button class="button" onclick="rotateCrop()">Suggest / सुझाव</button>
        <div class="result" id="res5"></div>
    </div>

    <div class="tool">
        <h3>6️⃣ Pest Risk Score</h3>
        <p>Theory: Estimates pest attack probability based on humidity & temp.</p>
        Humidity %: <input type="number" id="hum6"><br>
        Temperature °C: <input type="number" id="temp6"><br>
        <button class="button" onclick="pestRisk()">Check / जोखिम</button>
        <div class="result" id="res6"></div>
    </div>

    <div class="tool">
        <h3>7️⃣ Growth Stage Advisor</h3>
        <p>Theory: Advises action based on crop age.</p>
        Crop Age (days): <input type="number" id="age7"><br>
        <button class="button" onclick="growthStage()">Check / जाँचें</button>
        <div class="result" id="res7"></div>
    </div>

    <div class="tool">
        <h3>8️⃣ Harvest Time Predictor</h3>
        <p>Theory: Suggests if crop ready for harvest.</p>
        Crop: 
        <select id="crop8">
            <option value="wheat">Wheat / गेहूँ</option>
            <option value="rice">Rice / चावल</option>
            <option value="maize">Maize / मक्का</option>
        </select><br>
        Crop Age (days): <input type="number" id="age8"><br>
        <button class="button" onclick="harvestCheck()">Check / जाँचें</button>
        <div class="result" id="res8"></div>
    </div>

    <div class="tool">
        <h3>9️⃣ Fertilizer Efficiency Checker</h3>
        <p>Theory: Measures output yield per fertilizer input.</p>
        Fertilizer (kg): <input type="number" id="fert9"><br>
        Yield (quintal): <input type="number" id="yield9"><br>
        <button class="button" onclick="fertEff()">Check / जाँचें</button>
        <div class="result" id="res9"></div>
    </div>

    <div class="tool">
        <h3>🔟 Profit Forecast Tool</h3>
        <p>Theory: Predicts profit based on yield & market price.</p>
        Yield (quintal): <input type="number" id="yield10"><br>
        Price per quintal ₹: <input type="number" id="price10"><br>
        Total Cost ₹: <input type="number" id="cost10"><br>
        <button class="button" onclick="profitCalc()">Calculate / अनुमानित लाभ</button>
        <div class="result" id="res10"></div>
    </div>

    <button class="button" onclick="backToDash()">⬅ Back to Dashboard / डैशबोर्ड</button>
</div>

<script>
function openCategory(){
    document.getElementById("dashboard").style.display="none";
    document.getElementById("category1").style.display="block";
}
function backToDash(){
    document.getElementById("category1").style.display="none";
    document.getElementById("dashboard").style.display="block";
}

// Tool Functions
function calcYield(){
    let area = parseFloat(document.getElementById("area1").value);
    let seed = parseFloat(document.getElementById("seed1").value);
    let rain = parseFloat(document.getElementById("rain1").value);
    let res = area * seed * (rain/500);
    document.getElementById("res1").innerHTML = "Estimated Yield / अनुमानित उत्पादन: "+res.toFixed(2)+" quintals";
}

function checkSoil(){
    let ph = parseFloat(document.getElementById("ph2").value);
    let res="";
    if(ph<6) res="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + खाद डालें";
    else if(ph>7.5) res="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → जैविक खाद डालें";
    else res="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → सामान्य खाद";
    document.getElementById("res2").innerHTML=res;
}

function calcWater(){
    let temp=parseFloat(document.getElementById("temp3").value);
    let base=6000;
    if(temp>35) base*=1.2;
    else if(temp<20) base*=0.9;
    document.getElementById("res3").innerHTML="Water Requirement / पानी आवश्यकता: "+Math.round(base)+" liters/acre/day";
}

function irrigate(){
    let soil=document.getElementById("soil4").value;
    let res="";
    if(soil=="sandy") res="Irrigate every 4 days / हर 4 दिन सिंचाई करें";
    else if(soil=="clay") res="Irrigate every 8 days / हर 8 दिन सिंचाई करें";
    else res="Irrigate every 6 days / हर 6 दिन सिंचाई करें";
    document.getElementById("res4").innerHTML=res;
}

function rotateCrop(){
    let crop=document.getElementById("crop5").value;
    let map={"wheat":"Plant legumes next / अगली फसल दालें लगाएँ","rice":"Plant maize next / अगली फसल मक्का","maize":"Plant wheat next / अगली फसल गेहूँ"};
    document.getElementById("res5").innerHTML=map[crop];
}

function pestRisk(){
    let hum=parseFloat(document.getElementById("hum6").value);
    let temp=parseFloat(document.getElementById("temp6").value);
    let risk=(hum/100)*temp;
    let status=risk>25?"High Pest Risk / उच्च कीट जोखिम":"Low to Moderate Risk / कम-मध्यम जोखिम";
    document.getElementById("res6").innerHTML="Pest Risk Score / कीट जोखिम: "+risk.toFixed(2)+" → "+status;
}

function growthStage(){
    let age=parseInt(document.getElementById("age7").value);
    let res="";
    if(age<30) res="Vegetative Stage → Focus on nitrogen / पौध अवस्था → नाइट्रोजन पर ध्यान दें";
    else if(age<60) res="Flowering Stage → Balanced nutrients / फूल आने का चरण → संतुलित पोषक तत्व";
    else res="Maturity Stage → Reduce irrigation / परिपक्वता → सिंचाई कम करें";
    document.getElementById("res7").innerHTML=res;
}

function harvestCheck(){
    let crop=document.getElementById("crop8").value;
    let age=parseInt(document.getElementById("age8").value);
    let res="";
    if(crop=="wheat" && age>=120) res="Ready for harvest / कटाई के लिए तैयार";
    else if(crop=="rice" && age>=150) res="Ready for harvest / कटाई के लिए तैयार";
    else res="Not ready yet / अभी तैयार नहीं";
    document.getElementById("res8").innerHTML=res;
}

function fertEff(){
    let fert=parseFloat(document.getElementById("fert9").value);
    let yieldAmt=parseFloat(document.getElementById("yield9").value);
    let eff=(yieldAmt/fert)*100;
    document.getElementById("res9").innerHTML="Efficiency / दक्षता: "+eff.toFixed(2)+"%";
}

function profitCalc(){
    let y=parseFloat(document.getElementById("yield10").value);
    let p=parseFloat(document.getElementById("price10").value);
    let c=parseFloat(document.getElementById("cost10").value);
    let profit=(y*p)-c;
    document.getElementById("res10").innerHTML="Estimated Profit / अनुमानित लाभ: ₹"+profit.toFixed(2);
}
</script>

</body>
</html>
