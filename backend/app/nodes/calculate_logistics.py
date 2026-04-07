from app.db.mock_rules import LOGISTICS_RULES
from app.graph.state import GraphState


def calculate_logistics(state: GraphState) -> dict:
    category = state.get("category", "general_waste")
    plan = LOGISTICS_RULES.get(category, LOGISTICS_RULES["general_waste"])
    return {"logistics_plan": dict(plan)}
