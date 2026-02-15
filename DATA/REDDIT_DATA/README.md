## Explanation of Data Files 

### shipping_posts_raw
- Contains all of the raw text and metadata from scraped reddit posts

### shipping_comments_raw
- Contains all of the raw text and metadata from scraped reddit comments

### shipping_comments_clean
- Follows the same format as shipping_comments_raw, but has removed comments with no valuable data
- Used in data analysis
- Too large to be displayed in a tabular format

### shipping_comments_clean_first_5
- Takes in the first 5 observations from shipping_comments_clean to demonstrate the data in a tabular format

### shipping_comments_final_clean
- Removes unnused information from shipping_comments_clean to demonstrate just the text data in an easy-to-read format
- Too large to be displayed in a tabular format

### shipping_comments__final_clean_first_5
- Takes in the first 5 observations from shipping_comments_final_clean to demonstrate the data in a tabular format
