import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('yt-title-data.csv')

def title_length(title):
    return len(title.split())

length_views = {}

for index, row in df.iterrows():
    length = title_length(row['Title'])
    if length not in length_views:
        length_views[length] = 0
    length_views[length] += row['Views']

length_views_df = pd.DataFrame(list(length_views.items()), columns=['title_length', 'total_views'])

length_views_df.sort_values(by='title_length', inplace=True)

length_views_df.reset_index(drop=True, inplace=True)


print(length_views_df)


plt.figure(figsize=(10, 6))
plt.bar(length_views_df['title_length'], length_views_df['total_views'], color='blue')
plt.xlabel('Title Length (Number of Words)')
plt.ylabel('Total Views')
plt.title('Total Views by Title Length')
plt.show()