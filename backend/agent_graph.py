from typing import TypedDict, Dict
from langgraph.graph import StateGraph, START, END

# ==========================================
# 1. DEFINE THE STATE (The Data Passed Between Nodes)
# ==========================================
class AgentState(TypedDict):
    waste_input: str        # User's raw text (e.g., "500L of used oil")
    category: str           # Set by Muhammad's node (e.g., "hazardous_oil")
    compliance_rules: str   # Set by Muhammad's SQL check
    logistics_plan: str     # Set by Payal's routing logic
    final_report: dict      # Final JSON formatted for the React frontend

# ==========================================
# 2. DEFINE THE NODES (Team Tasks)
# ==========================================

def categorize_waste(state: AgentState) -> Dict:
    """ MUHAMMAD'S TASK: Use LLM to extract the category from the input. """
    print(f"--- CATEGORIZING WASTE: {state['waste_input']} ---")
    
    # TODO @Muhammad: Put your LLM Prompt here to classify the waste
    # Simulated output for now:
    inferred_category = "used_industrial_oil" 
    
    return {"category": inferred_category}

def check_compliance(state: AgentState) -> Dict:
    """ MUHAMMAD'S TASK: Query ESG/EPA laws based on the category. """
    print(f"--- CHECKING COMPLIANCE FOR: {state['category']} ---")
    
    # TODO @Muhammad: Put your SQL/RAG logic here to fetch laws
    # Simulated output for now:
    rules = "Must be handled by certified hazardous waste transporter."
    
    return {"compliance_rules": rules}

def calculate_logistics(state: AgentState) -> Dict:
    """ PAYAL'S TASK: Use Python tools to calculate carbon and find facilities. """
    print(f"--- CALCULATING LOGISTICS FOR: {state['category']} ---")
    
    # TODO @Payal: Put your API calls / Carbon Math tools here
    # Simulated output for now:
    plan = "Route to SafeDispose Inc. Carbon saved: 500kg CO2e"
    
    return {"logistics_plan": plan}

def generate_final_report(state: AgentState) -> Dict:
    """ TEAM TASK: Synthesize everything into the React JSON schema. """
    print("--- GENERATING FINAL JSON REPORT ---")
    
    # TODO: Use a final LLM call to format this perfectly for the React UI
    final_json = {
        "status": "Action Required: Hazardous",
        "action": state['logistics_plan'],
        "rule": state['compliance_rules'],
        "carbonSaved": "500 kg CO2e", # Extract from logistics plan
        "financialImpact": "-$150.00 (Disposal Fee)"
    }
    
    return {"final_report": final_json}

# ==========================================
# 3. BUILD AND COMPILE THE GRAPH
# ==========================================
workflow = StateGraph(AgentState)

# Add all the nodes
workflow.add_node("categorize", categorize_waste)
workflow.add_node("compliance", check_compliance)
workflow.add_node("logistics", calculate_logistics)
workflow.add_node("report", generate_final_report)

# Define the flow (Edges)
workflow.add_edge(START, "categorize")
workflow.add_edge("categorize", "compliance")
workflow.add_edge("compliance", "logistics")
workflow.add_edge("logistics", "report")
workflow.add_edge("report", END)

# Compile the final agent
ecoroute_agent = workflow.compile()

# ==========================================
# TEST RUNNER (For Local Debugging)
# ==========================================
if __name__ == "__main__":
    test_input = {"waste_input": "500 liters of used industrial hydraulic oil"}
    print("Starting EcoRoute Agent Run...\n")
    
    final_state = ecoroute_agent.invoke(test_input)
    
    print("\n=== FINAL OUTPUT FOR REACT UI ===")
    print(final_state['final_report'])