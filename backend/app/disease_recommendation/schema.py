from pydantic import BaseModel
from typing import List, Dict, Any


class DiseaseRecommendationResponse(
    BaseModel
):

    disease_name: str

    confidence: float

    severity: str

    causal_organism: str

    symptoms: List[str]

    favorable_conditions: List[str]

    prevention: List[str]

    chemical_control: List[str]

    kannada_translation: Dict[
        str,
        Any
    ]