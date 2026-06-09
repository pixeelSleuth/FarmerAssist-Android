def evaluate_operator(
    actual,
    operator,
    expected
):

    if operator == ">":
        return actual > expected

    elif operator == "<":
        return actual < expected

    elif operator == ">=":
        return actual >= expected

    elif operator == "<=":
        return actual <= expected

    elif operator == "==":
        return actual == expected

    elif operator == "!=":
        return actual != expected

    return False


def evaluate_between(
    actual,
    minimum,
    maximum
):

    return minimum <= actual <= maximum


def evaluate_conditions(
    conditions,
    context
):

    for field, rule in conditions.items():

        if field not in context:

            print(
                f"[MISSING FIELD] {field}"
            )

            return False

        actual = context[field]

        if isinstance(rule, dict):

            operator = rule.get(
                "operator"
            )

            if operator == "between":

                if not evaluate_between(
                    actual,
                    rule["min"],
                    rule["max"]
                ):

                    print(
                        f"[BETWEEN FAILED] "
                        f"{field}={actual}"
                    )

                    return False

            else:

                if not evaluate_operator(
                    actual,
                    operator,
                    rule["value"]
                ):

                    print(
                        f"[OPERATOR FAILED] "
                        f"{field}={actual} "
                        f"{operator} "
                        f"{rule['value']}"
                    )

                    return False

        else:

            if actual != rule:

                print(
                    f"[EQUALITY FAILED] "
                    f"{field}"
                )

                return False

    return True