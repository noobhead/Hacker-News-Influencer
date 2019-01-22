##########
# Script to find the words that appear most offen in the headlines
# This could help in writing catchy headlines and also for good SEO
########## 

from read import load_data
from collections import Counter
hn_stories = load_data()
headlines =  hn_stories["headline"]

# combining the headlines together into one long string
combined_headlines = ""
for headline in headlines.tolist():
    combined_headlines += str(headline).lower() + " "

# splitting the combined_headlines into words as list
word_list = combined_headlines.split(" ")

# Count of the words in combined_headlines
c = Counter(word_list)

# printing the 100 words that occur the most
for (word, num) in c.most_common(100):
    print(word) 