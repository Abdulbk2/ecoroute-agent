from pathlib import Path
import sys

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))


from app.db.mock_rules import COMPLIANCE_RULES, LOGISTICS_RULES
from app.graph.state import GraphState


def test_graph_state_supports_required_keys():
    state: GraphState = {
        "waste_input": "2 tons of scrap copper wire",
        "category": "scrap_copper",
        "compliance_rules": "Non-hazardous. High resale value.",
        "logistics_plan": {"action": "Route to scrap yard"},
        "final_report": {"status": "Action Required: High Value"},
    }

    assert state["category"] == "scrap_copper"


def test_dummy_rule_sets_cover_known_categories():
    assert "industrial_oil" in COMPLIANCE_RULES
    assert "scrap_copper" in COMPLIANCE_RULES
    assert "e_waste" in LOGISTICS_RULES


def test_import_workflow_builder():
    from app.graph.workflow import build_workflow

    workflow = build_workflow()

    assert workflow is not None
