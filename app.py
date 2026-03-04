<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body {
    margin:0; font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg,#1e3c72,#2a5298,#6dd5ed,#2193b0);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white; text-align:center;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1,h2{margin:20px 0;}
button{
    padding:12px 30px; margin:10px;
    border:none; border-radius:20px;
    background:linear-gradient(45deg,#fdd835,#fbc02d);
    color:#2f6f2f; font-weight:bold; cursor:pointer;
    font-size:18px;
}
button:hover{transform:scale(1.05);}
.card{
    width:80%; margin:15px auto; padding:20px;
    background:rgba(0,0,0,0.35); border-radius:20px;
    cursor:pointer; transition:0.3s; font-size:20px;
}
.card:hover{background:rgba(0,0,0,0.5); transform:scale(1.02);}
input{padding:5px; margin:5px; border-radius:5px;}
#app{max-width:600px; margin:auto;}
</style>
</head>
<body>
<div id="app">
<!-- Starting Screen -->
<div id="startScreen">
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi</h2>
<button onclick="showDashboard()">Enter App / ऐप में प्रवेश करें</button>
</div>
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body {
    margin:0; font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg,#1e3c72,#2a5298,#6dd5ed,#2193b0);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white; text-align:center;
}
@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
h1,h2{margin:20px 0;}
button{
    padding:12px 30px; margin:10px;
    border:none; border-radius:20px;
    background:linear-gradient(45deg,#fdd835,#fbc02d);
    color:#2f6f2f; font-weight:bold; cursor:pointer;
    font-size:18px;
}
button:hover{transform:scale(1.05);}
.card{
    width:80%; margin:15px auto; padding:20px;
    background:rgba(0,0,0,0.35); border-radius:20px;
    cursor:pointer; transition:0.3s; font-size:20px;
}
.card:hover{background:rgba(0,0,0,0.5); transform:scale(1.02);}
input{padding:5px; margin:5px; border-radius:5px;}
#app{max-width:600px; margin:auto;}
</style>
</head>
<body>
<div id="app">
<!-- Starting Screen -->
<div id="startScreen">
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Har Kisan Ka Digital Saathi</h2>
<button onclick="showDashboard()">Enter App / ऐप में प्रवेश करें</button>
</div>

<!-- Dashboard -->
<div id="dashboard" style="display:none;">
<h1>Dashboard / डैशबोर्ड</h1>
<div class="card" onclick="showCropTools()">🌾 Crop Management / फ़सल प्रबंधन</div>
</div>

<!-- Crop Tools -->
<div id="cropTools" style="display:none;">
<h1>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h1>
<div class="card" onclick="showTool('yield')">1️⃣ Crop Yield Estimator / फ़सल अनुमान</div>
<div class="card" onclick="showTool('soil')">2️⃣ Soil Nutrient Balancer / मिट्टी पोषण संतुलन</div>
<div class="card" onclick="showTool('water')">3️⃣ Water Demand Calculator / जल आवश्यकता कैलकुलेटर</div>
<div class="card" onclick="showTool('irrigation')">4️⃣ Irrigation Interval Predictor / सिंचाई अंतराल पूर्वानुमान</div>
<div class="card" onclick="showTool('rotation')">5️⃣ Crop Rotation Planner / फ़सल चक्र योजना</div>
<div class="card" onclick="showTool('pest')">6️⃣ Pest Risk Score / कीट जोखिम मूल्यांकन</div>
<div class="card" onclick="showTool('growth')">7️⃣ Growth Stage Advisor / विकास अवस्था सलाहकार</div>
<div class="card" onclick="showTool('harvest')">8️⃣ Harvest Time Predictor / कटाई समय पूर्वानुमान</div>
<div class="card" onclick="showTool('fertilizer')">9️⃣ Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच</div>
<div class="card" onclick="showTool('profit')">🔟 Profit Forecast Tool / लाभ पूर्वानुमान</div>
<button onclick="showDashboard()">⬅ Back to Dashboard / डैशबोर्ड पर वापस</button>
</div>

<!-- Tool View -->
<div id="toolView" style="display:none;">
<h1 id="toolTitle"></h1>
<div id="toolTheory"></div>
<div id="toolForm"></div>
<div id="toolResult" style="margin-top:20px;font-size:20px;"></div>
<button onclick="showCropTools()">⬅ Back to Crop Tools / फ़सल टूल्स पर वापस</button>
</div>

</div>

<script>
// Show/Hide Screens
function showDashboard(){document.getElementById('startScreen').style.display='none'; document.getElementById('dashboard').style.display='block'; document.getElementById('cropTools').style.display='none'; document.getElementById('toolView').style.display='none';}
function showCropTools(){document.getElementById('dashboard').style.display='none'; document.getElementById('cropTools').style.display='block'; document.getElementById('toolView').style.display='none';}
function showTool(tool){
    document.getElementById('dashboard').style.display='none';
    document.getElementById('cropTools').style.display='none';
    document.getElementById('toolView').style.display='block';
    const title=document.getElementById('toolTitle');
    const theory=document.getElementById('toolTheory');
    const formDiv=document.getElementById('toolForm');
    const result=document.getElementById('toolResult');
    result.innerHTML='';
    if(tool==='yield'){
        title.innerHTML="🌾 Crop Yield Estimator / फ़सल अनुमान";
        theory.innerHTML="<p>Theory: Estimates yield based on area, seed rate & rainfall.</p>";
        formDiv.innerHTML=`Area (acres): <input id='area'><br>Seed rate (kg/acre): <input id='seed'><br>Rainfall (mm): <input id='rain'><br><button onclick="calculateYield()">Calculate</button>`;
    } else if(tool==='soil'){
        title.innerHTML="🧪 Soil Nutrient Balancer / मिट्टी पोषण संतुलन";
        theory.innerHTML="<p>Theory: Adjusts nutrients based on soil pH.</p>";
        formDiv.innerHTML=`Soil pH: <input id='ph'><br><button onclick="calculateSoil()">Check</button>`;
    } else if(tool==='water'){
        title.innerHTML="💧 Water Demand Calculator / जल आवश्यकता कैलकुलेटर";
        theory.innerHTML="<p>Theory: Calculates water need based on temperature.</p>";
        formDiv.innerHTML=`Temperature °C: <input id='temp'><br><button onclick="calculateWater()">Calculate</button>`;
    } else if(tool==='irrigation'){
        title.innerHTML="📅 Irrigation Interval Predictor / सिंचाई अंतराल पूर्वानुमान";
        theory.innerHTML="<p>Theory: Determines irrigation frequency based on soil type.</p>";
        formDiv.innerHTML=`Soil (sandy/loamy/clay): <input id='soil'><br><button onclick="calculateIrrigation()">Predict</button>`;
    } else if(tool==='rotation'){
        title.innerHTML="🌿 Crop Rotation Planner / फ़सल चक्र योजना";
        theory.innerHTML="<p>Theory: Suggests next crop to maintain soil fertility.</p>";
        formDiv.innerHTML=`Last Crop: <input id='lastCrop'><br><button onclick="calculateRotation()">Suggest</button>`;
    } else if(tool==='pest'){
        title.innerHTML="🦠 Pest Risk Score / कीट जोखिम मूल्यांकन";
        theory.innerHTML="<p>Theory: Estimates pest attack probability based on humidity & temperature.</p>";
        formDiv.innerHTML=`Humidity %: <input id='hum'><br>Temperature °C: <input id='temp'><br><button onclick="calculatePest()">Check</button>`;
    } else if(tool==='growth'){
        title.innerHTML="🌾 Growth Stage Advisor / विकास अवस्था सलाहकार";
        theory.innerHTML="<p>Theory: Advises action based on crop age.</p>";
        formDiv.innerHTML=`Crop age (days): <input id='age'><br><button onclick="calculateGrowth()">Check</button>`;
    } else if(tool==='harvest'){
        title.innerHTML="🌾 Harvest Time Predictor / कटाई समय पूर्वानुमान";
        theory.innerHTML="<p>Theory: Suggests if crop is ready for harvest.</p>";
        formDiv.innerHTML=`Crop type: <input id='crop'><br>Crop age (days): <input id='age'><br><button onclick="calculateHarvest()">Check</button>`;
    } else if(tool==='fertilizer'){
        title.innerHTML="🧪 Fertilizer Efficiency Checker / उर्वरक दक्षता जाँच";
        theory.innerHTML="<p>Theory: Measures output yield per fertilizer input.</p>";
        formDiv.innerHTML=`Fertilizer (kg): <input id='fert'><br>Yield (quintal): <input id='yield'><br><button onclick="calculateFertilizer()">Check</button>`;
    } else if(tool==='profit'){
        title.innerHTML="💰 Profit Forecast Tool / लाभ पूर्वानुमान";
        theory.innerHTML="<p>Theory: Predicts profit based on yield & market price.</p>";
        formDiv.innerHTML=`Yield (quintal): <input id='yield'><br>Price per quintal ₹: <input id='price'><br>Total cost ₹: <input id='cost'><br><button onclick="calculateProfit()">Calculate</button>`;
    }
}

// Calculation Functions
function calculateYield(){
    const area=parseFloat(document.getElementById('area').value);
    const seed=parseFloat(document.getElementById('seed').value);
    const rain=parseFloat(document.getElementById('rain').value);
    const res=(area*seed*(rain/500)).toFixed(2);
    document.getElementById('toolResult').innerHTML=`Estimated Yield / अनुमानित उत्पादन: ${res} quintals`;
}
function calculateSoil(){
    const ph=parseFloat(document.getElementById('ph').value);
    let res='';
    if(ph<6) res="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कम्पोस्ट डालें";
    else if(ph>7.5) res="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → कार्बनिक खाद डालें";
    else res="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → सामान्य उर्वरक";
    document.getElementById('toolResult').innerHTML=res;
}
function calculateWater(){
    const temp=parseFloat(document.getElementById('temp').value);
    let base=6000;
    if(temp>35) base*=1.2;
    else if(temp<20) base*=0.9;
    document.getElementById('toolResult').innerHTML=`Water Requirement / जल आवश्यकता: ${Math.round(base)} liters/acre/day`;
}
function calculateIrrigation(){
    const soil=document.getElementById('soil').value.toLowerCase();
    let res='';
    if(soil==='sandy') res="Irrigate every 4 days / हर 4 दिन सिंचाई करें";
    else if(soil==='clay') res="Irrigate every 8 days / हर 8 दिन सिंचाई करें";
    else res="Irrigate every 6 days / हर 6 दिन सिंचाई करें";
    document.getElementById('toolResult').innerHTML=res;
}
function calculateRotation(){
    const last=document.getElementById('lastCrop').value.toLowerCase();
    const rotation={"wheat":"Plant legumes next / अगली फसल दलहनी","rice":"Plant maize next / अगली फसल मक्का","maize":"Plant wheat next / अगली फसल गेहूं"};
    const res=rotation[last] || "Plant legumes for soil recovery / मिट्टी सुधार के लिए दलहनी लगाएं";
    document.getElementById('toolResult').innerHTML=res;
}
function calculatePest(){
    const hum=parseFloat(document.getElementById('hum').value);
    const temp=parseFloat(document.getElementById('temp').value);
    const risk=(hum/100)*temp;
    const res=risk>25?"⚠ High Pest Risk / उच्च कीट जोखिम":"Low to Moderate Risk / कम या मध्यम जोखिम";
    document.getElementById('toolResult').innerHTML=`Pest Risk Score / कीट जोखिम स्कोर: ${risk.toFixed(2)}<br>${res}`;
}
function calculateGrowth(){
    const age=parseInt(document.getElementById('age').value);
    let res='';
    if(age<30) res="Vegetative Stage → Focus on nitrogen / पौधे की वृद्धि चरण → नाइट्रोजन पर ध्यान दें";
    else if(age<60) res="Flowering Stage → Balanced nutrients / फूल आने का चरण → संतुलित पोषण";
    else res="Maturity Stage → Reduce irrigation / परिपक्वता चरण → सिंचाई कम करें";
    document.getElementById('toolResult').innerHTML=res;
}
function calculateHarvest(){
    const crop=document.getElementById('crop').value.toLowerCase();
    const age=parseInt(document.getElementById('age').value);
    let ready=false;
    if((crop==='wheat' && age>=120) || (crop==='rice' && age>=150)) ready=true;
    const res=ready?"Ready for harvest / कटाई के लिए तैयार":"Not ready yet / अभी तैयार नहीं";
    document.getElementById('toolResult').innerHTML=res;
}
function calculateFertilizer(){
    const fert=parseFloat(document.getElementById('fert').value);
    const yield_amt=parseFloat(document.getElementById('yield').value);
    const eff=(yield_amt/fert)*100;
    document.getElementById('toolResult').innerHTML=`Efficiency / दक्षता: ${eff.toFixed(2)}%`;
}
function calculateProfit(){
    const yield_amt=parseFloat(document.getElementById('yield').value);
    const price=parseFloat(document.getElementById('price').value);
    const cost=parseFloat(document.getElementById('cost').value);
    const profit=(yield_amt*price)-cost;
    document.getElementById('toolResult').innerHTML=`Estimated Profit / अनुमानित लाभ: ₹${profit.toFixed(2)}`;
}
</script>
</body>
</html>
