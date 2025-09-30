
# Champions League Win Rate Analysis

This project analyzes Champions League team statistics to identify which metrics (other than goals/assists) most strongly correlate with winning. Data is collected from [FBref](https://fbref.com) using custom Python web scraping utilities.

---

## Requirements & Setup

### Prerequisites

* Python 3.8+
* [pip](https://pip.pypa.io/en/stable/)

### Install dependencies

```bash
pip install requests pandas beautifulsoup4
```

*(optional but recommended: use a virtual environment)*

### Project Files

* **Webscraping.py** → contains scraping functions (`linkloader`, `write_to_csv_from_file`)
* **analysis.py** (or similar) → contains `win_rate_analysis_tournament()`
* **output/** → directory where generated CSVs will be saved

---

## Workflow

1. **Load Links**
   Use the `linkloader()` function in `Webscraping.py` with a Champions League stats page URL (example: 2018–19 season).

   ```python
   from Webscraping import linkloader
   linkloader("https://fbref.com/en/comps/8/2018-2019/2018-2019-Champions-League-Stats")
   ```

   This generates a CSV file containing all match links (used to avoid rate-limit errors).

2. **Generate Match Data CSVs**
   Run:

   ```python
   from Webscraping import write_to_csv_from_file
   write_to_csv_from_file("2018-2019 Champions League.csv")
   ```

   This will create 3 CSV files (`QF`, `SF`, `Ro16`) with team stats for every game from the Round of 16 to the Semifinals (52 games).

3. **Analyze Win Rates**
   Use the generated files with `win_rate_analysis_tournament()`:

   ```python
   from analysis import win_rate_analysis_tournament
   win_rate_analysis_tournament("QF_file.csv", "SF_file.csv", "Ro16_file.csv")
   ```

   This computes how often a team leading in various stats (e.g., shots, xG, passes) won or drew their matches.

---

## Example Results (2018–19 Edition)

* Leading in **PK Converted** → won/drew 71.15% of matches
* Leading in **Shots on Target** → 65.38%
* Leading in **Red Cards** (fewer) → 69.23%
* Leading in **GCA (Goal-Creating Actions)** → 73.07%
* Leading in **npXG** → 63.46%
* Leading in **Tackles** → 50.0%
* Leading in **Blocked Shots** → 44.23%

*(Full breakdown in output logs.)*

---

## Other Seasons

Repeat the same steps with any Champions League stats page in this format:

* [2020–21 Champions League](https://fbref.com/en/comps/8/2020-2021/2020-2021-Champions-League-Stats)
* [2019–20 Champions League](https://fbref.com/en/comps/8/2019-2020/2019-2020-Champions-League-Stats)
* [2018–19 Champions League](https://fbref.com/en/comps/8/2018-2019/2018-2019-Champions-League-Stats)

Works with any **main Champions League stats page** on FBref.

---

## Summary

* Scrapes match-level team stats (Round of 16 to Semifinals).
* Avoids rate-limit errors by staging link collection.
* Outputs CSVs + win-rate analysis for multiple stats.
* Reusable across seasons.

---

👉 Do you want me to also add a **“Sample Output CSV” snippet** so readers can see the structure of the scraped data before running the analysis?
