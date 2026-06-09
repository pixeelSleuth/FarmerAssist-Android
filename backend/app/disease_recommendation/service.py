import json
from pathlib import Path


DISEASE_FILE_MAPPING = {

    "Turcicum Leaf Blight":
        "tlb_info.json",

    "Common Rust":
        "common_rust.json",

    "Pokkah Boeng":
        "pokkah_boeng.json"
}


class DiseaseRecommendationService:

    KB_PATH = Path(
        "app/knowledge_base/diseases"
    )

    @classmethod
    def get_recommendation(
        cls,
        disease_name,
        confidence
    ):

        filename = (
            DISEASE_FILE_MAPPING
            .get(disease_name)
        )

        if not filename:

            return None

        disease_file = (
            cls.KB_PATH / filename
        )

        with open(
            disease_file,
            "r",
            encoding="utf-8"
        ) as f:

            disease_info = json.load(f)

        severity = cls.calculate_severity(
            confidence
        )

        return {

            "disease_name":
                disease_name,

            "confidence":
                confidence,

            "severity":
                severity,

            "causal_organism":
                disease_info.get(
                    "causal_organism"
                ),

            "symptoms":
                disease_info.get(
                    "symptoms",
                    []
                ),

            "favorable_conditions":
                disease_info.get(
                    "favorable_conditions",
                    []
                ),

            "prevention":
                disease_info.get(
                    "prevention",
                    []
                ),

            "chemical_control":
                disease_info.get(
                    "chemical_control",
                    []
                ),

            "kannada_translation":
                disease_info.get(
                    "kannada_translation",
                    {}
                )
        }

    @staticmethod
    def calculate_severity(
        confidence
    ):

        if confidence >= 0.90:
            return "HIGH"

        elif confidence >= 0.75:
            return "MEDIUM"

        return "LOW"