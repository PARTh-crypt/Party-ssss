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
<title>PARTH'S KISAN SAATHI – Crop Management</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg,#1e3c72,#2a5298,#00b09b,#96c93d);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white;
    display:flex;
    justify-content:center;
    align-items:flex-start;
    flex-direction:column;
    min-height:100vh;
    text-align:center;
    padding-top:20px;
}

@keyframes bgMove {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

h1{
    font-family:'Playfair Display',serif;
    font-size:42px;
    margin:0;
    padding:10px;
    text-shadow:2px 2px 8px rgba(0,0,0,0.4);
}

h2{
    font-size:24px;
    margin:5px;
    padding:5px;
    text-shadow:1px 1px 6px rgba(0,0,0,0.3);
}

/* Button grid */
.button-container{
    margin-top:30px;
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap:15px;
    width:90%;
    margin-left:auto;
    margin-right:auto;
}

.tool-btn{
    padding:18px 20px;
    border-radius:25px;
    border:none;
    background:rgba(255,255,255,0.25);
    color:white;
    font-weight:bold;
    font-size:16px;
    cursor:pointer;
    text-shadow:1px 1px 3px rgba(0,0,0,0.4);
    transition:0.3s;
}

.tool-btn:hover{
    background:rgba(255,255,255,0.45);
    transform:scale(1.05);
}

#toolArea{
    margin-top:40px;
    background:rgba(0,0,0,0.35);
    padding:20px;
    border-radius:15px;
    width:90%;
    margin-left:auto;
    margin-right:auto;
    min-height:150px;
}

/* Input style */
input, select{
    padding:8px;
    border-radius:8px;
    border:none;
    width:80%;
    margin-bottom:10px;
}
button.calc-btn{
    padding:8px 16px;
    border:none;
    border-radius:12px;
    background:#fdd835;
    color:#2f6f2f;
    font-weight:bold;
    cursor:pointer;
}
button.calc-btn:hover{
    transform:scale(1.05);
}
</style>
</head>
<body>

<h1>🌾 PARTH'S KISAN SAATHI</h1>
<h2>Crop Management / फ़सल प्रबंधन</h2>

<div class="button-container">
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

<div id="toolArea">
    <h3>Select a tool above to start / ऊपर से टूल चुनें</h3>
</div>

<script>
function showTool(id){
    const area = document.getElementById("toolArea");
    let html = "";
    if(id===1){
        html = `<h3>🌾 Crop Yield Estimator</h3>
        <p>Theory: Estimates yield based on area, seed rate & rainfall / क्षेत्रफल, बीज दर और वर्षा पर अनुमानित उत्पादन।</p>
        Area (acres / एकड़): <input id="area" type="number"><br>
        Seed rate (kg/acre / बीज दर): <input id="seed" type="number"><br>
        Rainfall (mm / वर्षा): <input id="rain" type="number"><br>
        <button class="calc-btn" onclick="yieldCalc()">Calculate / गणना करें</button>
        <p id="res"></p>`;
    }
    else if(id===2){
        html = `<h3>🧪 Soil Nutrient Balancer</h3>
        <p>Theory: Adjust nutrients based on soil pH / मिट्टी के pH के आधार पर पोषण समायोजित करें।</p>
        Soil pH: <input id="ph" type="number"><br>
        <button class="calc-btn" onclick="nutrientCalc()">Check / जांचें</button>
        <p id="res"></p>`;
    }
    else if(id===3){
        html = `<h3>💧 Water Demand Calculator</h3>
        <p>Theory: Calculates water need based on temperature / तापमान के आधार पर जल आवश्यकताओं की गणना।</p>
        Temperature °C / तापमान: <input id="temp" type="number"><br>
        <button class="calc-btn" onclick="waterCalc()">Calculate / गणना करें</button>
        <p id="res"></p>`;
    }
    else if(id===4){
        html = `<h3>📅 Irrigation Interval Predictor</h3>
        <p>Theory: Irrigation frequency based on soil type / मिट्टी के प्रकार के आधार पर सिंचाई अंतराल।</p>
        Soil type / मिट्टी: <select id="soil">
            <option value="sandy">Sandy / रेतीली</option>
            <option value="loamy">Loamy / दोमट</option>
            <option value="clay">Clay / चिकनी</option>
        </select><br>
        <button class="calc-btn" onclick="irrigationCalc()">Predict / अनुमानित करें</button>
        <p id="res"></p>`;
    }
    else if(id===5){
        html = `<h3>🌿 Crop Rotation Planner</h3>
        <p>Theory: Suggests next crop / अगली फसल सुझाता है।</p>
        Last Crop / पिछली फसल: <select id="lastcrop">
            <option value="wheat">Wheat / गेहूं</option>
            <option value="rice">Rice / धान</option>
            <option value="maize">Maize / मक्का</option>
        </select><br>
        <button class="calc-btn" onclick="rotationCalc()">Suggest / सुझाएँ</button>
        <p id="res"></p>`;
    }
    else if(id===6){
        html = `<h3>🦠 Pest Risk Score</h3>
        <p>Theory: Estimates pest risk based on humidity & temp / आर्द्रता और तापमान के आधार पर कीट जोखिम।</p>
        Humidity % / आर्द्रता: <input id="hum" type="number"><br>
        Temperature °C / तापमान: <input id="temp2" type="number"><br>
        <button class="calc-btn" onclick="pestCalc()">Check / जांचें</button>
        <p id="res"></p>`;
    }
    else if(id===7){
        html = `<h3>🌾 Growth Stage Advisor</h3>
        <p>Theory: Advises based on crop age / फसल की आयु के आधार पर सलाह।</p>
        Crop age days / फसल उम्र: <input id="age" type="number"><br>
        <button class="calc-btn" onclick="growthCalc()">Check / जांचें</button>
        <p id="res"></p>`;
    }
    else if(id===8){
        html = `<h3>🌾 Harvest Time Predictor</h3>
        <p>Theory: Suggests if crop is ready / फसल कटाई के लिए तैयार है।</p>
        Crop type / फसल: <select id="crop">
            <option value="wheat">Wheat / गेहूं</option>
            <option value="rice">Rice / धान</option>
        </select><br>
        Crop age days / फसल उम्र: <input id="age2" type="number"><br>
        <button class="calc-btn" onclick="harvestCalc()">Check / जांचें</button>
        <p id="res"></p>`;
    }
    else if(id===9){
        html = `<h3>🧪 Fertilizer Efficiency Checker</h3>
        <p>Theory: Measures output per fertilizer input / उर्वरक इनपुट के अनुसार उत्पादन।</p>
        Fertilizer kg / उर्वरक: <input id="fert" type="number"><br>
        Yield quintal / उत्पादन: <input id="yield" type="number"><br>
        <button class="calc-btn" onclick="fertCalc()">Check / जांचें</button>
        <p id="res"></p>`;
    }
    else if(id===10){
        html = `<h3>💰 Profit Forecast Tool</h3>
        <p>Theory: Predicts profit based on yield & price / उत्पादन और मूल्य के आधार पर लाभ का अनुमान।</p>
        Yield quintal / उत्पादन: <input id="yield2" type="number"><br>
        Price ₹ / मूल्य: <input id="price" type="number"><br>
        Total cost ₹ / कुल लागत: <input id="cost" type="number"><br>
        <button class="calc-btn" onclick="profitCalc()">Calculate / गणना करें</button>
        <p id="res"></p>`;
    }

    area.innerHTML = html;
}

// =================== Calculations ===================
function yieldCalc(){
    const area = parseFloat(document.getElementById("area").value);
    const seed = parseFloat(document.getElementById("seed").value);
    const rain = parseFloat(document.getElementById("rain").value);
    const res = area*seed*(rain/500);
    document.getElementById("res").innerText = "Estimated Yield / अनुमानित उत्पादन: "+res.toFixed(2)+" quintals";
}

function nutrientCalc(){
    const ph = parseFloat(document.getElementById("ph").value);
    let msg="";
    if(ph<6) msg="Soil acidic → Add Lime + Compost / मिट्टी अम्लीय → चूना + कंपोस्ट डालें";
    else if(ph>7.5) msg="Soil alkaline → Add Organic manure / मिट्टी क्षारीय → कार्बनिक खाद डालें";
    else msg="Soil balanced → Standard fertilizer dose / मिट्टी संतुलित → मानक उर्वरक";
    document.getElementById("res").innerText = msg;
}

function waterCalc(){
    const temp = parseFloat(document.getElementById("temp").value);
    let base = 6000;
    if(temp>35) base*=1.2;
    else if(temp<20) base*=0.9;
    document.getElementById("res").innerText="Water Requirement / जल आवश्यकता: "+Math.round(base)+" liters/acre/day";
}

function irrigationCalc(){
    const soil = document.getElementById("soil").value;
    let msg="";
    if(soil==="sandy") msg="Irrigate every 4 days / हर 4 दिन सिंचाई करें";
    else if(soil==="clay") msg="Irrigate every 8 days / हर 8 दिन सिंचाई करें";
    else msg="Irrigate every 6 days / हर 6 दिन सिंचाई करें";
    document.getElementById("res").innerText=msg;
}

function rotationCalc(){
    const last = document.getElementById("lastcrop").value;
    let rot={"wheat":"Plant legumes next / अगली फसल: दलहन","rice":"Plant maize next / अगली फसल: मक्का","maize":"Plant wheat next / अगली फसल: गेहूं"};
    document.getElementById("res").innerText=rot[last]||"Plant legumes for soil recovery / मिट्टी की बहाली के लिए दलहन लगाएँ";
}

function pestCalc(){
    const hum = parseFloat(document.getElementById("hum").value);
    const temp = parseFloat(document.getElementById("temp2").value);
    const risk = (hum/100)*temp;
    let msg=risk>25?"⚠ High Pest Risk / उच्च कीट जोखिम":"Low to Moderate Risk / कम से मध्यम जोखिम";
    document.getElementById("res").innerText="Pest Risk Score / कीट जोखिम स्कोर: "+risk.toFixed(2)+" → "+msg;
}

function growthCalc(){
    const age = parseInt(document.getElementById("age").value);
    let stage="";
    if(age<30) stage="Vegetative Stage / पर्ण अवस्था → Nitrogen focus / नाइट्रोजन पर ध्यान";
    else if(age<60) stage="Flowering Stage / फूलन अवस्था → Balanced nutrients / संतुलित पोषण";
    else stage="Maturity Stage / परिपक्वता → Reduce irrigation / सिंचाई कम करें";
    document.getElementById("res").innerText=stage;
}

function harvestCalc(){
    const crop = document.getElementById("crop").value;
    const age = parseInt(document.getElementById("age2").value);
    let msg="Not ready yet / अभी तैयार नहीं";
    if(crop==="wheat" && age>=120) msg="Ready for harvest / कटाई के लिए तैयार";
    if(crop==="rice" && age>=150) msg="Ready for harvest / कटाई के लिए तैयार";
    document.getElementById("res").innerText=msg;
}

function fertCalc(){
    const fert = parseFloat(document.getElementById("fert").value);
    const yieldAmt = parseFloat(document.getElementById("yield").value);
    const eff=(yieldAmt/fert)*100;
    document.getElementById("res").innerText="Efficiency / दक्षता: "+eff.toFixed(2)+"%";
}

function profitCalc(){
    const yld = parseFloat(document.getElementById("yield2").value);
    const price = parseFloat(document.getElementById("price").value);
    const cost = parseFloat(document.getElementById("cost").value);
    const profit = (yld*price)-cost;
    document.getElementById("res").innerText="Estimated Profit / अनुमानित लाभ: ₹"+profit.toFixed(2);
}
</script>
</body>
</html>
