# scoring.py

def get_risk_category(risk_percent: float) -> str:
    """
    Return a text label based on the percentage risk.
    """
    if risk_percent <= 30:
        return "Low Risk"
    elif risk_percent <= 60:
        return "Moderate Risk"
    elif risk_percent <= 90:
        return "High Risk"
    else:
        return "Very High Risk"

def format_recommendation(risk_level: str) -> str:
    """
    Return recommendation text based on risk level.
    """
    if risk_level in ["High Risk", "Very High Risk"]:
        return (
            "1. Stop sending any further money or personal info.\n"
            "2. Verify the identity of the person or platform.\n"
            "3. Consult a trusted friend or financial professional.\n"
            "4. Consider reporting the incident to authorities."
        )
    elif risk_level == "Moderate Risk":
        return (
            "1. Exercise caution and verify all information independently.\n"
            "2. Discuss concerns with a trusted friend or advisor.\n"
            "3. If unsure, pause communication until legitimacy is confirmed."
        )
    else:  # Low Risk
        return (
            "No major red flags based on these questions, but remain vigilant.\n"
            "If new warning signs appear, reassess or seek advice."
        )
