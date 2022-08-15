#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bot.py
# Necessary information
Host = "irc.twitch.tv"                                  # The Twitch IRC server
Port = 6667                                             # Always use port 6667!
Nickname = ""                                           # The username of your bot
FollowerToken = ""                                      # Your Twitch follower token
SubscriberToken = ""                                    # Your Twitch subscriber token
Channel = "#"                                           # The channel you want to join
ClientID = ""                                           # The client ID of your bot
casterPercentage = 79                                   # Percentage of the category you want to check for
minStreams = 5                                          # Minimum amount of streams in a category
minViewers = 10                                         # Minimum amount of viewers in a category

# Useful information
ClientSecret = ""

# token needs to include scope that lets you view drops
AppAccessToken = ""
godToken = "" # Token with every possible scope. This is only to make it easier for me. I don't recommend using this