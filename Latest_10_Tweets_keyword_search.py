import tweepy

auth = tweepy.OAuthHandler('bosxoiztwGaZ0mhNOE4szwoxu', 'I5v9Uzf1XtgQS282OZsK7rLif797H3NMeZKJDLCuURcm1lUtgM')
auth.set_access_token('346514110-Ev3cMADviTTJ7HOOh0luD1vCIvhXHVYsqtP5mlBn', 'bl1gPcPTgvSupHt3eR8wuSgiQaoLtJEe7CmzMAlJCD8Nj')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

def limit_handler(Cursor):
	try:
		while True:
			yield Cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

search_string = 'COVID'
number_of_results = 10

for tweet in tweepy.Cursor(api.search,search_string).items(number_of_results):
	print(tweet.text)
