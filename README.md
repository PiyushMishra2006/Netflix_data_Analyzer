# 📊 Netflix Data Analysis using Pandas

## 📌 Project Overview

This project performs an in-depth analysis of Netflix content using Python and Pandas. The dataset is cleaned, transformed, and analyzed to uncover meaningful insights about content distribution, growth trends, genres, countries, and duration patterns of Movies and TV Shows.

---

## 📂 Dataset

* Source: Netflix Titles Dataset (CSV)
* Sample Size: 500 records (randomly selected for analysis)
* Key Columns:

  * Title, Type (Movie/TV Show)
  * Director, Cast
  * Country
  * Date Added
  * Release Year
  * Duration
  * Genre (`listed_in`)

---

## 🧹 Data Cleaning & Preprocessing

* Handled missing values:

  * `director` → "Unknown"
  * `cast` → "Not Available"
  * `country` → "Unknown"
* Converted `date_added` to datetime format
* Removed invalid/missing date entries
* Split and normalized multi-valued columns:

  * `country`
  * `listed_in` (genres)
* Extracted numerical values from `duration`
* Created separate datasets for:

  * Movies (`df_movie`)
  * TV Shows (`df_tv`)

---

## ⚙️ Feature Engineering

* `year_added` → Year content was added to Netflix
* `month_added` → Month of addition
* `content_age` → Age of content (based on release year)
* `duration_category` (Movies):

  * Short (0–60 min)
  * Medium (60–120 min)
  * Long (120+ min)
* `season_category` (TV Shows):

  * Short Series (1–2 seasons)
  * Medium Series (3–5 seasons)
  * Long Series (5+ seasons)

---

## 📊 Exploratory Data Analysis & Visualizations

The project includes multiple visualizations:

* Distribution of Movies vs TV Shows
* Content growth over the years
* Top 10 genres on Netflix
* Top content-producing countries
* Movie duration distribution
* TV show season distribution
* Genre vs Content Type (stacked comparison)
* Movies vs TV Shows growth trend

📁 All plots are available in the **`output/` folder**.

---

## 🔥 Key Insights

* Netflix content is **dominated by movies**, indicating a stronger focus on standalone content.
* Content addition **increased rapidly after 2016**, showing platform expansion.
* **International, Drama, and Comedy** are the most popular genres.
* **United States and India** are the top content-producing countries.
* Most movies fall in the **60–120 minute range**, reflecting standard industry duration.
* TV shows are primarily **short series (1–2 seasons)**, suggesting binge-friendly content strategy.
* Movies and TV shows show **distinct genre preferences**, with TV shows leaning more towards episodic formats like crime and reality.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib

---

## 📁 Project Structure

```
📦 Netflix-Data-Analysis
 ┣ 📜 netflix_titles.csv
 ┣ 📜 cleaned_netflix_data.csv
 ┣ 📜 analysis.py / notebook
 ┣ 📁 output
 ┃ ┣ 📊 plots/images
 ┗ 📜 README.md
```

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/PiyushMishra2006/Netflix_data_Analyzer.git/
   ```

2. Install dependencies:

   ```bash
   pip install pandas matplotlib
   ```

3. Run the script:

   ```bash
   python main.py
   ```

---

## 🎯 Conclusion

This project demonstrates practical use of Pandas for real-world data cleaning, transformation, and analysis. It highlights the ability to extract meaningful insights from raw datasets and present them through clear visualizations.

---

## 📌 Future Improvements

* Build an interactive dashboard (Streamlit/Power BI)
* Use full dataset instead of sampling
* Add advanced analytics or ML-based recommendations

---
