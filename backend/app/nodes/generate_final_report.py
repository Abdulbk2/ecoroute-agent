from app.graph.state import GraphState


def generate_final_report(state: GraphState) -> dict:
    logistics_plan = state.get("logistics_plan", {})

    return {
        "final_report": {
            "status": logistics_plan.get("status", "Action Required: Manual Review"),
            "action": logistics_plan.get("action", "Escalate to operations team for manual waste assessment."),
            "rule": state.get("compliance_rules", "Requires manual review before disposal or recycling."),
            "carbonSaved": logistics_plan.get("carbon_saved", "Unknown"),
            "financialImpact": logistics_plan.get("financial_impact", "Pending assessment"),
        }
    }
