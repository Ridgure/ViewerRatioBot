#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioLists.py

# This is where you can configure games you like/don't like
# The bot will automatically produce blackWhitelist.md with formatting so you can have an overview of the games

# Favorite games
# Here you put games that you own or really, really want to play

favoriteGames = [
    ['Category 1', [
        ['game1', 'gameid1'], ['game2', 'gameid2'], ['game3', 'gameid3'], ['game3', 'gameid3']
    ]],
    ['Category 2', [
        ['Subcategory 1', [
            ['game5', 'gameid5'], ['game6', 'gameid6'], ['game7', 'gameid7'], ['game8', 'gameid8']
        ]]
    ]]
]

# Wishlisted games
# Games that I could see myself playing

wishlisted = [
    ['Category 1', [
        ['game1', 'gameid1'], ['game2', 'gameid2'], ['game3', 'gameid3'], ['game3', 'gameid3']
    ]],
    ['Category 2', [
        ['Subcategory 1', [
            ['game5', 'gameid5'], ['game6', 'gameid6'], ['game7', 'gameid7'], ['game8', 'gameid8']
        ]]
    ]]
]

# Blacklisted games
# Games I don't want to play mostly because they are violent, competitive or skill based
# The id in the blacklist is the twitch category id used for api calls
# This id will be output by the bot in the output.py file

blacklist = [
    ['Category 1', [
        ['game1', 'gameid1'], ['game2', 'gameid2'], ['game3', 'gameid3'], ['game3', 'gameid3']
    ]],
    ['Category 2', [
        ['Subcategory 1', [
            ['game5', 'gameid5'], ['game6', 'gameid6'], ['game7', 'gameid7'], ['game8', 'gameid8']
        ]]
    ]]
]

