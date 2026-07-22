import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Load the report.json file and return its contents as a dictionary.
def _load_report():
    return json.loads(REPORT_PATH.read_text())

def test_total_requests():
    """Criterion 1: total_requests must equal the number of log lines."""
    assert _load_report()["total_requests"] == 6

def test_unique_ips():
    """Criterion 2: unique_ips must equal the number of distinct client IPs."""
    assert _load_report()["unique_ips"] == 3

def test_top_path():
    """Criterion 3: top_path must be the single most-requested path."""
    assert _load_report()["top_path"] == "/index.html"