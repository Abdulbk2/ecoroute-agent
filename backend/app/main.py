from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.graph.workflow import build_workflow


class WasteRequest(BaseModel):
    wasteType: str
    quantity: str
    unit: str


def create_app() -> FastAPI:
    app = FastAPI(title="EcoRoute Agent API", description="B2B AI Logistics Backend")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    def build_input_text(waste_type: str, quantity: str, unit: str) -> str:
        return f"{quantity} {unit} of {waste_type}"

    @app.post("/api/analyze")
    async def analyze(request: WasteRequest):
        waste_input = build_input_text(request.wasteType, request.quantity, request.unit)
        workflow = build_workflow()
        result = workflow.invoke({"waste_input": waste_input})
        return result.get("final_report", {"error": "Failed to generate report"})

    @app.get("/")
    async def read_root():
        return {"status": "EcoRoute API is running."}

    return app


app = create_app()
