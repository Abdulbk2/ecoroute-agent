from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_graph import ecoroute_agent  # Importing your compiled LangGraph

app = FastAPI(title="EcoRoute Agent API", description="B2B AI Logistics Backend")

# CRITICAL for Hackathons: Allow the Vite React frontend to communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This model matches the exact JSON your React form sends
class WasteRequest(BaseModel):
    wasteType: str
    quantity: str
    unit: str

@app.post("/api/analyze")
async def analyze_waste(request: WasteRequest):
    print(f"Received request from React: {request.quantity} {request.unit} of {request.wasteType}")
    
    # 1. Format the React data into a single string for the AI
    raw_input = f"{request.quantity} {request.unit} of {request.wasteType}"
    initial_state = {"waste_input": raw_input}
    
    # 2. Invoke the LangGraph Agent workflow
    # Note: In production, for long LLM calls, you might want to run this asynchronously.
    result = ecoroute_agent.invoke(initial_state)
    
    # 3. Return ONLY the final JSON payload back to the React Results Dashboard
    return result.get("final_report", {"error": "Failed to generate report"})

# Health check endpoint for Google Cloud Run
@app.get("/")
def read_root():
    return {"status": "EcoRoute API is running."}