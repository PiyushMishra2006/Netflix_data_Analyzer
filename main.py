import pandas as pd
import matplotlib.pyplot as plt

# Load and sample
df = pd.read_csv("netflix_titles.csv")
df = df.sample(500, random_state=42)

# Handle missing values
df.fillna({
    "director": "Unknown",
    "cast": "Not Available",
    "country": "Unknown"
}, inplace=True)

# Split and normalize multi-valued columns
df["country"] = df["country"].str.split(", ")
df = df.explode("country")

df["listed_in"] = df["listed_in"].str.split(", ")
df = df.explode("listed_in")

# Convert date and extract features
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df = df.dropna(subset=["date_added"])

df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month

# Correct content age (important fix)
df["content_age"] = 2026 - df["release_year"]

# Split datasets
df_movie = df[df["type"] == "Movie"].copy()
df_tv = df[df["type"] == "TV Show"].copy()

# Extract numeric duration
df_movie["duration"] = df_movie["duration"].str.extract(r"(\d+)").astype(int)
df_tv["duration"] = df_tv["duration"].str.extract(r"(\d+)").astype(int)

# Categorization
df_movie["duration_category"] = pd.cut(
    df_movie["duration"],
    bins=[0, 60, 120, 1000],
    labels=["Short", "Medium", "Long"]
)

df_tv["season_category"] = pd.cut(
    df_tv["duration"],
    bins=[0, 2, 5, 20],
    labels=["Short Series", "Medium Series", "Long Series"]
)

# Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

# ---------------- VISUALIZATIONS ---------------- #

# 1. Movies vs TV Shows
df["type"].value_counts().plot(kind="bar")
plt.title("Distribution of Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2. Growth over time
df.groupby("year_added").size().plot(kind="line", marker="o")
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# 3. Top Genres
df["listed_in"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Top Countries
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Movie Duration Distribution
df_movie["duration_category"].value_counts().plot(kind="bar")
plt.title("Movie Duration Distribution")
plt.xlabel("Duration Category")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 6. TV Show Seasons Distribution
df_tv["season_category"].value_counts().plot(kind="bar")
plt.title("TV Show Season Distribution")
plt.xlabel("Season Category")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 7. Genre vs Type (stacked)
genre_type = df.groupby(["listed_in", "type"]).size().unstack().fillna(0)
genre_type.head(10).plot(kind="bar", stacked=True)

plt.title("Genre Distribution by Content Type")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Growth comparison
df.groupby(["year_added", "type"]).size().unstack().plot(kind="line", marker="o")
plt.title("Movies vs TV Shows Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.show()