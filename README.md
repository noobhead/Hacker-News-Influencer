# Introduction
If you just started writing articles chances are you don’t have many readers, if any at all.
If you are wondering what you are doing wrong and what you need to do in order to build an audience, this project will help.

This project aims to help the publishers promote their articles on [Hacker News](https://news.ycombinator.com/) by knowing the words to be used in the Headlines that get as many upvotes as possible, the length of the most optimal headline, choosing the correct time for submitting the article to get more views, choosing the domains for writing the article in order for it to get submitted on Hacker News. 

## About Hacker News
[Hacker News](https://news.ycombinator.com/) News is a site where users can submit articles from across the internet (usually about technology and startups), and others can "upvote" the articles, signifying that they like them. The more upvotes a submission gets, the more popular it was in the community. Popular articles get to the "front page" of Hacker News, where they're more likely to be seen by others.

## Know your Dataset
We'll be working with a dataset of submissions to Hacker News from 2006 to 2015. This dataset was compiled by Arnaud Drizard using the Hacker News API, and can be found [here](https://github.com/arnauddri/hn). We've sampled 10000 rows from the data randomly, and removed all extraneous columns. Our dataset only has four columns: 

* submission_time -- when the story was submitted.
* upvotes -- number of upvotes the submission got.
* url -- the base domain of the submission.
* headline -- the headline of the submission. Users * can edit this, and it doesn't have to match the headline of the original article.

This could help people write headlines that get as many upvotes as possible, and submit articles at the right time. 
