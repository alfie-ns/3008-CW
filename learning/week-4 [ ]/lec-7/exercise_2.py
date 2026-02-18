from plotnine import (
    ggplot,
    aes,
    geom_histogram,
    facet_wrap,
    labs,
    theme_minimal
)
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "pokemon_data.csv")
pokemon_data = pd.read_csv(csv_path)

# Debug: show actual column names
print("Columns before cleaning:", pokemon_data.columns.tolist())

# Clean column names by stripping whitespace
pokemon_data.columns = pokemon_data.columns.str.strip()

print("Columns after cleaning:", pokemon_data.columns.tolist())

plot = (
    ggplot(pokemon_data, aes(x="weight", fill="type 1"))
    + geom_histogram(bins=30)
    + facet_wrap("type 1")
    + labs(x="Weight", y="Count")
    + theme_minimal()
)

plot.show()