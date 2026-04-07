from pathlib import Path
import sys

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))


def test_import_workflow_builder():
    from app.graph.workflow import build_workflow

    workflow = build_workflow()

    assert workflow is not None
