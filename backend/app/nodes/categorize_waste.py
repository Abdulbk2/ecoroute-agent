from app.graph.state import GraphState


def categorize_waste(state: GraphState) -> dict:
    text = state["waste_input"].lower().replace("_", " ")

    if any(keyword in text for keyword in ("oil", "hydraulic", "lubricant", "solvent")):
        return {"category": "industrial_oil"}

    if any(
        keyword in text
        for keyword in ("server", "laptop", "battery", "batteries", "e-waste", "e waste", "electronic", "lead acid")
    ):
        return {"category": "e_waste"}

    if "copper" in text:
        return {"category": "scrap_copper"}

    return {"category": "general_waste"}
