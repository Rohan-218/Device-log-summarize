import math


def clean_sensor_readings(values):
   
    cleaned = []

    for value in values:
        if value is None:
            continue

        try:
            number = float(value)
        except (ValueError, TypeError):
            continue

        if not math.isfinite(number) or number < 0:
            continue

        cleaned.append(min(number, 500.0))

    return cleaned
