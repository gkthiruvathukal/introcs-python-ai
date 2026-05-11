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
                     start: str = "2015-01-01",
                     end: str = "2015-12-31") -> list[dict]:
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
                        output: str = "graffiti_trend.png",
                        year_start: int = None,
                        year_end: int = None) -> None:
    """Save a bar chart of monthly graffiti request counts.

    year_start and year_end are inclusive; omit both to plot all years.
    """
    monthly: collections.Counter = collections.Counter()
    with open(filename, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                date = datetime.strptime(row["Creation Date"], "%m/%d/%Y")
                if year_start is not None and date.year < year_start:
                    continue
                if year_end is not None and date.year > year_end:
                    continue
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


# start: visualize_by_year
def visualize_by_year(filename: str,
                       output: str = "graffiti_by_year.png",
                       min_year: int = 2010) -> None:
    """Save a bar chart of total graffiti removal requests per year."""
    yearly: collections.Counter = collections.Counter()
    with open(filename, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                date = datetime.strptime(row["Creation Date"], "%m/%d/%Y")
                if date.year >= min_year:
                    yearly[date.year] += 1
            except ValueError:
                continue

    years = sorted(yearly)
    counts = [yearly[y] for y in years]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(years, counts, color='steelblue', width=0.6)
    ax.set_title("311 Graffiti Removal Requests Per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Requests")
    ax.set_xticks(years)
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"{int(x):,}")
    )
    plt.tight_layout()
    plt.savefig(output, dpi=100)
    plt.close()
    print(f"Saved {output}")
# end: visualize_by_year


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Chicago 311 Graffiti Removal dataset analysis tool.'
    )
    sub = parser.add_subparsers(dest='command', required=True)

    p_fetch = sub.add_parser('fetch', help='Download the dataset from the Chicago Data Portal.')
    p_fetch.add_argument('-o', '--output', default='311_graffiti.csv',
                         help='Destination filename (default: 311_graffiti.csv)')

    p_load = sub.add_parser('load', help='Preview the first N rows.')
    p_load.add_argument('-i', '--input', default='311_graffiti.csv')
    p_load.add_argument('-l', '--limit', type=int, default=5,
                        help='Number of rows to display (default: 5)')

    p_agg = sub.add_parser('aggregate', help='Count requests grouped by a column.')
    p_agg.add_argument('-i', '--input', default='311_graffiti.csv')
    p_agg.add_argument('-g', '--group-by', default='ZIP Code',
                       help='Column to group by (default: "ZIP Code")')
    p_agg.add_argument('-n', '--top', type=int, default=10,
                       help='Number of top groups to show (default: 10)')

    p_filt = sub.add_parser('filter', help='Filter rows by status and date range.')
    p_filt.add_argument('-i', '--input', default='311_graffiti.csv')
    p_filt.add_argument('-s', '--status', default='Completed',
                        help='Request status to match (default: Completed)')
    p_filt.add_argument('--start', default='2015-01-01',
                        help='Start date YYYY-MM-DD (default: 2015-01-01)')
    p_filt.add_argument('--end', default='2015-12-31',
                        help='End date YYYY-MM-DD (default: 2015-12-31)')
    p_filt.add_argument('-l', '--limit', type=int, default=10,
                        help='Max rows to print (default: 10)')

    p_year = sub.add_parser('visualize-year', help='Save a yearly bar chart to a PNG file.')
    p_year.add_argument('-i', '--input', default='311_graffiti.csv')
    p_year.add_argument('-o', '--output', default='graffiti_by_year.png')
    p_year.add_argument('--min-year', type=int, default=2010,
                        help='Earliest year to include (default: 2000)')

    p_viz = sub.add_parser('visualize', help='Save a monthly bar chart to a PNG file.')
    p_viz.add_argument('-i', '--input', default='311_graffiti.csv')
    p_viz.add_argument('-o', '--output', default='graffiti_trend.png')
    p_viz.add_argument('--year-start', type=int, default=None,
                       help='First year to include (default: all)')
    p_viz.add_argument('--year-end', type=int, default=None,
                       help='Last year to include (default: all)')

    args = parser.parse_args()

    if args.command == 'fetch':
        fetch_graffiti(args.output)

    elif args.command == 'load':
        rows = load_graffiti(args.input, args.limit)
        for row in rows:
            print(row['Creation Date'], row['Status'], row['ZIP Code'])

    elif args.command == 'aggregate':
        results = aggregate_graffiti(args.input, args.group_by, args.top)
        for key, count in results:
            print(f"{key:20s}  {count:6,}")

    elif args.command == 'filter':
        matches = filter_graffiti(args.input, args.status, args.start, args.end)
        print(f"{len(matches):,} '{args.status}' requests from {args.start} to {args.end}")
        for row in matches[:args.limit]:
            print(row['Creation Date'], row['Status'], row['ZIP Code'])

    elif args.command == 'visualize-year':
        visualize_by_year(args.input, args.output, args.min_year)

    elif args.command == 'visualize':
        visualize_graffiti(args.input, args.output, args.year_start, args.year_end)
