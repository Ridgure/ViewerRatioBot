#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioConfigTemplate.py

# Necessary information
FollowerToken = ""                                      # Your Twitch follower token
ClientID = ""                                           # The client ID of your bot

# Settings
# I like to have casterPercentage at 79% because
# if there are 5 streams it rounds 3.95 down to 3 and will check the 3rd stream
casterPercentage = 79                                   # Percentage of the category you want to check for
MINIMUM_STREAMS = 5                                     # Minimum amount of streams in a category
MINIMUM_VIEWERS = 10                                    # Minimum amount of viewers in a category
loopLength = 10                                         # Minutes you want your loop to run for
