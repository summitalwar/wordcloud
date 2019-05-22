# =============================================================================
# --- Wordcloud generator
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt

import lib

from wordcloud import WordCloud, STOPWORDS

fn_ip = "Youtube04-Eminem"

# =============================================================================
# --- DO NOT CHANGE ANYTHING FROM HERE
# =============================================================================
path = lib.cfg.path
df_ip = pd.read_csv(path + "\\data\\input\\" + fn_ip + ".csv")

comment_words = ' '
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df_ip.CONTENT:
    # typecaste each val to string
    val = str(val)
    # split the value
    tokens = val.split()
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    for words in tokens:
        comment_words = comment_words + words + ' '

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.show()
