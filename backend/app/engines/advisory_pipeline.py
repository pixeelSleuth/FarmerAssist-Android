from app.services.crop_stage_service import determine_stage
from app.services.weather_service import get_current_weather
from app.rule_engine.services.rule_service import evaluate_all_rules
from app.context_builder.service import ContextBuilder
from app.advisory.service import AdvisoryEngine
from app.advisory.repository import save_advisory
from app.notifications.service import NotificationService
from app.db.mysql import get_db


class AdvisoryPipeline:
    def __init__(self, db=None):
        self.db = db
    

    async def run(self, farmer):

        crop_stage = determine_stage(
            farmer.sowing_date
        )

        weather = get_current_weather(
            farmer.latitude,
            farmer.longitude
        )

        weather_history = []

        context = await ContextBuilder.build(
            farmer,
            crop_stage,
            weather,
            weather_history
        )
        print("\n========== CONTEXT ==========")

        for key, value in context.items():
            print(key, "=", value)

        print("=============================\n")

        triggered_rules = (
            evaluate_all_rules(
                context
            )
        )

        advisories = AdvisoryEngine.generate(
            triggered_rules
        )

        for advisory in advisories:

            save_advisory(
                farmer_id=farmer.farmer_id,
                advisory=advisory
            )
            if advisory["severity"] == "HIGH":
                NotificationService.send_notification(

                    db=self.db,

                    farmer_id=farmer.farmer_id,

                    title=advisory["title"],

                    message=advisory["reason"],

                )

        return advisories