import urllib.request
import csv
import collections
from datetime import datetime
import matplotlib.pyplot as plt

DATASET_URL = (
    "https://data.cityofchicago.org/api/views/hec5-y4x5/rows.csv"
    "?accessType=DOWNLOAD"
)


# start: fetch_graffiti
def fetch_graffiti(output: str = "311_graffiti.csv") -> None:
    """Download the 311 Graffiti Removal dataset from the Chicago Data Portal."""
    print(f"Downloading to {output} ...")
    urllib.request.urlretrieve(DATASET_URL, output)
    print("Done.")
# end: fetch_graffiti


# start: load_graffiti
def load_graffiti(filename: str, limit: int = 5) -> list[dict]:
    """Read the first limit rows and return them as a list of dicts."""
    rows = []
    with open(filename, newline='', encoding='utf-8') as f:
        for i, row in enumerate(csv.DictReader(f)):
            if i >= limit:
                break
            rows.append(row)
    return rows
# end: load_graffiti


# start: aggregate_graffiti
def aggregate_graffiti(filename: str, group_by: str = "ZIP Code",
                        top: int = 10) -> list[tuple[str, int]]:
    """Count requests per group_by value and return the top N as (key, count) pairs."""
    counter: collections.Counter = collections.Counter()
    with open(filename, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            counter[row[group_by]] += 1
    return counter.most_common(top)
# end: aggregate_graffiti


# start: filter_graffiti
def filter_graffiti(filename: str, status: str = "Completed",
                     start: str = "2024-01-01",
                     end: str = "2024-01-31") -> list[dict]:
    """Return rows whose Status matches and Creation Date falls in [start, end]."""
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt   = datetime.strptime(end,   "%Y-%m-%d")
    results = []
    with open(filename, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                row_date = datetime.strptime(row["Creation Date"], "%m/%d/%Y")
            except ValueError:
                continue
            if row["Status"] == status and start_dt <= row_date <= end_dt:
                results.append(row)
    return results
# end: filter_graffiti


# start: visualize_graffiti
def visualize_graffiti(filename: str,
                        output: str = "graffiti_trend.png") -> None:
    """Save a bar chart of monthly graffiti request counts."""
    monthly: collections.Counter = collections.Counter()
    with open(filename, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                date = datetime.strptime(row["Creation Date"], "%m/%d/%Y")
                monthly[date.strftime("%Y-%m")] += 1
            except ValueError:
                continue

    months = sorted(monthly)
    counts = [monthly[m] for m in months]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(months, counts, color='steelblue')
    ax.set_title("311 Graffiti Removal Requests Per Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Requests")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output, dpi=100)
    plt.close()
    print(f"Saved {output}")
# end: visualize_graffiti
