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

Ds4002-Group14-Projects/
│
├── README.md
│   └── Project overview, software requirements, documentation map,
│       and reproduction instructions.
│
├── SCRIPTS/
│   │
│   ├── reddit_script/
│   │   │
│   │   ├── Script_01_Data_Collection.ipynb
│   │   │   └── Scrapes Reddit posts and comments for USPS, UPS,
│   │   │       FedEx, and DHL. Cleans text and exports:
│   │   │       - shipping_posts_raw.csv
│   │   │       - shipping_comments_raw.csv
│   │   │       - shipping_comments_clean.csv
│   │   │
│   │   ├── Script_02_Exploratory_Analysis.ipynb
│   │   │   └── Performs exploratory data analysis (EDA):
│   │   │       - Comment counts
│   │   │       - Sentiment distributions
│   │   │       - Mean sentiment + 95% CI
│   │   │       - Visualizations (histograms, boxplots, stacked bars)
│   │   │
│   │   ├── Script_03_Statistical_Analysis.ipynb
│   │   │   └── Performs hypothesis testing:
│   │   │       - One-way ANOVA
│   │   │       - Tukey HSD post-hoc
│   │   │       - Binomial tests (>50% negative)
│   │   │       - Chi-square test
│   │   │       - Cramer's V effect size
│   │
│   ├── trustpilot_scripts/
│   │   │
│   │   ├── trustpilot_scraper.ipynb
│   │   │   └── Scrapes Trustpilot reviews for shipping companies.
│   │   │
│   │   ├── trustpilot_analysis.ipynb
│   │   │   └── Performs sentiment analysis and statistical testing
│   │   │       on Trustpilot review data.
│
├── output/
│   │
│   ├── figures/
│   │   └── Saved plots used in MI3 presentation
│   │
│   ├── tables/
│   │   └── Statistical output tables:
│   │       - anova_results.csv
│   │       - tukey_results.csv
│   │       - binomial_results.csv
│   │       - chi_square_results.csv
│   │       - summary_mean_compound_ci.csv
│   │
│   ├── shipping_posts_raw.csv
│   ├── shipping_comments_raw.csv
│   └── shipping_comments_clean.csv
│
└── requirements.txt (optional but recommended)
    └── Lists required Python packages


## Instructions for Reproducing Results
1. 
2. 
