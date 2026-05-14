from rich.console import Console
from rich.panel import Panel
from rich.table import Table


# start: data
COUNTRIES = [
    {"country": "Canada", "continent": "North America", "population": 38.8},
    {"country": "France", "continent": "Europe", "population": 68.0},
    {"country": "Germany", "continent": "Europe", "population": 84.4},
    {"country": "Japan", "continent": "Asia", "population": 124.5},
    {"country": "United States", "continent": "North America", "population": 334.9},
]
# end: data


# start: table
def country_table(countries: list[dict]) -> Table:
    """Build a Rich table from a list of country dictionaries."""
    table = Table(title="Sample Country Data")
    table.add_column("Country")
    table.add_column("Continent")
    table.add_column("Population", justify="right")

    for row in countries:
        table.add_row(
            row["country"],
            row["continent"],
            f'{row["population"]:.1f} million',
        )

    return table
# end: table


# start: summary
def summarize(countries: list[dict]) -> str:
    """Return a short text summary of the country data."""
    count = len(countries)
    total = sum(row["population"] for row in countries)
    largest = max(countries, key=lambda row: row["population"])
    return (
        f"{count} countries, {total:.1f} million people total. "
        f"Largest: {largest['country']}."
    )
# end: summary


# start: main
def main() -> None:
    console = Console()
    console.print(Panel("Terminal apps can present data clearly."))
    console.print(country_table(COUNTRIES))
    console.print(summarize(COUNTRIES))


if __name__ == "__main__":
    main()
# end: main
