from typing import Any, Dict, TypedDict


class GraphState(TypedDict):
    waste_input: str
    category: str
    compliance_rules: str
    logistics_plan: Dict[str, Any]
    final_report: Dict[str, Any]
