from src.cleaner import clean_sensor_readings


def test_mixed_values():
    assert clean_sensor_readings(
        [10, "20.5", None, -5, "invalid", 600]
    ) == [10.0, 20.5, 500.0]


def test_empty_list():
    assert clean_sensor_readings([]) == []


def test_all_invalid_values():
    assert clean_sensor_readings(
        [None, "invalid", -10]
    ) == []
