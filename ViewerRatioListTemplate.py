#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioLists.py

# This is where you can configure games you like/don't like
# The bot will automatically produce blackWhitelist.md with formatting so you can have an overview of the games

# Favorite games
# Here you put games that you own or really, really want to play

favoriteGames = [
    ['Category 1', [
        ['game1', 'game2', 'game3', 'game4']
    ]],
    ['Category 2', [
        ['game5', 'game6', 'game7', 'game8']
    ]]
]

# Wishlisted games
# Games that I could see myself playing

wishlisted = [
    ['Category 1', [
        ['game1', 'game2', 'game3', 'game4']
    ]],
    ['Category 2', [
        ['game5', 'game6', 'game7', 'game8']
    ]]
]

# Blacklisted games
# Games I don't want to play mostly because they are violent, competitive or skill based
# The id in the blacklist is the twitch category id used for api calls
# This id will be output by the bot in the output.py file

blacklist = [
    ['Category 1', [
        ['game1', 'id1'], ['game2', 'id2']
    ]],
    ['Category 2', [
        ['game3', 'id3'], ['game4', 'id4']
    ]]
]

