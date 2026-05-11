import urllib.request
import pandas as pd
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
def load_graffiti(filename: str, limit: int | None = None) -> pd.DataFrame:
    """Load the dataset into a DataFrame; parse Creation Date as datetime."""
    df = pd.read_csv(filename, nrows=limit)
    df["Creation Date"] = pd.to_datetime(
        df["Creation Date"], format="%m/%d/%Y", errors="coerce"
    )
    return df
# end: load_graffiti


# start: aggregate_graffiti
def aggregate_graffiti(filename: str, group_by: str = "ZIP Code",
                        top: int = 10) -> pd.Series:
    """Return the top-N value counts for the given column."""
    df = load_graffiti(filename)
    return df[group_by].value_counts().head(top)
# end: aggregate_graffiti


# start: filter_graffiti
def filter_graffiti(filename: str, status: str = "Completed",
                     start: str = "2015-01-01",
                     end: str = "2015-12-31") -> pd.DataFrame:
    """Return rows whose Status matches and Creation Date falls in [start, end]."""
    df = load_graffiti(filename)
    mask = (
        (df["Status"] == status) &
        (df["Creation Date"] >= start) &
        (df["Creation Date"] <= end)
    )
    return df[mask]
# end: filter_graffiti


# start: visualize_graffiti
def visualize_graffiti(filename: str,
                        output: str = "graffiti_trend.png",
                        year_start: int | None = None,
                        year_end: int | None = None) -> None:
    """Save a bar chart of monthly graffiti request counts."""
    df = load_graffiti(filename).dropna(subset=["Creation Date"])
    if year_start is not None:
        df = df[df["Creation Date"].dt.year >= year_start]
    if year_end is not None:
        df = df[df["Creation Date"].dt.year <= year_end]

    monthly = df.groupby(df["Creation Date"].dt.to_period("M")).size()
    months = [str(m) for m in monthly.index]
    counts = monthly.to_list()

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
    df = load_graffiti(filename).dropna(subset=["Creation Date"])
    df = df[df["Creation Date"].dt.year >= min_year]

    yearly = df.groupby(df["Creation Date"].dt.year).size()
    years = list(yearly.index)
    counts = list(yearly.values)

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
                        help='Earliest year to include (default: 2010)')

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
        df = load_graffiti(args.input, args.limit)
        print(df[["Creation Date", "Status", "ZIP Code"]].to_string(index=False))

    elif args.command == 'aggregate':
        results = aggregate_graffiti(args.input, args.group_by, args.top)
        for key, count in results.items():
            print(f"{str(key):20s}  {count:6,}")

    elif args.command == 'filter':
        matches = filter_graffiti(args.input, args.status, args.start, args.end)
        print(f"{len(matches):,} '{args.status}' requests from {args.start} to {args.end}")
        print(matches[["Creation Date", "Status", "ZIP Code"]].head(args.limit).to_string(index=False))

    elif args.command == 'visualize-year':
        visualize_by_year(args.input, args.output, args.min_year)

    elif args.command == 'visualize':
        visualize_graffiti(args.input, args.output, args.year_start, args.year_end)
