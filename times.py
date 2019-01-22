#########
# Script to find At what times are the most articles submitted?
# This could help in choosing correct time for submitting the article in order for it to get more views and upvotes on Hacker News
########## 

from read import load_data
from dateutil.parser import parse

def extract_hour(submission_time):
    datetime_obj = parse(submission_time)
    hour = datetime_obj.hour
    return hour

hn_stories = load_data()
time_col = hn_stories["submission_time"]
hn_stories["hour"] = time_col.apply(extract_hour)

hour_count = hn_stories["hour"].value_counts()
print(hour_count) 