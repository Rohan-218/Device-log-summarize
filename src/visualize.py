import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt


def generate_chart(json_path, image_path):
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            devices = json.load(file)
    except FileNotFoundError:
        print(f"Error: JSON file not found: {json_path}", file=sys.stderr)
        return False
    except (json.JSONDecodeError, OSError) as error:
        print(f"Error reading JSON: {error}", file=sys.stderr)
        return False

    if not isinstance(devices, list):
        print("Error: Expected a JSON list of devices.", file=sys.stderr)
        return False

    if not devices:
        print("No device data available to plot.")
        return False

    try:
        device_ids = [item["device_id"] for item in devices]
        temperatures = [
            float(item["average_temperature"]) for item in devices
        ]
    except (KeyError, TypeError, ValueError) as error:
        print(f"Invalid device data: {error}", file=sys.stderr)
        return False

    output_path = Path(image_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.bar(device_ids, temperatures)
    plt.title("Average Temperature by Device")
    plt.xlabel("Device ID")
    plt.ylabel("Average Temperature (°C)")
    plt.xticks(rotation=30, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    print(f"Chart saved to: {output_path}")
    return True


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent

    success = generate_chart(
        base_dir / "output" / "device_summary.json",
        base_dir / "output" / "temperature_chart.png",
    )

    if not success:
        sys.exit(1)
