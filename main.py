import sys
from pathlib import Path

from src.processor import process_telemetry


def main():
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "device_telemetry.csv"
    json_path = base_dir / "output" / "device_summary.json"

    try:
        results = process_telemetry(csv_path, json_path)
        print(f"\nProcessed successfully. Devices included: {len(results)}")
        print(f"JSON output: {json_path}")
    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
        sys.exit(1)
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error processing telemetry: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    import csv
    main()
