#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioBot.py
import typing
from datetime import datetime, timedelta
import statistics
import time
import math
import os

import requests
import re
from ViewerRatioConfig import *
from blacklistedStreams import *
from ViewerRatioLists import *
from tags import *
from output import *
from typing import cast

global gameViewers
global pagination
global paginationTopGames
global gameStreams
global topGameViewers
global medianList
global gameViewersLooped
global gameStreamsLooped
global gameViewerRatioLooped
global hostGamesLooped
global gameViewersMedianLooped
global viewerRatioMedianRatioLooped
global topGameIds
global topGameIdsLooped
global topGameNames
global stopGettingGames
global dropsGames
global firstRun
global worthGames
global gameViewersMedian
global MINIMUM_STREAMS
global MINIMUM_VIEWERS
global loopStart
global combined_tags
global new_games_ids
global totalGames
global totalViewers
global totalStreams
global totalViewerRatio
global totalViewersMedian
global totalViewerRatioMedianRatio

global topGameIdsLoopedPrinted
global hostGamesLoopedPrinted
global gameViewersLoopedPrinted
global gameStreamsLoopedPrinted
global gameViewerRatioLoopedPrinted
global gameViewersMedianLoopedPrinted
global viewerRatioMedianRatioLoopedPrinted
global viewerRatioMedianRatioLoopedSorted

# Globals permanent through while true loops
gameViewersLooped: list[int] = []
gameStreamsLooped: list[int] = []
gameViewerRatioLooped: list[float] = []
hostGamesLooped: list[str] = []
gameViewersMedianLooped: list[float] = []
viewerRatioMedianRatioLooped: list[float] = []
topGameIdsLooped: list[str] = []
loops: int = 0
worthGames: int = 0
dropsGames: list[str] = []
firstRun: bool = True

latestGameFileName: str

topGameIdsLoopedPrinted: list[str] = []
hostGamesLoopedPrinted: list[str] = []
gameViewersLoopedPrinted: list[int] = []
gameStreamsLoopedPrinted: list[int] = []
gameViewerRatioLoopedPrinted: list[float] = []
gameViewersMedianLoopedPrinted: list[float] = []
viewerRatioMedianRatioLoopedPrinted: list[float] = []
viewerRatioMedianRatioLoopedSorted: list[float] = []


def list_item(list_var: list, index_first_level: int, index_second_level: int | None = None, index_third_level: int | None = None) -> str:
    if index_third_level is not None:
        return cast(str, list_var[index_first_level][1][index_second_level][1][index_third_level][0])
    elif index_second_level is not None:
        return cast(str, list_var[index_first_level][1][index_second_level][0])
    else:
        return cast(str, list_var[index_first_level][0])


def second_list_item(list_var: list, index_first_level: int, index_second_level: int | None = None, index_third_level: int | None = None) -> str:
    if index_third_level is not None:
        return cast(str, list_var[index_first_level][1][index_second_level][1][index_third_level][1])
    elif index_second_level is not None:
        return cast(str, list_var[index_first_level][1][index_second_level][1])
    else:
        return cast(str, list_var[index_first_level][1])


def nested_list(nested_list_var: list, index_first_level: int, index_second_level: int | None = None, index_third_level: int | None = None) -> list[str]:
    if index_third_level is not None:
        return cast(list[str], nested_list_var[index_first_level][1][index_second_level][1][index_third_level][1])
    elif index_second_level is not None:
        return cast(list[str], nested_list_var[index_first_level][1][index_second_level][1])
    else:
        return cast(list[str], nested_list_var[index_first_level][1])


def last_nested_list(nested_list_var: list, index_first_level: int, index_second_level: int | None = None, index_third_level: int | None = None) -> list[str]:
    if index_third_level is not None:
        return cast(list[str], nested_list_var[index_first_level][-1][index_second_level][1][index_third_level][1])
    elif index_second_level is not None:
        return cast(list[str], nested_list_var[index_first_level][-1][index_second_level][1])
    else:
        return cast(list[str], nested_list_var[index_first_level][-1])


def print_every_ten(list_of_strings: list[str]) -> None:
    new_games_print_list: list[str] = []
    for print_games_index in range(len(list_of_strings)):
        new_games_print_list.append(list_of_strings[print_games_index])
        if print_games_index % 10 == 9:
            print((print_games_index - 8), "-", (print_games_index + 1), ", ".join(new_games_print_list))
            new_games_print_list = []
    if not (len(new_games_print_list) % 10) == 0:
        print((len(list_of_strings) - (len(list_of_strings) % 10) + 1), "-", len(list_of_strings), ", ".join(new_games_print_list))


# Update blacklist readme file
print('Updating black/whitelist')
f = open("tmpfile.py", "w", encoding='utf-8')
f.writelines('<a href="http://www.twitch.tv/ridgure"><img src="https://pbs.twimg.com/profile_banners/4144666635/1656852039/1500x500" title="FVCproductions" alt="FVCproductions"></a>')
f.writelines('\n')
f.writelines('\n<h1 align="center">')
f.writelines('\n  <br>')
f.writelines('\n  <a href="http://www.twitch.tv/ridgure"><img src="https://pbs.twimg.com/profile_images/965416492924891136/N-EvLzcd_400x400.jpg" alt="Markdownify" width="200"></a>')
f.writelines('\n  <br>')
f.writelines('\n  White black list')
f.writelines('\n  <br>')
f.writelines('\n</h1>')
f.writelines('\n')
f.writelines('\n<h4 align="center">A black and whitelist containing games I want to and do not want to stream on my Twitch channel <a href="https://twitch.tv/ridgure" target="_blank">Twitch.tv/Ridgure</a>.</h4>')
f.writelines('\n<div align="center">This list contains games I am interested in wanting to stream depending on the type of game and the community around the game</div>')
f.writelines('\n')
f.writelines('\n')
f.writelines('\n<p align="center">')
f.writelines('\n  <a href="#favorite-games">Favorite games</a> •')
f.writelines('\n  <a href="#whitelist">Whitelist</a> •')
f.writelines('\n  <a href="#blacklist">Blacklist</a>')
f.writelines('\n</p>')
f.writelines('\n')
f.writelines('\n## Favorite games:')
f.writelines('\n')
f.writelines('\n **Categories:**')
favoriteCategories: list = []
for favorite_category in range(len(FAVORITE_GAMES)):
    favoriteCategories.append(list_item(FAVORITE_GAMES, favorite_category))
f.writelines("\n" + ', '.join(favoriteCategories))
f.writelines('\n')
singularCategories = False
for favorite_category in range(len(FAVORITE_GAMES)):
    if isinstance(nested_list(FAVORITE_GAMES, favorite_category, 0), str):
        if not singularCategories:
            f.writelines('\n|   |**Favorite games**|')
            f.writelines('\n|---|---------------------|')
        singularCategories = True
        gameCategories = []
        for category in range(len(nested_list(FAVORITE_GAMES, favorite_category))):
            gameCategories.append(list_item(FAVORITE_GAMES, favorite_category, category))
        f.writelines('\n|**' + list_item(FAVORITE_GAMES, favorite_category) + '**|' + ', '.join(gameCategories) + '|')
    else:
        if singularCategories:
            f.writelines('\n')
        singularCategories = False
        subCategories = []
        for favorite_game in range(len(nested_list(FAVORITE_GAMES, favorite_category))):
            subCategories.append(list_item(FAVORITE_GAMES, favorite_category, favorite_game))
        f.writelines('\n')
        f.writelines('\n|**' + list_item(FAVORITE_GAMES, favorite_category) + '**|_' + ', '.join(subCategories) + '_|')
        f.writelines('\n|----------------|-----------------------------------------------------------------------|')
        for category in range(len(nested_list(FAVORITE_GAMES, favorite_category))):
            categoryGames = []
            for game in range(len(nested_list(FAVORITE_GAMES, favorite_category, category))):
                categoryGames.append(list_item(FAVORITE_GAMES, favorite_category, category, game))
            f.writelines('\n|**' + list_item(FAVORITE_GAMES, favorite_category, category) + '**|' + ', '.join(categoryGames) + '|')
        f.writelines('\n')
f.writelines('\n')
f.writelines('\n<a href="#white-black-list">Back to top</a>')
f.writelines('\n## Whitelist:')
f.writelines('\n')
f.writelines('\n **Categories:**')
whitelistCategories = []
for wishlist_category in range(len(WISHLISTED)):
    whitelistCategories.append(list_item(WISHLISTED, wishlist_category))
f.writelines("\n" + ', '.join(whitelistCategories))
f.writelines('\n')
singularCategories = False
for wishlist_category in range(len(WISHLISTED)):
    if isinstance(nested_list(WISHLISTED, wishlist_category, 0), str):
        if not singularCategories:
            f.writelines('\n|   |**Whitelisted games**|')
            f.writelines('\n|---|---------------------|')
        singularCategories = True
        categoryGames = []
        for game in range(len(nested_list(WISHLISTED, wishlist_category))):
            categoryGames.append(list_item(WISHLISTED, wishlist_category, game))
        f.writelines('\n|**' + list_item(WISHLISTED, wishlist_category) + '**|' + ', '.join(categoryGames) + '|')
    else:
        if singularCategories:
            f.writelines('\n')
        singularCategories = False
        subCategories = []
        for favorite_game in range(len(nested_list(WISHLISTED, wishlist_category))):
            subCategories.append(list_item(WISHLISTED, wishlist_category, favorite_game))
        f.writelines('\n')
        f.writelines('\n|**' + list_item(WISHLISTED, wishlist_category) + '**|_' + ', '.join(subCategories) + '_|')
        f.writelines('\n|---|---------------------|')
        for favorite_game in range(len(nested_list(WISHLISTED, wishlist_category))):
            categoryGames = []
            for game in range(len(nested_list(WISHLISTED, wishlist_category, favorite_game))):
                categoryGames.append(list_item(WISHLISTED, wishlist_category, favorite_game, game))
            f.writelines('\n|**' + list_item(WISHLISTED, wishlist_category, favorite_game) + '**|' + ', '.join(categoryGames) + '|')
        f.writelines('\n')
f.writelines('\n')
f.writelines('\n<a href="#whitelist">Back to top</a>')
f.writelines('\n## Blacklist:')
f.writelines('\n')
f.writelines('\n **Categories:**')
blacklistCategories = []
for blacklist_category in range(len(BLACKLIST)):
    blacklistCategories.append(list_item(BLACKLIST, blacklist_category))
f.writelines("\n" + ', '.join(blacklistCategories))
f.writelines('\n')
singularCategories = False
for blacklist_category in range(len(BLACKLIST)):
    blacklistedGames = []
    if isinstance(nested_list(BLACKLIST, blacklist_category, 0), str):
        if not singularCategories:
            f.writelines('\n|   |**Blacklisted games**|')
            f.writelines('\n|---|---------------------|')
        singularCategories = True
        for favorite_category in range(len(nested_list(BLACKLIST, blacklist_category))):
            blacklistedGames.append(list_item(BLACKLIST, blacklist_category, favorite_category))
        f.writelines('\n|**' + list_item(BLACKLIST, blacklist_category) + '**|' + ', '.join(blacklistedGames) + '|')
    else:
        if singularCategories:
            f.writelines('\n')
        singularCategories = False
        subCategories = []
        for favorite_game in range(len(nested_list(BLACKLIST, blacklist_category))):
            subCategories.append(list_item(BLACKLIST, blacklist_category, favorite_game))
        f.writelines('\n|**' + list_item(BLACKLIST, blacklist_category) + '**|_' + ', '.join(subCategories) + '_|')
        f.writelines('\n|---|---------------------|')
        for favorite_game in range(len(nested_list(BLACKLIST, blacklist_category))):
            blacklistedGames = []
            for favorite_category in range(len(nested_list(BLACKLIST, blacklist_category, favorite_game))):
                blacklistedGames.append(list_item(BLACKLIST, blacklist_category, favorite_game, favorite_category))
            f.writelines('\n|**' + list_item(BLACKLIST, blacklist_category, favorite_game) + '**|' + ', '.join(blacklistedGames) + '|')
        f.writelines('\n')
f.writelines('\n')
f.writelines('\n<a href="#blacklist">Back to top</a>')
f.close()
os.replace('tmpfile.py', 'blackWhitelist.md')
print('Black/whitelist has been updated')


def get_more_game_viewers() -> None:
    global pagination
    global topGameViewers
    url_game_viewers = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[
        -1] + "&after=" + pagination
    params_game_viewers = {"Client-ID": "" + CLIENT_ID + "", "Authorization": "Bearer " + FOLLOWER_TOKEN}
    game_viewers_response: requests.models.Response = requests.get(url_game_viewers, headers=params_game_viewers)
    if game_viewers_response.status_code == 200:
        pass
    elif game_viewers_response.status_code == 400:
        print("Bad request")
    elif game_viewers_response.status_code == 429:
        print("Too many moregameviewer requests")
    request_more_viewers = game_viewers_response.json()
    if not request_more_viewers['pagination'] == {}:
        pagination = request_more_viewers['pagination']['cursor']
        for a in request_more_viewers['data']:
            if int(a['viewer_count']) == 1:
                topGameViewers = topGameViewers + 0
            else:
                topGameViewers = topGameViewers + int(a['viewer_count'])
        get_more_game_viewers()


def get_more_games() -> None:
    global paginationTopGames
    global topGameIds
    global topGameNames
    global pagination
    global topGameViewers
    global stopGettingGames
    url_more_games = "https://api.twitch.tv/helix/games/top?first=100" + "&after=" + paginationTopGames
    params_more_games = {"Client-ID": "" + CLIENT_ID + "", "Authorization": "Bearer " + FOLLOWER_TOKEN}
    more_games_response: requests.models.Response = requests.get(url_more_games, headers=params_more_games)
    if more_games_response.status_code == 200:
        pass
    elif more_games_response.status_code == 400:
        print("Bad request")
    elif more_games_response.status_code == 429:
        print("Too many more games requests")
    more_games_response_json = more_games_response.json()
    if TESTING:
        print(more_games_response_json)
        print(more_games_response_json['data'])
    if not more_games_response_json['pagination'] == {}:
        paginationTopGames = more_games_response_json['pagination']['cursor']
        for i in more_games_response_json['data']:
            duplicate_game = False
            for topGame in range(len(topGameNames)):
                if i['name'] == topGameNames[topGame]:
                    duplicate_game = True
            if not duplicate_game:
                topGameIds.append(i['id'])
                topGameNames.append(i['name'])
        get_more_game_viewers()
        pagination = ""
    if topGameViewers < 100:
        stopGettingGames = stopGettingGames + 1
    topGameViewers = 0
    if stopGettingGames < 3:
        get_more_games()
    # elif TESTING:
    #     print("Raw streamed games are: " + str(len(topGameIds)) + " " + str(topGameNames))


def get_more_streams(i: int) -> None:
    try:
        global pagination
        global gameViewers
        global gameStreams
        global medianList
        global dropsGames
        global combined_tags
        url_more = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[i] + "&after=" + pagination
        params_more = {"Client-ID": "" + CLIENT_ID + "", "Authorization": "Bearer " + FOLLOWER_TOKEN}
        more_streams_response: requests.models.Response = requests.get(url_more, headers=params_more)
        if more_streams_response.status_code == 200:
            pass
        elif more_streams_response.status_code == 400:
            print("Bad request")
        elif more_streams_response.status_code == 429:
            print("Too many morestreams requests")
        get_streams_request = more_streams_response.json()
        if not get_streams_request['pagination'] == {}:
            pagination = get_streams_request['pagination']['cursor']
            gameStreams[i] = gameStreams[i] + len(get_streams_request['data'])
            # if testing:
            #     print('Getting more streams')
            for e in get_streams_request['data']:
                # if testing and e['game_name'].lower() == testGame.lower():
                #     print(e)
                started_at = e['started_at']
                year, month, day, hour, minute, second = int(started_at[0:4]), int(started_at[5:7]), int(
                    started_at[8:10]), int(started_at[11:13]), int(started_at[14:16]), int(started_at[17:19])
                started_at = datetime(year, month, day, hour, minute, second)
                hours, minutes, seconds = convert_timedelta(datetime.now() - started_at)
                if not e['tags'] is None:
                    for t in range(len(e['tags'])):
                        new_tag = True
                        for w in range(len(whitelistedTags)):
                            if w == (len(whitelistedTags) - 1):
                                for p in range(len(nested_list(whitelistedTags, w))):
                                    for v in range(len(nested_list(whitelistedTags, w, p))):
                                        if p == (len(nested_list(whitelistedTags, w)) - 1):
                                            if e['tags'][t].lower() in (tag.lower() for tag in nested_list(whitelistedTags, w, p, v)):
                                                new_tag = False
                                        elif e['tags'][t][0].lower() == list_item(whitelistedTags, w, p)[0]:
                                            if e['tags'][t].lower() in (tag.lower() for tag in nested_list(whitelistedTags, w, p, v)):
                                                new_tag = False
                                        if not new_tag:
                                                break
                            else:
                                if e['tags'][t].lower() in (tag.lower() for tag in nested_list(whitelistedTags, w)):
                                    new_tag = False
                        if new_tag:
                            for b in range(len(blacklistedTags)):
                                if e['tags'][t].lower() in (tag.lower() for tag in nested_list(blacklistedTags, b)):
                                    new_tag = False
                        if new_tag:
                            for c in range(len(combined_tags)):
                                for v in range(len(nested_list(combined_tags, c))):
                                    if nested_list(combined_tags, c, v):
                                        if c == (len(combined_tags) - 1):
                                            if e['tags'][t].lower() in (tag.lower() for tag in nested_list(combined_tags, c, v)):
                                                new_tag = False
                                        elif e['tags'][t][0].lower() == list_item(combined_tags, c)[0]:
                                            if e['tags'][t].lower() in (tag.lower() for tag in nested_list(combined_tags, c, v)):
                                                new_tag = False
                                        if not new_tag:
                                            break
                        if new_tag:
                            otherTag = True
                            for m in range(len(combined_tags)):
                                if not m == (len(combined_tags) - 1):
                                    if e['tags'][t][0].lower() == combined_tags[m][0][0]:
                                        nested_list(combined_tags, m, (len(e['tags'][t]) - 1)).append(e['tags'][t])
                                        otherTag = False
                            if otherTag:
                                last_nested_list(combined_tags, 1, (len(e['tags'][t]) - 1)).append(e['tags'][t])
                if not hours > 18:
                    if not e['user_name'] in BLACKLISTED_STREAMS:
                        blacklisted = False
                        for b in range(len(blacklistedTags)):
                            if not e['tags'] is None:
                                for t in range(len(e['tags'])):
                                    if 'drop' in e['tags'][t].lower():
                                        if not e['game_id'] in dropsGames:
                                            dropsGames.append(e['game_id'])
                                    if e['tags'][t].lower() in (tag.lower() for tag in blacklistedTags[b][1]):
                                        if TESTING and e['game_name'].lower() == TEST_GAME.lower():
                                            print(e['game_name'] + ' stream has the blacklisted tag: ' + e['tags'][t])
                                        blacklisted = True
                                        break
                                if blacklisted:
                                    break
                        for b in range(len(BLACKLISTED_TITLES)):
                            if b == 0:
                                for t in range(len(BLACKLISTED_TITLES[b][1])):
                                    if re.search(BLACKLISTED_TITLES[b][1][t].lower(), e['title'].lower()):
                                        blacklisted = True
                                        break
                            elif e['game_name'] == BLACKLISTED_TITLES[b][0]:
                                for t in range(len(BLACKLISTED_TITLES[b][1])):
                                    if re.search(BLACKLISTED_TITLES[b][1][t].lower(), e['title'].lower()):
                                        if TESTING and e['game_name'].lower() == TEST_GAME.lower():
                                            print(e['game_name'] + ' stream has the blacklisted title segmment: "' +
                                                  BLACKLISTED_TITLES[b][1][t] + '" in the title: ' + e['title'])
                                        blacklisted = True
                                        break
                            if blacklisted:
                                break
                        for b in range(len(BLACKLISTED_PARTIAL_STREAMS)):
                            if b == 0:
                                if nested_list(BLACKLISTED_PARTIAL_STREAMS, b)[0]:
                                    for t in range(len(nested_list(BLACKLISTED_PARTIAL_STREAMS, b, 1))):
                                        if re.search('(' + list_item(BLACKLISTED_PARTIAL_STREAMS, b, t).lower() + ').*(' + second_list_item(BLACKLISTED_PARTIAL_STREAMS, b, t).lower() + ')', e['user_name'].lower()):
                                            blacklisted = True
                                            break
                            elif e['game_name'].lower() == list_item(BLACKLISTED_PARTIAL_STREAMS, b).lower():
                                for t in range(len(nested_list(BLACKLISTED_PARTIAL_STREAMS, b))):
                                    if re.search('(' + list_item(BLACKLISTED_PARTIAL_STREAMS, b, t).lower() + ').*(' +
                                                 second_list_item(BLACKLISTED_PARTIAL_STREAMS, b, t).lower() + ')',
                                                 e['user_name'].lower()):
                                        blacklisted = True
                                        break
                            if blacklisted:
                                break

                            gameViewers[i] = gameViewers[i] + int(e['viewer_count'])
                            medianList[i].append(int(e['viewer_count']))
                        if TESTING and e['game_name'].lower() == TEST_GAME.lower() and e['viewer_count'] > 4:
                            print(e['game_name'] + " streamer " + e['user_name'].lower() + " has " + str(
                                e['viewer_count']) + " viewers for a total of " + str(gameViewers[i]) + " viewers so far")
            get_more_streams(i)
    except Exception as x:
        print('Error in getting more streams')
        print(x)
        if TESTING:
            raise
    except requests.exceptions.ConnectTimeout:
        print("timeout", url_more)


def printData() -> None:
    global gameViewersLooped
    global gameStreamsLooped
    global gameViewerRatioLooped
    global hostGamesLooped
    global gameViewersMedianLooped
    global viewerRatioMedianRatioLooped
    global worthGames
    global gameViewersMedian
    global gameStreams
    global gameViewers
    global firstRun
    global topGameIdsLoopedPrinted
    global hostGamesLoopedPrinted
    global gameViewersLoopedPrinted
    global gameStreamsLoopedPrinted
    global gameViewerRatioLoopedPrinted
    global gameViewersMedianLoopedPrinted
    global viewerRatioMedianRatioLoopedPrinted
    global viewerRatioMedianRatioLoopedSorted
    global MINIMUM_STREAMS

    # if testing:
    #     print("Before math has been done")
    #     print(len(topGameNames), topGameNames)
    #     print(len(topGameIds), topGameIds)
    #     print(len(hostGamesLooped), hostGamesLooped)
    #     print(len(topGameIdsLooped), topGameIdsLooped)
    testExist = 0
    testNonExist = 0
    if TESTING:
        print("The top game names are: ")
        print(topGameNames)
    for i in range(len(topGameNames)):
        existingGame = False
        for h in range(len(hostGamesLooped)):
            if TESTING:
                if topGameNames[i] == 'Minecraft' and hostGamesLooped[h] == 'Minecraft':
                    print("Before adding")
                    print(gameViewers[i])
                    print(gameViewersLooped[h])
            if topGameNames[i] == hostGamesLooped[h]:
                gameViewersLooped[h] = gameViewersLooped[h] + gameViewers[i]
                if (gameViewersLooped[h] / loops) < MINIMUM_VIEWERS:
                    gameViewersLooped[h] = 0
                gameStreamsLooped[h] = gameStreamsLooped[h] + gameStreams[i]
                if (math.trunc(gameStreamsLooped[h]) / loops) < MINIMUM_STREAMS:
                    gameStreamsLooped[h] = 0
                if gameViewersLooped[h] == 0:
                    gameViewerRatioLooped[h] = 0
                elif gameStreamsLooped[h] == 0:
                    gameViewerRatioLooped[h] = 0
                else:
                    gameViewerRatioLooped[h] = gameViewersLooped[h] / gameStreamsLooped[h]
                if TESTING:
                    if topGameNames[i] == 'Minecraft' and hostGamesLooped[h] == 'Minecraft':
                        print("Medians are: ", gameViewersMedianLooped[h], gameViewersMedian[h])
                gameViewersMedianLooped[h] = gameViewersMedianLooped[h] + gameViewersMedian[i]
                if TESTING:
                    if topGameNames[i] == 'Minecraft' and hostGamesLooped[h] == 'Minecraft':
                        print("Ratio consists of: ", gameViewerRatioLooped[h], gameViewersMedianLooped[h])
                viewerRatioMedianRatioLooped[h] = gameViewerRatioLooped[h] * gameViewersMedianLooped[h]
                existingGame = True
                testExist = testExist + 1
        if not existingGame:
            gameViewersLooped.append(gameViewers[i])
            if (gameViewersLooped[-1] / loops) < MINIMUM_VIEWERS:
                gameViewersLooped[-1] = 0
            gameStreamsLooped.append(gameStreams[i])
            if (math.trunc(gameStreamsLooped[-1]) / loops) < MINIMUM_STREAMS:
                gameStreamsLooped[-1] = 0
            if gameViewersLooped[-1] == 0:
                gameViewerRatioLooped.append(0)
            elif gameStreamsLooped[-1] == 0:
                gameViewerRatioLooped.append(0)
            else:
                gameViewerRatioLooped.append(gameViewersLooped[-1] / gameStreamsLooped[-1])
            gameViewersMedianLooped.append(gameViewersMedian[i])
            viewerRatioMedianRatioLooped.append(gameViewerRatioLooped[-1] * gameViewersMedianLooped[-1])
            hostGamesLooped.append(topGameNames[i])
            testNonExist = testNonExist + 1
    if TESTING:
        print("After math has been done")
        print(testExist, testNonExist)
        print(len(topGameNames), topGameNames)
        print(len(topGameIds), topGameIds)
        print(len(hostGamesLooped), hostGamesLooped)
        print(len(topGameIdsLooped), topGameIdsLooped)

    dummy: list[int | float | str] = []
    topGameIdsLoopedPrinted = topGameIdsLooped[:]
    hostGamesLoopedPrinted = hostGamesLooped[:]
    gameViewersLoopedPrinted = gameViewersLooped[:]
    gameStreamsLoopedPrinted = gameStreamsLooped[:]
    gameViewerRatioLoopedPrinted = gameViewerRatioLooped[:]
    gameViewersMedianLoopedPrinted = gameViewersMedianLooped[:]
    viewerRatioMedianRatioLoopedPrinted = viewerRatioMedianRatioLooped[:]
    viewerRatioMedianRatioLoopedSorted = viewerRatioMedianRatioLooped[:]

    dummy[:], topGameIdsLoopedPrinted[:] = zip(
        *sorted(zip(viewerRatioMedianRatioLoopedPrinted, topGameIdsLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], hostGamesLoopedPrinted[:] = zip(
        *sorted(zip(viewerRatioMedianRatioLoopedPrinted, hostGamesLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameViewersLoopedPrinted[:] = zip(
        *sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameViewersLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameStreamsLoopedPrinted[:] = zip(
        *sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameStreamsLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameViewerRatioLoopedPrinted[:] = zip(
        *sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameViewerRatioLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameViewersMedianLoopedPrinted[:] = zip(
        *sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameViewersMedianLoopedPrinted), key=lambda p: (p[0], p[1])))
    viewerRatioMedianRatioLoopedSorted = sorted(viewerRatioMedianRatioLoopedSorted)


def print_strings() -> None:
    global firstRun
    global worthGames
    global latestGameFileName
    global gameViewersLooped
    global gameStreamsLooped
    global gameViewerRatioLooped
    global hostGamesLooped
    global gameViewersMedianLooped
    global viewerRatioMedianRatioLooped
    global hostGamesLoopedPrinted
    global gameViewersLoopedPrinted
    global gameStreamsLoopedPrinted
    global gameViewerRatioLoopedPrinted
    global gameViewersMedianLoopedPrinted
    global viewerRatioMedianRatioLoopedPrinted
    global viewerRatioMedianRatioLoopedSorted
    global new_games_ids
    global totalGames
    global totalViewers
    global totalStreams
    global totalViewerRatio
    global totalViewersMedian
    global totalViewerRatioMedianRatio
    time_of_day: str = ""
    special_days: list = [
        ["Newyears", 1, 1],
        ["Valentines-day", 2, 14],
        ["Christmas-day", 12, 25],
        ["Newyears", 12, 31]
    ]
    is_special_day: bool = False
    for special_day in range(len(special_days)):
        if int(datetime.today().strftime("%m")) == special_days[special_day][2] and int(
                datetime.today().strftime("%d")) == special_days[special_day][3]:
            is_special_day = True
            day_after_special_day: bool = False
            for dayBefore in range(len(special_days)):
                if int((datetime.now() - timedelta(1)).strftime("%m")) == special_days[dayBefore][2] and int(
                        (datetime.now() - timedelta(1)).strftime("%d")) == special_days[dayBefore][3] - 1:
                    day_after_special_day = True
                    if 0 <= int(datetime.now().strftime("%H")) < 2:
                        time_of_day = f"0200-0200_{special_days[dayBefore][0]}"
            if not day_after_special_day:
                time_of_day = "1600-0200"
            if 2 <= int(datetime.today().strftime("%H")) < 17:
                time_of_day = "0200-0200_" + special_days[special_day][0]
    if int(datetime.today().strftime("%m")) == 2 and int(datetime.today().strftime("%d")) == 15 and 0 <= int(
            datetime.now().strftime("%H")) < 2:
        if 0 <= int(datetime.today().strftime("%H")) < 2:
            time_of_day = "0200-0200_Valentines-day"
    if not is_special_day:
        if datetime.today().weekday() == 5:
            if 0 <= int(datetime.now().strftime("%H")) < 2:
                time_of_day = "1600-0200"
            else:
                time_of_day = "0200-0200_Saturday"
        elif datetime.today().weekday() == 6:
            if 0 <= int(datetime.now().strftime("%H")) < 2:
                time_of_day = "0200-0200_Saturday"
            elif 2 <= int(datetime.now().strftime("%H")) < 17:
                time_of_day = "0200-1700_Sunday"
            else:
                time_of_day = "1700-0000_Sunday"
        else:
            if 0 <= int(datetime.now().strftime("%H")) < 2:
                time_of_day = "1600-0200"
            elif 2 <= int(datetime.now().strftime("%H")) < 7:
                time_of_day = "0200-0700"
            elif 7 <= int(datetime.now().strftime("%H")) < 12:
                time_of_day = "0700-1200"
            elif 12 <= int(datetime.now().strftime("%H")) < 16:
                time_of_day = "1200-1600"
            else:
                time_of_day = "1600-0200"
    print("The time of day is ", time_of_day)
    latestGameFileName = f"{time_of_day}_latestGames.csv"
    recentGameFileName = "recent.csv"
    if not firstRun:
        # Read recent file if existing or make new one
        if not os.path.isfile(recentGameFileName):
            createRecentGamesFile = open(recentGameFileName, "x", encoding='utf-8')
            createRecentGamesFile.close()
        if not os.path.isfile(latestGameFileName):
            outputLatestGameLines = ["Game, Median, Average, " + str(int(time.time())) + "\n"]
        else:
            # Read latest file if existing or make new one
            readLatestGamesFile = open(latestGameFileName, "r", encoding='utf-8')
            outputLatestGameLines = readLatestGamesFile.readlines()
            readLatestGamesFile.close()
            # add new timestamp
            outputLatestGameLines[0] = outputLatestGameLines[0][:-1] + ", " + str(int(time.time())) + "\n"
            if datetime.now().weekday() == 0:
                removeDataOlderThan = 432000
            elif datetime.now().weekday() == 1:
                removeDataOlderThan = 345600
            elif datetime.now().weekday() == 5 or datetime.now().weekday() == 6:
                removeDataOlderThan = 777600
            else:
                removeDataOlderThan = 259200
            # if data older than 5 days scrap data
            gameLineTimestamps = outputLatestGameLines[0][:-1].split(",")
            oldTimeStamps = []
            for timestamp in range(len(gameLineTimestamps)):
                if timestamp > 2 and (int(time.time()) - int(gameLineTimestamps[timestamp])) > removeDataOlderThan:
                    oldTimeStamps.append(timestamp)
            if oldTimeStamps:
                for oldDataLine in range(len(outputLatestGameLines)):
                    gamelineVmRats = outputLatestGameLines[oldDataLine][:-1].split(",")
                    gamelineVmRatsTemp = []
                    for value in range(len(gamelineVmRats)):
                        if value not in oldTimeStamps:
                            gamelineVmRatsTemp.append(gamelineVmRats[value])
                    gamelineVmRats = gamelineVmRatsTemp
                    outputLatestGameLines[oldDataLine] = ",".join(gamelineVmRats) + "\n"
            # Add new data to each line or 0 if there is no new data
            outputLatestGameLinesTemp = [outputLatestGameLines[0]]
            for savedGameLine in range(len(outputLatestGameLines)):
                if savedGameLine > 0:
                    if TESTING:
                        print('Test 2: ' + outputLatestGameLines[savedGameLine])
                    outputLatestGameLines[savedGameLine] = outputLatestGameLines[savedGameLine][:-1] + ", 0\n"
                    if TESTING:
                        print('Test 3: ' + outputLatestGameLines[savedGameLine])
                    if not outputLatestGameLines[savedGameLine].split(",")[2] == ' 0':
                        outputLatestGameLinesTemp.append(outputLatestGameLines[savedGameLine])
            outputLatestGameLines = outputLatestGameLinesTemp
    viewAmount = len(hostGamesLooped)
    if TESTING:
        print(len(hostGamesLooped), hostGamesLooped)
        print(len(topGameIds), topGameIdsLooped)
    for i in range(len(combined_tags)):
        lengthTags = []
        for v in range(len(combined_tags[i][1])):
            if combined_tags[i][1][v][1]:
                for r in range(len(combined_tags[i][1][v][1])):
                    lengthTags.append(combined_tags[i][1][v][1][r])
        if TESTING:
            if lengthTags:
                print("New tags with " + list_item(combined_tags, i) + " are: " + ', '.join(str(x) for x in lengthTags))
    if TESTING:
        print(len(hostGamesLoopedPrinted), "The host game looped printed are: ")
        print(hostGamesLoopedPrinted)
        print(len(topGameIdsLooped), "The host game id looped printed are: ")
        print(topGameIdsLoopedPrinted)
    for i in range(viewAmount):
        if viewerRatioMedianRatioLoopedSorted[i - viewAmount] > 0:
            gameViewersLoopedAverage = int(gameViewersLoopedPrinted[i - viewAmount]) / loops
            gameStreamsLoopedAverage = int(gameStreamsLoopedPrinted[i - viewAmount]) / loops
            gameViewerRatioLoopedAverage = gameViewerRatioLoopedPrinted[i - viewAmount]
            gameViewersMedianLoopedAverage = gameViewersMedianLoopedPrinted[i - viewAmount] / loops
            if gameViewersMedianLoopedAverage == 0:
                viewerRatioMedianRatioLoopedAverage = 0.0
            else:
                viewerRatioMedianRatioLoopedAverage = viewerRatioMedianRatioLoopedSorted[i - viewAmount] / loops
            if viewerRatioMedianRatioLoopedAverage > 30 and gameViewersMedianLoopedAverage > 7:
                totalGames = totalGames + 1
                totalViewers = totalViewers + int(gameViewersLoopedAverage)
                totalStreams = totalStreams + int(gameStreamsLoopedAverage)
                totalViewerRatio = totalViewerRatio + gameViewerRatioLoopedAverage
                totalViewersMedian = totalViewersMedian + gameViewersMedianLoopedAverage
                totalViewerRatioMedianRatio = totalViewerRatioMedianRatio + viewerRatioMedianRatioLoopedAverage
            printString = (str(viewAmount - i) + ". " + hostGamesLoopedPrinted[i - viewAmount] + " has " +
                           str(round(gameViewersLoopedAverage)) + "v watching " +
                           str(round(gameStreamsLoopedAverage)) + "s with a vrat of: " +
                           str(round(gameViewerRatioLoopedAverage, 2)) + " and the s at " + str(
                        CASTER_PERCENTAGE) + "% of the cat has " +
                           str(round(gameViewersMedianLoopedAverage, 2)) + "v and a vmrat of: " +
                           str(round(viewerRatioMedianRatioLoopedAverage)))
            if hostGamesLoopedPrinted[i - viewAmount] == 'Minecraft' or hostGamesLoopedPrinted[
                i - viewAmount] == 'Satisfactory':
                if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                    print('\033[34m' + printString + '\033[0m')  # Blue
                elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                    print('\033[32m' + printString + '\033[0m')  # Green
                else:
                    print(printString)
                ## Save game values of the last two weeks
                if not firstRun:
                    commaAmount = outputLatestGameLines[0].count(",")
                    # Add games to lines
                    for gameLine in range(len(outputLatestGameLines)):
                        existingLatestGame = False
                        if hostGamesLoopedPrinted[i - viewAmount] == outputLatestGameLines[gameLine].split(",")[0]:
                            existingLatestGame = True
                            # replace 0 with value if the game is popular
                            outputLatestGameLines[gameLine] = outputLatestGameLines[gameLine][0:-4] + ", " + str(
                                round(viewerRatioMedianRatioLoopedAverage)) + "\n"
                            # if TESTING:
                                # print('Test 4: ' + outputLatestGameLines[gameLine])
                            break
                    if not existingLatestGame:
                        # Add 0s and the value if there is a new popular game
                        outputLatestGameLines.append(
                            hostGamesLoopedPrinted[i - viewAmount] + (commaAmount - 1) * ", 0" + ", " + str(
                                round(viewerRatioMedianRatioLoopedAverage)) + "\n")
            elif viewerRatioMedianRatioLoopedAverage > 0:
                printed = False
                favoriteGame = False
                wishlistedGame = False
                # Check if game id is a favorite
                for loopedCategory in range(len(FAVORITE_GAMES)):
                    if isinstance(second_list_item(FAVORITE_GAMES, loopedCategory, 0), str):
                        for loopedGame in range(len(nested_list(FAVORITE_GAMES, loopedCategory))):
                            if topGameIdsLoopedPrinted[i - viewAmount] == nested_list(FAVORITE_GAMES, loopedCategory, loopedGame):
                                if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                    print('\033[34m' + printString + '\033[0m')  # Blue
                                else:
                                    print('\033[32m' + printString + '\033[0m')  # Green
                                favoriteGame = True
                                break
                    else:
                        for loopedSubCategory in range(len(nested_list(FAVORITE_GAMES, loopedCategory))):
                            for loopedGame in range(len(nested_list(FAVORITE_GAMES, loopedCategory, loopedSubCategory))):
                                if topGameIdsLoopedPrinted[i - viewAmount] == nested_list(FAVORITE_GAMES, loopedCategory, loopedSubCategory, loopedGame):
                                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                        print('\033[34m' + printString + '\033[0m')  # Blue
                                    else:
                                        print('\033[32m' + printString + '\033[0m')  # Green
                                    favoriteGame = True
                                    break
                # Check if game id is on the wishlist
                if not favoriteGame:
                    for loopedCategory in range(len(WISHLISTED)):
                        if isinstance(second_list_item(WISHLISTED, loopedCategory, 0), str):
                            for loopedGame in range(len(nested_list(WISHLISTED, loopedCategory))):
                                if topGameIdsLoopedPrinted[i - viewAmount] == second_list_item(WISHLISTED, loopedCategory, loopedGame):
                                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                        print('\033[34m' + printString + '\033[0m')  # Blue
                                    else:
                                        print('\033[33m' + printString + '\033[0m')  # Yellow
                                    wishlistedGame = True
                                    break
                        else:
                            wishlistedGameBreaker = False
                            for loopedSubCategory in range(len(nested_list(WISHLISTED, loopedCategory))):
                                for loopedGame in range(len(nested_list(WISHLISTED, loopedCategory, loopedSubCategory))):
                                    if topGameIdsLoopedPrinted[i - viewAmount] == second_list_item(WISHLISTED, loopedCategory, loopedSubCategory, loopedGame)[1]:
                                        if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                            print('\033[34m' + printString + '\033[0m')  # Blue
                                        else:
                                            print('\033[33m' + printString + '\033[0m')  # Yellow
                                        wishlistedGame = True
                                        wishlistedGameBreaker = True
                                        break
                            if wishlistedGameBreaker:
                                break
                # Check if a game with this name is not already favorited or whitelisted under another id
                if not favoriteGame and not wishlistedGame:
                    newGameLooped = True
                    gamelistsLooped = [BLACKLIST, FAVORITE_GAMES, WISHLISTED]
                    for gamelistLooped in range(len(gamelistsLooped)):
                        for categoryLooped in range(len(gamelistsLooped[gamelistLooped])):
                            if isinstance(second_list_item(gamelistsLooped[gamelistLooped], categoryLooped, 0), str):
                                for gameLooped in range(len(nested_list(gamelistsLooped[gamelistLooped], categoryLooped))):
                                    if hostGamesLoopedPrinted[i - viewAmount].lower() == list_item(gamelistsLooped[gamelistLooped], categoryLooped, gameLooped).lower():
                                        newGameLooped = False
                                        break
                            else:
                                for subCategoryLooped in range(len(nested_list(gamelistsLooped[gamelistLooped], categoryLooped))):
                                    for gameLooped in range(len(nested_list(gamelistsLooped[gamelistLooped], categoryLooped, subCategoryLooped))):
                                        if hostGamesLoopedPrinted[i - viewAmount].lower() == list_item(gamelistsLooped[gamelistLooped], categoryLooped, subCategoryLooped, gameLooped).lower():
                                            newGameLooped = False
                                            break
                    print(printString)
                    if newGameLooped:
                        addedGameLooped = False
                        for addedNewGamesLooped in range(len(new_games_ids)):
                            if hostGamesLoopedPrinted[i - viewAmount].lower() == list_item(new_games_ids, addedNewGamesLooped).lower():
                                addedGameLooped = True
                                break
                        if not addedGameLooped:
                            new_games_ids.append(
                                [hostGamesLoopedPrinted[i - viewAmount], topGameIdsLoopedPrinted[i - viewAmount]])
                # Save game values of the last two weeks
                if not firstRun:
                    commaAmount = outputLatestGameLines[0].count(",")
                    # Add games to lines
                    for gameLine in range(len(outputLatestGameLines)):
                        existingLatestGame = False
                        if hostGamesLoopedPrinted[i - viewAmount] == outputLatestGameLines[gameLine].split(",")[0]:
                            existingLatestGame = True
                            # replace 0 with value if the game is popular
                            outputLatestGameLines[gameLine] = outputLatestGameLines[gameLine][0:-4] + ", " + str(
                                round(viewerRatioMedianRatioLoopedAverage)) + "\n"
                            if TESTING:
                                print('Test 4: ' + outputLatestGameLines[gameLine])
                            break
                    if not existingLatestGame:
                        # Add 0s and the value if there is a new popular game
                        outputLatestGameLines.append(hostGamesLoopedPrinted[i - viewAmount] + (commaAmount - 1) * ", 0" + ", " + str(
                                round(viewerRatioMedianRatioLoopedAverage)) + "\n")
    # Add in the median of all viewer median ratios
    if not firstRun:
        mVmRats = []
        avgVmRats = []
        for gameLine in range(len(outputLatestGameLines)):
            if gameLine > 0:
                if TESTING:
                    print(outputLatestGameLines[gameLine])
                gameVmRats = outputLatestGameLines[gameLine].split(",")[3:]
                game_vmrats_int: list[int] = []
                for VmRatStored in range(len(gameVmRats)):
                    game_vmrats_int.append(int(gameVmRats[VmRatStored]))
                mVmRatStored = statistics.median(game_vmrats_int)
                mVmRats.append(mVmRatStored)
                avgGameVmRatStored = round(sum(game_vmrats_int) / len(game_vmrats_int))
                avgVmRats.append(mVmRatStored)
                outputLatestGameLines[gameLine] = outputLatestGameLines[gameLine].split(",")[0] + ", " + str(
                    mVmRatStored) + ", " + str(avgGameVmRatStored) + "," + ','.join(
                    outputLatestGameLines[gameLine].split(",")[3:])

        # Sort lines by average
        outputGamesHeader = outputLatestGameLines[0]
        outputLatestGameLines.pop(0)
        outputLatestGameLinesSorted = outputLatestGameLines[:]
        mVmRats[:], outputLatestGameLinesSorted[:] = (list(x) for x in
                                                      zip(*sorted(zip(mVmRats, outputLatestGameLinesSorted),
                                                                  key=lambda pair: pair[0])))
        outputLatestGameLinesReversed = outputLatestGameLinesSorted[:]
        outputLatestGameLinesReversed.reverse()
        latestGameLineTemp = []
        latestGameLineTemp.append(outputGamesHeader)
        for latestGameLine in range(len(outputLatestGameLinesReversed)):
            latestGameLineTemp.append(outputLatestGameLinesReversed[latestGameLine])
        outputLatestGameLines = latestGameLineTemp

    # Write back to file
    if not firstRun:
        latestGamesFile = open("tmpfile.csv", "w", encoding='utf-8')
        for latestGameLine in range(len(outputLatestGameLines)):
            latestGamesFile.writelines(outputLatestGameLines[latestGameLine])
        latestGamesFile.close()
        os.replace('tmpfile.csv', latestGameFileName)
        recentGamesFile = open("tmpfile.csv", "w", encoding='utf-8')
        for recentGameLine in range(len(outputLatestGameLines)):
            recentGamesFile.writelines(outputLatestGameLines[recentGameLine])
        recentGamesFile.close()
        os.replace('tmpfile.csv', recentGameFileName)

    print("Favorite games:")
    for i in range(viewAmount):
        gameViewersLoopedAverage = int(gameViewersLoopedPrinted[i - viewAmount]) / loops
        gameStreamsLoopedAverage = int(gameStreamsLoopedPrinted[i - viewAmount]) / loops
        gameViewerRatioLoopedAverage = gameViewerRatioLoopedPrinted[i - viewAmount]
        gameViewersMedianLoopedAverage = gameViewersMedianLoopedPrinted[i - viewAmount] / loops
        if gameViewersMedianLoopedAverage == 0:
            viewerRatioMedianRatioLoopedAverage = 0
        else:
            viewerRatioMedianRatioLoopedAverage = viewerRatioMedianRatioLoopedSorted[i - viewAmount] / loops
        printString = (
                str(viewAmount - i) + ". " + hostGamesLoopedPrinted[i - viewAmount] + " has " +
                str(round(gameViewersLoopedAverage)) + "v watching " +
                str(round(gameStreamsLoopedAverage)) + "s with a vrat of: " +
                str(round(gameViewerRatioLoopedAverage, 2)) + " and the s at " + str(
            CASTER_PERCENTAGE) + "% of the cat has " +
                str(round(gameViewersMedianLoopedAverage, 2)) + "v and a vmrat of: " +
                str(round(viewerRatioMedianRatioLoopedAverage))
        )
        if hostGamesLoopedPrinted[i - viewAmount] == 'Minecraft' or hostGamesLoopedPrinted[
            i - viewAmount] == 'Satisfactory':
            if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                print('\033[34m' + printString + '\033[0m')
            elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                print('\033[32m' + printString + '\033[0m')
            else:
                print(printString)
        elif viewerRatioMedianRatioLoopedAverage > 0:
            # Check if game is favorite
            for category in range(len(FAVORITE_GAMES)):
                if isinstance(second_list_item(FAVORITE_GAMES, category, 0), str):
                    for game in range(len(nested_list(FAVORITE_GAMES, category))):
                        if topGameIdsLoopedPrinted[i - viewAmount] == second_list_item(FAVORITE_GAMES, category, game):
                            if viewerRatioMedianRatioLoopedAverage >= 1000:
                                print('\033[34m' + printString + '\033[0m')
                            elif 1000 > viewerRatioMedianRatioLoopedAverage > 100:
                                print('\033[32m' + printString + '\033[0m')
                            else:
                                print(printString)
                            break
                else:
                    favoriteGameBreaker = False
                    for subCategory in range(len(nested_list(FAVORITE_GAMES, category))):
                        for game in range(len(nested_list(FAVORITE_GAMES, category, subCategory))):
                            if topGameIdsLoopedPrinted[i - viewAmount] == second_list_item(FAVORITE_GAMES, category, subCategory, game):
                                if viewerRatioMedianRatioLoopedAverage >= 1000:
                                    print('\033[34m' + printString + '\033[0m')
                                elif 1000 > viewerRatioMedianRatioLoopedAverage > 100:
                                    print('\033[32m' + printString + '\033[0m')
                                else:
                                    print(printString)
                                favoriteGameBreaker = True
                                break
                    if favoriteGameBreaker:
                        break
            # Check if game is on the wishlist
            for category in range(len(WISHLISTED)):
                if isinstance(second_list_item(WISHLISTED, category, 0), str):
                    for game in range(len(nested_list(WISHLISTED, category))):
                        if topGameIdsLoopedPrinted[i - viewAmount] == second_list_item(WISHLISTED, category, game) and viewerRatioMedianRatioLoopedAverage > 100:
                            print('\033[33m' + printString + '\033[0m')  # Yellow
                            break
                else:
                    wishlistedGameBreaker = False
                    for subCategory in range(len(nested_list(WISHLISTED, category))):
                        for game in range(len(nested_list(WISHLISTED, category, subCategory))):
                            if topGameIdsLoopedPrinted[i - viewAmount] == second_list_item(WISHLISTED, category, subCategory, game) and viewerRatioMedianRatioLoopedAverage > 100:
                                print('\033[33m' + printString + '\033[0m')  # Yellow
                                wishlistedGameBreaker = True
                                break
                    if wishlistedGameBreaker:
                        break
    if totalGames > 0:
        print(str(totalGames) + 'g have ' + str(totalViewers) + 'v watching ' + str(
            totalStreams) + 's with an avgvrat of: ' + str(
            round(totalViewerRatio / totalGames, 2)) + ", the s at " + str(
            CASTER_PERCENTAGE) + "% of the cat has an avg of " + str(
            round(totalViewersMedian / totalGames)) + "v and an avgvmrat of: " + str(
            round(totalViewerRatioMedianRatio / totalGames)))
    if new_games_ids:
        newGamesReversed = []
        for game in range(len(new_games_ids[::-1])):
            newGamesReversed.append(new_games_ids[game][0])
        if len(newGamesReversed) == 1:
            print("The newest game is: " + newGamesReversed[0])
        else:
            print("The new games are:")
            print_every_ten(newGamesReversed)

    hostGamesLoopedPrintedReversed = hostGamesLoopedPrinted[:]
    hostGamesLoopedPrintedReversed.reverse()
    # Write games to a txt file
    f = open("tmpfile.py", "w", encoding='utf-8')
    f.writelines("# !/usr/bin/env python")
    f.writelines("\n# -*- coding: utf-8 -*-")
    f.writelines("\n# output.py")
    f.writelines("\nhost_games: list[str] = " + str(hostGamesLoopedPrintedReversed))
    f.writelines("\nnew_games_ids: list[list[str, str]] = " + str(new_games_ids))
    f.writelines("\ncombined_tags = [\n")
    for l in range(len(combined_tags)):
        f.writelines("    ['" + list_item(combined_tags, l) + "', [\n")
        for v in range(len(nested_list(combined_tags, l))):
            f.writelines("        ['" + list_item(combined_tags, l, v) + "', [")
            if combined_tags[l][1][v][1]:
                f.writelines("'" + "', '".join(nested_list(combined_tags, l, v)) + "']],\n")
            else:
                f.writelines("]],\n")
        f.writelines("    ]], \n")
    f.writelines("]")
    f.writelines("\n")
    f.close()
    os.replace('tmpfile.py', 'output.py')


def convert_timedelta(duration: timedelta) -> tuple[int, int, int]:
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


# Print new blacklist additions
if not new_games_ids == []:
    if TESTING:
        blacklistedGameAmount = 0
        favoriteGameAmount = 0
        wishlistedGameAmount = 0
        for blacklist_category in range(len(BLACKLIST)):
            if isinstance(second_list_item(BLACKLIST, blacklist_category, 0), str):
                blacklistedGameAmount = blacklistedGameAmount + len(nested_list(BLACKLIST, blacklist_category))
            else:
                for favorite_category in range(len(nested_list(BLACKLIST, blacklist_category))):
                    blacklistedGameAmount = blacklistedGameAmount + len(nested_list(BLACKLIST, blacklist_category, favorite_category))
        for favorite_game_category in range(len(FAVORITE_GAMES)):
            if isinstance(second_list_item(FAVORITE_GAMES, favorite_game_category, 0), str):
                favoriteGameAmount = favoriteGameAmount + len(nested_list(FAVORITE_GAMES, favorite_game_category))
            else:
                for favorite_category in range(len(nested_list(FAVORITE_GAMES, favorite_game_category))):
                    favoriteGameAmount = favoriteGameAmount + len(nested_list(FAVORITE_GAMES, favorite_game_category, favorite_category))
        for wishlist_category in range(len(WISHLISTED)):
            if isinstance(second_list_item(WISHLISTED, wishlist_category, 0), str):
                wishlistedGameAmount = wishlistedGameAmount + len(nested_list(WISHLISTED, wishlist_category))
            else:
                for favorite_category in range(len(nested_list(WISHLISTED, wishlist_category))):
                    wishlistedGameAmount = wishlistedGameAmount + len(nested_list(WISHLISTED, wishlist_category, favorite_category))
        print("Getting blacklist game ids. " + str(blacklistedGameAmount) + " games blacklisted, " + str(
            favoriteGameAmount) + " favorite games and " + str(
            wishlistedGameAmount) + " games wishlisted for a total of " + str(
            blacklistedGameAmount + favoriteGameAmount + wishlistedGameAmount) + " games analyzed")
    if new_games_ids:
        lastRun = False
        for game in range(len(new_games_ids)):
            if len(new_games_ids) == 1:
                print("The newest game is:", new_games_ids[0][0])
            elif game == 0:
                print("1 - 5", new_games_ids[0:5])
            elif game % 5 == 0:
                if len(new_games_ids) < game + 5:
                    print(str(game) + " - " + str(len(new_games_ids)), new_games_ids[game:])
                else:
                    print(str(game) + " - " + str(game + 5), new_games_ids[game:game + 5])
            encodedGameName = new_games_ids[game][0].replace(" ", "%20").replace("'", "%27").replace(".",
                                                                                                     "%2E").replace("!",
                                                                                                                    "%21")
            print("https://www.twitch.tv/directory/game/" + encodedGameName)
    else:
        if TESTING:
            print("No new blacklist additions")
            url = "https://api.twitch.tv/helix/games?name=" + TEST_GAME
            params = {"Client-ID": "" + CLIENT_ID + "", "Authorization": "Bearer " + FOLLOWER_TOKEN}
            test_game_response = requests.get(url, headers=params)
            if test_game_response.status_code == 200:
                pass
            elif test_game_response.status_code == 400:
                print("Bad request")
            elif test_game_response.status_code == 429:
                print("Too many testname requests")
            test_game_response_json = test_game_response.json()
            print("Typical game data is: " + str(test_game_response_json))
while True:
    try:
        gameViewers: list[int] = []
        gameStreams: list[int] = []
        medianList: list = []
        gameViewersMedian: list = []
        topGameNames: list = []
        topGameIds: list = []
        topGameViewers: int = 0
        stopGettingGames: int = 0
        pagination: str = ""
        paginationTopGames: str = ""
        totalGames: int = 0
        totalViewers: int = 0
        totalStreams: int = 0
        totalViewerRatio: float = 0.0
        totalViewersMedian: float = 0.0
        totalViewerRatioMedianRatio: float = 0.0

        # Establish givens
        from output import *

        print("Getting streamed games")
        if loops == 0:
            loopStart = datetime.now()
        get_more_games()
        if TESTING:
            print("Streamed games have been gotten")
            print("The top game names are: ", topGameNames)

        # Extract id from blacklist
        blacklistIds = []
        for i in range(len(BLACKLIST)):
            if isinstance(second_list_item(BLACKLIST, i, 0), str):
                for a in range(len(nested_list(BLACKLIST, i))):
                    blacklistIds.append(nested_list(BLACKLIST, i, a))
            else:
                for favorite_category in range(len(nested_list(BLACKLIST, i))):
                    for a in range(len(nested_list(BLACKLIST, i, favorite_category))):
                        blacklistIds.append(nested_list(BLACKLIST, i, favorite_category, a))

        # Remove blacklisted games
        topGameIdsTemp = []
        topGameNamesTemp = []
        for i in range(len(topGameIds)):
            if not topGameIds[i] in blacklistIds:
                topGameIdsTemp.append(topGameIds[i])
                topGameNamesTemp.append(topGameNames[i])
        topGameIds = topGameIdsTemp
        topGameNames = topGameNamesTemp

        if not combined_tags:
            combined_tags = [
                ['a',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['b',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['c',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['d',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['e',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['f',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['g',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['h',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['i',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['j',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['k',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['l',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['m',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['n',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['o',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['p',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['q',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['r',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['s',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['t',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['u',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['v',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['w',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['x',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['y',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['z',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['1',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['2',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['3',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['4',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['5',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['6',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['7',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['8',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['9',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['0',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['Other',
                 [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []],
                  ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []],
                  ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]]
            ]

        # Add games that were not included
        if loops > 0:
            if TESTING:
                print("The new top game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
                print("The old top game names are: " + str(len(hostGamesLooped)) + " " + str(hostGamesLooped))
                print("The new top game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
                print("The old top game ids are: " + str(len(topGameIdsLooped)) + " " + str(topGameIdsLooped))
            for i in range(len(topGameIdsLooped)):
                existingGame = False
                for t in range(len(topGameIds)):
                    if topGameIdsLooped[i] == topGameIds[t]:
                        existingGame = True
                if not existingGame:
                    topGameIds.append(topGameIdsLooped[i])
                    topGameNames.append(hostGamesLooped[i])

        if TESTING:
            print("The added game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
            print("The added game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
        try:
            for i in range(len(topGameIds)):
                url = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[
                    i]
                params = {"Client-ID": "" + CLIENT_ID + "", "Authorization": "Bearer " + FOLLOWER_TOKEN}
                gameid_response: requests.models.Response = requests.get(url, headers=params)
                if gameid_response.status_code == 200:
                    pass
                elif gameid_response.status_code == 400:
                    print("Bad request")
                elif gameid_response.status_code == 429:
                    print("Too many gameid requests")
                gameid_response_json = gameid_response.json()
                # if testing and gameid_response_json['data'][0]['game_name'].lower() == testGame.lower():
                #     print(topGameIds[i])
                #     print(gameid_response_json)
                gameStreams.append(0)
                gameViewers.append(0)
                medianList.append([])
                if TESTING:
                    if i == 0:
                        print('Getting info for games')
                    if topGameNames[i].lower() == TEST_GAME.lower():
                        print("Getting info for " + TEST_GAME)
                if gameid_response_json['pagination'] == {}:
                    pass
                else:
                    # if testing:
                    # print('Getting first streams')
                    # print(gameid_response_json)
                    gameStreams[i] = gameStreams[i] + len(gameid_response_json['data'])
                    testingTags: list[str] = []
                    for e in gameid_response_json['data']:
                        # Print streams in testgame
                        # print('Getting first stream')
                        started_at = e['started_at']
                        year, month, day, hour, minute, second = int(started_at[0:4]), int(started_at[5:7]), int(started_at[8:10]), int(started_at[11:13]), int(started_at[14:16]), int(started_at[17:19])
                        started_at_datetime = datetime(year, month, day, hour, minute, second)
                        hours, minutes, seconds = convert_timedelta(datetime.now() - started_at_datetime)
                        if not hours > 18:
                            if not e['user_name'] in BLACKLISTED_STREAMS:
                                blacklisted = False
                                for blacklist_category in range(len(blacklistedTags)):
                                    if not e['tags'] is None:
                                        for t in range(len(e['tags'])):
                                            if 'drop' in e['tags'][t].lower():
                                                if not e['game_id'] in dropsGames:
                                                    dropsGames.append(e['game_id'])
                                            if e['tags'][t].lower() in (tag.lower() for tag in blacklistedTags[blacklist_category][1]):
                                                if TESTING and e['game_name'].lower() == TEST_GAME.lower():
                                                    print(e['game_name'] + ' stream has the blacklisted tag: ' +
                                                          e['tags'][t])
                                                blacklisted = True
                                                break
                                            # Check what tags the test game has
                                            if TESTING and e['game_name'].lower() == TEST_GAME.lower():
                                                whitelistedTag = False
                                                for c in range(len(whitelistedTags[0:-2])):
                                                    if e['tags'][t].lower() in (tag.lower() for tag in nested_list(whitelistedTags, c)):
                                                        whitelistedTag = True
                                                        break
                                                if not whitelistedTag:
                                                    existingTag = False
                                                    for testing_tag in range(len(testingTags)):
                                                        if e['tags'][t].lower() == testingTags[testing_tag].lower():
                                                            existingTag = True
                                                            break
                                                    if not existingTag:
                                                        testingTags.append(e['tags'][t])
                                # Check what title the game has
                                for blacklist_category in range(len(BLACKLISTED_TITLES)):
                                    if blacklist_category == 0:
                                        for t in range(len(BLACKLISTED_TITLES[blacklist_category][1])):
                                            if re.search(BLACKLISTED_TITLES[blacklist_category][1][t].lower(), e['title'].lower()):
                                                if TESTING and e['game_name'].lower() == TEST_GAME.lower():
                                                    print(e[
                                                              'game_name'] + ' stream has the blacklisted title segment: "' +
                                                          BLACKLISTED_TITLES[blacklist_category][1][t] + '" in the title: ' + e['title'])
                                                blacklisted = True
                                                break
                                    elif e['game_name'] == BLACKLISTED_TITLES[blacklist_category][0]:
                                        for t in range(len(BLACKLISTED_TITLES[blacklist_category][1])):
                                            if re.search(BLACKLISTED_TITLES[blacklist_category][1][t].lower(), e['title'].lower()):
                                                if TESTING and e['game_name'].lower() == TEST_GAME.lower():
                                                    print(e[
                                                              'game_name'] + ' stream has the blacklisted title segment: "' +
                                                          BLACKLISTED_TITLES[blacklist_category][1][t] + '" in the title: ' + e['title'])
                                                blacklisted = True
                                                break
                                for blacklist_category in range(len(BLACKLISTED_PARTIAL_STREAMS)):
                                    if blacklist_category == 0:
                                        if nested_list(BLACKLISTED_PARTIAL_STREAMS, blacklist_category)[0]:
                                            for t in range(len(nested_list(BLACKLISTED_PARTIAL_STREAMS, blacklist_category))):
                                                if re.search('(' + list_item(BLACKLISTED_PARTIAL_STREAMS, blacklist_category, t).lower() + ').*(' + second_list_item(BLACKLISTED_PARTIAL_STREAMS, blacklist_category, t).lower() + ')', e['user_name'].lower()):
                                                    blacklisted = True
                                                    break
                                    elif e['game_name'].lower() == list_item(BLACKLISTED_PARTIAL_STREAMS, blacklist_category).lower():
                                        for t in range(len(nested_list(BLACKLISTED_PARTIAL_STREAMS, blacklist_category))):
                                            if len(nested_list(BLACKLISTED_PARTIAL_STREAMS, blacklist_category)[t]) == 1:
                                                if list_item(BLACKLISTED_PARTIAL_STREAMS, blacklist_category, t).lower() == e['user_name'].lower():
                                                    if TESTING:
                                                        if topGameNames[i].lower() == TEST_GAME.lower():
                                                            print(e['user_name'])
                                                    blacklisted = True
                                                    break
                                            elif re.search(
                                                    '(' + list_item(BLACKLISTED_PARTIAL_STREAMS, blacklist_category, t).lower() + ').*(' +
                                                    second_list_item(BLACKLISTED_PARTIAL_STREAMS, blacklist_category, t).lower() + ')',
                                                    e['user_name'].lower()):
                                                if TESTING:
                                                    if topGameNames[i] == 'Tibia':
                                                        print(e['user_name'])
                                                blacklisted = True
                                                break
                                if not blacklisted:
                                    gameViewers[i] = gameViewers[i] + int(e['viewer_count'])
                                    medianList[i].append(int(e['viewer_count']))
                                    if TESTING and e['game_name'].lower() == TEST_GAME.lower() and e[
                                        'viewer_count'] > 4:
                                        if e['tags']:
                                            print(e['game_name'] + " streamer " + e['user_name'] + " has " + str(
                                                e['viewer_count']) + " viewers with the title " + e[
                                                      'title'] + " and the tags " + ", ".join(e['tags']))
                                        else:
                                            print(e['game_name'] + " streamer " + e['user_name'] + " has " + str(
                                                e['viewer_count']) + " viewers with the title " + e[
                                                      'title'] + " and no tags")
                    if gameid_response_json['data']:
                        if TESTING and gameid_response_json['data'][0]['game_name'].lower() == TEST_GAME.lower():
                            if testingTags:
                                print("Tags for " + TEST_GAME + " are:", testingTags)
                            else:
                                print("No new tags for " + TEST_GAME)
                    pagination = gameid_response_json['pagination']['cursor']
                    get_more_streams(i)
                if TESTING and topGameNames[i].lower() == TEST_GAME.lower():
                    print("Info for " + TEST_GAME + " has been gotten")
                # If all viewers are in top 90% set views to 0
                for favorite_game in range(len(medianList[i])):
                    if int(medianList[i][favorite_game]) > (gameViewers[i] * (TOP_STREAMER_PERCENTAGE / 100)):
                        gameViewers[i] = 0
                if math.trunc(int(gameStreams[i])) < MINIMUM_STREAMS:
                    gameViewersMedian.append(0)
                else:
                    casterPercentile = (
                            len(medianList[i]) - (math.trunc(len(medianList[i]) * (CASTER_PERCENTAGE / 100))))
                    if math.trunc(len(medianList[i])) < MINIMUM_STREAMS:
                        median = 0
                    else:
                        median = medianList[i][casterPercentile]
                    gameViewersMedian.append(median)
                if firstRun:
                    if (i + 1) == len(topGameIds):
                        print("\r" + str(len(topGameIds)) + " of " + str(len(topGameIds)), flush=True)
                    elif i <= 4:
                        print(str(i + 1) + " of " + str(len(topGameIds)) + ' - ' + topGameNames[i])
                    elif i == 9:
                        print(str(i + 1) + " of " + str(len(topGameIds)) + ' - ' + ', '.join(
                            [topGameNames[5], topGameNames[6], topGameNames[7], topGameNames[8], topGameNames[9]]))
                    elif i == 19 or i == 29 or i == 39 or i == 49:
                        print(str(i + 1) + " of " + str(len(topGameIds)) + ' - ' + ', '.join(
                            [topGameNames[i - 9], topGameNames[i - 8], topGameNames[i - 7], topGameNames[i - 6],
                             topGameNames[i - 5], topGameNames[i - 4], topGameNames[i - 3], topGameNames[i - 2],
                             topGameNames[i - 1], topGameNames[i]]))
                    elif i % 50 == 0 and not i == 50:
                        print("\r" + str(i) + " of " + str(len(topGameIds)), end="", flush=True)
                else:
                    if len(topGameIds) < 200:
                        if (i + 1) == len(topGameIds):
                            print("\r" + str(len(topGameIds)) + " of " + str(len(topGameIds)), flush=True)
                        elif i % 50 == 0:
                            print("\r" + str(i) + " of " + str(len(topGameIds)), end="", flush=True)
                    else:
                        if (i + 1) == len(topGameIds):
                            print("\r" + str(len(topGameIds)) + " of " + str(len(topGameIds)), flush=True)
                        elif i % 100 == 0:
                            print("\r" + str(i) + " of " + str(len(topGameIds)), end="", flush=True)
        except Exception as e:
            print(e)
            if TESTING:
                raise
                print(gameid_response_json)
    except Exception as x:
        print(x)
        if TESTING:
            raise
    except requests.exceptions.ConnectTimeout:
        print("timeout", url)
    except KeyboardInterrupt:
        print('Keyboard interrupt exception is caught')

    if TESTING:
        print("Before drop removal")
        print(len(topGameNames), topGameNames)
        print(len(gameViewers), gameViewers)
        print(len(topGameIds), topGameIds)
        for favorite_category in range(len(topGameIds)):
            if topGameNames[favorite_category] == 'Minecraft':
                print(topGameNames[favorite_category] + " has: " + str(gameViewers[favorite_category]) + " viewers")
            if topGameNames[favorite_category].lower() == TEST_GAME.lower():
                print(topGameNames[favorite_category] + " has: " + str(gameViewers[favorite_category]) + " viewers")

    # remove games with drops
    topGameIdsTemp = []
    topGameNamesTemp = []
    gameViewersTemp = []
    gameStreamsTemp = []
    if TESTING:
        print(len(topGameIds))
        print(len(topGameIds))
    for i in range(len(topGameIds)):
        if not topGameIds[i] in dropsGames:
            topGameIdsTemp.append(topGameIds[i])
            topGameNamesTemp.append(topGameNames[i])
            gameViewersTemp.append(gameViewers[i])
            gameStreamsTemp.append(gameStreams[i])
    topGameIds = topGameIdsTemp
    topGameNames = topGameNamesTemp
    gameViewers = gameViewersTemp
    gameStreams = gameStreamsTemp

    if TESTING:
        print("After drop removal")
        print(len(topGameNames), topGameNames)
        print(len(gameViewers), gameViewers)
        print(len(gameViewers), gameViewers)
        print(len(topGameIds), topGameIds)
        if TESTING:
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
                if topGameNames[i].lower() == TEST_GAME.lower():
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")

    for i in range(len(topGameIds)):
        if gameViewers[i] < MINIMUM_VIEWERS:
            gameViewers[i] = 0
        if math.trunc(int(gameStreams[i])) < MINIMUM_STREAMS:
            gameStreams[i] = 0

    # Calculate viewer ratio
    gameViewerRatio = []
    for i in range(len(topGameIds)):
        if gameViewers[i] == 0:
            gameViewerRatio.append(0.0)
        elif gameStreams[i] == 0:
            gameViewerRatio.append(0.0)
        else:
            if gameViewers[i] / gameStreams[i] == 1:
                gameViewerRatio.append(0.0)
            else:
                gameViewerRatio.append(gameViewers[i] / gameStreams[i])

    # calculate viewermedianratio
    viewerRatioMedianRatio = []
    for i in range(len(topGameIds)):
        viewerRatioMedianRatio.append(gameViewerRatio[i] * gameViewersMedian[i])

    viewAmount = len(topGameIds)
    loopAmount = 5
    loops = loops + 1

    # Calculate if the loop should be reset after this
    hours, minutes, seconds = convert_timedelta(datetime.now() - loopStart)
    restartLoops = False
    if minutes >= LOOP_LENGTH:
        restartLoops = True
    if loops == 1:

        # Transfer variables to other variables for use in next loop
        hostGamesLooped = topGameNames[:]
        topGameIdsLooped = topGameIds[:]
        gameViewersLooped = gameViewers[:]
        gameStreamsLooped = gameStreams[:]
        gameViewerRatioLooped = gameViewerRatio[:]
        gameViewersMedianLooped = gameViewersMedian[:]
        viewerRatioMedianRatioLooped = viewerRatioMedianRatio[:]
        viewerRatioMedianRatioSorted = viewerRatioMedianRatio[:]

        if TESTING:
            print("Before sorting")
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
                if topGameNames[i].lower() == TEST_GAME.lower():
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")

        # if testing:
        #     print(topGameNames)
        #     print(gameViewers)
        #     print(gameStreams)

        # Sort by all lists by viewerRatioMedianRatio
        dummy: list[int | float | str] = []
        dummy[:], topGameNames[:] = zip(*sorted(zip(viewerRatioMedianRatio, topGameNames), key=lambda p: (p[0], p[1])))
        dummy[:], topGameIds[:] = zip(*sorted(zip(viewerRatioMedianRatio, topGameIds), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewers[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameViewers), key=lambda p: (p[0], p[1])))
        dummy[:], gameStreams[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameStreams), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewerRatio[:] = zip(
            *sorted(zip(viewerRatioMedianRatio, gameViewerRatio), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewersMedian[:] = zip(
            *sorted(zip(viewerRatioMedianRatio, gameViewersMedian), key=lambda p: (p[0], p[1])))
        viewerRatioMedianRatioSorted[:] = sorted(viewerRatioMedianRatioSorted)
        # if testing:
        #     print(topGameNames)
        #     print(gameViewers)
        #     print(gameStreams)
        #     print(viewerRatioMedianRatio)

        if TESTING:
            print("After sorting")
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
                if topGameNames[i].lower() == TEST_GAME.lower():
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
            print("The top game ids are: " + str(topGameIds))
            print("The top game names are: " + str(topGameNames))

        if firstRun:
            for i in range(len(combined_tags)):
                lengthTags = []
                for v in range(len(combined_tags[i][1])):
                    if combined_tags[i][1][v][1]:
                        for r in range(len(combined_tags[i][1][v][1])):
                            lengthTags.append(combined_tags[i][1][v][1][r])
                if TESTING:
                    if lengthTags:
                        print("New tags with " + list_item(combined_tags, i) + " are: " + ', '.join(str(x) for x in lengthTags))
            for i in range(viewAmount):
                if viewerRatioMedianRatioSorted[i - viewAmount] > 0:
                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) > 30 and gameViewersMedian[i - viewAmount] > 7:
                        totalGames = totalGames + 1
                        totalViewers = totalViewers + gameViewers[i - viewAmount]
                        totalStreams = totalStreams + gameStreams[i - viewAmount]
                        totalViewerRatio = totalViewerRatio + gameViewerRatio[i - viewAmount]
                        totalViewersMedian = totalViewersMedian + gameViewersMedian[i - viewAmount]
                        totalViewerRatioMedianRatio = totalViewerRatioMedianRatio + viewerRatioMedianRatioSorted[
                            i - viewAmount]
                    printString = (str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                                   str(round(gameViewers[i - viewAmount])) + "v watching " +
                                   str(round(gameStreams[i - viewAmount])) + "s with a vrat of: " +
                                   str(round(gameViewerRatio[i - viewAmount], 2)) + " and the s at " + str(
                                CASTER_PERCENTAGE) + "% of the cat has " +
                                   str(round(gameViewersMedian[i - viewAmount], 2)) + "v and a vmrat of: " +
                                   str(round(viewerRatioMedianRatioSorted[i - viewAmount])))
                    favoriteGame = False
                    wishlistedGame = False
                    for category in range(len(FAVORITE_GAMES)):
                        if isinstance(second_list_item(FAVORITE_GAMES, category, 0), str):
                            for game in range(len(nested_list(FAVORITE_GAMES, category))):
                                if topGameIds[i - viewAmount] == second_list_item(FAVORITE_GAMES, category, game):
                                    print('\033[32m' + printString + '\033[0m')  # Green
                                    favoriteGame = True
                        else:
                            for subCategory in range(len(nested_list(FAVORITE_GAMES, category))):
                                for game in range(len(nested_list(FAVORITE_GAMES, category, subCategory))):
                                    if topGameIds[i - viewAmount] == second_list_item(FAVORITE_GAMES, category, subCategory, game):
                                        print('\033[32m' + printString + '\033[0m')  # Green
                                        favoriteGame = True
                    if not favoriteGame:
                        # Check if game is on the wishlist
                        for category in range(len(WISHLISTED)):
                            if isinstance(second_list_item(WISHLISTED, category, 0), str):
                                for game in range(len(nested_list(WISHLISTED, category))):
                                    if topGameIds[i - viewAmount] == second_list_item(WISHLISTED, category, game):
                                        print('\033[33m' + printString + '\033[0m')  # Yellow
                                        wishlistedGame = True
                            else:
                                for subCategory in range(len(nested_list(WISHLISTED, category))):
                                    for game in range(len(nested_list(WISHLISTED, category, subCategory))):
                                        if topGameIds[i - viewAmount] == second_list_item(WISHLISTED, category, subCategory, game):
                                            print('\033[33m' + printString + '\033[0m')  # Yellow
                                            wishlistedGame = True
                    # Check if a game with this name is not already favorited or whitelisted under another id
                    if not favoriteGame and not wishlistedGame:
                        newGame = True
                        gameLists = [BLACKLIST, FAVORITE_GAMES, WISHLISTED]
                        for gamelist in range(len(gameLists)):
                            for category in range(len(gameLists[gamelist])):
                                if isinstance(second_list_item(gameLists[gamelist], category, 0), str):
                                    for game in range(len(nested_list(gameLists[gamelist], category))):
                                        if topGameNames[i - viewAmount].lower() == list_item(gameLists[gamelist], category, game).lower():
                                            newGame = False
                                            break
                                else:
                                    for subCategory in range(len(nested_list(gameLists[gamelist], category))):
                                        for game in range(len(nested_list(gameLists[gamelist], category, subCategory))):
                                            if topGameNames[i - viewAmount].lower() == list_item(gameLists[gamelist], category, subCategory, game).lower():
                                                newGame = False
                                                break
                        if newGame:
                            addedGame = False
                            for addedNewGames in range(len(new_games_ids)):
                                if topGameNames[i - viewAmount].lower() == list_item(new_games_ids, addedNewGames).lower():
                                    addedGame = True
                                    break
                            if not addedGame:
                                new_games_ids.append([topGameNames[i - viewAmount], topGameIds[i - viewAmount]])
                        print(printString)
                        if TESTING:
                            print(len(topGameNames[i - viewAmount]), topGameNames[i - viewAmount],
                                  len(topGameIds[i - viewAmount]), topGameIds[i - viewAmount])
            print("Favorite games first run:")
            for i in range(viewAmount):
                if topGameNames[i - viewAmount] == 'Minecraft' or topGameNames[i - viewAmount] == 'Satisfactory':
                    printString = (
                            str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                            str(round(gameViewers[i - viewAmount])) + "v watching " +
                            str(round(gameStreams[i - viewAmount])) + "s with a vrat of: " +
                            str(round(gameViewerRatio[i - viewAmount], 2)) + " and the s at " + str(
                        CASTER_PERCENTAGE) + "% of the cat has " +
                            str(round(gameViewersMedian[i - viewAmount], 2)) + "v and a vmrat of: " +
                            str(round(viewerRatioMedianRatioSorted[i - viewAmount]))
                    )
                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                        print('\033[34m' + printString + '\033[0m')  ## Blue
                    elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                        print('\033[32m' + printString + '\033[0m')  ## Green
                    else:
                        print(printString)
                elif viewerRatioMedianRatioSorted[i - viewAmount] > 0:
                    printString = (str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                                   str(round(gameViewers[i - viewAmount])) + "v watching " +
                                   str(round(gameStreams[i - viewAmount])) + "s with a vrat of: " +
                                   str(round(gameViewerRatio[i - viewAmount], 2)) + " and the s at " + str(
                                CASTER_PERCENTAGE) + "% of the cat has " +
                                   str(round(gameViewersMedian[i - viewAmount], 2)) + "v and a vmrat of: " +
                                   str(round(viewerRatioMedianRatioSorted[i - viewAmount])))
                    newGame = False
                    favoriteGame = False
                    wishlistedGame = False
                    # Print game if favorited
                    for category in range(len(FAVORITE_GAMES)):
                        if isinstance(second_list_item(FAVORITE_GAMES, category, 0), str):
                            for game in range(len(nested_list(FAVORITE_GAMES, category))):
                                if topGameIds[i - viewAmount] == second_list_item(FAVORITE_GAMES, category, game):
                                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                        print('\033[34m' + printString + '\033[0m')  ## Blue
                                    elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                        print('\033[32m' + printString + '\033[0m')  ## Green
                                    else:
                                        print(printString)  ## White
                                    favoriteGame = True
                        else:
                            for subCategory in range(len(nested_list(FAVORITE_GAMES, category))):
                                for game in range(len(nested_list(FAVORITE_GAMES, category, subCategory))):
                                    if topGameIds[i - viewAmount] == second_list_item(FAVORITE_GAMES, category, subCategory, game):
                                        if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                            print('\033[34m' + printString + '\033[0m')  ## Blue
                                        elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                            print('\033[32m' + printString + '\033[0m')  ## Green
                                        else:
                                            print(printString)  ## White
                                        favoriteGame = True
                    # Print game if on wishlist
                    if not favoriteGame:
                        for category in range(len(WISHLISTED)):
                            if isinstance(second_list_item(WISHLISTED, category, 0), str):
                                for game in range(len(nested_list(WISHLISTED, category))):
                                    if topGameIds[i - viewAmount] == second_list_item(WISHLISTED, category, game):
                                        if topGameIds[i - viewAmount] == second_list_item(WISHLISTED, category, game) and round(
                                                viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                            print('\033[33m' + printString + '\033[0m')  # Yellow
                                        else:
                                            print(printString)  # White
                            else:
                                for subCategory in range(len(nested_list(WISHLISTED, category))):
                                    for game in range(len(nested_list(WISHLISTED, category, subCategory))):
                                        if topGameIds[i - viewAmount] == second_list_item(WISHLISTED, category, subCategory, game):
                                            if topGameIds[i - viewAmount] == second_list_item(WISHLISTED, category, subCategory, game) and round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                                print('\033[33m' + printString + '\033[0m')  # Yellow
                                            else:
                                                print(printString)  # White
            if totalGames > 0:
                print(str(totalGames) + 'g have ' + str(totalViewers) + 'v watching s ' + str(
                    totalStreams) + ' with an avgvrat of: ' + str(
                    round(totalViewerRatio / totalGames, 2)) + ", the s at " + str(
                    CASTER_PERCENTAGE) + "% of the cat has an avg of " + str(
                    round(totalViewersMedian / totalGames)) + "v and an avgvmrat of: " + str(
                    round(totalViewerRatioMedianRatio / totalGames)))
            if new_games_ids:
                newGamesReversed = []
                for game in range(len(new_games_ids[::-1])):
                    newGamesReversed.append(new_games_ids[game][0])
                if len(newGamesReversed) == 1:
                    print("The newest, streamable game is: " + newGamesReversed[0])
                else:
                    print("The new, streamable games are:")
                    print_every_ten(newGamesReversed)
            else:
                print("No new, streamable games detected")
    elif not restartLoops:
        printData()
        if firstRun:
            print_strings()
    elif restartLoops:
        firstRun = False
        printData()
        print_strings()
        loops = 0
    hours, minutes, seconds = convert_timedelta(datetime.now() - loopStart)
    print('Data from the last {} minute{}, {} second{}'.format(minutes, 's' if seconds != 1 else '', seconds, 's' if seconds != 1 else ''))
    print("Current time: " + str(datetime.now().strftime('%H:%M:%S')))
