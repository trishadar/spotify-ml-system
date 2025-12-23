import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and rename columns
genres = pd.read_csv("data/processed/genre_distribution.csv")
genres.rename(columns={"Unnamed: 0": "genre"}, inplace=True)

# Take top 10 genres
top = genres.head(10)

# Set style
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Plot horizontal bars
barplot = sns.barplot(
    x="count",
    y="genre",
    data=top,
    palette="viridis"
)

# Add count labels at the end of each bar
for index, value in enumerate(top["count"]):
    barplot.text(
        value + 0.2,  # small offset to the right of the bar
        index,
        str(value),
        color='black',
        va='center',
        fontsize=11
    )

plt.title("Top Genres in My Listening History", fontsize=16, weight='bold')
plt.xlabel("Play Count", fontsize=12)
plt.ylabel("")
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()
plt.show()
