from app.rule_engine.loader.rules_loader import (
    get_rules_by_category
)

from app.rule_engine.evaluators.generic_evaluator import (
    evaluate_conditions
)


def evaluate_category(
    category,
    context
):

    rules = get_rules_by_category(
        category
    )

    triggered = []

    print(
        f"\n{category.upper()} RULES:",
        len(rules)
    )

    for rule in rules:

        conditions = (
            rule.get(
                "conditions",
                {}
            )
        )

        try:

            if evaluate_conditions(
                conditions,
                context
            ):

                triggered.append(
                    rule
                )

        except Exception as e:

            print(
                f"Rule Error:"
                f" {rule.get('rule_id')}"
            )

            print(e)

    print(
        f"TRIGGERED {category}:",
        len(triggered)
    )

    return triggered


def evaluate_all_rules(
    context
):

    categories = [

        "weather",

        "disease",

        "irrigation",

        "fertilizer",

        "pest",

        "yield"
    ]

    results = []

    print("\n================")
    print("RULE ENGINE")
    print("================")

    print(context)

    for category in categories:

        category_results = (
            evaluate_category(
                category,
                context
            )
        )

        results.extend(
            category_results
        )

    results.sort(

        key=lambda rule: (

            rule.get(
                "priority",
                99
            ),

            -rule.get(
                "risk_score",
                0
            ),

            -rule.get(
                "confidence",
                0
            )
        )
    )

    print(
        "\nTOTAL TRIGGERED:",
        len(results)
    )

    return results