# # # # #   WORKING ON PYTHON 3.6.5     # # # # #
# # # # #   MADE BY:    @rTUNAboss           # # # # #

import tweepy
import json
from dhooks import Webhook, Embed
import time

from discord_extraction import extract_discord_link

# Replace this with an ID of an account you want to get the discord invite from
#USER_ID = "718857559403270144" #CYBERSOLE
#USER_ID = "929793229725110272" #RTUNABOSS
USER_ID = "982012720374575110" #PINGPATROL

CONSUMER_KEY = "4qd4A7TBrMNYw6ZlmUFfufkzk"
CONSUMMER_SECRET = "LXDMiUzihJGrQQOmjVrqpEmHTZ0lRuYYqRV4AZkaOOWTWtuwJj"
ACCESS_TOKEN = "929793229725110272-2JgeMXl2Ssnbz1LhI3VxyZRGSkyuc50"
ACCESS_TOKEN_SECRET = "tavInwIsdBfjjwaNyIRUkxglq7uWZ6kA0D15rpLHo12wV"


class StreamListener(tweepy.StreamListener):
    def on_data(self, data):
        
        # Extract only the tweet text
        j = json.loads(data)
    
        if str(j["id"]) == str(USER_ID):
            print(data)
            try:
                tweet_url = f"https://twitter.com/{j['user']['screen_name']}/status/{j['id']}"
            except Exception as e:
                print(e)

            try:
                tweet = j["text"]
                # Search for a discord invite and print it
                invite = extract_discord_link(tweet)
                if invite:
                    #print(invite)
                    send_hook(text="INVITE FOUND 1", url=tweet_url, website_url=invite)
            except Exception as e:
                print(e)

            #print("\ntrying method n.2")

            try:
                url = j["entities"]["urls"][0]["expanded_url"]
                
                if url.startswith("https://discord") or url.startswith("http://discord"):
                    send_hook(text="INVITE FOUND 2", url=tweet_url, website_url=url)
                elif "discord" in url:
                    send_hook(text="INVITE FOUND 3", url=tweet_url, website_url=url)

                #else:
                    #print("No discord url found")
                #print(invite)

            except Exception as e:
                print(e)

            try:
                entities = j['entities']
                if entities:
                    url = entities['urls'][0]["expanded_url"]
                    send_hook(text="INVITE FOUND 4", url=tweet_url, website_url=url)
                else:
                    print("No discord url found")
                #print(invite)
            except Exception as e:
                print(e)



    def on_error(self, status):
        # On error, print the status code
        print(status)

        if status == 420:
            return False
    

def authenticate(api_key, secret_key, access_token, secret_token):

    auth = tweepy.OAuthHandler(api_key, secret_key)
    auth.set_access_token(access_token, secret_token)
    api = tweepy.API(auth, 
                     wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)
  
    return api


def send_hook(text,url,website_url=None):
    webhook_url = "https://discordapp.com/api/webhooks/603952496959815702/9V3R3vyNbjPcDERc1gO-iGOsM1gz07723I93scyy_8zGbzql2xSBF2vmLYKQq1LJRc32"
    hook = Webhook(url=webhook_url)

    embed = Embed(
        title = f"{text}",
        url = url,
        color=65280,
        timestamp = 'now',
    )

    if website_url:
        embed.add_field('POSSIBLE LINK', value=website_url)
    #embed.set_author(name='New post by {instagram_user}')
    embed.set_footer(text='Worth_the_cop', icon_url="https://scontent-frx5-1.cdninstagram.com/vp/aadc24b1c711307a28abcb5c2b8f4c16/5DCC61B6/t51.2885-19/s320x320/64845864_325154095079310_267583884244287488_n.jpg?_nc_ht=scontent-frx5-1.cdninstagram.com")
    hook.send(embed=embed)




if __name__ == "__main__":
    '''
    tweet = []
    api = authenticate(CONSUMER_KEY, CONSUMMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    while True:
        tweets = api.user_timeline(id=USER_ID, count=1)
        latest_tweet = tweets[0]
        #latest_tweet.append(tweet)
        j = latest_tweet._json
        # print(type(j))
        contents =  j["text"]

        # url = j["entities"]["urls"][0]["expanded_url"]
        #if url:
            #send_hook()
        tweet_url = f"https://twitter.com/{j['user']['screen_name']}/status/{j['id']}"
        if tweet_url not in tweet:
            send_hook(text="CYBER RESTOCK GOGOGO", url=tweet_url, url2=url)
        tweet.append(tweet_url)
        #print(tweet_url)
        time.sleep(1)   

        #send_hook()
    '''

    listener = StreamListener()

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = tweepy.Stream(auth, listener)

    stream.filter(follow=[USER_ID])