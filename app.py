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
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PARTH'S KISAN SAATHI</title>

<style>
body{
margin:0;
font-family:Arial, sans-serif;
background:linear-gradient(135deg,#134e5e,#71b280);
color:white;
text-align:center;
}

.section{display:none;padding:20px;}
.active{display:block;}

h1{font-size:26px;margin-top:20px;}

.main-btn{
width:90%;
padding:15px;
margin:10px;
font-size:18px;
border:none;
border-radius:15px;
background:#fdd835;
color:#2f6f2f;
font-weight:bold;
cursor:pointer;
}

.tool-btn{
width:90%;
padding:14px;
margin:6px;
font-size:17px;
border:none;
border-radius:12px;
background:white;
cursor:pointer;
}

.answer-btn{
width:70%;
padding:12px;
margin:10px;
font-size:16px;
border:none;
border-radius:10px;
background:#fdd835;
cursor:pointer;
}

.result{
margin:20px;
padding:15px;
background:rgba(0,0,0,0.3);
border-radius:12px;
}
</style>

<script>

function showSection(id){
document.querySelectorAll(".section").forEach(sec=>sec.classList.remove("active"));
document.getElementById(id).classList.add("active");
}

let tools = {
1:{q:"क्या खेत में बारिश हो रही है? / Is it raining?",
yes:["बारिश से नमी बढ़ती है।","आज सिंचाई न करें।"],
no:["मिट्टी सूख सकती है।","हल्की सिंचाई करें।"]},

2:{q:"पत्ते हरे हैं? / Leaves green?",
yes:["फसल स्वस्थ है।","अभी खाद न डालें।"],
no:["पोषक तत्व कमी।","नाइट्रोजन खाद डालें।"]},

3:{q:"कीड़े दिख रहे हैं? / Pests visible?",
yes:["कीट नुकसान करते हैं।","कीटनाशक स्प्रे करें।"],
no:["फसल सुरक्षित।","सप्ताह में जांच करें।"]},

4:{q:"मिट्टी सूखी है? / Soil dry?",
yes:["जड़ कमजोर हो सकती है।","तुरंत पानी दें।"],
no:["नमी पर्याप्त है।","पानी की जरूरत नहीं।"]},

5:{q:"दाने सख्त हैं? / Grains hard?",
yes:["कटाई का समय है।","कटाई शुरू करें।"],
no:["फसल कच्ची है।","कुछ दिन प्रतीक्षा करें।"]},

6:{q:"बहुत गर्मी है? / Too much heat?",
yes:["अधिक गर्मी नुकसानदेह।","पानी बढ़ाएं।"],
no:["तापमान सामान्य।","सामान्य देखभाल करें।"]},

7:{q:"आसमान बादल है? / Cloudy sky?",
yes:["बारिश संभव।","आज स्प्रे न करें।"],
no:["बारिश कम संभावना।","सिंचाई कर सकते हैं।"]},

8:{q:"हाल में खाद डाली? / Added fertilizer recently?",
yes:["अधिक खाद नुकसान।","और खाद न डालें।"],
no:["पोषक तत्व कम।","संतुलित खाद डालें।"]},

9:{q:"पत्ते पीले हैं? / Yellow leaves?",
yes:["नाइट्रोजन कमी।","यूरिया डालें।"],
no:["पौधा स्वस्थ।","सामान्य देखभाल रखें।"]},

10:{q:"फसल पूरी सूखी है? / Crop fully dry?",
yes:["भंडारण योग्य।","सूखी जगह रखें।"],
no:["नमी है।","और सुखाएं।"]}
};

function openTool(id){
document.getElementById("question").innerHTML = tools[id].q;

document.getElementById("answers").innerHTML =
"<button class='answer-btn' onclick='showResult("+id+",\"yes\")'>हाँ / Yes</button>"+
"<button class='answer-btn' onclick='showResult("+id+",\"no\")'>नहीं / No</button>";

document.getElementById("result").innerHTML="";
}

function showResult(id,type){
let theory = tools[id][type][0];
let practical = tools[id][type][1];

document.getElementById("result").innerHTML =
"<div class='result'><b>Theory:</b><br>"+theory+
"<br><br><b>Practical:</b><br>"+practical+"</div>";
}

</script>
</head>

<body>

<!-- START SCREEN -->
<div id="start" class="section active">
<h1>🌾 PARTH'S KISAN SAATHI</h1>
<h3>Har Kisan Ka Digital Saathi</h3>
<button class="main-btn" onclick="showSection('dashboard')">
Enter App / ऐप में प्रवेश करें
</button>
</div>

<!-- DASHBOARD -->
<div id="dashboard" class="section">
<h1>📊 Dashboard / डैशबोर्ड</h1>
<button class="main-btn" onclick="showSection('crop')">
🌱 Crop Management / फसल प्रबंधन
</button>
<button class="main-btn" onclick="showSection('start')">
⬅ Back to Start
</button>
</div>

<!-- CROP SECTION -->
<div id="crop" class="section">
<h1>🌱 Crop Tools</h1>

<button class="tool-btn" onclick="openTool(1)">🌧 Rain</button>
<button class="tool-btn" onclick="openTool(2)">🌿 Plant Health</button>
<button class="tool-btn" onclick="openTool(3)">🐛 Pest</button>
<button class="tool-btn" onclick="openTool(4)">💧 Soil</button>
<button class="tool-btn" onclick="openTool(5)">🌾 Harvest</button>
<button class="tool-btn" onclick="openTool(6)">🌡 Heat</button>
<button class="tool-btn" onclick="openTool(7)">☁ Cloud</button>
<button class="tool-btn" onclick="openTool(8)">🧪 Fertilizer</button>
<button class="tool-btn" onclick="openTool(9)">🍂 Yellow Leaves</button>
<button class="tool-btn" onclick="openTool(10)">🏪 Storage</button>

<h2 id="question"></h2>
<div id="answers"></div>
<div id="result"></div>

<button class="main-btn" onclick="showSection('dashboard')">
⬅ Back to Dashboard
</button>
</div>

</body>
</html>
