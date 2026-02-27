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
@app.route("/dashboard")
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI - Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg, #87ceeb, #a8e063, #fff176, #ffffff);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white;
    display:flex;
    justify-content:center;
    align-items:flex-start;
    flex-direction:column;
    min-height:100vh;
    text-align:center;
    padding-top:40px;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.overlay{
    background:rgba(0,0,0,0.35);
    padding:30px;
    width:100%;
    max-width:500px;
    margin:auto;
    border-radius:15px;
}

/* Headings */
h1{ font-family:'Playfair Display', serif; font-size:48px; margin:0; padding:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.4); }
h2{ font-size:24px; margin:0; padding:5px; text-shadow:1px 1px 6px rgba(0,0,0,0.3); }

/* Buttons vertical */
.cat-btn{
    margin:12px 0;
    padding:18px 30px;
    border-radius:25px;
    border:none;
    background:rgba(255,255,255,0.25);
    color:white;
    font-weight:bold;
    font-size:18px;
    cursor:pointer;
    text-shadow:1px 1px 3px rgba(0,0,0,0.4);
    transition:0.3s;
    width:100%;
}
.cat-btn:hover{
    background:rgba(255,255,255,0.45);
    transform:scale(1.03);
}

.button-container{
    margin-top:30px;
    display:flex;
    flex-direction:column;
    align-items:center;
}
</style>
</head>
<body>
<div class="overlay">
<h1>PARTH'S KISAN SAATHI</h1>
<h2>Dashboard / डैशबोर्ड</h2>

<div class="button-container">
    <button class="cat-btn" onclick="alert('Category 1 – Crop Management / फ़सल प्रबंधन')">🌾 Crop Management / फ़सल प्रबंधन</button>
    <button class="cat-btn" onclick="alert('Category 2 – Irrigation Management / सिंचाई प्रबंधन')">💧 Irrigation Management / सिंचाई प्रबंधन</button>
    <button class="cat-btn" onclick="alert('Category 3 – Pest & Disease Control / कीट एवं रोग नियंत्रण')">🦠 Pest & Disease Control / कीट एवं रोग नियंत्रण</button>
    <button class="cat-btn" onclick="alert('Category 4 – Organic & AI Farming / ऑर्गेनिक & एआई खेती')">🌱 Organic & AI Farming / ऑर्गेनिक & एआई खेती</button>
    <button class="cat-btn" onclick="alert('Category 5 – Fertilizer Planning / उर्वरक योजना')">🧴 Fertilizer Planning / उर्वरक योजना</button>
    <button class="cat-btn" onclick="alert('Category 6 – Seed Management / बीज प्रबंधन')">🌾 Seed Management / बीज प्रबंधन</button>
    <button class="cat-btn" onclick="alert('Category 7 – Profit & Yield Tracking / लाभ & उत्पादन ट्रैकिंग')">📊 Profit & Yield Tracking / लाभ & उत्पादन ट्रैकिंग</button>
    <button class="cat-btn" onclick="alert('Category 8 – Smart Farming Tools / स्मार्ट खेती उपकरण')">💻 Smart Farming Tools / स्मार्ट खेती उपकरण</button>
    <button class="cat-btn" onclick="alert('Category 9 – Harvesting & Guidance / कटाई & मार्गदर्शन')">🌾 Harvesting & Guidance / कटाई & मार्गदर्शन</button>
    <button class="cat-btn" onclick="alert('Category 10 – Soil & Crop Care / मिट्टी & फ़सल देखभाल')">🛠️ Soil & Crop Care / मिट्टी & फ़सल देखभाल</button>
    <button class="cat-btn" onclick="alert('Category 11 – Reminders & Notes / रिमाइंडर & नोट्स')">📌 Reminders & Notes / रिमाइंडर & नोट्स</button>
</div>
</div>
</body>
</html>
"""
@app.route("/category1")
def category1():
    return """
<!DOCTYPE html>
<html>
<head>
<title>PARTH'S KISAN SAATHI - Crop Management</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0;
    font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg, #87ceeb, #a8e063, #fff176, #ffffff);
    background-size:400% 400%;
    animation:bgMove 20s ease infinite;
    color:#fff;
    display:flex;
    justify-content:flex-start;
    align-items:center;
    flex-direction:column;
    min-height:100vh;
    text-align:center;
    padding-top:30px;
}
@keyframes bgMove {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}
h1{ font-family:'Playfair Display', serif; font-size:48px; margin:0; padding:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.4); }
h2{ font-size:24px; margin:0; padding:5px; text-shadow:1px 1px 6px rgba(0,0,0,0.3); }

.cat-btn{
    margin:12px;
    padding:18px 30px;
    border-radius:25px;
    border:none;
    background:rgba(255,255,255,0.25);
    color:white;
    font-weight:bold;
    font-size:18px;
    cursor:pointer;
    text-shadow:1px 1px 3px rgba(0,0,0,0.4);
    transition:0.3s;
}
.cat-btn:hover{
    background:rgba(255,255,255,0.45);
    transform:scale(1.05);
}

#tools-section{
    margin-top:30px;
    padding:20px;
    width:80%;
    max-width:700px;
    background:rgba(0,128,0,0.15);
    border-radius:15px;
    text-align:left;
}
#tools-section h3{ color:#2f6f2f; }
#tools-section ul{ list-style:disc; margin-left:20px; }

#practical{
    margin-top:20px;
}
.q-block{
    background:rgba(255,255,255,0.15);
    padding:15px;
    border-radius:12px;
    margin-bottom:15px;
}
.option-btn{
    display:block;
    width:100%;
    margin:8px 0;
    padding:10px;
    border:none;
    border-radius:8px;
    background:rgba(255,255,255,0.25);
    color:white;
    font-weight:bold;
    cursor:pointer;
    transition:0.3s;
}
.option-btn:hover{
    background:rgba(255,255,255,0.45);
}
</style>
</head>
<body>

<h1>PARTH'S KISAN SAATHI</h1>
<h2>Category 1 – Crop Management / फ़सल प्रबंधन</h2>

<div id="tools-section">
    <h3>Theory / Tools:</h3>
    <ul>
        <li>Soil Type Analysis / मिट्टी प्रकार विश्लेषण</li>
        <li>Sowing Techniques / बुवाई तकनीक</li>
        <li>Fertilizer Usage / उर्वरक उपयोग</li>
        <li>Water Requirement Tips / पानी की आवश्यकता सुझाव</li>
        <li>Crop Rotation Planning / फ़सल घुमाव योजना</li>
        <li>Pest Management / कीट प्रबंधन</li>
        <li>Disease Control / रोग नियंत्रण</li>
        <li>Harvesting Guidelines / कटाई के दिशा-निर्देश</li>
        <li>Storage Techniques / भंडारण तकनीक</li>
        <li>Market Planning / बाजार योजना</li>
    </ul>
</div>

<div id="practical">
    <h3>Practical / व्यावहारिक</h3>
    
    <!-- Question 1 -->
    <div class="q-block">
        <p>1️⃣ Soil Type Identification / मिट्टी प्रकार पहचानें</p>
        <button class="option-btn" onclick="alert('Clay Soil / चिकनी मिट्टी – Moderate water retention / मध्यम जल धारण')">Clay / चिकनी</button>
        <button class="option-btn" onclick="alert('Sandy Soil / रेतीली मिट्टी – Fast drainage / तेज जल निकासी')">Sandy / रेतीली</button>
        <button class="option-btn" onclick="alert('Loamy Soil / दोमट मिट्टी – Fertile & balanced / उर्वरक & संतुलित')">Loamy / दोमट</button>
        <button class="option-btn" onclick="alert('Silty Soil / सिल्टी मिट्टी – Smooth texture / चिकनी बनावट')">Silty / सिल्टी</button>
    </div>
    
    <!-- Question 2 -->
    <div class="q-block">
        <p>2️⃣ Best Sowing Season / सबसे अच्छा बुवाई मौसम</p>
        <button class="option-btn" onclick="alert('Rabi Crops / रबी फसल – Oct to Dec / अक्टूबर से दिसम्बर')">Rabi / रबी</button>
        <button class="option-btn" onclick="alert('Kharif Crops / खरीफ फसल – June to Sep / जून से सितम्बर')">Kharif / खरीफ</button>
    </div>

</div>

</body>
</html>
"""
