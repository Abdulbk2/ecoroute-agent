from typing import Any, Dict, NotRequired, TypedDict


class GraphState(TypedDict):
    waste_input: str
    category: NotRequired[str]
    compliance_rules: NotRequired[str]
    logistics_plan: NotRequired[Dict[str, Any]]
    final_report: NotRequired[Dict[str, Any]]
