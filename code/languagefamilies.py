# Question: Which family of languages has the highest density of speakers?

import pandas as pd
africa = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-01-13/africa.csv')


# Calculate the average number of speakers per language in each family
family_density = (
    africa.groupby("family")
    .agg(
        total_speakers=("native_speakers", "sum"),
        n_languages=("language", "nunique")
    )
    .assign(
        speaker_density=lambda x: x["total_speakers"] / x["n_languages"]
    )
    .sort_values("speaker_density", ascending=False)
)

print(family_density)

# Family with the highest speaker density
highest_density = family_density.iloc[0]

print("\nFamily with the highest speaker density:")
print(highest_density)

import pandas as pd
import matplotlib.pyplot as plt

africa = pd.read_csv(
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-01-13/africa.csv"
)

# Calculate speaker density for each language family
family_density = (
    africa.groupby("family")
    .agg(
        total_speakers=("native_speakers", "sum"),
        n_languages=("language", "nunique")
    )
    .assign(
        speaker_density=lambda x: x["total_speakers"] / x["n_languages"]
    )
    .sort_values("speaker_density", ascending=False)
)


plot_data = family_density.sort_values("speaker_density")

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    plot_data.index,
    plot_data["speaker_density"]
)

ax.set_title(
    "Average Native Speakers per Language Family",
    fontsize=16,
    pad=15
)
ax.set_xlabel("Average native speakers per language")
ax.set_ylabel("Language family")

# Add values to the ends of the bars
for bar in bars:
    value = bar.get_width()
    ax.text(
        value,
        bar.get_y() + bar.get_height() / 2,
        f" {value:,.0f}",
        va="center"
    )

plt.tight_layout()
plt.show()

# Print the answer
highest = family_density.iloc[0]

print(
    f"\nFamily with the highest speaker density: {family_density.index[0]}"
)
print(
    f"Average speakers per language: "
    f"{highest['speaker_density']:,.0f}"
)