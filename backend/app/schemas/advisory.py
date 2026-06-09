from pydantic import BaseModel


class TriggeredRule(
    BaseModel
):

    rule_id: str

    rule_name: str

    priority: int

    action: dict


class AdvisoryResponse(
    BaseModel
):

    triggered_rules: list[
        TriggeredRule
    ]