# # # # #   WORKING ON PYTHON 3.6.5     # # # # #
# # # # #   MADE BY:    @rTUNAboss           # # # # #

import re

def extract_discord_link(tweet):
    link = re.search("discord.gg/......", tweet)
    if link:
        return "https://" + link.group(0)
    link2 = re.search("discordapp.com/invite/......", tweet)
    if link2:
        return "https://" + link.group(0)
