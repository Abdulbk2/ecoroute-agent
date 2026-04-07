from app.db.mock_rules import COMPLIANCE_RULES
from app.graph.state import GraphState


def check_compliance(state: GraphState) -> dict:
    category = state.get("category", "general_waste")
    rule = COMPLIANCE_RULES.get(category, COMPLIANCE_RULES["general_waste"])
    return {"compliance_rules": rule}
