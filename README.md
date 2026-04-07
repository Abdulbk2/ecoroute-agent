# ♻️ EcoRoute: Agentic Industrial Waste Intelligence

**Built for the Agentic Edge AI APAC Hackathon 2026**

EcoRoute is an Agentic AI logistics platform designed to eliminate the guesswork, compliance risks, and carbon emissions associated with industrial waste disposal. By leveraging LangGraph and an API-first architecture, EcoRoute automates the identification, regulatory compliance, and routing of hazardous and high-value materials.

![EcoRoute Dashboard Preview](https://via.placeholder.com/800x400.png?text=EcoRoute+Enterprise+Dashboard) *(Note: Add a real screenshot of your UI here!)*

## 🚀 The Problem & The Solution
**The Problem:** Industrial facilities currently rely on manual processes to navigate complex EPA regulations and locate specialized disposal facilities. A single misclassification of materials like Used Industrial Oil or E-Waste can result in $75,000/day fines and severe environmental damage.

**The Solution:** EcoRoute replaces manual lookup with an intelligent Agentic workflow. Users simply input their waste parameters, and our LangGraph backend takes over:
1. **Categorizes** the exact material profile.
2. **Cross-references** live EPA/ESG regulatory databases.
3. **Calculates** carbon offsets and financial impact (disposal fees vs. asset recovery).
4. **Routes** the material to the optimal certified local facility.

## 🧠 The Tech Stack
EcoRoute is a full-stack application completely decoupled for edge-device integration.
* **Frontend:** React, Vite, Tailwind-inspired custom CSS
* **API Bridge:** FastAPI (Python), Uvicorn
* **Agentic Engine:** LangGraph (StateGraph architecture)
* **Deployment:** Docker, Google Cloud Run

## 📡 Phase 2: The IoT Hardware Integration
EcoRoute wasn't just built as a web app; it is built as the "brain" for industrial IoT. 
In our next phase, EcoRoute's API will connect directly to edge sensors on factory waste tanks. When a sensor detects a tank is at 90% capacity, the hardware will ping the FastAPI endpoint, and the AI agent will automatically dispatch a HAZMAT vehicle—achieving **Zero-Touch Logistics.**

## 💻 Local Setup & Installation

**1. Clone the Repository**
```bash
git clone [https://github.com/Abdulbk2/ecoroute-agent.git](https://github.com/Abdulbk2/ecoroute-agent.git)
cd ecoroute-agent
2. Start the FastAPI Backend (Terminal 1)

Bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
cd backend
uvicorn main:app --reload --port 8000
3. Start the React Frontend (Terminal 2)

Bash
cd frontend
npm install
npm run dev
The application will now be running on http://localhost:5173 with an internal proxy routing to the Python backend.

📂 Architecture Flow (LangGraph)
Our AI utilizes a strict State Machine to prevent hallucination and ensure absolute compliance:
[User Input] ➔ Categorize Node ➔ Compliance Node ➔ Logistics Node ➔ JSON Synthesis ➔ [React UI]

👥 The Team
Abdulrahman Yahaya - IoT Architecture, Full-Stack API Pipeline, React UI

Muhammad - Agentic Backend Logic & Compliance Validation

Payal - Logistics Routing & Carbon Math Tools

Sravani - DevOps & Cloud Run Deployment


***

### How to push this quickly:
1. Save that text into a file named `README.md` in your main `ecoroute_agent` folder.
2. Run your final trio of git commands:
```bash
git add README.md
git commit -m "Added professional hackathon README"
git push origin main
