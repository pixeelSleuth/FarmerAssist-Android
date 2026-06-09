import json

from functools import lru_cache

RULES_PATH = (
    "app/knowledge_base/rules/rules.json"
)


@lru_cache(maxsize=1)
def load_rules():

    with open(
        RULES_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def get_rules_by_category(
    category: str
):

    data = load_rules()

    rules = []

    # Support multiple JSON structures

    if isinstance(data, dict):

        if "rule_sets" in data:

            for rule_set in data["rule_sets"]:

                rule_category = (
                    rule_set.get(
                        "category",
                        ""
                    )
                    .strip()
                    .lower()
                )

                if (
                    rule_category
                    ==
                    category.lower()
                ):

                    rules.extend(
                        rule_set.get(
                            "rules",
                            []
                        )
                    )

        elif "rules" in data:

            for rule in data["rules"]:

                rule_category = (
                    rule.get(
                        "category",
                        ""
                    )
                    .strip()
                    .lower()
                )

                if (
                    rule_category
                    ==
                    category.lower()
                ):

                    rules.append(rule)

    elif isinstance(data, list):

        for rule in data:

            rule_category = (
                rule.get(
                    "category",
                    ""
                )
                .strip()
                .lower()
            )

            if (
                rule_category
                ==
                category.lower()
            ):

                rules.append(rule)

    return rules