def calculate_severity(risk_score: int):

    if risk_score >= 80:
        return "HIGH"

    if risk_score >= 50:
        return "MEDIUM"

    return "LOW"