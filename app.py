from flask import Flask, request

app = Flask(__name__)

# ==========================
# Starting Screen (Already Given)
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
h1{
font-family: 'Playfair Display', serif;
font-size:56px;
margin:10px;
text-shadow:2px 2px 8px rgba(0,0,0,0.3);
}
h2{
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
<title>Dashboard / डैशबोर्ड</title>
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
a{text-decoration:none;color:white;}
</style>
</head>
<body>
<h1>Dashboard / डैशबोर्ड</h1>
<a href="/crop"><div class="card">🌾 Crop Management / फ़सल प्रबंधन</div></a>
</body>
</html>
"""

# ==========================
# Crop Management Tools
# ==========================
@app.route("/crop")
def crop():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Crop Management Tools</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<style>
body{
    margin:0; font-family:'Montserrat',sans-serif;
    background: linear-gradient(135deg,#11998e,#38ef7d,#30cfd0,#330867);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color:white; text-align:center;
}
@keyframes bgMove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}
h1{margin-top:20px; font-family:'Playfair Display', serif;}
.card{
    width:90%;
    margin:15px auto;
    padding:20px;
    border-radius:20px;
    background:rgba(0,0,0,0.35);
    font-size:20px;
    cursor:pointer;
    transition:0.3s;
}
.card:hover{background:rgba(0,0,0,0.5); transform:scale(1.02);}
a{text-decoration:none;color:white;}
</style>
</head>
<body>
<h1>🌾 Crop Management Tools / फ़सल प्रबंधन टूल्स</h1>
""" + \
"".join([f"<a href='/tool/{i}'><div class='card'>{i}️⃣ Tool {i} / टूल {i}</div></a>" for i in range(1,11)]) + \
"""
<a href='/dashboard'><div class='card'>⬅ Back to Dashboard / डैशबोर्ड पर वापस</div></a>
</body>
</html>
"""

# ==========================
# Tool Engine
# ==========================
@app.route("/tool/<int:tool_id>", methods=["GET","POST"])
def tool(tool_id):
    result=""
    if request.method=="POST":
        result="<h3>Result displayed here (practical calculation will go)</h3>"
    return f"""
<html>
<head>
<title>Tool {tool_id}</title>
<style>
body{{margin:0; font-family:'Montserrat',sans-serif; background: linear-gradient(135deg,#11998e,#38ef7d,#30cfd0,#330867); background-size: 400% 400%; animation: bgMove 20s ease infinite; color:white; text-align:center;}}
@keyframes bgMove{{0%{{background-position:0% 50%;}}50%{{background-position:100% 50%;}}100%{{background-position:0% 50%;}}}}
h2{{margin-top:20px;}}
form{{margin-top:20px;}}
input{{padding:5px; margin:5px;}}
button{{padding:8px 20px; margin-top:10px; border-radius:8px; background:linear-gradient(45deg,#fdd835,#fbc02d); border:none; color:#2f6f2f; font-weight:bold; cursor:pointer;}}
button:hover{{transform:scale(1.05);}}
</style>
</head>
<body>
<h2>Tool {tool_id} / टूल {tool_id}</h2>
{result}
<br><br>
<a href='/crop'>⬅ Back to Crop Tools / फ़सल टूल्स पर वापस</a>
</body>
</html>
"""

if __name__=="__main__":
    app.run(debug=True)
