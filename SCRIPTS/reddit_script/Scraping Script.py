#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ============================================
# MI3 - Script 01: Reddit Data Collection
# ============================================

import os
import re
import time
from datetime import datetime

import pandas as pd
import requests
from tqdm import tqdm


# In[14]:


# Output folder for all generated CSV files
OUTDIR = "output"

# Scraping parameters
POSTS_PER_SUB = 50            # Number of recent posts to scrape per subreddit (<=100)
COMMENT_LIMIT = 500           # Limit passed to Reddit comments endpoint
MAX_COMMENTS_PER_POST = 300   # Maximum comments extracted per post
SLEEP_BETWEEN_POSTS = 1.0     # Throttle between posts (seconds)
SLEEP_BETWEEN_SUBS = 1.5      # Throttle between subreddits (seconds)

# Cleaning options
FILTER_BOILERPLATE = True     # Remove obvious moderator/bot boilerplate

# Custom User-Agent (required by Reddit API policy)
USER_AGENT = "ds4002-shipping-sentiment/1.0 (contact: your_email@uva.edu)"

# Target subreddits mapped to company names
SUBREDDITS = {
    "USPS": "USPS",
    "UPS": "UPS",
    "FedEx": "FedEx",
    "DHL": "dhl"
}

# Create output folder if it doesn't exist
os.makedirs(OUTDIR, exist_ok=True)

print("Setup complete.")


# In[16]:


HEADERS = {"User-Agent": USER_AGENT}

def fetch_new_posts(subreddit, limit=50):
    """
    Fetches the most recent posts from a subreddit.
    Returns a list of post metadata dictionaries.
    """

    limit = min(limit, 100)  # Reddit API max per request
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit={limit}"

    r = safe_get(url, HEADERS)
    data = r.json()["data"]["children"]

    rows = []

    for post in data:
        d = post["data"]

        rows.append({
            "subreddit": subreddit,
            "post_id": d.get("id"),
            "created_utc": d.get("created_utc"),
            "title": d.get("title"),
            "selftext": d.get("selftext"),
            "score": d.get("score"),
            "num_comments": d.get("num_comments"),
            "permalink": "https://www.reddit.com" + d.get("permalink", "")
        })

    return rows


# In[17]:


# Collect posts from each company subreddit
all_posts = []

for company, sub in SUBREDDITS.items():
    print(f"Fetching posts for {company} (r/{sub})")

    rows = fetch_new_posts(sub, POSTS_PER_SUB)

    # Attach company label
    for r in rows:
        r["company"] = company

    all_posts.extend(rows)

    time.sleep(SLEEP_BETWEEN_SUBS)

posts_df = pd.DataFrame(all_posts)

# Convert timestamp to datetime
posts_df["created_dt"] = pd.to_datetime(
    posts_df["created_utc"], unit="s", utc=True
)

# Combine title + body into single text column
posts_df["post_text"] = (
    posts_df["title"].fillna("") + "\n" +
    posts_df["selftext"].fillna("")
).str.strip()

posts_df.head()


# In[18]:


def fetch_comments_json(subreddit, post_id, limit=500):
    """
    Retrieves comment JSON for a specific post.
    """
    url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?limit={limit}&sort=confidence"
    r = safe_get(url, HEADERS)
    return r.json()


# In[19]:


def extract_comments(listing, company, subreddit, post_id, max_comments=300):
    """
    Recursively extracts comments (including nested replies).
    Returns a list of comment dictionaries.
    """

    comments_section = listing[1]["data"]["children"]
    rows = []

    def walk(nodes):
        nonlocal rows

        for n in nodes:
            if len(rows) >= max_comments:
                return

            # Only process actual comments (kind = t1)
            if n["kind"] == "t1":
                d = n["data"]

                rows.append({
                    "company": company,
                    "subreddit": subreddit,
                    "post_id": post_id,
                    "comment_id": d.get("id"),
                    "comment_created_utc": d.get("created_utc"),
                    "comment_body": d.get("body"),
                    "comment_score": d.get("score"),
                    "parent_id": d.get("parent_id")
                })

                # Recursively extract replies
                replies = d.get("replies")
                if isinstance(replies, dict):
                    walk(replies["data"]["children"])

    walk(comments_section)
    return rows


# In[20]:


def extract_comments(listing, company, subreddit, post_id, max_comments=300):
    """
    Recursively extracts comments (including nested replies).
    Returns a list of comment dictionaries.
    """

    comments_section = listing[1]["data"]["children"]
    rows = []

    def walk(nodes):
        nonlocal rows

        for n in nodes:
            if len(rows) >= max_comments:
                return

            # Only process actual comments (kind = t1)
            if n["kind"] == "t1":
                d = n["data"]

                rows.append({
                    "company": company,
                    "subreddit": subreddit,
                    "post_id": post_id,
                    "comment_id": d.get("id"),
                    "comment_created_utc": d.get("created_utc"),
                    "comment_body": d.get("body"),
                    "comment_score": d.get("score"),
                    "parent_id": d.get("parent_id")
                })

                # Recursively extract replies
                replies = d.get("replies")
                if isinstance(replies, dict):
                    walk(replies["data"]["children"])

    walk(comments_section)
    return rows


# In[21]:


# Loop through posts and collect comments
all_comments = []
failed_posts = []

for _, row in tqdm(posts_df.iterrows(), total=len(posts_df)):

    try:
        listing = fetch_comments_json(
            row["subreddit"],
            row["post_id"],
            COMMENT_LIMIT
        )

        rows = extract_comments(
            listing,
            row["company"],
            row["subreddit"],
            row["post_id"],
            MAX_COMMENTS_PER_POST
        )

        all_comments.extend(rows)
        time.sleep(SLEEP_BETWEEN_POSTS)

    except Exception as e:
        failed_posts.append({
            "company": row["company"],
            "post_id": row["post_id"],
            "error": repr(e)
        })

comments_df = pd.DataFrame(all_comments)
comments_df.head()


# In[22]:


def basic_clean(text):
    """
    Basic text cleaning:
    - Remove line breaks
    - Remove URLs
    - Collapse extra whitespace
    """

    if text is None:
        return ""

    t = str(text)
    t = t.replace("\n", " ").replace("\r", " ")
    t = re.sub(r"(https?://\S+|www\.\S+)", "", t)
    t = re.sub(r"\s+", " ", t).strip()

    return t


# In[23]:


def should_keep(text):
    """
    Filters:
    - Empty comments
    - Deleted/removed comments
    - Extremely short comments
    """

    t = text.strip().lower()

    if t in ("", "[deleted]", "[removed]"):
        return False

    if len(t) < 3:
        return False

    return True


# In[24]:


BOILERPLATE_PATTERNS = [
    "welcome to the community",
    "please ensure",
    "automoderator"
]

def is_boilerplate(text):
    """
    Detects common moderator/bot boilerplate phrases.
    """
    t = text.lower()
    return any(p in t for p in BOILERPLATE_PATTERNS)


# In[25]:


# Convert timestamp
comments_df["comment_created_dt"] = pd.to_datetime(
    comments_df["comment_created_utc"], unit="s", utc=True
)

# Clean text
comments_df["text_raw"] = comments_df["comment_body"].fillna("")
comments_df["text_clean"] = comments_df["text_raw"].apply(basic_clean)

# Basic filtering
comments_df["keep_basic"] = comments_df["text_clean"].apply(should_keep)

# Optional boilerplate filtering
if FILTER_BOILERPLATE:
    comments_df["is_boilerplate"] = comments_df["text_clean"].apply(is_boilerplate)
    comments_df["keep_final"] = comments_df["keep_basic"] & (~comments_df["is_boilerplate"])
else:
    comments_df["keep_final"] = comments_df["keep_basic"]

# Final cleaned dataset
comments_clean_df = comments_df[comments_df["keep_final"]].copy()

print("Raw comments:", len(comments_df))
print("Cleaned comments:", len(comments_clean_df))


# In[26]:


# Save raw data
posts_df.to_csv(os.path.join(OUTDIR, "shipping_posts_raw.csv"), index=False)
comments_df.to_csv(os.path.join(OUTDIR, "shipping_comments_raw.csv"), index=False)

# Save cleaned comments
comments_clean_df.to_csv(
    os.path.join(OUTDIR, "shipping_comments_clean.csv"),
    index=False
)

# Save failed posts log
pd.DataFrame(failed_posts).to_csv(
    os.path.join(OUTDIR, "reddit_failed_posts.csv"),
    index=False
)

print("Files saved successfully.")


# In[ ]:




