from plotnine import ggplot, aes, geom_point, labs, theme_minimal
import pandas as pd

pokeman_data = pd.read_csv("pokemon_data.csv")


plot = (
    ggplot(pokeman_data, aes(x="base_experience", y="hp"))
    + geom_point(colour="#006400")
    + labs(x="Base Experience", y="HP")
    + theme_minimal()
)

plot.show()