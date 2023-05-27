#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioBot.py

import datetime
import math
import os

import requests
import re
from ViewerRatioConfig import *
from blacklistedStreams import *
from ViewerRatioLists import *
from tags import *
from output import *
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
global minStreams
global minViewers
global loopStart
global combinedTags
global newGames
global totalGames
global totalViewers
global totalStreams
global totalViewerRatio
global totalViewersMedian
global totalViewerRatioMedianRatio

# Globals permanent through while true loops
gameViewersLooped = []
gameStreamsLooped = []
gameViewerRatioLooped = []
hostGamesLooped = []
gameViewersMedianLooped = []
viewerRatioMedianRatioLooped = []
topGameIdsLooped = []
loops = 0
worthGames = 0
dropsGames = []
firstRun = True
tags = []

newBlacklistAdditions = []

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
favoriteCategories = []
for g in range(len(favoriteGames)):
    favoriteCategories.append(favoriteGames[g][0])
f.writelines("\n" + ', '.join(favoriteCategories))
f.writelines('\n')
singularCategories = False
for g in range(len(favoriteGames)):
    if type(favoriteGames[g][1][0][1]) == str:
        if not singularCategories:
            f.writelines('\n|   |**Favorite games**|')
            f.writelines('\n|---|---------------------|')
        singularCategories = True
        f.writelines('\n|**' + favoriteGames[g][0] + '**|' + ', '.join(favoriteGames[g][1]) + '|')
    else:
        if singularCategories:
            f.writelines('\n')
        singularCategories = False
        subCategories = []
        for m in range(len(favoriteGames[g][1])):
            subCategories.append(favoriteGames[g][1][m][0])
        f.writelines('\n')
        f.writelines('\n|**' + favoriteGames[g][0] + '**|_' + ', '.join(subCategories) + '_|')
        f.writelines('\n|----------------|-----------------------------------------------------------------------|')
        for m in range(len(favoriteGames[g][1])):
            f.writelines('\n|**' + favoriteGames[g][1][m][0] + '**|' + ', '.join(favoriteGames[g][1][m][1]) + '|')
        f.writelines('\n')
f.writelines('\n')
f.writelines('\n<a href="#white-black-list">Back to top</a>')
f.writelines('\n## Whitelist:')
f.writelines('\n')
f.writelines('\n **Categories:**')
whitelistCategories = []
for w in range(len(wishlisted)):
    whitelistCategories.append(wishlisted[w][0])
f.writelines("\n" + ', '.join(whitelistCategories))
f.writelines('\n')
singularCategories = False
for w in range(len(wishlisted)):
    if type(wishlisted[w][1][0][1]) == str:
        if not singularCategories:
            f.writelines('\n|   |**Whitelisted games**|')
            f.writelines('\n|---|---------------------|')
        singularCategories = True
        f.writelines('\n|**' + wishlisted[w][0] + '**|' + ', '.join(wishlisted[w][1]) + '|')
    else:
        if singularCategories:
            f.writelines('\n')
        singularCategories = False
        subCategories = []
        for m in range(len(wishlisted[w][1])):
            subCategories.append(wishlisted[w][1][m][0])
        f.writelines('\n')
        f.writelines('\n|**' + wishlisted[w][0] + '**|_' + ', '.join(subCategories) + '_|')
        f.writelines('\n|---|---------------------|')
        for m in range(len(wishlisted[w][1])):
            f.writelines('\n|**' + wishlisted[w][1][m][0] + '**|' + ', '.join(wishlisted[w][1][m][1]) + '|')
        f.writelines('\n')
f.writelines('\n')
f.writelines('\n<a href="#white-black-list">Back to top</a>')
f.writelines('\n## Blacklist:')
f.writelines('\n')
f.writelines('\n **Categories:**')
blacklistCategories = []
for b in range(len(blacklist)):
    blacklistCategories.append(blacklist[b][0])
f.writelines("\n" + ', '.join(blacklistCategories))
f.writelines('\n')
singularCategories = False
for b in range(len(blacklist)):
    blacklistedGames = []
    if type(blacklist[b][1][0][1]) == str:
        if not singularCategories:
            f.writelines('\n|   |**Blacklisted games**|')
            f.writelines('\n|---|---------------------|')
        singularCategories = True
        for g in range(len(blacklist[b][1])):
            blacklistedGames.append(blacklist[b][1][g][0])
        f.writelines('\n|**' + blacklist[b][0] + '**|' + ', '.join(blacklistedGames) + '|')
    else:
        if singularCategories:
            f.writelines('\n')
        singularCategories = False
        subCategories = []
        for m in range(len(blacklist[b][1])):
            subCategories.append(blacklist[b][1][m][0])
        f.writelines('\n|**' + blacklist[b][0] + '**|_' + ', '.join(subCategories) + '_|')
        f.writelines('\n|---|---------------------|')
        for m in range(len(blacklist[b][1])):
            blacklistedGames = []
            for g in range(len(blacklist[b][1][m][1])):
                blacklistedGames.append(blacklist[b][1][m][1][g][0])
            f.writelines('\n|**' + blacklist[b][1][m][0] + '**|' + ', '.join(blacklistedGames) + '|')
        f.writelines('\n')
f.writelines('\n')
f.writelines('\n<a href="#white-black-list">Back to top</a>')
f.close()
os.replace('tmpfile.py', 'blackWhitelist.md')
print('Black/whitelist has been updated')

def getMoreGameViewers():
    global pagination
    global topGameViewers
    urlGameViewers = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[-1] + "&after=" + pagination
    paramsGameViewers = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
    r = requests.get(urlGameViewers, headers=paramsGameViewers).json()
    if not r['pagination'] == {}:
        pagination = r['pagination']['cursor']
        for a in r['data']:
            if int(a['viewer_count']) == 1:
                topGameViewers = topGameViewers + 0
            else:
                topGameViewers = topGameViewers + int(a['viewer_count'])
        getMoreGameViewers()


def getMoreGames():
    global paginationTopGames
    global topGameIds
    global topGameNames
    global pagination
    global topGameViewers
    global stopGettingGames
    urlMoreGames = "https://api.twitch.tv/helix/games/top?first=100" + "&after=" + paginationTopGames
    paramsMoreGames = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
    r = requests.get(urlMoreGames, headers=paramsMoreGames).json()
    if not r['pagination'] == {}:
        paginationTopGames = r['pagination']['cursor']
        for i in r['data']:
            topGameIds.append(i['id'])
            topGameNames.append(i['name'])
        getMoreGameViewers()
        pagination = ""
    if topGameViewers < 100:
        stopGettingGames = stopGettingGames + 1
    topGameViewers = 0
    if stopGettingGames < 3:
        getMoreGames()
    # elif testing:
    #     print("Raw streamed games are: " + str(len(topGameIds)) + " " + str(topGameNames))


def getMoreStreams(i):
    try:
        global pagination
        global gameViewers
        global gameStreams
        global medianList
        global dropsGames
        global combinedTags
        urlMore = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[i] + "&after=" + pagination
        paramsMore = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        r = requests.get(urlMore, headers=paramsMore).json()
        if not r['pagination'] == {}:
            pagination = r['pagination']['cursor']
            gameStreams[i] = str(int(gameStreams[i]) + int(len(r['data'])))
            # if testing:
            #     print('Getting more streams')
            for e in r['data']:
                if testing:
                    if e['game_id'] == 'Lineage 2':
                        print(e['user_name'])
                startedAt = e['started_at']
                year, month, day, hour, minute, second = int(startedAt[0:4]), int(startedAt[5:7]), int(startedAt[8:10]), int(startedAt[11:13]), int(startedAt[14:16]), int(startedAt[17:19])
                startedAt = datetime.datetime(year, month, day, hour, minute, second)
                now = datetime.datetime.now()
                hours, minutes, seconds = convert_timedelta(now - startedAt)
                if not e['tags'] is None:
                    for t in range(len(e['tags'])):
                        newTag = True
                        for w in range(len(whitelistedTags)):
                            if w == (len(whitelistedTags) - 1):
                                for p in range(len(whitelistedTags[w][1])):
                                    for v in range(len(whitelistedTags[w][1][p][1])):
                                        if p == (len(whitelistedTags[w][1]) - 1):
                                            if e['tags'][t].lower() in (tag.lower() for tag in whitelistedTags[w][1][p][1][v][1]):
                                                newTag = False
                                        elif e['tags'][t][0].lower() == whitelistedTags[w][1][p][0][0]:
                                            if e['tags'][t].lower() in (tag.lower() for tag in whitelistedTags[w][1][p][1][v][1]):
                                                newTag = False
                                        if not newTag:
                                            break
                            else:
                                if e['tags'][t].lower() in (tag.lower() for tag in whitelistedTags[w][1]):
                                    newTag = False
                        if newTag:
                            for b in range(len(blacklistedTags)):
                                if e['tags'][t].lower() in (tag.lower() for tag in blacklistedTags[b][1]):
                                    newTag = False
                        if newTag:
                            for c in range(len(combinedTags)):
                                for v in range(len(combinedTags[c][1])):
                                    if combinedTags[c][1][v][1]:
                                        if c == (len(combinedTags) - 1):
                                            if e['tags'][t].lower() in (tag.lower() for tag in combinedTags[c][1][v][1]):
                                                newTag = False
                                        elif e['tags'][t][0].lower() == combinedTags[c][0][0]:
                                            if e['tags'][t].lower() in (tag.lower() for tag in combinedTags[c][1][v][1]):
                                                newTag = False
                                        if not newTag:
                                            break
                        if newTag:
                            otherTag = True
                            for m in range(len(combinedTags)):
                                if not m == (len(combinedTags) - 1):
                                    if e['tags'][t][0].lower() == combinedTags[m][0][0]:
                                        combinedTags[m][1][(len(e['tags'][t]) - 1)][1].append(e['tags'][t])
                                        otherTag = False
                            if otherTag:
                                combinedTags[-1][1][(len(e['tags'][t]) - 1)][1].append(e['tags'][t])
                if not hours > 18:
                    if not e['user_name'] in blacklistedStreams:
                        blacklisted = False
                        for b in range(len(blacklistedTags)):
                            if not e['tags'] is None:
                                for t in range(len(e['tags'])):
                                    if 'drop' in e['tags'][t].lower():
                                        if not e['game_id'] in dropsGames:
                                            dropsGames.append(e['game_id'])
                                    if e['tags'][t].lower() in (tag.lower() for tag in blacklistedTags[b][1]):
                                        if testing and e['game_name'] == testGame:
                                            print(e['game_name'] + ' stream has the blacklisted tag: ' + e['tags'][t])
                                        blacklisted = True
                                        break
                                if blacklisted:
                                    break
                        for b in range(len(blacklistedTitles)):
                            if b == 0:
                                for t in range(len(blacklistedTitles[b][1])):
                                    if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                        blacklisted = True
                                        break
                            elif e['game_name'] == blacklistedTitles[b][0]:
                                for t in range(len(blacklistedTitles[b][1])):
                                    # if testing and e['game_name'] == testGame:
                                    #     print(blacklistedTitles[b][1][t].lower())
                                    #     print(e['title'].lower())
                                    if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                        if testing and e['game_name'] == testGame:
                                            print(e['game_name'] + ' stream has the blacklisted title segmment: "' + blacklistedTitles[b][1][t] + '" in the title: ' + e['title'])
                                        blacklisted = True
                                        break
                            if blacklisted:
                                break
                        for b in range(len(blacklistedPartialStreams)):
                            if b == 0:
                                if blacklistedPartialStreams[b][1][0]:
                                    for t in range(len(blacklistedPartialStreams[b][1])):
                                        if re.search('(' + blacklistedPartialStreams[b][1][t][0].lower() + ').*(' +
                                                     blacklistedPartialStreams[b][1][t][1].lower() + ')',
                                                     e['user_name'].lower()):
                                            blacklisted = True
                                            break
                            elif e['game_name'].lower() == blacklistedPartialStreams[b][0].lower():
                                for t in range(len(blacklistedPartialStreams[b][1])):
                                    if re.search('(' + blacklistedPartialStreams[b][1][t][0].lower() + ').*(' +
                                                 blacklistedPartialStreams[b][1][t][1].lower() + ')',
                                                 e['user_name'].lower()):
                                        blacklisted = True
                                        break
                            if blacklisted:
                                break
                        if not blacklisted:
                            gameViewers[i] = str(int(gameViewers[i]) + int(e['viewer_count']))
                            medianList[i].append(int(e['viewer_count']))
                            if testing:
                                if e['game_name'].lower() == testGame:
                                    print(e['game_name'] + " streamer " + e['user_name'].lower() + " has " + str(
                                        e['viewer_count']) + " viewers  for a total of " + str(gameViewers[i]) + " viewers so far")
            getMoreStreams(i)
    except Exception as x:
        print('Error in getting more streams')
        print(x)
        if testing:
            raise
    except requests.exceptions.ConnectTimeout:
        print("timeout", urlMore)


def printData():
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
    global hostGamesLoopedPrinted
    global gameViewersLoopedPrinted
    global gameStreamsLoopedPrinted
    global gameViewerRatioLoopedPrinted
    global gameViewersMedianLoopedPrinted
    global viewerRatioMedianRatioLoopedPrinted
    global viewerRatioMedianRatioLoopedSorted
    global minStreams
    # if testing:
    #     print("Before math has been done")
    #     print(len(topGameNames), topGameNames)
    #     print(len(topGameIds), topGameIds)
    #     print(len(hostGamesLooped), hostGamesLooped)
    #     print(len(topGameIdsLooped), topGameIdsLooped)
    testExist = 0
    testNonExist = 0
    for i in range(len(topGameNames)):
        existingGame = False
        for h in range(len(hostGamesLooped)):
            if testing:
                if topGameNames[i] == 'Minecraft' and hostGamesLooped[h] == 'Minecraft':
                    print("Before adding")
                    print(gameViewers[i])
                    print(gameViewersLooped[h])
            if topGameNames[i] == hostGamesLooped[h]:
                gameViewersLooped[h] = str(int(gameViewersLooped[h]) + int(gameViewers[i]))
                if (int(gameViewersLooped[h]) / loops) < minViewers:
                    gameViewersLooped[h] = "0"
                gameStreamsLooped[h] = str(int(gameStreamsLooped[h]) + int(gameStreams[i]))
                if (math.trunc(int(gameStreamsLooped[h])) / loops) < minStreams:
                    gameStreamsLooped[h] = "0"
                if gameViewersLooped[h] == "0":
                    gameViewerRatioLooped[h] = 0
                elif gameStreamsLooped[h] == "0":
                    gameViewerRatioLooped[h] = 0
                else:
                    gameViewerRatioLooped[h] = int(gameViewersLooped[h]) / int(gameStreamsLooped[h])
                if testing:
                    if topGameNames[i] == 'Minecraft' and hostGamesLooped[h] == 'Minecraft':
                        print("Medians are: ", gameViewersMedianLooped[h], gameViewersMedian[h])
                gameViewersMedianLooped[h] = int(gameViewersMedianLooped[h]) + int(gameViewersMedian[i])
                if testing:
                    if topGameNames[i] == 'Minecraft' and hostGamesLooped[h] == 'Minecraft':
                        print("Ratio consists of: ", gameViewerRatioLooped[h], gameViewersMedianLooped[h])
                viewerRatioMedianRatioLooped[h] = gameViewerRatioLooped[h] * gameViewersMedianLooped[h]
                existingGame = True
                testExist = testExist + 1
        if not existingGame:
            gameViewersLooped.append(gameViewers[i])
            if (int(gameViewersLooped[-1]) / loops) < minViewers:
                gameViewersLooped[-1] = "0"
            gameStreamsLooped.append(gameStreams[i])
            if (math.trunc(int(gameStreamsLooped[-1])) / loops) < minStreams:
                gameStreamsLooped[-1] = "0"
            if gameViewersLooped[-1] == "0":
                gameViewerRatioLooped.append(0)
            elif gameStreamsLooped[-1] == "0":
                gameViewerRatioLooped.append(0)
            else:
                gameViewerRatioLooped.append(int(gameViewersLooped[-1]) / int(gameStreamsLooped[-1]))
            gameViewersMedianLooped.append(gameViewersMedian[i])
            viewerRatioMedianRatioLooped.append(gameViewerRatioLooped[-1] * gameViewersMedianLooped[-1])
            hostGamesLooped.append(topGameNames[i])
            testNonExist = testNonExist + 1
    # if testing:
    #     print("After math has been done")
    #     print(testExist, testNonExist)
    #     print(len(topGameNames), topGameNames)
    #     print(len(topGameIds), topGameIds)
    #     print(len(hostGamesLooped), hostGamesLooped)
    #     print(len(topGameIdsLooped), topGameIdsLooped)


    dummy = []
    hostGamesLoopedPrinted = hostGamesLooped[:]
    gameViewersLoopedPrinted = gameViewersLooped[:]
    gameStreamsLoopedPrinted = gameStreamsLooped[:]
    gameViewerRatioLoopedPrinted = gameViewerRatioLooped[:]
    gameViewersMedianLoopedPrinted = gameViewersMedianLooped[:]
    viewerRatioMedianRatioLoopedPrinted = viewerRatioMedianRatioLooped[:]
    viewerRatioMedianRatioLoopedSorted = viewerRatioMedianRatioLooped[:]

    dummy[:], hostGamesLoopedPrinted[:] = zip(*sorted(zip(viewerRatioMedianRatioLoopedPrinted, hostGamesLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameViewersLoopedPrinted[:] = zip(*sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameViewersLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameStreamsLoopedPrinted[:] = zip(*sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameStreamsLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameViewerRatioLoopedPrinted[:] = zip(*sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameViewerRatioLoopedPrinted), key=lambda p: (p[0], p[1])))
    dummy[:], gameViewersMedianLoopedPrinted[:] = zip(*sorted(zip(viewerRatioMedianRatioLoopedPrinted, gameViewersMedianLoopedPrinted), key=lambda p: (p[0], p[1])))
    viewerRatioMedianRatioLoopedSorted = sorted(viewerRatioMedianRatioLoopedSorted)


def printStrings():
    global worthGames
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
    global newGames
    global totalGames
    global totalViewers
    global totalStreams
    global totalViewerRatio
    global totalViewersMedian
    global totalViewerRatioMedianRatio
    viewAmount = len(hostGamesLooped)
    for i in range(len(combinedTags)):
        lengthTags = []
        for v in range(len(combinedTags[i][1])):
            if combinedTags[i][1][v][1]:
                for r in range(len(combinedTags[i][1][v][1])):
                    lengthTags.append(combinedTags[i][1][v][1][r])
        if lengthTags:
            print("New tags with " + combinedTags[i][0] + " are: " + ', '.join(str(x) for x in lengthTags))
    for i in range(viewAmount):
        if viewerRatioMedianRatioLoopedSorted[i - viewAmount] > 0:
            gameViewersLoopedAverage = int(gameViewersLoopedPrinted[i - viewAmount]) / loops
            gameStreamsLoopedAverage = int(gameStreamsLoopedPrinted[i - viewAmount]) / loops
            gameViewerRatioLoopedAverage = gameViewerRatioLoopedPrinted[i - viewAmount]
            gameViewersMedianLoopedAverage = gameViewersMedianLoopedPrinted[i - viewAmount] / loops
            if gameViewersMedianLoopedAverage == 0:
                viewerRatioMedianRatioLoopedAverage = 0
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
                           str(round(gameViewerRatioLoopedAverage, 2)) + " and the s at " + str(casterPercentage) + "% of the cat has " +
                           str(round(gameViewersMedianLoopedAverage, 2)) + "v and a vmrat of: " +
                           str(round(viewerRatioMedianRatioLoopedAverage)))
            if hostGamesLoopedPrinted[i - viewAmount] == 'Minecraft' or hostGamesLoopedPrinted[i - viewAmount] == 'Satisfactory':
                if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                    print('\033[34m' + printString + '\033[0m')
                elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                    print('\033[32m' + printString + '\033[0m')
                else:
                    print(printString)
            elif viewerRatioMedianRatioLoopedAverage > 0:
                newGameLooped = False
                printed = False
                favoriteGame = False
                wishlistedGame = False
                for f in range(len(favoriteGames)):
                    if type(favoriteGames[f][1][0][1]) == str:
                        if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1]):
                            if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                print('\033[34m' + printString + '\033[0m')  # Blue
                            else:
                                print('\033[32m' + printString + '\033[0m')  # Green
                            favoriteGame = True
                            break
                    else:
                        for m in range(len(favoriteGames[f][1])):
                            if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1][m][1]):
                                if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                    print('\033[34m' + printString + '\033[0m')  # Blue
                                else:
                                    print('\033[32m' + printString + '\033[0m')  # Green
                                favoriteGame = True
                                break
                if not favoriteGame:
                    for w in range(len(wishlisted)):
                        if type(wishlisted[w][1][0][1]) == str:
                            if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1]):
                                if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                    print('\033[34m' + printString + '\033[0m')  # Blue
                                else:
                                    print('\033[33m' + printString + '\033[0m')  # Yellow
                                wishlistedGame = True
                                break
                        else:
                            wishlistedGameBreaker = False
                            for m in range(len(wishlisted[w][1])):
                                if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1][m][1]):
                                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                        print('\033[34m' + printString + '\033[0m')  # Blue
                                    else:
                                        print('\033[33m' + printString + '\033[0m')  # Yellow
                                    wishlistedGame = True
                                    wishlistedGameBreaker = True
                                    break
                            if wishlistedGameBreaker:
                                break
                if not favoriteGame and not wishlistedGame:
                    newGameLooped = True
                    for y in range(len(newGames)):
                        if newGames[y] == hostGamesLoopedPrinted[i - viewAmount]:
                            newGameLooped = False
                    print(printString)
                    if newGameLooped:
                        newGames.append(hostGamesLoopedPrinted[i - viewAmount])
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
                str(round(gameViewerRatioLoopedAverage, 2)) + " and the s at " + str(casterPercentage) + "% of the cat has " +
                str(round(gameViewersMedianLoopedAverage, 2)) + "v and a vmrat of: " +
                str(round(viewerRatioMedianRatioLoopedAverage))
        )
        if hostGamesLoopedPrinted[i - viewAmount] == 'Minecraft' or hostGamesLoopedPrinted[i - viewAmount] == 'Satisfactory':
            if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                print('\033[34m' + printString + '\033[0m')
            elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                print('\033[32m' + printString + '\033[0m')
            else:
                print(printString)
        elif viewerRatioMedianRatioLoopedAverage > 0:
            for f in range(len(favoriteGames)):
                if type(favoriteGames[f][1][0][1]) == str:
                    if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1]):
                        if viewerRatioMedianRatioLoopedAverage >= 1000:
                            print('\033[34m' + printString + '\033[0m')
                        elif 1000 > viewerRatioMedianRatioLoopedAverage > 100:
                            print('\033[32m' + printString + '\033[0m')
                        else:
                            print(printString)
                        break
                else:
                    favoriteGameBreaker = False
                    for m in range(len(favoriteGames[f][1])):
                        if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1][m][1]):
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
            for w in range(len(wishlisted)):
                if type(wishlisted[w][1][0][1]) == str:
                    if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1]) and viewerRatioMedianRatioLoopedAverage > 100:
                        print('\033[33m' + printString + '\033[0m')
                        break
                else:
                    wishlistedGameBreaker = False
                    for m in range(len(wishlisted[w][1])):
                        if hostGamesLoopedPrinted[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1][m][1]) and viewerRatioMedianRatioLoopedAverage > 100:
                            print('\033[33m' + printString + '\033[0m')
                            wishlistedGameBreaker = True
                            break
                    if wishlistedGameBreaker:
                        break
    print(str(totalGames) + 'g have ' + str(totalViewers) + 'v watching ' + str(totalStreams) + 's with an avgvrat of: ' + str(round(totalViewerRatio / totalGames, 2)) + ", the s at " + str(casterPercentage) + "% of the cat has an avg of " + str(round(totalViewersMedian / totalGames)) + "v and an avgvmrat of: " + str(round(totalViewerRatioMedianRatio / totalGames)))
    if newGames:
        newGamesReversed = newGames[:]
        newGamesReversed.reverse()
        newGamesPrintList = []
        if len(newGamesReversed) == 1:
            print("The newest game is: " + newGamesReversed[0])
        else:
            print("The new games are:")
            for i, a in enumerate(newGamesReversed):
                newGamesPrintList.append(a)
                if i % 10 == 9:
                    print((i - 8), "-", (i + 1), newGamesPrintList)
                    newGamesPrintList = []
            if not (len(newGamesReversed) % 10) == 0:
                print((len(newGamesReversed) - (len(newGamesReversed) % 10) + 1), "-",
                      len(newGamesReversed), ", ".join(newGamesPrintList))

    hostGamesLoopedPrintedReversed = hostGamesLoopedPrinted[:]
    hostGamesLoopedPrintedReversed.reverse()
    # Write games to a txt file
    f = open("tmpfile.py", "w", encoding='utf-8')
    f.writelines("# !/usr/bin/env python")
    f.writelines("\n# -*- coding: utf-8 -*-")
    f.writelines("\n# output.py")
    f.writelines("\nhostGames = " + str(hostGamesLoopedPrintedReversed))
    f.writelines("\nnewGames = " + str(newGames))
    f.writelines("\ncombinedTags = [\n")
    for l in range(len(combinedTags)):
        f.writelines("    ['" + combinedTags[l][0] + "', [\n")
        for v in range(len(combinedTags[l][1])):
            f.writelines("        ['" + combinedTags[l][1][v][0] + "', [")
            if combinedTags[l][1][v][1]:
                f.writelines("'" + "', '".join(combinedTags[l][1][v][1]) + "']],\n")
            else:
                f.writelines("]],\n")
        f.writelines("    ]], \n")
    f.writelines("]")
    f.writelines("\nnewBlacklistAdditionsOutput = " + str(newBlacklistAdditions))
    f.writelines("\n")
    f.close()
    os.replace('tmpfile.py', 'output.py')


def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


# Print new blacklist additions
if not newGames == []:
    if testing:
        blacklistedGameAmount = 0
        favoriteGameAmount = 0
        wishlistedGameAmount = 0
        for b in range(len(blacklist)):
            if type(blacklist[b][1][0][1]) == str:
                blacklistedGameAmount = blacklistedGameAmount + len(blacklist[b][1])
            else:
                for g in range(len(blacklist[b][1])):
                    blacklistedGameAmount = blacklistedGameAmount + len(blacklist[b][1][g][1])
        for f in range(len(favoriteGames)):
            if type(favoriteGames[f][1][0][1]) == str:
                favoriteGameAmount = favoriteGameAmount + len(favoriteGames[f][1])
            else:
                for g in range(len(favoriteGames[f][1])):
                    favoriteGameAmount = favoriteGameAmount + len(favoriteGames[f][1][g][1])
        for w in range(len(wishlisted)):
            if type(wishlisted[f][1][0][1]) == str:
                wishlistedGameAmount = wishlistedGameAmount + len(wishlisted[w][1])
            else:
                for g in range(len(wishlisted[w][1])):
                    wishlistedGameAmount = wishlistedGameAmount + len(wishlisted[w][1][g][1])
        print("Getting blacklist game ids. " + str(blacklistedGameAmount) + " games blacklisted, " + str(favoriteGameAmount) + " favorite games and " + str(wishlistedGameAmount) + " games wishlisted for a total of " + str(blacklistedGameAmount + favoriteGameAmount + wishlistedGameAmount) + " games analyzed")
    for i in range(len(newGames)):
        if "+" in newGames[i]:
            newGames[i] = re.sub(r"\+", "%2b", newGames[i])
        if "&" in newGames[i]:
            newGames[i] = re.sub(r"&", "%26", newGames[i])
        if ":" in newGames[i]:
            newGames[i] = re.sub(r"&", "%26", newGames[i])
        url = "https://api.twitch.tv/helix/games?name=" + newGames[i]
        params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        request = requests.get(url, headers=params)
        r = request.json()
        if request.status_code == 200:
            pass
        elif request.status_code == 400:
            print("Bad request")
        elif request.status_code == 429:
            print("Too many game requests")
        try:
            newBlacklistAdditions.append([newGames[i], r['data'][0]['id']])
        except Exception as e:
            if r['data'] == []:
                print('The category ' + newGames[i] + ' does no longer exist and will be removed from the list of new games')
                f = open("output.py", "r", encoding='utf-8')
                outputLines = f.readlines()
                f.close()
                f = open("tmpfile.py", "w", encoding='utf-8')
                outputLines[4] = outputLines[4].replace(", '" + newGames[i] + "'", '')
                for l in range(len(outputLines)):
                    f.writelines(outputLines[l])
                f.close()
                os.replace('tmpfile.py', 'output.py')
            else:
                print("Error in appending new blacklist additions")
                print(e)
                if testing:
                    raise
                quit()
    if newBlacklistAdditions:
        if len(newBlacklistAdditions) == 1:
            print("The newest game is:", newBlacklistAdditions[0])
        else:
            newBlacklistPrintList = []
            for i, a in enumerate(newBlacklistAdditions):
                newBlacklistPrintList.append(a)
                if i % 5 == 4:
                    print((i - 3), "-", (i + 1), newBlacklistPrintList)
                    newBlacklistPrintList = []
            if not (len(newBlacklistAdditions) % 5) == 0:
                print((len(newBlacklistAdditions) - (len(newBlacklistAdditions) % 5) + 1), "-", len(newBlacklistAdditions), newBlacklistPrintList)
else:
    if testing:
        print("No new blacklist additions")
        url = "https://api.twitch.tv/helix/games?name=" + testGame
        params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        r = requests.get(url, headers=params).json()
        print("Typical game data is: " + str(r))

while True:
    try:
        gameViewers = []
        gameStreams = []
        medianList = []
        gameViewersMedian = []
        topGameNames = []
        topGameIds = []
        topGameViewers = 0
        stopGettingGames = 0
        pagination = ""
        paginationTopGames = ""
        totalGames = 0
        totalViewers = 0
        totalStreams = 0
        totalViewerRatio = 0
        totalViewersMedian = 0
        totalViewerRatioMedianRatio = 0

        print("Getting streamed games")
        if loops == 0:
            loopStart = datetime.datetime.now()
        getMoreGames()
        if testing:
            print("Streamed games have been gotten")

        # Extract id from blacklist
        blacklistIds = []
        for i in range(len(blacklist)):
            if type(blacklist[i][1][0][1]) == str:
                for a in range(len(blacklist[i][1])):
                    blacklistIds.append(blacklist[i][1][a][1])
            else:
                for g in range(len(blacklist[i][1])):
                    for a in range(len(blacklist[i][1][g][1])):
                        blacklistIds.append(blacklist[i][1][g][1][a][1])
        # Remove blacklisted games
        topGameIdsTemp = []
        topGameNamesTemp = []
        for i in range(len(topGameIds)):
            if not topGameIds[i] in blacklistIds:
                topGameIdsTemp.append(topGameIds[i])
                topGameNamesTemp.append(topGameNames[i])
        topGameIds = topGameIdsTemp
        topGameNames = topGameNamesTemp

        # Establish givens
        from output import *
        if not combinedTags:
            combinedTags = [
                ['a', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['b', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['c', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['d', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['e', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['f', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['g', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['h', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['i', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['j', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['k', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['l', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['m', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['n', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['o', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['p', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['q', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['r', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['s', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['t', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['u', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['v', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['w', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['x', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['y', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['z', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['1', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['2', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['3', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['4', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['5', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['6', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['7', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['8', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['9', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['0', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]],
                ['Other', [['1', []], ['2', []], ['3', []], ['4', []], ['5', []], ['6', []], ['7', []], ['8', []], ['9', []], ['10', []], ['11', []], ['12', []], ['13', []], ['14', []], ['15', []], ['16', []], ['17', []], ['18', []], ['19', []], ['20', []], ['21', []], ['22', []], ['23', []], ['24', []], ['25', []]]]
            ]

        # Add games that were not included
        existingGame = False
        if loops > 0:
            # if testing:
            #     print("The new top game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
            #     print("The old top game names are: " + str(len(hostGamesLooped)) + " " + str(hostGamesLooped))
            #     print("The new top game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
            #     print("The old top game ids are: " + str(len(topGameIdsLooped)) + " " + str(topGameIdsLooped))
            for i in range(len(topGameIdsLooped)):
                for t in range(len(topGameIds)):
                    if topGameIdsLooped[i] == topGameIds[t]:
                        existingGame = True
                if not existingGame:
                    topGameIds.append(topGameIdsLooped[i])
                    topGameNames.append(hostGamesLooped[i])

        # if testing:
        #     print("The added game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
        #     print("The added game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
        try:
            for i in range(len(topGameIds)):
                url = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[i]
                params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
                r = requests.get(url, headers=params).json()
                # if testing:
                #     print(topGameIds[i])
                #     print(r)
                gameStreams.append("0")
                gameViewers.append("0")
                medianList.append([])
                if testing:
                    if i == 0:
                        print('Getting info for games')
                    if topGameNames[i] == testGame:
                        print("Getting info for " + testGame)
                if r['pagination'] == {}:
                    pass
                else:
                    # if testing:
                        # print('Getting first streams')
                        # print(r)
                    gameStreams[i] = str(int(gameStreams[i]) + len(r['data']))
                    testingTags = []
                    for e in r['data']:
                        # Print streams in testgame
                        # print('Getting first stream')
                        startedAt = e['started_at']
                        year, month, day, hour, minute, second = int(startedAt[0:4]), int(startedAt[5:7]), int(startedAt[8:10]), int(startedAt[11:13]), int(startedAt[14:16]), int(startedAt[17:19])
                        startedAt = datetime.datetime(year, month, day, hour, minute, second)
                        now = datetime.datetime.now()
                        hours, minutes, seconds = convert_timedelta(now - startedAt)
                        if not hours > 18:
                            if not e['user_name'] in blacklistedStreams:
                                blacklisted = False
                                for b in range(len(blacklistedTags)):
                                    if not e['tags'] is None:
                                        for t in range(len(e['tags'])):
                                            if 'drop' in e['tags'][t].lower():
                                                if not e['game_id'] in dropsGames:
                                                    dropsGames.append(e['game_id'])
                                            if e['tags'][t].lower() in (tag.lower() for tag in blacklistedTags[b][1]):
                                                if testing and e['game_name'] == testGame:
                                                    print(e['game_name'] + ' stream has the blacklisted tag: ' + e['tags'][t])
                                                blacklisted = True
                                                break
                                            # Check what tags the test game has
                                            if testing and e['game_name'] == testGame and not blacklisted:
                                                whitelistedTag = False
                                                for c in range(len(whitelistedTags[0:-2])):
                                                    if e['tags'][t].lower() in (tag.lower() for tag in whitelistedTags[c][1]):
                                                        whitelistedTag = True
                                                        break
                                                if not whitelistedTag:
                                                    existingTag = False
                                                    for f in range(len(testingTags)):
                                                        if e['tags'][t].lower() == testingTags[f].lower():
                                                            existingTag = True
                                                            break
                                                    if not existingTag:
                                                        testingTags.append(e['tags'][t])
                                    if blacklisted:
                                        break
                                # Check what title the game has
                                for b in range(len(blacklistedTitles)):
                                    if b == 0:
                                        for t in range(len(blacklistedTitles[b][1])):
                                            if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                                if testing and e['game_name'] == testGame:
                                                    print(e['game_name'] + ' stream has the blacklisted title segment: "' + blacklistedTitles[b][1][t] + '" in the title: ' + e['title'])
                                                blacklisted = True
                                                break
                                    elif e['game_name'] == blacklistedTitles[b][0]:
                                        for t in range(len(blacklistedTitles[b][1])):
                                            if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                                if testing and e['game_name'] == testGame:
                                                    print(e['game_name'] + ' stream has the blacklisted title segment: "' + blacklistedTitles[b][1][t] + '" in the title: ' + e['title'])
                                                blacklisted = True
                                                break
                                for b in range(len(blacklistedPartialStreams)):
                                    if b == 0:
                                        if blacklistedPartialStreams[b][1][0]:
                                            for t in range(len(blacklistedPartialStreams[b][1])):
                                                if re.search('(' + blacklistedPartialStreams[b][1][t][0].lower() + ').*(' + blacklistedPartialStreams[b][1][t][1].lower() + ')', e['user_name'].lower()):
                                                    blacklisted = True
                                                    break
                                    elif e['game_name'].lower() == blacklistedPartialStreams[b][0].lower():
                                        for t in range(len(blacklistedPartialStreams[b][1])):
                                            if len(blacklistedPartialStreams[b][1][t]) == 1:
                                                if blacklistedPartialStreams[b][1][t][0].lower() == e['user_name'].lower():
                                                    if testing:
                                                        if topGameNames[i] == testGame:
                                                            print(e['user_name'])
                                                    blacklisted = True
                                                    break
                                            elif re.search('(' + blacklistedPartialStreams[b][1][t][0].lower() + ').*(' + blacklistedPartialStreams[b][1][t][1].lower() + ')', e['user_name'].lower()):
                                                if testing:
                                                    if topGameNames[i] == 'Tibia':
                                                        print(e['user_name'])
                                                blacklisted = True
                                                break
                                if not blacklisted:
                                    gameViewers[i] = str(int(gameViewers[i]) + int(e['viewer_count']))
                                    medianList[i].append(int(e['viewer_count']))
                                    if testing and e['game_name'].lower() == testGame.lower() and e['viewer_count'] > 4:
                                        print(e['game_name'] + " streamer " + e['user_name'] + " has " + str(e['viewer_count']) + " viewers with the title " + e['title'] + " and the tags " + ", ".join(e['tags']))
                    if r['data']:
                        if testing and r['data'][0]['game_name'] == testGame:
                            if testingTags:
                                print("Tags for " + testGame + " are:", testingTags)
                            else:
                                print("No new tags for " + testGame)
                    pagination = r['pagination']['cursor']
                    getMoreStreams(i)
                if testing and topGameNames[i] == testGame:
                    print("Info for " + testGame + " has been gotten")
                # If all viewers are in top 90% set views to 0
                for m in range(len(medianList[i])):
                    if int(medianList[i][m]) > (int(gameViewers[i]) * (topStreamerPercentage / 100)):
                        gameViewers[i] = 0
                if math.trunc(int(gameStreams[i])) < minStreams:
                    gameViewersMedian.append(0)
                else:
                    casterPercentile = (len(medianList[i]) - (math.trunc(len(medianList[i]) * (casterPercentage / 100))))
                    if math.trunc(len(medianList[i])) < minStreams:
                        median = 0
                    else:
                        median = medianList[i][casterPercentile]
                    gameViewersMedian.append(median)
                if firstRun:
                    if (i + 1) == len(topGameIds):
                        print(str(len(topGameIds)) + " of " + str(len(topGameIds)))
                    elif i <= 5:
                        print(str(i) + " of " + str(len(topGameIds)))
                    elif 10 <= i < 50:
                        if i % 10 == 0:
                            print(str(i) + " of " + str(len(topGameIds)))
                    elif i % 50 == 0:
                        print(str(i) + " of " + str(len(topGameIds)))
                else:
                    if len(topGameIds) < 200:
                        if (i + 1) == len(topGameIds):
                            print(str(len(topGameIds)) + " of " + str(len(topGameIds)))
                        elif i % 50 == 0:
                            print(str(i) + " of " + str(len(topGameIds)))
                    else:
                        if (i + 1) == len(topGameIds):
                            print(str(len(topGameIds)) + " of " + str(len(topGameIds)))
                        elif i % 100 == 0:
                            print(str(i) + " of " + str(len(topGameIds)))
        except Exception as e:
            print(e)
            if testing:
                raise
    except Exception as x:
        print(x)
        if testing:
            raise
    except requests.exceptions.ConnectTimeout:
        print("timeout", url)
    except KeyboardInterrupt:
        print('Keyboard interrupt exception is caught')

    if testing:
        print("Before drop removal")
        # print(len(topGameNames), topGameNames)
        # print(len(gameViewers), gameViewers)
        # print(len(topGameIds), topGameIds)
        for g in range(len(topGameIds)):
            if topGameNames[g] == 'Minecraft':
                print(topGameNames[g] + " has: " + str(gameViewers[g]) + " viewers")
            if topGameNames[g] == testGame:
                print(topGameNames[g] + " has: " + str(gameViewers[g]) + " viewers")

    # remove games with drops
    topGameIdsTemp = []
    topGameNamesTemp = []
    gameViewersTemp = []
    gameStreamsTemp = []
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
    topGameIdsLooped = topGameIds[:]

    if testing:
        print("After drop removal")
        # print(len(topGameNames), topGameNames)
        # print(len(gameViewers), gameViewers)
        # print(len(gameViewers), gameViewers)
        # print(len(topGameIds), topGameIds)
        if testing:
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
                if topGameNames[i] == testGame:
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")

    for i in range(len(topGameIds)):
        if int(gameViewers[i]) < minViewers:
            gameViewers[i] = "0"
        if math.trunc(int(gameStreams[i])) < minStreams:
            gameStreams[i] = "0"

    # Calculate viewer ratio
    gameViewerRatio = []
    for i in range(len(topGameIds)):
        if gameViewers[i] == "0":
            gameViewerRatio.append(0)
        elif gameStreams[i] == "0":
            gameViewerRatio.append(0)
        else:
            if (int(gameViewers[i]) / int(gameStreams[i])) == 1:
                gameViewerRatio.append(0)
            else:
                gameViewerRatio.append(int(gameViewers[i]) / int(gameStreams[i]))

    # calculate viewermedianratio
    viewerRatioMedianRatio = []
    for i in range(len(topGameIds)):
        viewerRatioMedianRatio.append(gameViewerRatio[i] * gameViewersMedian[i])

    viewAmount = len(topGameIds)
    loopAmount = 5
    loops = loops + 1

    # Calculate if the loop should be reset after this
    now = datetime.datetime.now()
    hours, minutes, seconds = convert_timedelta(now - loopStart)
    restartLoops = False
    if minutes >= loopLength:
        restartLoops = True
    if loops == 1:

        # Transfer variables to other variables for use in next loop
        hostGamesLooped = topGameNames[:]
        gameViewersLooped = gameViewers[:]
        gameStreamsLooped = gameStreams[:]
        gameViewerRatioLooped = gameViewerRatio[:]
        gameViewersMedianLooped = gameViewersMedian[:]
        viewerRatioMedianRatioLooped = viewerRatioMedianRatio[:]
        viewerRatioMedianRatioSorted = viewerRatioMedianRatio[:]

        if testing:
            print("Before sorting")
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
                if topGameNames[i] == testGame:
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")

        # if testing:
        #     print(topGameNames)
        #     print(gameViewers)
        #     print(gameStreams)

        # Sort by all lists by viewerRatioMedianRatio
        dummy = []
        dummy[:], topGameNames[:] = zip(*sorted(zip(viewerRatioMedianRatio, topGameNames), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewers[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameViewers), key=lambda p: (p[0], p[1])))
        dummy[:], gameStreams[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameStreams), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewerRatio[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameViewerRatio), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewersMedian[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameViewersMedian), key=lambda p: (p[0], p[1])))
        viewerRatioMedianRatioSorted[:] = sorted(viewerRatioMedianRatioSorted)
        # if testing:
        #     print(topGameNames)
        #     print(gameViewers)
        #     print(gameStreams)
        #     print(viewerRatioMedianRatio)

        if testing:
            print("After sorting")
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
                if topGameNames[i] == testGame:
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")

        if firstRun:
            for i in range(len(combinedTags)):
                lengthTags = []
                for v in range(len(combinedTags[i][1])):
                    if combinedTags[i][1][v][1]:
                        for r in range(len(combinedTags[i][1][v][1])):
                            lengthTags.append(combinedTags[i][1][v][1][r])
                if lengthTags:
                    print("New tags with " + combinedTags[i][0] + " are: " + ', '.join(str(x) for x in lengthTags))
            for i in range(viewAmount):
                if viewerRatioMedianRatioSorted[i - viewAmount] > 0:
                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) > 30 and gameViewersMedian[i - viewAmount] > 7:
                        totalGames = totalGames + 1
                        totalViewers = totalViewers + int(gameViewers[i - viewAmount])
                        totalStreams = totalStreams + int(gameStreams[i - viewAmount])
                        totalViewerRatio = totalViewerRatio + gameViewerRatio[i - viewAmount]
                        totalViewersMedian = totalViewersMedian + gameViewersMedian[i - viewAmount]
                        totalViewerRatioMedianRatio = totalViewerRatioMedianRatio + viewerRatioMedianRatioSorted[i - viewAmount]
                    printString = (str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                                   str(round(int(gameViewers[i - viewAmount]))) + "v watching " +
                                   str(round(int(gameStreams[i - viewAmount]))) + "s with a vrat of: " +
                                   str(round(gameViewerRatio[i - viewAmount], 2)) + " and the s at " + str(casterPercentage) + "% of the cat has " +
                                   str(round(gameViewersMedian[i - viewAmount], 2)) + "v and a vmrat of: " +
                                   str(round(viewerRatioMedianRatioSorted[i - viewAmount])))
                    newGame = False
                    favoriteGame = False
                    wishlistedGame = False
                    for f in range(len(favoriteGames)):
                        if type(favoriteGames[f][1][0][1]) == str:
                            if topGameNames[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1]):
                                print('\033[32m' + printString + '\033[0m')
                                favoriteGame = True
                                break
                        else:
                            favoriteGameBreaker = False
                            for g in range(len(favoriteGames[f][1])):
                                if topGameNames[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1][g][1]):
                                    print('\033[32m' + printString + '\033[0m')
                                    favoriteGame = True
                                    favoriteGameBreaker = True
                                    break
                            if favoriteGameBreaker:
                                break
                    if not favoriteGame:
                        for w in range(len(wishlisted)):
                            if type(wishlisted[w][1][0][1]) == str:
                                if topGameNames[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1]):
                                    print('\033[33m' + printString + '\033[0m')
                                    wishlistedGame = True
                                    break
                            else:
                                wishlistedGameBreaker = False
                                for g in range(len(wishlisted[w][1])):
                                    if topGameNames[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1][g][1]):
                                        print('\033[33m' + printString + '\033[0m')
                                        wishlistedGame = True
                                        wishlistedGameBreaker = True
                                        break
                                if wishlistedGameBreaker:
                                    break
                    if not favoriteGame and not wishlistedGame:
                        newGame = True
                        for n in range(len(newGames)):
                            if newGames[n].lower() == topGameNames[i - viewAmount].lower():
                                newGame = False
                        if newGame:
                            newGames.append(topGameNames[i - viewAmount])
                        print(printString)
            print("Favorite games:")
            for i in range(viewAmount):
                if topGameNames[i - viewAmount] == 'Minecraft' or topGameNames[i - viewAmount] == 'Satisfactory':
                    printString = (
                            str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                            str(round(int(gameViewers[i - viewAmount]))) + "v watching " +
                            str(round(int(gameStreams[i - viewAmount]))) + "s with a vrat of: " +
                            str(round(gameViewerRatio[i - viewAmount], 2)) + " and the s at " + str(casterPercentage) + "% of the cat has " +
                            str(round(gameViewersMedian[i - viewAmount], 2)) + "v and a vmrat of: " +
                            str(round(viewerRatioMedianRatioSorted[i - viewAmount]))
                    )
                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                        print('\033[34m' + printString + '\033[0m')
                    elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                        print('\033[32m' + printString + '\033[0m')
                    else:
                        print(printString)
                elif viewerRatioMedianRatioSorted[i - viewAmount] > 0:
                    printString = (
                            str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                            str(round(int(gameViewers[i - viewAmount]))) + "v watching " +
                            str(round(int(gameStreams[i - viewAmount]))) + "s with a vrat of: " +
                            str(round(gameViewerRatio[i - viewAmount], 2)) + " and the s at " + str(casterPercentage) + "% of the cat has " +
                            str(round(gameViewersMedian[i - viewAmount], 2)) + "v and a vmrat of: " +
                            str(round(viewerRatioMedianRatioSorted[i - viewAmount]))
                    )
                    favoriteGame = False
                    for f in range(len(favoriteGames)):
                        if type(favoriteGames[f][1][0][1]) == str:
                            if topGameNames[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1]):
                                if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                    print('\033[34m' + printString + '\033[0m')
                                elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                    print('\033[32m' + printString + '\033[0m')
                                else:
                                    print(printString)
                                favoriteGame = True
                                break
                        else:
                            favoriteGameBreaker = False
                            for m in range(len(favoriteGames[f][1])):
                                if topGameNames[i - viewAmount].lower() in (game.lower() for game in favoriteGames[f][1][m][1]):
                                    if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                        print('\033[34m' + printString + '\033[0m')
                                    elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                        print('\033[32m' + printString + '\033[0m')
                                    else:
                                        print(printString)
                                    favoriteGame = True
                                    favoriteGameBreaker = True
                                    break
                            if favoriteGameBreaker:
                                break
                    if not favoriteGame:
                        for w in range(len(wishlisted)):
                            if type(wishlisted[w][1][0][1]) == str:
                                if topGameNames[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1]) and round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                    print('\033[33m' + printString + '\033[0m')
                                    break
                            else:
                                wishlistedGameBreaker = False
                                for m in range(len(wishlisted[w][1])):
                                    if topGameNames[i - viewAmount].lower() in (game.lower() for game in wishlisted[w][1][m][1]) and round(viewerRatioMedianRatioSorted[i - viewAmount]) > 100:
                                        print('\033[33m' + printString + '\033[0m')
                                        wishlistedGameBreaker = True
                                        break
                                if wishlistedGameBreaker:
                                    break
            print(str(totalGames) + 'g have ' + str(totalViewers) + 'v watching s ' + str(totalStreams) + ' with an avgvrat of: ' + str(round(totalViewerRatio / totalGames, 2)) + ", the s at " + str(casterPercentage) + "% of the cat has an avg of " + str(round(totalViewersMedian / totalGames)) + "v and an avgvmrat of: " + str(round(totalViewerRatioMedianRatio / totalGames)))
            if newGames:
                newGamesReversed = newGames[:]
                newGamesReversed.reverse()
                newGamesPrintList = []
                if len(newGamesReversed) == 1:
                    print("The newest game is: " + newGamesReversed[0])
                else:
                    print("The new games are:")
                    for i, a in enumerate(newGamesReversed):
                        newGamesPrintList.append(a)
                        if i % 10 == 9:
                            print((i - 8), "-", (i + 1), newGamesPrintList)
                            newGamesPrintList = []
                    if not (len(newGamesReversed) % 10) == 0:
                        print((len(newGamesReversed) - (len(newGamesReversed) % 10) + 1), "-",
                              len(newGamesReversed), ", ".join(newGamesPrintList))
    elif not restartLoops:
        printData()
        if firstRun:
            printStrings()
    elif restartLoops:
        printData()
        printStrings()
        firstRun = False
        loops = 0
    now = datetime.datetime.now()
    hours, minutes, seconds = convert_timedelta(now - loopStart)
    print('Data from the last {} minute{}, {} second{}'.format(minutes, 's' if seconds != 1 else '',seconds, 's' if seconds != 1 else ''))
    print("Current time: " + str(now.strftime('%H:%M:%S')))
