# # # # #   WORKING ON PYTHON 3.6.5     # # # # #
# # # # #   MADE BY:    @rtunazzz | rtuna#4321           # # # # #
# TODO:
# ADD BIO CHANGE SUPPORT
# Add threading support
# Add OCR

print(r'''
 ____    ____   _   _  ______       __     __ _        
|  _ \  / __ \ | \ | ||___  /    /\ \ \   / /(_)       
| |_) || |  | ||  \| |   / /    /  \ \ \_/ /  _   ___  
|  _ < | |  | || . ` |  / /    / /\ \ \   /  | | / _ \ 
| |_) || |__| || |\  | / /__  / ____ \ | | _ | || (_) |
|____/  \____/ |_| \_|/_____|/_/    \_\|_|(_)|_| \___/ 
''')
print(" • made by: rtuna#4321 | @rtunazzz")
print(" • personal use only")


# # # # # # # # # # # # # # # # # # # #     IMPORTING LIBRARIES        # # # # # # # # # # # # # # # # # # # #

#External
import tweepy
from dhooks import Webhook, Embed

import datetime
import json
import time
import re
import random
# import threading

# # # # # # # # # # # # # # # # # # # #     DEFINING STATIC VARIABLES        # # # # # # # # # # # # # # # # # # # #
#TODO Paste here your d iscord webhooks
TWITTER_FILTERED = ""
TWITTER_UNFILTERED = ""

#TODO List here all IDs of accounts you want to monitor
USER_IDS = [
    "929793229725110272",   #me
    "718857559403270144",   #Cyber
    "886027671993536512",   #Offline - Lucas
    "863006606124085248",   #SOleSorcerer
    "1044054193365934081",  #Kodai
    "990276109383225344",   #F3ather
    "1092061875318210560",  #GaneshBot
    "1008988284989534208",  #TKS
    "1354387910",           #NSB
    "831219416453042176",   #EVE_Robotics
    "914897340280053763",   #EVEAIO
    "936472526472933376",   #Backdoor
    "940121522269691904",   #GhostAIO
    "838811219452649473",   #SneakerCopter
    "887790349699227650",   #DestroyerBots
    "1094899148845920262",  #RuggAIO
    "1053046389704409089",  #PrismAIO
    "1056226100513329152",  #DreamAIO
    "929817052709134336",   #WhatBot
    "997644265156116480",   #Balkobot
    "1032215346189672448",  #BlackOutIO
    "1126199639135354885",  #Sky_AIO
    "1035491698254733313",  #SoleTerminator
    "1001896176428441601",  #AdeptBots
    "968299339117363200",   #WrathBots

    ]



#Loads crednetials
with open("credentials.json", "r") as f:
    credentials = json.loads(f.read())
CONSUMER_KEY = credentials['CONSUMER_KEY']
CONSUMER_SECRET = credentials['CONSUMER_SECRET']
ACCESS_TOKEN = credentials['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']


#Hex list for webhook colors
HEX_LIST = [
    16725342,
    16604024,
    16736311,
    16750950,
    16750899,
    16763955,
    16777062,
    13434624,
    6750054,
    11202769,
    5292006,
    16740095,
    15611090,
    16711884,
]

#TODO Setup
keywords = [
    'restock',
    'password',
    'live',
]
# # # # # # # # # # # # # # # # # # # #     DEFINING FUNCTIONS        # # # # # # # # # # # # # # # # # # # #
#####   WEBHOOK FUNCTIONS    #####
def notify_twitter(webhook_url, tweet_content, user,tweet_url, profile_pic, screen_name, url=None):
    '''Sends Embed to the TwitterMonitor'''
    hook = Webhook(url=webhook_url, username=user, avatar_url=profile_pic)
    color=random.choice(HEX_LIST)

    embed = Embed(
        # title = f"New tweet from {user}",
        url = tweet_url,
        color=color,
        timestamp = 'now',
        description = tweet_content,
    )

    embed.set_author(name=screen_name,icon_url=profile_pic,url=f'https://twitter.com/{screen_name}')
    # embed.set_footer(text=f'BONZAY Twitter • {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}',icon_url='https://cdn.discordapp.com/emojis/636516489322561536.png?v=1')
    embed.set_footer(text=f'BONZAY Twitter',icon_url='https://cdn.discordapp.com/emojis/636516489322561536.png?v=1')

    twitter_url_builder=f'https://twitter.com/{screen_name}'
    if url:
         embed.add_field('LINK FOUND', value=url, inline=False)
    embed.add_field('Links', value=f'[Profile](https://twitter.com/{screen_name}) — [Likes]({twitter_url_builder}/likes) — [Replies]({twitter_url_builder}/with_replies) — [Media]({twitter_url_builder}/media) — [TweetLink]({tweet_url})', inline=False)
    hook.send(embed=embed)

def notify_password_url(webhook_url, password_url, screen_name, profile_pic):
    
    hook = Webhook(url=webhook_url, username=screen_name, avatar_url=profile_pic)
    color= random.choice(HEX_LIST)


    embed = Embed(
        title = "Possible link found:",
        color=color,
        description = password_url,
    )

    embed.set_author(name=screen_name,icon_url=profile_pic,url=f'https://twitter.com/{screen_name}')
    embed.set_footer(text=f'BONZAY Twitter • {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}',icon_url='https://cdn.discordapp.com/emojis/636516489322561536.png?v=1')

    # if url:
    #      embed.add_field('Link in tweet', value=url)


    #embed.set_author(name='New post by {instagram_user}')
    # if tweet_content:
    #     embed.add_field("Tweet description", tweet_content)
    # embed.image(image)
    hook.send(embed=embed)
def notify_discord_invite(webhook_url, invite_url, screen_name, profile_pic):
    hook = Webhook(url=webhook_url)
    color= random.choice(HEX_LIST)

    embed = Embed(
        title = "Discord invite found:",
        color=color,
        description = invite_url,
    )

    embed.set_author(name=screen_name,icon_url=profile_pic,url=f'https://twitter.com/{screen_name}')
    embed.set_footer(text='BONZAY', icon_url="https://cdn.discordapp.com/emojis/636516489322561536.png?v=1")

    hook.send(embed=embed)

#####   JSON EXTRACTING FUNCTIONS    #####
def get_url(j):
    '''Takes in json file and returns a URL if it's in the passed tweet data'''
    tweet_url = j["entities"]["urls"][0]["expanded_url"]
    if 'twitter.com' not in tweet_url:
        return tweet_url.lower()
def get_tweet_url(j):
    '''Takes in json file with tweet data and returns a tweet url'''
    return f"https://twitter.com/{j['user']['screen_name']}/status/{j['id']}"
def get_profile_pic(j):
    '''Takes in json file and returns an URL of users profile picture'''
    return j["user"]["profile_image_url"]
def get_tweet_content(j):
    '''Takes in json file and returns tweet contents'''
    tweet_text = j['text']
    tweet_url_list = j['entities']['urls']
    for val in tweet_url_list:
        short_url = val['url']
        expanded_url = val['expanded_url']
        tweet_text = tweet_text.replace(short_url, expanded_url)

    return tweet_text

def get_screen_name(j):
    '''Takes in json file and returns users screen name'''
    return j['user']['screen_name']
def get_user_url(j):
    '''Takes in json of tweet data and returns URL provided in users BIO'''
    return j['user']['url']
def get_user(j):
    return j["user"]["name"]

#####   STRING EDITING FUNCTIONS    #####
def tweet_description_into_lines(j):
    '''Takes json file and parses it into lines of text description'''
    tweet_description = j['text']
    return tweet_description.split('\n')
def remove_spaces(string):
    '''Takes in a string and returns the same string with spaces removed.

    Example: "Hi how are you" -> "Hihowareyou"'''
    return string.strip().replace(" ", "")
def compile_final_url(user_url, passw):
    '''Takes in user_url and password and contstruct final URL with password in it.'''
    match = re.search(r"^(https?:\/\/)?[^\/]*", user_url)
    stripped_url = match.group(0)
    if 'http' in stripped_url:
        return stripped_url + f'/?password={passw}'
    else:
        return f"https://{stripped_url}/?password={passw}"

#####   PASSWORD EXTRACTING FUNCTIONS    #####
def password_with_colon(line_without_spaces):
    '''CASE for "password:" (e.g password:109458101) if found, returns the password'''
    if "password:" in line_without_spaces:
        match = re.search(r"(?<=:).*",line_without_spaces)
        return match.group(0)
def password_with_is(line):
    '''CASE for "password is" (e.g. password is 1029124) if found, returns the password'''
    if "password is" in line:
        match = re.search(r"(?<=is).*",line)
        return match.group(0).replace(' ', '')
def password_with_space(line):
    '''CASE for password followed by space (e.g. password 09034865924) if found, returns the password'''
    if "password" in line:
        # match = re.search(r"(?<=password).*",line) # this matches the whole line
        match = re.search(r"(?<=password) ?[^ ]*",line) # this matches only to the first space 
        return match.group(0).replace(" ", '')

#####   PASSWORD EXTRACTING FUNCTIONS    #####
def build_regex_search(keywords):
    '''Builds a regex string to match either of the passed keywords and returns it.'''
    re_string = r''
    num = 1
    for kw in keywords:
        if num < len(keywords):
            re_base = r'\b(\w*' + kw + r'\w*)\b|'
            re_string += re_base
            num += 1
        else:
            re_base = r'\b(\w*' + kw + r'\w*)\b'
            re_string += re_base
    return re_string

regex_string = build_regex_search(keywords)

class StreamListener(tweepy.StreamListener):


    def on_data(self, data):
        j = json.loads(data)
        if "delete" not in j:
            try:
                tweet_content = get_tweet_content(j)
                # if the id matches one of the IDs we are monitoring:
                if j["user"]["id_str"] in USER_IDS and "RT" not in tweet_content:

                    #if any of the users above tweets, send message to unfiltered
                    user = get_user(j)
                    tweet_url = get_tweet_url(j)
                    profile_pic_url = get_profile_pic(j)
                    screen_name = get_screen_name(j)
                    notify_twitter(
                        webhook_url=TWITTER_UNFILTERED,
                        tweet_content=tweet_content,
                        user=user,
                        tweet_url=tweet_url,
                        profile_pic=profile_pic_url,
                        screen_name=screen_name,    
                        )

                    #search for a keyword match
                    r = re.match(regex_string, tweet_content, re.IGNORECASE)
                    if r:
                        notify_twitter(
                            webhook_url=TWITTER_FILTERED,
                            tweet_content=tweet_content,
                            user=user,
                            tweet_url=tweet_url,
                            profile_pic=profile_pic_url,
                            screen_name=screen_name
                            )
                        #search for password
                        lines = tweet_description_into_lines(j)

                        for line in lines:
                            
                            line_without_spaces = remove_spaces(line)
                            
                            passw = password_with_colon(line_without_spaces)
                            if passw:
                                # user_url = get_user_url(j)
                                final_url = compile_final_url(url, passw)
                                #TODO Edit variables below so they only load once (probs will be using scheme:
                                #                                                  new tweet -> noitify -> search for password -> notify password)
                                profile_pic = get_profile_pic(j)
                                screen_name = get_screen_name(j)
                                notify_password_url(TWITTER_FILTERED, final_url, screen_name, profile_pic)
                                break

                            passw = password_with_is(line)
                            if passw:
                                # user_url = get_user_url(j)
                                final_url = compile_final_url(url, passw)
                                profile_pic = get_profile_pic(j)
                                screen_name = get_screen_name(j)
                                notify_password_url(TWITTER_FILTERED, final_url, screen_name, profile_pic)
                                break

                            passw = password_with_space(line)
                            # print(passw)
                            if passw:
                                # user_url = get_user_url(j)
                                final_url = compile_final_url(url, passw)
                                profile_pic = get_profile_pic(j)
                                screen_name = get_screen_name(j)
                                notify_password_url(TWITTER_FILTERED, final_url, screen_name, profile_pic)
                                break
                    else:
                    
                        try:
                            url = get_url(j)
                        except:
                            url = None
                            pass
                        # url = None
                        # user = get_user(j)
                        # tweet_url = get_tweet_url(j)
                        # profile_pic_url = get_profile_pic(j)
                        # screen_name = get_screen_name(j)

                        if (url != None) and ('discord.gg' in url):
                            notify_discord_invite(TWITTER_FILTERED, url, screen_name, profile_pic_url)
                        else:
                            if url:
                                notify_twitter(
                                webhook_url=TWITTER_FILTERED,
                                tweet_content=tweet_content,
                                user=user,
                                tweet_url=tweet_url,
                                profile_pic=profile_pic_url,
                                screen_name=screen_name,
                                url=url
                                )

                            #search for password
                            lines = tweet_description_into_lines(j)

                            for line in lines:
                                
                                line_without_spaces = remove_spaces(line)
                                
                                passw = password_with_colon(line_without_spaces)
                                if passw:
                                    # user_url = get_user_url(j)
                                    final_url = compile_final_url(url, passw)
                                    #TODO Edit variables below so they only load once (probs will be using scheme:
                                    #                                                  new tweet -> noitify -> search for password -> notify password)
                                    profile_pic = get_profile_pic(j)
                                    screen_name = get_screen_name(j)
                                    notify_password_url(TWITTER_FILTERED, final_url, screen_name, profile_pic)
                                    break

                                passw = password_with_is(line)
                                if passw:
                                    # user_url = get_user_url(j)
                                    final_url = compile_final_url(url, passw)
                                    profile_pic = get_profile_pic(j)
                                    screen_name = get_screen_name(j)
                                    notify_password_url(TWITTER_FILTERED, final_url, screen_name, profile_pic)
                                    break

                                passw = password_with_space(line)
                                # print(passw)
                                if passw:
                                    # user_url = get_user_url(j)
                                    final_url = compile_final_url(url, passw)
                                    profile_pic = get_profile_pic(j)
                                    screen_name = get_screen_name(j)
                                    notify_password_url(TWITTER_FILTERED, final_url, screen_name, profile_pic)
                                    break
            except Exception as e:
                print(e)



    def on_error(self, status):
        # On error, print the status code
        print(status)

        if status == 420:
            return False


# # # # # # # # # # # # # # # # # # # #     RUNNING THE CODE        # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    listener = StreamListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = tweepy.Stream(auth, listener)

    stream.filter(follow=USER_IDS, is_async=True)



# # # # # # # # # # # # # # # # # # # #     UNUSED        # # # # # # # # # # # # # # # # # # # #

'''
def test():
    with open("test_tweet.json", "r") as f:
        j = json.loads(f.read())
    
    try:
        #if there is a url in the tweet, include it
        url = get_url(j)
        
        user = j["user"]["name"]
        content = get_tweet_content(j)
        tweet_url = get_tweet_url(j)
        profile_pic = get_profile_pic(j)
        screen_name = get_screen_name(j)
        if url:
            notify_twitter(
            tweet_content=content,
            user=user,
            tweet_url=tweet_url,
            profile_pic=profile_pic,
            screen_name=screen_name,
            url=url
            )
        else:
            raise Exception
    except:
        pass

    lines = tweet_description_into_lines(j)
    
    for line in lines:
        
        line_without_spaces = remove_spaces(line)
        
        try:
            passw = password_with_colon(line_without_spaces)
            if passw:
                user_url = get_user_url(j)
                final_url = compile_final_url(user_url, passw)
                #TODO Edit variables below so they only load once (probs will be using scheme:
                #                                                  new tweet -> noitify -> search for password -> notify password)
                profile_pic = get_profile_pic(j)
                screen_name = get_screen_name(j)
                notify_password_url(final_url, screen_name, profile_pic)
            else:
                raise Exception


        except:
            try:
                passw = password_with_is(line)
                print(passw)
                if passw:
                    user_url = get_user_url(j)
                    final_url = compile_final_url(user_url, passw)
                    profile_pic = get_profile_pic(j)
                    screen_name = get_screen_name(j)
                    notify_password_url(final_url, screen_name, profile_pic)
                else:
                    raise Exception


            except:
                print("Trying 3")
                try:
                    passw = password_with_space(line)
                    print(passw)
                    if passw:
                        user_url = get_user_url(j)
                        final_url = compile_final_url(user_url, passw)
                        profile_pic = get_profile_pic(j)
                        screen_name = get_screen_name(j)
                        notify_password_url(final_url, screen_name, profile_pic)
                except:
                    pass
test()
'''

'''

def on_image(j):
    pass
    # MORE TESTING NEEDED

    img = j["entities"]["media"]
    
#CASE if password with spaces is written in text (ex. "p a s s w o r d")
# elif "password" in line_without_spaces:
#     if ":" in line_without_spaces:
#         match = re.search(r"(?<=:).*",line_without_spaces)
#         passw = match.group(0)
#     else:
#         passw = 

#CASE if pass is written in line
# elif "pass" in line:
#     match = re.search(r'passw?o?r?d?:?[^ ]*', line_without_spaces)
#     str_match = match.group(0)


'''
