COMPLIANCE_RULES = {
    "industrial_oil": "Must be handled by a certified hazardous waste transporter. Cannot be mixed with other solvents.",
    "scrap_copper": "Non-hazardous. High resale value.",
    "e_waste": "Requires strict data destruction certification and heavy metal containment.",
    "general_waste": "Requires manual review before disposal or recycling.",
}


LOGISTICS_RULES = {
    "industrial_oil": {
        "status": "Action Required: Hazardous Waste",
        "action": "Route to nearest oil re-refining facility.",
        "carbon_saved": "850 kg CO2e",
        "financial_impact": "-$250.00 (Handling Cost)",
    },
    "scrap_copper": {
        "status": "Action Required: High Value",
        "action": "Route to local certified scrap yard.",
        "carbon_saved": "1,200 kg CO2e",
        "financial_impact": "+$850.00 (Est. Resale)",
    },
    "e_waste": {
        "status": "Action Required: Certified Processing",
        "action": "Route to certified e-waste recycler with data wiping capabilities.",
        "carbon_saved": "640 kg CO2e",
        "financial_impact": "-$120.00 (Secure Processing)",
    },
    "general_waste": {
        "status": "Action Required: Manual Review",
        "action": "Escalate to operations team for manual waste assessment.",
        "carbon_saved": "Unknown",
        "financial_impact": "Pending assessment",
    },
}
