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
<title>Parth's Kisan Saathi - Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    min-height:100vh;
    background: linear-gradient(135deg, #f6d365,#fda085,#84fab0,#8fd3f4);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
    color:#fff;
    text-align:center;
}
@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}
h1{font-family:'Playfair Display', serif; font-size:48px; margin-top:40px; text-shadow:2px 2px 8px rgba(0,0,0,0.3);}
.card{
    width:80%;
    margin:20px auto;
    padding:20px;
    border-radius:20px;
    background: rgba(0,0,0,0.25);
    cursor:pointer;
    font-size:22px;
    transition:0.3s;
}
.card:hover{transform:scale(1.05);background: rgba(0,0,0,0.4);}
.button{
    margin:10px;
    padding:12px 20px;
    border:none;
    border-radius:12px;
    background: rgba(255,255,255,0.25);
    color:white;
    font-weight:bold;
    font-size:18px;
    cursor:pointer;
}
.button:hover{background: rgba(255,255,255,0.45);}
input[type=number]{padding:6px; border-radius:8px; border:none; width:100px; text-align:center;}
</style>
</head>
<body>

<h1>PARTH'S KISAN SAATHI<br>किसान डैशबोर्ड</h1>

<div id="dashboard">
    <div class="card" onclick="openCategory('crop')">🌾 Crop Management / फ़सल प्रबंधन</div>
</div>

<div id="tools" style="display:none;">
    <h1>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h1>
    <div id="toolButtons"></div>
    <div style="margin-top:20px;"><button class="button" onclick="backToDashboard()">⬅ Back / वापस जाएँ</button></div>
    <div id="toolArea" style="margin-top:20px;"></div>
</div>

<script>
// ====================== Tools Data ======================
const tools = [
{ id:1, name:"Crop Yield Estimator", theory:"Estimates yield based on area, seed rate & rainfall.\nक्षेत्रफल, बीज दर और वर्षा के आधार पर उत्पादन का अनुमान लगाता है।", func:()=>{
    const area = Number(prompt("Area (acres) / क्षेत्रफल:"));
    const seed = Number(prompt("Seed rate (kg/acre) / बीज दर:"));
    const rain = Number(prompt("Rainfall (mm) / वर्षा:"));
    alert("Estimated Yield / अनुमानित उत्पादन: "+((area*seed*(rain/500)).toFixed(2))+" quintals");
}},
{ id:2, name:"Soil Nutrient Balancer", theory:"Adjusts nutrient need based on soil pH.\nमिट्टी के पीएच के आधार पर पोषक तत्व आवश्यकताओं को समायोजित करता है।", func:()=>{
    const ph = Number(prompt("Soil pH / मिट्टी का pH:"));
    if(ph<6) alert("Soil acidic → Add Lime + Compost\nमिट्टी अम्लीय → चूना + खाद डालें");
    else if(ph>7.5) alert("Soil alkaline → Add Organic manure\nमिट्टी क्षारीय → जैविक खाद डालें");
    else alert("Soil balanced → Standard fertilizer dose\nमिट्टी संतुलित → सामान्य उर्वरक खुराक");
}},
{ id:3, name:"Water Demand Calculator", theory:"Calculates water need based on temperature.\nतापमान के आधार पर जल की आवश्यकता की गणना करता है।", func:()=>{
    const temp = Number(prompt("Temperature °C / तापमान:"));
    let base = 6000;
    if(temp>35) base*=1.2; else if(temp<20) base*=0.9;
    alert("Water Requirement / पानी की आवश्यकता: "+Math.round(base)+" liters/acre/day");
}},
{ id:4, name:"Irrigation Interval Predictor", theory:"Determines irrigation frequency based on soil type.\nमिट्टी के प्रकार के आधार पर सिंचाई की आवृत्ति निर्धारित करता है।", func:()=>{
    const soil = prompt("Soil type (sandy/loamy/clay) / मिट्टी का प्रकार:").toLowerCase();
    if(soil=="sandy") alert("Irrigate every 4 days / हर 4 दिन सिंचाई करें");
    else if(soil=="clay") alert("Irrigate every 8 days / हर 8 दिन सिंचाई करें");
    else alert("Irrigate every 6 days / हर 6 दिन सिंचाई करें");
}},
{ id:5, name:"Crop Rotation Planner", theory:"Suggests next crop to maintain soil fertility.\nमिट्टी की उर्वरता बनाए रखने के लिए अगली फसल सुझाता है।", func:()=>{
    const last = prompt("Last crop / पिछली फसल:").toLowerCase();
    const rotation = {"wheat":"Plant legumes next / अगली फसल दालें लगाएँ","rice":"Plant maize next / अगली फसल मक्का लगाएँ","maize":"Plant wheat next / अगली फसल गेहूँ लगाएँ"};
    alert(rotation[last]||"Plant legumes for soil recovery / मिट्टी सुधार के लिए दालें लगाएँ");
}},
{ id:6, name:"Pest Risk Score", theory:"Estimates pest attack probability based on humidity & temperature.\nआर्द्रता और तापमान के आधार पर कीटों के हमले की संभावना का अनुमान लगाता है।", func:()=>{
    const hum = Number(prompt("Humidity % / आर्द्रता:"));
    const temp = Number(prompt("Temperature °C / तापमान:"));
    const risk = (hum/100)*temp;
    alert("Pest Risk Score / कीट जोखिम स्कोर: "+risk.toFixed(2));
}},
{ id:7, name:"Growth Stage Advisor", theory:"Advises action based on crop age.\nफसल की उम्र के आधार पर सुझाव देता है।", func:()=>{
    const age = Number(prompt("Crop age days / फसल की उम्र (दिन):"));
    if(age<30) alert("Vegetative Stage → Focus on nitrogen / वृद्धि चरण → नाइट्रोजन पर ध्यान दें");
    else if(age<60) alert("Flowering Stage → Balanced nutrients / फूलने का चरण → संतुलित पोषक तत्व");
    else alert("Maturity Stage → Reduce irrigation / पकने का चरण → सिंचाई कम करें");
}},
{ id:8, name:"Harvest Time Predictor", theory:"Suggests if crop is ready for harvest.\nजाँच करता है कि फसल कटाई के लिए तैयार है या नहीं।", func:()=>{
    const crop = prompt("Crop type / फसल का प्रकार:").toLowerCase();
    const age = Number(prompt("Crop age days / फसल की उम्र (दिन):"));
    if(crop=="wheat" && age>=120) alert("Ready for harvest / कटाई के लिए तैयार");
    else if(crop=="rice" && age>=150) alert("Ready for harvest / कटाई के लिए तैयार");
    else alert("Not ready yet / अभी तैयार नहीं");
}},
{ id:9, name:"Fertilizer Efficiency Checker", theory:"Measures output yield per fertilizer input.\nउर्वरक इनपुट के प्रति उत्पादन मापता है।", func:()=>{
    const fert = Number(prompt("Fertilizer applied kg / उपयोग किया गया उर्वरक:"));
    const yield_amt = Number(prompt("Yield quintal / उत्पादन (क्विंटल):"));
    const eff = (yield_amt/fert)*100;
    alert("Efficiency / दक्षता: "+eff.toFixed(2)+"%");
}},
{ id:10, name:"Profit Forecast Tool", theory:"Predicts profit based on yield & market price.\nउत्पादन और बाजार मूल्य के आधार पर लाभ का अनुमान लगाता है।", func:()=>{
    const yield_amt = Number(prompt("Yield quintal / उत्पादन (क्विंटल):"));
    const price = Number(prompt("Market price ₹/quintal / बाजार मूल्य:"));
    const cost = Number(prompt("Total cost ₹ / कुल लागत:"));
    const profit = (yield_amt*price)-cost;
    alert("Estimated Profit / अनुमानित लाभ: ₹"+profit.toFixed(2));
}}
];

// ====================== Functions ======================
function openCategory(cat){
    document.getElementById('dashboard').style.display='none';
    document.getElementById('tools').style.display='block';
    const toolButtonsDiv = document.getElementById('toolButtons');
    toolButtonsDiv.innerHTML = '';
    tools.forEach(t=>{
        const btn = document.createElement('button');
        btn.className='button';
        btn.innerHTML = `${t.id}️⃣ ${t.name}`;
        btn.onclick = function(){
            alert("Theory / सिद्धांत:\n"+t.theory);
            t.func();
        };
        toolButtonsDiv.appendChild(btn);
    });
}

function backToDashboard(){
    document.getElementById('dashboard').style.display='block';
    document.getElementById('tools').style.display='none';
}
</script>
</body>
</html>
