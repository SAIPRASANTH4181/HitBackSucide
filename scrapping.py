import snscrape.base
import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools

# our search term, using syntax for Twitter's Advanced Search
search = '#suicide since:2015-01-01 until:2021-09-26 lang:en' # -filter:nativeretweets'

# the scraped tweets, this is a generator
scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

# slicing the generator to keep only the first 10000 tweets
sliced_scraped_tweets = itertools.islice(scraped_tweets, 10000)

# convert to a DataFrame and keep only relevant columns
df = pd.DataFrame(sliced_scraped_tweets)[['date','content']]