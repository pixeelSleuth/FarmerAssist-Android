from app.db.mysql import SessionLocal
from app.models.advisory_log import AdvisoryLog


def save_advisory(
    farmer_id,
    advisory
):

    db = SessionLocal()

    try:

        record = AdvisoryLog(

            farmer_id=farmer_id,

            rule_id=advisory.get(
                "rule_id"
            ),

            advisory_type=advisory.get(
                "category"
            ),

            category=advisory.get(
                "category"
            ),

            severity=advisory.get(
                "severity"
            ),

            risk_score=advisory.get(
                "risk_score"
            ),

            confidence_score=advisory.get(
                "confidence"
            ),

            advisory_text=advisory.get(
                "reason"
            )
        )

        db.add(record)

        db.commit()

    finally:

        db.close()


def get_recent_advisories(farmer_id):

    db = SessionLocal()

    try:
        advisories = (
            db.query(AdvisoryLog)
            .filter(
                AdvisoryLog.farmer_id == farmer_id
            )
            .order_by(
                AdvisoryLog.generated_at.desc()
            )
            .limit(10)
            .all()
        )
        return advisories
    finally:
        db.close()