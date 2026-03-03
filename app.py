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
<title>Parth's Kisan Saathi - Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    text-align:center;
    color:white;
    background: linear-gradient(135deg,#1e3c72,#2a5298,#6dd5ed,#2193b0);
    background-size:400% 400%;
    animation:bgMove 20s ease infinite;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1{
    font-family:'Playfair Display', serif;
    margin:30px 0;
}
.card{
    width:90%;
    max-width:500px;
    margin:20px auto;
    padding:25px;
    border-radius:20px;
    background:rgba(0,0,0,0.35);
    font-size:20px;
    cursor:pointer;
    transition:0.3s;
}
.card:hover{
    background:rgba(0,0,0,0.55);
    transform:scale(1.03);
}
button{
    padding:10px 25px;
    margin-top:15px;
    border:none;
    border-radius:10px;
    font-weight:bold;
    cursor:pointer;
    background: linear-gradient(45deg,#fdd835,#fbc02d);
    color:#2f6f2f;
}
button:hover{
    transform:scale(1.05);
}
input{
    padding:6px;
    margin:5px;
    border-radius:5px;
    border:none;
}
form{
    margin-top:20px;
}
.result{
    margin-top:15px;
    font-size:18px;
    color:#ffeb3b;
}
a{
    text-decoration:none;
    color:white;
}
</style>
</head>
<body>

<h1>Dashboard / डैशबोर्ड</h1>

<div class="card" onclick="showTools()">🌾 Crop Management / फ़सल प्रबंधन</div>

<div id="tools" style="display:none;">
<h2>Crop Tools / फ़सल टूल्स</h2>

<div class="card" onclick="showForm(1)">1️⃣ Crop Yield Estimator / फ़सल अनुमान</div>
<div class="card" onclick="showForm(2)">2️⃣ Soil Nutrient Balancer / मिट्टी पोषण</div>
<div class="card" onclick="showForm(3)">3️⃣ Water Demand Calculator / जल आवश्यकता</div>
<div class="card" onclick="showForm(4)">4️⃣ Irrigation Interval Predictor / सिंचाई अंतराल</div>
<div class="card" onclick="showForm(5)">5️⃣ Crop Rotation Planner / फ़सल चक्र योजना</div>
<div class="card" onclick="showForm(6)">6️⃣ Pest Risk Score / कीट जोखिम</div>
<div class="card" onclick="showForm(7)">7️⃣ Growth Stage Advisor / विकास अवस्था</div>
<div class="card" onclick="showForm(8)">8️⃣ Harvest Time Predictor / कटाई समय</div>
<div class="card" onclick="showForm(9)">9️⃣ Fertilizer Efficiency Checker / उर्वरक दक्षता</div>
<div class="card" onclick="showForm(10)">🔟 Profit Forecast Tool / लाभ पूर्वानुमान</div>

<button onclick="hideTools()">⬅ Back to Dashboard / डैशबोर्ड पर वापस</button>

<div id="formContainer"></div>
</div>

<script>
function showTools(){
    document.getElementById('tools').style.display='block';
    window.scrollTo(0,0);
}
function hideTools(){
    document.getElementById('tools').style.display='none';
    document.getElementById('formContainer').innerHTML='';
}

function showForm(id){
    let html='';
    if(id==1){
        html=`<h3>🌾 Crop Yield Estimator / फ़सल अनुमान</h3>
        <p>Enter area, seed rate & rainfall / क्षेत्र, बीज दर और वर्षा दर्ज करें</p>
        Area (acres): <input id="area"><br>
        Seed rate (kg/acre): <input id="seed"><br>
        Rainfall (mm): <input id="rain"><br>
        <button onclick="calcYield()">Calculate / गणना</button>
        <div class="result" id="res"></div>`;
    }else if(id==2){
        html=`<h3>🧪 Soil Nutrient Balancer / मिट्टी पोषण</h3>
        Soil pH: <input id="ph"><br>
        <button onclick="checkSoil()">Check / जाँचें</button>
        <div class="result" id="res"></div>`;
    }else if(id==3){
        html=`<h3>💧 Water Demand Calculator / जल आवश्यकता</h3>
        Temperature °C: <input id="temp"><br>
        <button onclick="calcWater()">Calculate / गणना</button>
        <div class="result" id="res"></div>`;
    }else if(id==4){
        html=`<h3>📅 Irrigation Interval Predictor / सिंचाई अंतराल</h3>
        Soil (sandy/loamy/clay): <input id="soil"><br>
        <button onclick="predictIrr()">Predict / पूर्वानुमान</button>
        <div class="result" id="res"></div>`;
    }else if(id==5){
        html=`<h3>🌿 Crop Rotation Planner / फ़सल चक्र योजना</h3>
        Last Crop: <input id="crop"><br>
        <button onclick="rotation()">Suggest / सुझाव</button>
        <div class="result" id="res"></div>`;
    }else if(id==6){
        html=`<h3>🦠 Pest Risk Score / कीट जोखिम</h3>
        Humidity %: <input id="hum"><br>
        Temperature °C: <input id="temp2"><br>
        <button onclick="pestRisk()">Check / जाँचें</button>
        <div class="result" id="res"></div>`;
    }else if(id==7){
        html=`<h3>🌾 Growth Stage Advisor / विकास अवस्था</h3>
        Crop age (days): <input id="age"><br>
        <button onclick="growthStage()">Check / जाँचें</button>
        <div class="result" id="res"></div>`;
    }else if(id==8){
        html=`<h3>🌾 Harvest Time Predictor / कटाई समय</h3>
        Crop type: <input id="ctype"><br>
        Crop age (days): <input id="age2"><br>
        <button onclick="harvest()">Check / जाँचें</button>
        <div class="result" id="res"></div>`;
    }else if(id==9){
        html=`<h3>🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता</h3>
        Fertilizer (kg): <input id="fert"><br>
        Yield (quintal): <input id="yield"><br>
        <button onclick="fertCheck()">Check / जाँचें</button>
        <div class="result" id="res"></div>`;
    }else if(id==10){
        html=`<h3>💰 Profit Forecast Tool / लाभ पूर्वानुमान</h3>
        Yield (quintal): <input id="yield2"><br>
        Price per quintal ₹: <input id="price"><br>
        Total cost ₹: <input id="cost"><br>
        <button onclick="profit()">Calculate / गणना</button>
        <div class="result" id="res"></div>`;
    }
    document.getElementById('formContainer').innerHTML=html;
}

function calcYield(){
    let area=parseFloat(document.getElementById('area').value);
    let seed=parseFloat(document.getElementById('seed').value);
    let rain=parseFloat(document.getElementById('rain').value);
    let res=Math.round(area*seed*(rain/500)*100)/100;
    document.getElementById('res').innerHTML=`Estimated Yield / अनुमानित उत्पादन: ${res} quintals`;
}
function checkSoil(){
    let ph=parseFloat(document.getElementById('ph').value);
    let r='';
    if(ph<6) r="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कम्पोस्ट डालें";
    else if(ph>7.5) r="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → कार्बनिक खाद डालें";
    else r="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → सामान्य उर्वरक";
    document.getElementById('res').innerHTML=r;
}
function calcWater(){
    let temp=parseFloat(document.getElementById('temp').value);
    let base=6000;
    if(temp>35) base*=1.2;
    else if(temp<20) base*=0.9;
    document.getElementById('res').innerHTML=`Water Requirement / जल आवश्यकता: ${Math.round(base)} liters/acre/day`;
}
function predictIrr(){
    let soil=document.getElementById('soil').value.toLowerCase();
    let r='';
    if(soil=='sandy') r="Irrigate every 4 days / हर 4 दिन सिंचाई करें";
    else if(soil=='clay') r="Irrigate every 8 days / हर 8 दिन सिंचाई करें";
    else r="Irrigate every 6 days / हर 6 दिन सिंचाई करें";
    document.getElementById('res').innerHTML=r;
}
function rotation(){
    let last=document.getElementById('crop').value.toLowerCase();
    let rotation={"wheat":"Plant legumes next / अगली फसल दलहनी","rice":"Plant maize next / अगली फसल मक्का","maize":"Plant wheat next / अगली फसल गेहूं"};
    let r=rotation[last]||"Plant legumes for soil recovery / मिट्टी सुधार के लिए दलहनी लगाएं";
    document.getElementById('res').innerHTML=r;
}
function pestRisk(){
    let hum=parseFloat(document.getElementById('hum').value);
    let temp=parseFloat(document.getElementById('temp2').value);
    let risk=(hum/100)*temp;
    let r=risk>25?"⚠ High Pest Risk / उच्च कीट जोखिम":"Low to Moderate Risk / कम या मध्यम जोखिम";
    document.getElementById('res').innerHTML=`Pest Risk Score / कीट जोखिम स्कोर: ${risk.toFixed(2)}<br>${r}`;
}
function growthStage(){
    let age=parseInt(document.getElementById('age').value);
    let r=age<30?"Vegetative Stage → Focus on nitrogen / पौधे की वृद्धि चरण → नाइट्रोजन पर ध्यान दें":
          age<60?"Flowering Stage → Balanced nutrients / फूल आने का चरण → संतुलित पोषण":
          "Maturity Stage → Reduce irrigation / परिपक्वता चरण → सिंचाई कम करें";
    document.getElementById('res').innerHTML=r;
}
function harvest(){
    let crop=document.getElementById('ctype').value.toLowerCase();
    let age=parseInt(document.getElementById('age2').value);
    let r=(crop=="wheat" && age>=120)||(crop=="rice" && age>=150)?"Ready for harvest / कटाई के लिए तैयार":"Not ready yet / अभी तैयार नहीं";
    document.getElementById('res').innerHTML=r;
}
function fertCheck(){
    let fert=parseFloat(document.getElementById('fert').value);
    let yieldAmt=parseFloat(document.getElementById('yield').value);
    let eff=(yieldAmt/fert)*100;
    document.getElementById('res').innerHTML=`Efficiency / दक्षता: ${eff.toFixed(2)}%`;
}
function profit(){
    let yieldAmt=parseFloat(document.getElementById('yield2').value);
    let price=parseFloat(document.getElementById('price').value);
    let cost=parseFloat(document.getElementById('cost').value);
    let profit=(yieldAmt*price)-cost;
    document.getElementById('res').innerHTML=`Estimated Profit / अनुमानित लाभ: ₹${profit.toFixed(2)}`;
}
</script>
</body>
</html>
 """
 <!-- =========================
Dashboard + Crop Tools
========================= -->
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI - Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg,#1e3c72,#2a5298,#6dd5ed,#2193b0);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white;
    text-align:center;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1{margin-top:30px; font-family:'Playfair Display', serif;}
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
.card:hover{background:rgba(255,255,255,0.35); transform:scale(1.03);}
button{
    padding:10px 20px;
    margin-top:10px;
    border-radius:10px;
    border:none;
    background:linear-gradient(45deg,#fdd835,#fbc02d);
    color:#2f6f2f;
    font-weight:bold;
    cursor:pointer;
}
button:hover{transform:scale(1.05);}
input{padding:5px; margin:5px;}
.hidden{display:none;}
</style>
</head>
<body>

<div id="dashboard">
<h1>Dashboard / डैशबोर्ड</h1>

<div class="card" onclick="openTool('tool1')">🌾 Crop Yield Estimator / फ़सल अनुमान</div>
<div class="card" onclick="openTool('tool2')">🧪 Soil Nutrient Balancer / मिट्टी पोषण संतुलन</div>
<div class="card" onclick="openTool('tool3')">💧 Water Demand Calculator / जल आवश्यकता कैलकुलेटर</div>
<div class="card" onclick="openTool('tool4')">📅 Irrigation Interval Predictor / सिंचाई अंतराल पूर्वानुमान</div>
<div class="card" onclick="openTool('tool5')">🌿 Crop Rotation Planner / फ़सल चक्र योजना</div>
<div class="card" onclick="openTool('tool6')">🦠 Pest Risk Score / कीट जोखिम मूल्यांकन</div>
<div class="card" onclick="openTool('tool7')">🌾 Growth Stage Advisor / विकास अवस्था सलाहकार</div>
<div class="card" onclick="openTool('tool8')">🌾 Harvest Time Predictor / कटाई समय पूर्वानुमान</div>
<div class="card" onclick="openTool('tool9')">🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच</div>
<div class="card" onclick="openTool('tool10')">💰 Profit Forecast Tool / लाभ पूर्वानुमान</div>
</div>

<!-- =========================
Tool Section
========================= -->
<div id="tools" class="hidden">
<h1 id="toolTitle"></h1>
<div id="toolTheory"></div>
<div id="toolForm"></div>
<div id="toolResult"></div>
<button onclick="backToDashboard()">⬅ Back to Dashboard / डैशबोर्ड पर वापस</button>
</div>

<script>
const toolsData = {
"tool1":{
"title":"🌾 Crop Yield Estimator / फ़सल अनुमान",
"theory":"Estimates yield based on area, seed rate & rainfall.",
"form":"Area (acres): <input id='area' type='number'><br>Seed rate (kg/acre): <input id='seed' type='number'><br>Rainfall (mm): <input id='rain' type='number'><br><button onclick='calcYield()'>Calculate</button>"
},
"tool2":{
"title":"🧪 Soil Nutrient Balancer / मिट्टी पोषण संतुलन",
"theory":"Adjusts nutrients based on soil pH.",
"form":"Soil pH: <input id='ph' type='number'><br><button onclick='checkSoil()'>Check</button>"
},
"tool3":{
"title":"💧 Water Demand Calculator / जल आवश्यकता कैलकुलेटर",
"theory":"Calculates water need based on temperature.",
"form":"Temperature °C: <input id='temp' type='number'><br><button onclick='calcWater()'>Calculate</button>"
},
"tool4":{
"title":"📅 Irrigation Interval Predictor / सिंचाई अंतराल पूर्वानुमान",
"theory":"Determines irrigation frequency based on soil type.",
"form":"Soil (sandy/loamy/clay): <input id='soil' type='text'><br><button onclick='predictIrrigation()'>Predict</button>"
},
"tool5":{
"title":"🌿 Crop Rotation Planner / फ़सल चक्र योजना",
"theory":"Suggests next crop to maintain soil fertility.",
"form":"Last Crop: <input id='lastCrop' type='text'><br><button onclick='suggestCrop()'>Suggest</button>"
},
"tool6":{
"title":"🦠 Pest Risk Score / कीट जोखिम मूल्यांकन",
"theory":"Estimates pest attack probability based on humidity & temperature.",
"form":"Humidity %: <input id='humidity' type='number'><br>Temperature °C: <input id='temp2' type='number'><br><button onclick='checkPest()'>Check</button>"
},
"tool7":{
"title":"🌾 Growth Stage Advisor / विकास अवस्था सलाहकार",
"theory":"Advises action based on crop age.",
"form":"Crop age (days): <input id='age' type='number'><br><button onclick='growthStage()'>Check</button>"
},
"tool8":{
"title":"🌾 Harvest Time Predictor / कटाई समय पूर्वानुमान",
"theory":"Suggests if crop is ready for harvest.",
"form":"Crop type: <input id='cropType' type='text'><br>Crop age (days): <input id='cropAge' type='number'><br><button onclick='checkHarvest()'>Check</button>"
},
"tool9":{
"title":"🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच",
"theory":"Measures output yield per fertilizer input.",
"form":"Fertilizer (kg): <input id='fert' type='number'><br>Yield (quintal): <input id='yieldAmt' type='number'><br><button onclick='fertEfficiency()'>Check</button>"
},
"tool10":{
"title":"💰 Profit Forecast Tool / लाभ पूर्वानुमान",
"theory":"Predicts profit based on yield & market price.",
"form":"Yield (quintal): <input id='yield2' type='number'><br>Price per quintal ₹: <input id='price' type='number'><br>Total cost ₹: <input id='cost' type='number'><br><button onclick='calcProfit()'>Calculate</button>"
}
};

function openTool(id){
document.getElementById('dashboard').classList.add('hidden');
document.getElementById('tools').classList.remove('hidden');
document.getElementById('toolTitle').innerHTML=toolsData[id].title;
document.getElementById('toolTheory').innerHTML="<p>"+toolsData[id].theory+"</p>";
document.getElementById('toolForm').innerHTML=toolsData[id].form;
document.getElementById('toolResult').innerHTML="";
}
function backToDashboard(){
document.getElementById('dashboard').classList.remove('hidden');
document.getElementById('tools').classList.add('hidden');
document.getElementById('toolResult').innerHTML="";
}

// =========================
// Tool Calculations
// =========================
function calcYield(){
let area=parseFloat(document.getElementById('area').value);
let seed=parseFloat(document.getElementById('seed').value);
let rain=parseFloat(document.getElementById('rain').value);
let result=Math.round(area*seed*(rain/500)*100)/100;
document.getElementById('toolResult').innerHTML="<h3>Estimated Yield / अनुमानित उत्पादन: "+result+" quintals</h3>";
}
function checkSoil(){
let ph=parseFloat(document.getElementById('ph').value);
let r="";
if(ph<6) r="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कम्पोस्ट डालें";
else if(ph>7.5) r="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → कार्बनिक खाद डालें";
else r="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → सामान्य उर्वरक";
document.getElementById('toolResult').innerHTML="<h3>"+r+"</h3>";
}
function calcWater(){
let temp=parseFloat(document.getElementById('temp').value);
let base=6000;
if(temp>35) base*=1.2;
else if(temp<20) base*=0.9;
document.getElementById('toolResult').innerHTML="<h3>Water Requirement / जल आवश्यकता: "+Math.round(base)+" liters/acre/day</h3>";
}
function predictIrrigation(){
let soil=document.getElementById('soil').value.toLowerCase();
let r="";
if(soil=="sandy") r="Irrigate every 4 days / हर 4 दिन सिंचाई करें";
else if(soil=="clay") r="Irrigate every 8 days / हर 8 दिन सिंचाई करें";
else r="Irrigate every 6 days / हर 6 दिन सिंचाई करें";
document.getElementById('toolResult').innerHTML="<h3>"+r+"</h3>";
}
function suggestCrop(){
let last=document.getElementById('lastCrop').value.toLowerCase();
let rotation={"wheat":"Plant legumes next / अगली फसल दलहनी", "rice":"Plant maize next / अगली फसल मक्का","maize":"Plant wheat next / अगली फसल गेहूं"};
let r=rotation[last] || "Plant legumes for soil recovery / मिट्टी सुधार के लिए दलहनी लगाएं";
document.getElementById('toolResult').innerHTML="<h3>"+r+"</h3>";
}
function checkPest(){
let hum=parseFloat(document.getElementById('humidity').value);
let temp=parseFloat(document.getElementById('temp2').value);
let risk=(hum/100)*temp;
let r=risk>25?"⚠ High Pest Risk / उच्च कीट जोखिम":"Low to Moderate Risk / कम या मध्यम जोखिम";
document.getElementById('toolResult').innerHTML="<h3>Pest Risk Score / कीट जोखिम स्कोर: "+Math.round(risk*100)/100+"<br>"+r+"</h3>";
}
function growthStage(){
let age=parseInt(document.getElementById('age').value);
let r="";
if(age<30) r="Vegetative Stage → Focus on nitrogen / पौधे की वृद्धि चरण → नाइट्रोजन पर ध्यान दें";
else if(age<60) r="Flowering Stage → Balanced nutrients / फूल आने का चरण → संतुलित पोषण";
else r="Maturity Stage → Reduce irrigation / परिपक्वता चरण → सिंचाई कम करें";
document.getElementById('toolResult').innerHTML="<h3>"+r+"</h3>";
}
function checkHarvest(){
let crop=document.getElementById('cropType').value.toLowerCase();
let age=parseInt(document.getElementById('cropAge').value);
let r="";
if((crop=="wheat" && age>=120) || (crop=="rice" && age>=150)) r="Ready for harvest / कटाई के लिए तैयार";
else r="Not ready yet / अभी तैयार नहीं";
document.getElementById('toolResult').innerHTML="<h3>"+r+"</h3>";
}
function fertEfficiency(){
let fert=parseFloat(document.getElementById('fert').value);
let yieldAmt=parseFloat(document.getElementById('yieldAmt').value);
let eff=(yieldAmt/fert)*100;
document.getElementById('toolResult').innerHTML="<h3>Efficiency / दक्षता: "+Math.round(eff*100)/100+"%</h3>";
}
function calcProfit(){
let yieldAmt=parseFloat(document.getElementById('yield2').value);
let price=parseFloat(document.getElementById('price').value);
let cost=parseFloat(document.getElementById('cost').value);
let profit=(yieldAmt*price)-cost;
document.getElementById('toolResult').innerHTML="<h3>Estimated Profit / अनुमानित लाभ: ₹"+Math.round(profit*100)/100+"</h3>";
}
</script>

</body>
</html>
