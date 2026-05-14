import pandas as pd
import matplotlib.pyplot as plt


# start: countries_data
COUNTRIES = [
    {
        "Country": "Canada",
        "Continent": "North America",
        "Population": 38.8,
        "GDP": 2140,
        "Area": 9_984_670,
        "HDI": 0.936,
    },
    {
        "Country": "France",
        "Continent": "Europe",
        "Population": 68.0,
        "GDP": 3030,
        "Area": 551_695,
        "HDI": 0.910,
    },
    {
        "Country": "Germany",
        "Continent": "Europe",
        "Population": 84.4,
        "GDP": 4450,
        "Area": 357_114,
        "HDI": 0.950,
    },
    {
        "Country": "Italy",
        "Continent": "Europe",
        "Population": 58.9,
        "GDP": 2300,
        "Area": 301_340,
        "HDI": 0.906,
    },
    {
        "Country": "Japan",
        "Continent": "Asia",
        "Population": 124.5,
        "GDP": 4210,
        "Area": 377_975,
        "HDI": 0.925,
    },
    {
        "Country": "United Kingdom",
        "Continent": "Europe",
        "Population": 67.7,
        "GDP": 3340,
        "Area": 243_610,
        "HDI": 0.940,
    },
    {
        "Country": "United States",
        "Continent": "North America",
        "Population": 334.9,
        "GDP": 27360,
        "Area": 9_833_517,
        "HDI": 0.927,
    },
]
# end: countries_data


# start: create_dataframe
def create_country_dataframe() -> pd.DataFrame:
    """Return a DataFrame indexed by country name."""
    df = pd.DataFrame(COUNTRIES)
    return df.set_index("Country")
# end: create_dataframe


# start: select_examples
def print_selection_examples(df: pd.DataFrame) -> None:
    """Print a few common row and column selections."""
    print(df[["Population", "GDP"]])
    print()
    print(df.loc[["France", "Japan"], ["Population", "GDP"]])
    print()
    print(df.iloc[0:3])
# end: select_examples


# start: filter_sort_group
def summarize_countries(df: pd.DataFrame) -> pd.DataFrame:
    """Filter, sort, and group country data."""
    large = df[df["Population"] >= 60]
    print(large.sort_values("Population", ascending=False))
    print()

    by_continent = df.groupby("Continent")[["Population", "GDP"]].mean()
    return by_continent.sort_values("Population", ascending=False)
# end: filter_sort_group


# start: plot_gdp
def plot_gdp(df: pd.DataFrame, output: str = "country_gdp.png") -> None:
    """Save a bar chart of GDP by country."""
    ordered = df.sort_values("GDP", ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(ordered.index, ordered["GDP"], color="steelblue")
    ax.set_title("GDP by Country")
    ax.set_xlabel("Country")
    ax.set_ylabel("GDP, billions of US dollars")
    ax.tick_params(axis="x", labelrotation=30)
    plt.tight_layout()
    plt.savefig(output, dpi=120)
    plt.close()
    print(f"Saved {output}")
# end: plot_gdp


if __name__ == "__main__":
    countries = create_country_dataframe()
    print(countries)
    print()
    print(countries.describe())
    print()
    print_selection_examples(countries)
    print()
    print(summarize_countries(countries))
    plot_gdp(countries)
