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






## Instructions for Reproducing Results
1. 
2. 
