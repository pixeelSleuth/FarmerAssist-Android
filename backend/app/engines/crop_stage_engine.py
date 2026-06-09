from datetime import date

from app.services.lifecycle_loader import (
    load_lifecycle
)


class CropStageEngine:

    @staticmethod
    def calculate_crop_age(
        sowing_date
    ):

        return (
            date.today() - sowing_date
        ).days

    @staticmethod
    def get_stage(
        crop_age
    ):

        lifecycle = load_lifecycle()

        stages = lifecycle["Stages"]

        for stage in stages:

            title = stage["Title"]

            if title == "Emergence (0-15 DAS)":

                if 0 <= crop_age <= 15:

                    return {
                        "current_stage": "EMERGENCE",
                        "stage_name": title,
                        "stage_number": 4
                    }

            elif title == "Vegetative Stage (15-45 DAS)":

                if 16 <= crop_age <= 45:

                    return {
                        "current_stage": "VEGETATIVE",
                        "stage_name": title,
                        "stage_number": 5
                    }

            elif title == "Tasseling (45-65 DAS)":

                if 46 <= crop_age <= 65:

                    return {
                        "current_stage": "TASSELING",
                        "stage_name": title,
                        "stage_number": 6
                    }

            elif title == "Silking (65-75 DAS)":

                if 66 <= crop_age <= 75:

                    return {
                        "current_stage": "SILKING",
                        "stage_name": title,
                        "stage_number": 7
                    }

            elif title == "Grain Filling (75-105 DAS)":

                if 76 <= crop_age <= 105:

                    return {
                        "current_stage": "GRAIN_FILLING",
                        "stage_name": title,
                        "stage_number": 8
                    }

            elif title == "Harvest & Storage (105-120 DAS)":

                if 106 <= crop_age <= 120:

                    return {
                        "current_stage": "HARVEST",
                        "stage_name": title,
                        "stage_number": 9
                    }

        return {

            "current_stage": "UNKNOWN",

            "stage_name": "Unknown Stage",

            "stage_number": -1
        }