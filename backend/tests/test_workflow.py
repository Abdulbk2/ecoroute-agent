from pathlib import Path
import sys

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))


from app.db.mock_rules import COMPLIANCE_RULES, LOGISTICS_RULES
from app.graph.state import GraphState
from app.graph.workflow import build_workflow
from app.nodes.calculate_logistics import calculate_logistics
from app.nodes.check_compliance import check_compliance
from app.nodes.generate_final_report import generate_final_report


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
    workflow = build_workflow()

    assert workflow is not None


def test_check_compliance_uses_category_lookup():
    result = check_compliance({"waste_input": "2 tons of scrap copper wire", "category": "scrap_copper"})
    assert result == {"compliance_rules": "Non-hazardous. High resale value."}


def test_calculate_logistics_uses_category_lookup():
    result = calculate_logistics(
        {"waste_input": "500 liters of used industrial hydraulic oil", "category": "industrial_oil"}
    )

    assert result["logistics_plan"]["action"] == "Route to nearest oil re-refining facility."
    assert result["logistics_plan"]["status"] == "Action Required: Hazardous Waste"


def test_generate_final_report_matches_dashboard_shape():
    result = generate_final_report(
        {
            "compliance_rules": "Non-hazardous. High resale value.",
            "logistics_plan": {
                "status": "Action Required: High Value",
                "action": "Route to local certified scrap yard.",
                "carbon_saved": "1,200 kg CO2e",
                "financial_impact": "+$850.00 (Est. Resale)",
            },
        }
    )

    assert result["final_report"] == {
        "status": "Action Required: High Value",
        "action": "Route to local certified scrap yard.",
        "rule": "Non-hazardous. High resale value.",
        "carbonSaved": "1,200 kg CO2e",
        "financialImpact": "+$850.00 (Est. Resale)",
    }


def test_workflow_runs_end_to_end_for_e_waste():
    workflow = build_workflow()

    result = workflow.invoke({"waste_input": "150 kg of mixed corporate E-Waste old servers laptops batteries"})

    assert result["category"] == "e_waste"
    assert result["final_report"]["rule"].startswith("Requires strict data destruction")
    assert result["final_report"]["action"] == "Route to certified e-waste recycler with data wiping capabilities."
