import math
import csv
import json
from collections import defaultdict
from pathlib import Path


def process_telemetry(csv_path, json_path):
    devices = defaultdict(
        lambda: {"record_count": 0, "temperature_sum": 0.0,
                 "error_count": 0}
    )

    required_columns = {"device_id", "status", "temperature"}

    with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not required_columns.issubset(
            reader.fieldnames
        ):
            raise ValueError(
                "CSV must contain device_id, status, and temperature columns"
            )

        for row in reader:
            device_id = (row.get("device_id") or "").strip()
            status = (row.get("status") or "").strip().upper()

            try:
                temperature = float(row["temperature"])
            except (ValueError, TypeError, KeyError):
                continue

            if not device_id or not __import__("math").isfinite(temperature):
                continue

            device = devices[device_id]
            device["record_count"] += 1
            device["temperature_sum"] += temperature

            if status == "ERROR":
                device["error_count"] += 1

    results = []

    for device_id, stats in sorted(devices.items()):
        average = stats["temperature_sum"] / stats["record_count"]

        if average > 80.0:
            continue

        results.append({
            "device_id": device_id,
            "record_count": stats["record_count"],
            "average_temperature": round(average, 2),
            "error_count": stats["error_count"],
        })

    output_path = Path(json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print_summary(results)
    return results


def print_summary(results):
    headers = ("Device ID", "Records", "Avg Temp", "Errors")
    print(
        f"{headers[0]:<15} {headers[1]:>8} "
        f"{headers[2]:>12} {headers[3]:>8}"
    )
    print("-" * 47)

    for device in results:
        print(
            f"{device['device_id']:<15} "
            f"{device['record_count']:>8} "
            f"{device['average_temperature']:>12.2f} "
            f"{device['error_count']:>8}"
        )
