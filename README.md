# Device Telemetry Summarizer

A small Python tool that reads device telemetry from a CSV file, summarizes
temperature and error data per device, and writes the results as JSON. It can
also generate a chart of the average temperature for each included device.

## Requirements

- Python
- The packages listed in `requirements.txt` (`matplotlib` and `pytest`)

## Setup

From the project directory, create and activate a virtual environment, then
install the requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Input data

The summarizer reads `data/device_telemetry.csv`. The CSV must include these
columns:

| Column | Description |
| --- | --- |
| `device_id` | Device identifier |
| `status` | Device status; rows with `ERROR` contribute to the error count |
| `temperature` | Temperature value to include in the average |

Rows with an invalid or non-finite temperature, or a blank device ID, are
skipped. Devices whose average temperature is above 80 are excluded from the
summary.

## Run

Process the CSV and write the summary to `output/device_summary.json`:

```powershell
python main.py
```

The command prints a per-device summary and reports the number of devices
included. The JSON output contains a list of device objects with
`device_id`, `record_count`, `average_temperature` (rounded to two decimal
places), and `error_count`.

To create `output/temperature_chart.png` from the generated JSON summary:

```powershell
python src/visualize.py
```

Run `python main.py` first so the chart generator has summary data to read.

## Tests

Run the tests with:

```powershell
python -m pytest
```

## Project layout

```text
data/device_telemetry.csv   Input telemetry
main.py                     Summarization entry point
src/processor.py            CSV processing and JSON summary generation
src/cleaner.py              Sensor reading cleanup utility
src/visualize.py            Temperature chart generation
tests/                      Automated tests
output/                     Generated summary and chart
```
