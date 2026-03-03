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
# ==========================
# Dashboard
# ==========================
@app.route("/dashboard")
def dashboard():
<!DOCTYPE html>
<html>
<head>
<title>Kisan Saathi Dashboard</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body{
    margin:0;
    font-family:sans-serif;
    background: linear-gradient(135deg,#11998e,#38ef7d);
    color:white;
    text-align:center;
}

h1{
    padding:20px;
}

.tool-btn{
    width:85%;
    padding:15px;
    margin:10px;
    font-size:18px;
    border:none;
    border-radius:12px;
    background:#fdd835;
    cursor:pointer;
}

.result{
    margin:20px;
    padding:15px;
    background:rgba(0,0,0,0.2);
    border-radius:12px;
}
</style>

<script>
function showTool(tool){

let data = {
1:["बारिश हो रही है?",
   "Rain increases soil moisture.","आज सिंचाई न करें।",
   "Soil may dry.","हल्की सिंचाई करें।"],

2:["पौधा हरा है?",
   "Green leaves mean good nutrition.","खाद की जरूरत नहीं।",
   "Nutrient deficiency possible.","नाइट्रोजन खाद दें।"],

3:["कीड़े दिख रहे हैं?",
   "Pests damage crops.","कीटनाशक स्प्रे करें।",
   "Crop safe.","सप्ताह में जांच करें।"],

4:["मिट्टी सूखी है?",
   "Dry soil weakens roots.","तुरंत पानी दें।",
   "Moisture enough.","अभी पानी की जरूरत नहीं।"],

5:["दाने सख्त हैं?",
   "Hard grains mean harvest time.","कटाई शुरू करें।",
   "Crop immature.","1-2 सप्ताह प्रतीक्षा करें।"],

6:["बहुत गर्मी है?",
   "High heat harms crops.","पानी बढ़ाएं।",
   "Temperature normal.","सामान्य देखभाल करें।"],

7:["घने बादल हैं?",
   "Rain possible.","आज स्प्रे न करें।",
   "Low rain chance.","सिंचाई कर सकते हैं।"],

8:["खाद हाल में डाली?",
   "Excess fertilizer harmful.","और खाद न डालें।",
   "Nutrients may be low.","संतुलित खाद डालें।"],

9:["पत्ते पीले हैं?",
   "Nitrogen deficiency.","यूरिया डालें।",
   "Plant healthy.","सामान्य देखभाल करें।"],

10:["फसल सूखी है?",
    "Good for storage.","सूखी जगह स्टोर करें।",
    "Moisture present.","कुछ दिन और सुखाएं।"]
};

let item = data[tool];

document.getElementById("question").innerHTML = item[0];
document.getElementById("result").innerHTML = `
<button class="tool-btn" onclick="showAnswer(${tool},'yes')">हाँ / Yes</button>
<button class="tool-btn" onclick="showAnswer(${tool},'no')">नहीं / No</button>
`;
}

function showAnswer(tool,ans){

let data = {
1:["Rain increases soil moisture.","आज सिंचाई न करें.",
   "Soil may dry.","हल्की सिंचाई करें."],
2:["Green leaves good.","खाद जरूरत नहीं.",
   "Nutrient deficiency.","नाइट्रोजन खाद दें."],
3:["Pests harmful.","स्प्रे करें.",
   "Safe crop.","जांच करते रहें."],
4:["Dry soil bad.","पानी दें.",
   "Moisture ok.","जरूरत नहीं."],
5:["Harvest time.","कटाई करें.",
   "Not ready.","प्रतीक्षा करें."],
6:["Heat harmful.","पानी बढ़ाएं.",
   "Normal temp.","देखभाल करें."],
7:["Rain possible.","स्प्रे न करें.",
   "No rain.","सिंचाई करें."],
8:["Too much fertilizer bad.","और खाद न डालें.",
   "Nutrient low.","संतुलित खाद डालें."],
9:["Nitrogen low.","यूरिया डालें.",
   "Healthy plant.","देखभाल रखें."],
10:["Ready to store.","सूखी जगह रखें.",
    "Still wet.","और सुखाएं."]
};

let item = data[tool];

if(ans=="yes"){
document.getElementById("result").innerHTML =
"<div class='result'><b>Theory:</b><br>"+item[0]+"<br><br><b>Practical:</b><br>"+item[1]+"</div>";
}else{
document.getElementById("result").innerHTML =
"<div class='result'><b>Theory:</b><br>"+item[2]+"<br><br><b>Practical:</b><br>"+item[3]+"</div>";
}
}
</script>
</head>

<body>

<h1>🌾 Crop Management Dashboard<br>फसल प्रबंधन</h1>

<button class="tool-btn" onclick="showTool(1)">🌧 Rain</button>
<button class="tool-btn" onclick="showTool(2)">🌿 Plant Health</button>
<button class="tool-btn" onclick="showTool(3)">🐛 Pest</button>
<button class="tool-btn" onclick="showTool(4)">💧 Soil Dry</button>
<button class="tool-btn" onclick="showTool(5)">🌾 Harvest</button>
<button class="tool-btn" onclick="showTool(6)">🌡 Heat</button>
<button class="tool-btn" onclick="showTool(7)">☁ Cloud</button>
<button class="tool-btn" onclick="showTool(8)">🧪 Fertilizer</button>
<button class="tool-btn" onclick="showTool(9)">🍂 Yellow Leaves</button>
<button class="tool-btn" onclick="showTool(10)">🏪 Storage</button>

<h2 id="question"></h2>
<div id="result"></div>

</body>
</html>
