import twitter

def post_tweet(tweet):
    api = twitter.Api(consumer_key="ekMLO2hprqKlLHMV0H3vaewKW",
                      consumer_secret="H76VvVg5M4CwPKgDpLsZCJvlJrWPfXdLAc3JwwQDZ68dCMfjBi",
                      access_token_key="838396799031345153-wDhhIPtpVwUYnYq4AxJZ9kB2grPJBub",
                      access_token_secret="vjZJ6FDzb1B34Sl0NXOjIRqbpnBUiWsvkvZtW5uC9CegB")

    api.PostUpdate(tweet)
