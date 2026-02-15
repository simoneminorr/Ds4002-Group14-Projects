# Shipping Company Sentiment Analysis Project (DS4002 - Group 14)
This project explores the sentiment of the public towards the following shipping companies: DHL, USPS, UPS, and FedEx. Comments from the companies corresponding subreddits, and reviews from their corresponding Trustpilot pages were utilized. Data was scraped from Reddit, obtaining ~1700 unique comments, and 30 Truspilot reviews for each company were manually copied. Sentiment analyis was perfomed on this text data using the VADER python package, and this repository shows the results of this analysis.

## Contents of this Repository


## Software and Platform Selection
Software: 
 - Google Colab
 - Git / GitHub
 - Jupyter Notebook

Add-on Packages: 
 - vaderSentiment
 - pandas
 - numpy
 - matplotlib
 - SciPy
 - statsmodels
 - seaborn
 - requests
 - tqdm
 - time
 - datetime
 - re
 - os

Platform Used:
 - macOS

## Documentation Map

```text
Ds4002-Group14-Projects/
│
├── README.md
│   └── Contains:
│       • Project overview
│       • Research question & motivation
│       • Software & package requirements
│       • Documentation map
│       • Instructions for reproducing results
│
├── SCRIPTS/
│   │
│   ├── reddit_script/
│   │   │
│   │   ├── Script_01_Data_Collection.ipynb
│   │   │   └── Scrapes Reddit posts and comments for:
│   │       USPS, UPS, FedEx, DHL
│   │       • Cleans text data
│   │       • Removes boilerplate/spam
│   │       • Exports:
│   │           - shipping_posts_raw.csv
│   │           - shipping_comments_raw.csv
│   │           - shipping_comments_clean.csv
│   │
│   │   ├── Script_02_Exploratory_Analysis.ipynb
│   │   │   └── Performs exploratory data analysis (EDA):
│   │       • Comment counts by company
│   │       • Sentiment score distributions
│   │       • Mean sentiment with 95% confidence intervals
│   │       • Visualizations (histograms, boxplots, stacked bar charts)
│   │       • Saves plots to /output/figures/
│   │
│   │   └── Script_03_Statistical_Analysis.ipynb
│   │       └── Performs hypothesis testing:
│   │           • One-way ANOVA (mean sentiment differences)
│   │           • Levene’s test (variance assumption)
│   │           • Tukey HSD post-hoc comparisons
│   │           • Binomial tests (>50% negative sentiment)
│   │           • Chi-square test of independence
│   │           • Cramer's V (effect size)
│   │           • Saves statistical tables to /output/tables/
│   │
│   └── trustpilot_scripts/
│       │
│       ├── trustpilot_scraper.ipynb
│       │   └── Scrapes Trustpilot reviews for:
│       │       USPS, UPS, FedEx, DHL
│       │       • Collects review text and ratings
│       │       • Exports raw review dataset
│       │
│       └── trustpilot_analysis.ipynb
│           └── Performs:
│               • VADER sentiment analysis
│               • Exploratory analysis
│               • Statistical testing (parallel to Reddit analysis)
│               • Saves outputs to /output/
│
├── output/
│   │
│   ├── figures/
│   │   └── Saved visualizations used in MI3 presentation
│   │
│   ├── tables/
│   │   ├── anova_results.csv
│   │   ├── tukey_results.csv
│   │   ├── binomial_results.csv
│   │   ├── chi_square_results.csv
│   │   └── summary_mean_compound_ci.csv
│   │
│   ├── shipping_posts_raw.csv
│   ├── shipping_comments_raw.csv
│   └── shipping_comments_clean.csv
│
└── requirements.txt
    └── Lists required Python packages:
        pandas, numpy, matplotlib, seaborn,
        scipy, statsmodels, vaderSentiment,
        requests, tqdm
```







# Instructions for Reproducing Results

This section provides explicit, step-by-step instructions to reproduce all results from our study. Follow the steps carefully and in order.

---

## 1. Download the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/simoneminorr/Ds4002-Group14-Projects.git
cd Ds4002-Group14-Projects
```

Or download the ZIP file from GitHub and extract it locally.

---

## 2. Install Required Software

### Python Version
Ensure you are using **Python 3.9 or higher**.

### Install Required Packages

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels vaderSentiment requests tqdm
```

---

## 3. Reproduce Reddit Analysis (Main Study Results)

Navigate to:

```
SCRIPTS/reddit_script/
```

Run the following notebooks **in order**.

---

### Step 3.1 – Run `Script_01_Data_Collection.ipynb`

This notebook:

- Scrapes Reddit posts and comments for:
  - USPS  
  - UPS  
  - FedEx  
  - DHL  
- Cleans comment text
- Removes boilerplate/spam
- Exports:

```
output/shipping_posts_raw.csv
output/shipping_comments_raw.csv
output/shipping_comments_clean.csv
```

**Run all cells from top to bottom.**

✔ Confirm that `shipping_comments_clean.csv` is created before continuing.
However, to reproduce exactly the same result we have, ignore step 3.1 anddownload shipping_comment_clean.csv from the REDDIT_DATA folder and begin with step 3.2.

---

### Step 3.2 – Run `Script_02_Exploratory_Analysis.ipynb`

This notebook:

- Loads cleaned Reddit comments
- Computes VADER sentiment scores
- Produces:
  - Comment counts by company
  - Sentiment score distributions
  - Mean sentiment with 95% confidence intervals
  - Visualizations (histograms, boxplots, stacked bar charts)
- Saves figures to:

```
output/figures/
```

Run all cells in order.

✔ Confirm figures appear in `output/figures/`.

---

### Step 3.3 – Run `Script_03_Statistical_Analysis.ipynb`

This notebook performs hypothesis testing:

- Levene’s test (equal variance assumption)
- One-way ANOVA (mean sentiment differences)
- Tukey HSD post-hoc comparisons
- Binomial tests (>50% negative sentiment)
- Chi-square test of independence
- Cramer's V (effect size)

Statistical results are saved to:

```
output/tables/
```

Including:

- `anova_results.csv`
- `tukey_results.csv`
- `binomial_results.csv`
- `chi_square_results.csv`
- `summary_mean_compound_ci.csv`

Run all cells from top to bottom.

✔ Confirm all CSV files appear in `output/tables/`.

---

## 4. (Optional) Reproduce Trustpilot Analysis

Navigate to:

```
SCRIPTS/trustpilot_scripts/
```

Run in order:

1. `trustpilot_scraper.ipynb`
2. `trustpilot_analysis.ipynb`

This performs Trustpilot sentiment analysis and statistical testing parallel to the Reddit analysis.

Outputs are saved to the `output/` directory.

---

## 5. Verify Successful Reproduction

You have successfully reproduced the results if:

- All notebooks run without errors.
- The `output/` folder contains:
  - Cleaned datasets
  - Figures
  - Statistical result tables
- Script 03 prints:
  - ANOVA F-statistic and p-value
  - Tukey comparison table
  - Binomial test results per company
  - Chi-square statistic and p-value

---

## Notes

- Internet connection is required for scraping.
- If Reddit scraping fails due to rate limits, wait a few minutes and re-run.
- Always run notebooks in order (01 → 02 → 03).
- Do not skip steps.

