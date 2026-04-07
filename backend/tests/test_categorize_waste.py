from pathlib import Path
import sys

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))


from app.nodes.categorize_waste import categorize_waste


def test_categorize_waste_detects_industrial_oil():
    result = categorize_waste({"waste_input": "500 liters of used industrial hydraulic oil"})
    assert result == {"category": "industrial_oil"}


def test_categorize_waste_detects_scrap_copper():
    result = categorize_waste({"waste_input": "2 tons of scrap copper wire"})
    assert result == {"category": "scrap_copper"}


def test_categorize_waste_detects_e_waste_before_scrap_copper():
    result = categorize_waste({"waste_input": "server wire harness"})
    assert result == {"category": "e_waste"}


def test_categorize_waste_falls_back_for_non_copper_metal():
    result = categorize_waste({"waste_input": "steel wire shelf"})
    assert result == {"category": "general_waste"}


def test_categorize_waste_falls_back_to_general_waste():
    result = categorize_waste({"waste_input": "miscellaneous unknown material"})
    assert result == {"category": "general_waste"}
