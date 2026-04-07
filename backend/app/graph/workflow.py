from langgraph.graph import END, START, StateGraph

from app.graph.state import GraphState
from app.nodes.calculate_logistics import calculate_logistics
from app.nodes.categorize_waste import categorize_waste
from app.nodes.check_compliance import check_compliance
from app.nodes.generate_final_report import generate_final_report


def build_workflow():
    graph = StateGraph(GraphState)

    graph.add_node("categorize_waste", categorize_waste)
    graph.add_node("check_compliance", check_compliance)
    graph.add_node("calculate_logistics", calculate_logistics)
    graph.add_node("generate_final_report", generate_final_report)

    graph.add_edge(START, "categorize_waste")
    graph.add_edge("categorize_waste", "check_compliance")
    graph.add_edge("check_compliance", "calculate_logistics")
    graph.add_edge("calculate_logistics", "generate_final_report")
    graph.add_edge("generate_final_report", END)

    return graph.compile()
