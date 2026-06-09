from datetime import date


def calculate_crop_age(sowing_date):

    if sowing_date is None:
        return None

    return (
        date.today() - sowing_date
    ).days