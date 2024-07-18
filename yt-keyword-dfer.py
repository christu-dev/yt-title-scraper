import pandas as pd
from collections import Counter
import re

df = pd.read_csv('yt-title-data.csv')

def extract_keywords(title):
    words = re.findall(r'\b\w+\b', title.lower())
    return words

views_counter = Counter()
likes_counter = Counter()

for index, row in df.iterrows():
    keywords = extract_keywords(row['Title'])
    for keyword in keywords:
        views_counter[keyword] += row['Views']
        likes_counter[keyword] += row['Likes']

keywords_df = pd.DataFrame.from_dict({
    'keyword': views_counter.keys(),
    'total_views': views_counter.values(),
    'total_likes': likes_counter.values()
})

keywords_df.sort_values(by=['total_views', 'total_likes'], ascending=False, inplace=True)
keywords_df.reset_index(drop=True, inplace=True)


keywords_df.to_csv('keywords_ranking.csv', index=False)