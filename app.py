<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parth's Kisan Saathi</title>
    <style>
        :root {
            --primary: #2E7D32; /* Deep Green */
            --secondary: #81C784; /* Light Green */
            --accent: #FFD54F; /* Harvest Gold */
            --dark: #1B5E20;
            --light: #F1F8E9;
            --white: #ffffff;
            --shadow: 0 4px 15px rgba(0,0,0,0.1);
            --radius: 16px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: var(--light);
            color: #333;
            /* Aesthetic Farming Background */
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('https://images.unsplash.com/photo-1625246333195-58197bd47d26?q=80&w=1920&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            min-height: 100vh;
        }

        /* --- Header --- */
        header {
            background: rgba(255, 255, 255, 0.95);
            padding: 15px 20px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.2rem;
            font-weight: 800;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span {
            color: var(--accent);
        }

        .ai-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            transition: transform 0.2s;
        }

        .ai-btn:active {
            transform: scale(0.95);
        }

        /* --- Main Dashboard --- */
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 15px;
        }

        .welcome-text {
            color: white;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
            margin-bottom: 20px;
            text-align: center;
        }

        .welcome-text h1 {
            font-size: 1.8rem;
            margin-bottom: 5px;
        }

        .category-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
            gap: 15px;
        }

        .category-card {
            background: var(--white);
            border-radius: var(--radius);
            padding: 20px;
            text-align: center;
            cursor: pointer;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
            border-bottom: 4px solid var(--primary);
            position: relative;
            overflow: hidden;
        }

        .category-card:hover {
            transform: translateY(-5px);
            background: var(--light);
        }

        .cat-icon {
            font-size: 2rem;
            margin-bottom: 10px;
            display: block;
        }

        .cat-title {
            font-weight: 700;
            color: var(--dark);
            font-size: 0.95rem;
        }

        .cat-count {
            font-size: 0.75rem;
            color: #777;
            margin-top: 5px;
        }

        /* --- Tool Modal --- */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.6);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            backdrop-filter: blur(5px);
        }

        .modal-content {
            background: white;
            width: 90%;
            max-width: 500px;
            max-height: 90vh;
            border-radius: var(--radius);
            padding: 25px;
            overflow-y: auto;
            position: relative;
            animation: slideUp 0.3s ease;
        }

        @keyframes slideUp {
            from { transform: translateY(50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .close-modal {
            position: absolute;
            top: 15px;
            right: 15px;
            background: #eee;
            border: none;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            cursor: pointer;
            font-weight: bold;
        }

        .tool-list {
            list-style: none;
        }

        .tool-item {
            padding: 15px;
            border-bottom: 1px solid #eee;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background 0.2s;
        }

        .tool-item:hover {
            background: var(--light);
        }

        .tool-item h4 {
            color: var(--dark);
        }

        .tool-item span {
            font-size: 1.2rem;
            color: var(--secondary);
        }

        /* --- Active Tool Interface --- */
        .tool-interface {
            display: none;
        }

        .tool-header {
            border-bottom: 2px solid var(--accent);
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        .input-group {
            margin-bottom: 15px;
        }

        .input-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: var(--dark);
        }

        .input-group input, .input-group select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 1rem;
        }

        .action-btn {
            width: 100%;
            padding: 12px;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
        }

        .result-box {
            margin-top: 20px;
            padding: 15px;
            background: var(--light);
            border-radius: 8px;
            border-left: 5px solid var(--accent);
            display: none;
        }

        /* --- AI Chat Interface --- */
        .chat-container {
            display: none;
            flex-direction: column;
            height: 80vh;
        }

        .chat-history {
            flex-grow: 1;
            overflow-y: auto;
            padding: 10px;
            background: #f9f9f9;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        .message {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 10px;
            max-width: 80%;
            font-size: 0.9rem;
        }

        .user-msg {
            background: var(--primary);
            color: white;
            align-self: flex-end;
            margin-left: auto;
        }

        .ai-msg {
            background: #e0e0e0;
            color: #333;
            align-self: flex-start;
        }

        .chat-input-area {
            display: flex;
            gap: 10px;
        }

        .chat-input-area input {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 20px;
        }

        /* --- Footer --- */
        footer {
            text-align: center;
            padding: 20px;
            color: white;
            font-size: 0.8rem;
            margin-top: 40px;
        }

        /* Responsive */
        @media (max-width: 600px) {
            .category-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .welcome-text h1 {
                font-size: 1.4rem;
            }
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">
            🌾 PARTH'S <span>KISAN SAATHI</span>
        </div>
        <button class="ai-btn" onclick="openAI()">
            🤖 AI Assistant
        </button>
    </header>

    <div class="container">
        <div class="welcome-text">
            <h1>Welcome, Farmer</h1>
            <p>Select a category to find your tools</p>
        </div>

        <div class="category-grid" id="categoryGrid">
            <!-- Categories injected by JS -->
        </div>
    </div>

    <!-- Tool Modal -->
    <div class="modal-overlay" id="toolModal">
        <div class="modal-content">
            <button class="close-modal" onclick="closeModal()">×</button>
            <h2 id="modalTitle" style="color: var(--primary); margin-bottom: 15px;">Category Name</h2>
            
            <!-- List View -->
            <ul class="tool-list" id="toolList">
                <!-- Tools injected here -->
            </ul>

            <!-- Active Tool View -->
            <div class="tool-interface" id="activeToolView">
                <div class="tool-header">
                    <h3 id="activeToolName">Tool Name</h3>
                    <p id="activeToolDesc" style="font-size: 0.9rem; color: #666;">Description</p>
                </div>
                <div id="toolInputs">
                    <!-- Dynamic Inputs -->
                </div>
                <button class="action-btn" onclick="calculateResult()">Calculate</button>
                <div class="result-box" id="resultBox">
                    <strong>Result:</strong> <span id="resultValue"></span>
                </div>
                <button class="action-btn" style="background:#777; margin-top:10px;" onclick="backToTools()">Back to List</button>
            </div>
        </div>
    </div>

    <!-- AI Chat Modal -->
    <div class="modal-overlay" id="aiModal">
        <div class="modal-content" style="max-width: 400px;">
            <button class="close-modal" onclick="closeAI()">×</button>
            <h2 style="color: var(--primary); margin-bottom: 10px;">AI Kisan Assistant</h2>
            <div class="chat-container" id="chatContainer">
                <div class="chat-history" id="chatHistory">
                    <div class="message ai-msg">Namaste! I am your AI assistant. Ask me about crops, weather, or prices.</div>
                </div>
                <div class="chat-input-area">
                    <input type="text" id="chatInput" placeholder="Type your question..." onkeypress="handleEnter(event)">
                    <button class="action-btn" style="width: auto; margin:0;" onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
    </div>

    <footer>
        &copy; 2023 PARTH'S KISAN SAATHI. Empowering Farmers.
    </footer>

    <script>
        // --- DATA STRUCTURE ---
        // 11 Categories with 10 tools each (Representative subset for code brevity, but structure supports 10)
        const categories = [
            {
                id: 1, name: "Crop Calculator", icon: "🌾",
                tools: [
                    { id: "seed_calc", name: "Seed Requirement", desc: "Calculate seeds needed per acre.", inputs: [{label: "Area (Acres)", type: "number"}, {label: "Seed Rate (kg/acre)", type: "number"}], calc: (v1, v2) => (v1 * v2).toFixed(2) + " kg" },
                    { id: "fertilizer_calc", name: "Fertilizer Mix", desc: "Calculate NPK requirement.", inputs: [{label: "Crop Type", type: "select", options: ["Wheat", "Rice", "Cotton"]}, {label: "Area (Acres)", type: "number"}], calc: (v1, v2) => "Approx " + (v2 * 20) + " kg Urea needed." },
                    { id: "water_calc", name: "Water Irrigation", desc: "Water needed for irrigation.", inputs: [{label: "Area (Acres)", type: "number"}, {label: "Water Depth (mm)", type: "number"}], calc: (v1, v2) => (v1 * v2 * 10).toFixed(0) + " Liters" },
                    { id: "yield_est", name: "Yield Estimator", desc: "Estimate total yield.", inputs: [{label: "Area (Acres)", type: "number"}, {label: "Yield per Acre (kg)", type: "number"}], calc: (v1, v2) => (v1 * v2).toFixed(0) + " kg Total" },
                    { id: "cost_calc", name: "Cost of Cultivation", desc: "Total farming cost.", inputs: [{label: "Labor Cost", type: "number"}, {label: "Input Cost", type: "number"}], calc: (v1, v2) => "₹" + (v1 + v2) },
                    { id: "profit_calc", name: "Profit Calculator", desc: "Net profit estimation.", inputs: [{label: "Total Cost", type: "number"}, {label: "Selling Price", type: "number"}], calc: (v1, v2) => "Profit: ₹" + (v2 - v1) },
                    { id: "spray_calc", name: "Spray Mix", desc: "Chemical dosage for spray.", inputs: [{label: "Tank Capacity (L)", type: "number"}, {label: "Dosage (ml/L)", type: "number"}], calc: (v1, v2) => (v1 * v2).toFixed(1) + " ml Chemical needed" },
                    { id: "hoeing_calc", name: "Hoeing Days", desc: "Labor days for hoeing.", inputs: [{label: "Area (Acres)", type: "number"}], calc: (v1) => Math.ceil(v1 * 2) + " Days" },
                    { id: "harvest_calc", name: "Harvest Baskets", desc: "Baskets needed for harvest.", inputs: [{label: "Total Yield (kg)", type: "number"}], calc: (v1) => Math.ceil(v1 / 50) + " Baskets (50kg each)" },
                    { id: "transport_calc", name: "Transport Cost", desc: "Vehicle cost estimation.", inputs: [{label: "Distance (km)", type: "number"}, {label: "Rate per km", type: "number"}], calc: (v1, v2) => "₹" + (v1 * v2)
