import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from sklearn.datasets import load_iris

# Load iris dataset
iris_raw = load_iris()
iris = pd.DataFrame(iris_raw.data, columns=iris_raw.feature_names)
iris["Species"] = pd.Categorical.from_codes(
    iris_raw.target,
    iris_raw.target_names
)

# Rename for convenience to match R style
iris.rename(columns={
    "sepal length (cm)": "Sepal.Length"
}, inplace=True)

# Aggregate so bars behave like stat="identity"
agg = iris.groupby("Species", observed=False)["Sepal.Length"].sum().reset_index()
agg["Sepal.Length"] = agg["Sepal.Length"] * 1000  # Arbitrarily scaled

# Manual ugly palette
palette = {
    "setosa": "yellow",
    "versicolor": "purple",
    "virginica": "orange"
}

# Plot
fig, ax = plt.subplots()

# Horrid red background
ax.set_facecolor("red")

# Bar plot with clashing outline
bars = ax.barh(
    agg["Species"],
    agg["Sepal.Length"],
    color=[palette[s] for s in agg["Species"]],
    edgecolor="hotpink",
    height=0.5
)

# Useless distracting points
ax.scatter(
    agg["Sepal.Length"] + 500,
    agg["Species"],
    color="limegreen",
    s=100,
    marker="x"
)

# Exaggerated axis
ax.set_xlim(0, 1_000_000)
ax.set_xticks(np.arange(0, 1_000_001, 200_000))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}"))

# Labels
ax.set_title(
    "Iris Flowers Causing Global Warming Impact (in Mega-Units)",
    color="magenta",
    fontsize=20,
    fontweight="bold"
)
ax.set_xlabel("Disaster Level")
ax.set_ylabel("Flower Culprit")

# Over-rotated text
plt.xticks(rotation=135, color="blue", fontsize=14, fontstyle="italic")
plt.yticks(color="green", fontsize=8)

# Legend at top
handles = [
    plt.Rectangle((0,0),1,1, color=palette[s])
    for s in palette
]
ax.legend(handles, palette.keys(), loc="upper center")

plt.tight_layout()
plt.show()