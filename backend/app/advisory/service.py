from .utils import calculate_severity


class AdvisoryEngine:

    @staticmethod
    def generate(triggered_rules):

        advisories = []

        for rule in triggered_rules:

            advisory = {
                "rule_id": rule["rule_id"],

                "title": rule["rule_name"],

                "category": rule["category"],

                "severity": calculate_severity(
                    rule["risk_score"]
                ),

                "risk_score": rule["risk_score"],
                "confidence": rule["confidence"],

                "reason": rule["reason"],

                "recommended_actions":
                    rule["actions"]
            }

            advisories.append(advisory)

        advisories.sort(
            key=lambda x:
            (
                0 if x["severity"] == "HIGH" else
                1 if x["severity"] == "MEDIUM" else
                2
            )
        )

        return advisories