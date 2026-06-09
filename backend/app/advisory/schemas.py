from pydantic import BaseModel
from typing import List


class Advisory(BaseModel):
    rule_id: str
    title: str
    category: str
    severity: str
    reason: str
    recommended_actions: List[str]


class AdvisoryResponse(BaseModel):
    advisories: List[Advisory]