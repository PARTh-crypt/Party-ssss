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
    return """
<!DOCTYPE html>
<html>
<head>
<style>
body{
    margin:0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(135deg,#4facfe,#43e97b);
    text-align:center;
    color:white;
}
h1{
    padding-top:30px;
}
.category-btn{
    width:80%;
    padding:20px;
    margin:25px;
    font-size:22px;
    border:none;
    border-radius:18px;
    background:white;
    color:#2f6f2f;
    font-weight:bold;
    cursor:pointer;
}
.category-btn:hover{
    transform:scale(1.05);
}
</style>
</head>
<body>

<h1>Dashboard / डैशबोर्ड</h1>

<button class="category-btn" onclick="window.location.href='/crop'">
🌾 Crop Management / फसल प्रबंधन
</button>

</body>
</html>
"""
    # ==========================
# Crop Management
# ==========================
@app.route("/crop")
def crop():
    return """
<!DOCTYPE html>
<html>
<head>
<style>
body{
    margin:0;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(135deg,#11998e,#38ef7d);
    text-align:center;
    color:white;
}
h2{
    padding-top:20px;
}
.tool-btn{
    width:85%;
    padding:18px;
    margin:12px;
    font-size:18px;
    border:none;
    border-radius:15px;
    background:#fff176;
    color:#2f6f2f;
    font-weight:bold;
    cursor:pointer;
}
.tool-btn:hover{
    transform:scale(1.05);
}
</style>
</head>
<body>

<h2>Crop Tools / फसल उपकरण</h2>

<button class="tool-btn" onclick="window.location.href='/tool/1'">🌧 Rain Check / बारिश जांच</button>
<button class="tool-btn" onclick="window.location.href='/tool/2'">🌱 Plant Health / पौधा स्थिति</button>
<button class="tool-btn" onclick="window.location.href='/tool/3'">🐛 Pest Problem / कीट समस्या</button>
<button class="tool-btn" onclick="window.location.href='/tool/4'">💧 Water Need / पानी जरूरत</button>
<button class="tool-btn" onclick="window.location.href='/tool/5'">🌾 Harvest Time / कटाई समय</button>
<button class="tool-btn" onclick="window.location.href='/tool/6'">🌡 Temperature Effect / तापमान प्रभाव</button>
<button class="tool-btn" onclick="window.location.href='/tool/7'">🌤 Weather Advice / मौसम सलाह</button>
<button class="tool-btn" onclick="window.location.href='/tool/8'">🧪 Fertilizer Need / खाद जरूरत</button>
<button class="tool-btn" onclick="window.location.href='/tool/9'">🌿 Leaf Color Check / पत्ते रंग जांच</button>
<button class="tool-btn" onclick="window.location.href='/tool/10'">📦 Storage Advice / भंडारण सलाह</button>

</body>
</html>
"""
    # ==========================
# Tools Logic
# ==========================
@app.route("/tool/<int:id>")
def tool(id):

    data = {

        1:{
            "question":"क्या खेत में बारिश हो रही है? / Is it raining?",
            "yes":{
                "theory":"बारिश से मिट्टी की नमी बढ़ती है। / Rain increases soil moisture.",
                "practical":"आज सिंचाई न करें। पानी बचाएं। / Do not irrigate today. Save water."
            },
            "no":{
                "theory":"मिट्टी सूख सकती है। / Soil may dry.",
                "practical":"हल्की सिंचाई करें। / Do light irrigation."
            }
        },

        2:{
            "question":"पौधा हरा और मजबूत दिख रहा है? / Plant healthy green?",
            "yes":{
                "theory":"हरी पत्तियाँ अच्छे पोषण का संकेत हैं। / Green leaves show good nutrition.",
                "practical":"अभी खाद न डालें। सामान्य देखभाल करें। / No fertilizer needed now."
            },
            "no":{
                "theory":"पोषक तत्व की कमी हो सकती है। / Nutrient deficiency possible.",
                "practical":"नाइट्रोजन वाली खाद दें। / Add nitrogen fertilizer."
            }
        },

        3:{
            "question":"कीड़े या रोग दिख रहे हैं? / Pests visible?",
            "yes":{
                "theory":"कीट फसल को नुकसान पहुंचाते हैं। / Pests damage crops.",
                "practical":"कीटनाशक स्प्रे करें। / Spray pesticide."
            },
            "no":{
                "theory":"फसल सुरक्षित है। / Crop is safe.",
                "practical":"सप्ताह में एक बार निरीक्षण करें। / Inspect weekly."
            }
        },

        4:{
            "question":"मिट्टी बहुत सूखी है? / Is soil very dry?",
            "yes":{
                "theory":"सूखी मिट्टी से जड़ें कमजोर होती हैं। / Dry soil weakens roots.",
                "practical":"तुरंत सिंचाई करें। / Irrigate immediately."
            },
            "no":{
                "theory":"नमी पर्याप्त है। / Moisture sufficient.",
                "practical":"अभी पानी की जरूरत नहीं। / No irrigation needed."
            }
        },

        5:{
            "question":"दाने सख्त हो गए हैं? / Grains hard?",
            "yes":{
                "theory":"सख्त दाने कटाई का संकेत हैं। / Hard grains mean harvest time.",
                "practical":"कटाई शुरू करें। / Start harvesting."
            },
            "no":{
                "theory":"फसल अभी कच्ची है। / Crop still immature.",
                "practical":"1-2 सप्ताह प्रतीक्षा करें। / Wait 1-2 weeks."
            }
        },

        6:{
            "question":"बहुत अधिक गर्मी है? / Too much heat?",
            "yes":{
                "theory":"अधिक तापमान फसल को नुकसान दे सकता है। / High heat harms crops.",
                "practical":"अतिरिक्त सिंचाई करें। / Increase watering."
            },
            "no":{
                "theory":"तापमान सामान्य है। / Temperature normal.",
                "practical":"सामान्य देखभाल जारी रखें। / Continue normal care."
            }
        },

        7:{
            "question":"आसमान में घने बादल हैं? / Heavy clouds?",
            "yes":{
                "theory":"बारिश की संभावना है। / Rain likely.",
                "practical":"खाद या स्प्रे आज न करें। / Avoid fertilizer/spray today."
            },
            "no":{
                "theory":"बारिश की संभावना कम है। / Low rain chance.",
                "practical":"सिंचाई कर सकते हैं। / You may irrigate."
            }
        },

        8:{
            "question":"क्या आपने हाल में खाद डाली है? / Recently added fertilizer?",
            "yes":{
                "theory":"अधिक खाद नुकसान कर सकती है। / Excess fertilizer harmful.",
                "practical":"अभी और खाद न डालें। / Do not add more."
            },
            "no":{
                "theory":"पोषक तत्व की जरूरत हो सकती है। / Nutrients may be needed.",
                "practical":"संतुलित खाद डालें। / Add balanced fertilizer."
            }
        },

        9:{
            "question":"पत्ते पीले हो रहे हैं? / Leaves turning yellow?",
            "yes":{
                "theory":"नाइट्रोजन की कमी हो सकती है। / Nitrogen deficiency possible.",
                "practical":"यूरिया या नाइट्रोजन खाद दें। / Add urea."
            },
            "no":{
                "theory":"पौधा स्वस्थ है। / Plant healthy.",
                "practical":"सामान्य देखभाल रखें। / Maintain care."
            }
        },

        10:{
            "question":"फसल पूरी तरह सूख गई है? / Crop fully dry?",
            "yes":{
                "theory":"भंडारण के लिए सही समय है। / Good for storage.",
                "practical":"सूखी जगह में स्टोर करें। / Store in dry place."
            },
            "no":{
                "theory":"नमी बची है। / Moisture present.",
                "practical":"कुछ दिन और सुखाएं। / Dry for few more days."
            }
        }
    }

    item = data.get(id)

    return f"""
    <html>
    <head>
    <style>
    body{{
        margin:0;
        font-family:Montserrat;
        background: linear-gradient(135deg,#0f2027,#2c5364);
        color:white;
        text-align:center;
    }}
    h2{{padding-top:30px;}}
    .btn{{
        width:80%;
        padding:15px;
        margin:15px;
        font-size:18px;
        border:none;
        border-radius:12px;
        background:#fdd835;
        cursor:pointer;
    }}
    .result{{
        margin:20px;
        padding:15px;
        background:rgba(255,255,255,0.2);
        border-radius:12px;
    }}
    </style>

    <script>
    function showAnswer(type){{
        let theory = "{item['yes']['theory']}";
        let practical = "{item['yes']['practical']}";

        if(type == 'no'){{
            theory = "{item['no']['theory']}";
            practical = "{item['no']['practical']}";
        }}

        document.getElementById("result").innerHTML =
        "<div class='result'><b>Theory / सिद्धांत:</b><br>"+theory+
        "<br><br><b>Practical / व्यवहारिक उपाय:</b><br>"+practical+"</div>";
    }}
    </script>

    </head>
    <body>

    <h2>{item['question']}</h2>

    <button class="btn" onclick="showAnswer('yes')">हाँ / Yes</button>
    <button class="btn" onclick="showAnswer('no')">नहीं / No</button>

    <div id="result"></div>

    <br><br>
    <a href="/crop" style="color:white;">⬅ Back</a>

    </body>
    </html>
    """
