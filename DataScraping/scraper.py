import snscrape.modules.twitter as sntwitter
import pandas as pd

attributes = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('He has Generalised Anxiety Disorder since:2014-01-01 until:2023-1-18').get_items()):
    print(i)
    if i>10000:
        break
    attributes.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])

tweets_df = pd.DataFrame(attributes,columns=["User","Data Created", "Number of Likes", "Source of Tweet", "Tweet"])
tweets_df.to_csv('Anxiety2.csv')