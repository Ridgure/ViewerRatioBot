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
global tagIds
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
tagIds = []
combinedTags = []
newBlacklistAdditions = []

# Debug variable
testing = False
testGame = 'Tibia'

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
for g in range(len(favoriteGames)):
    f.writelines('\n**' + favoriteGames[g][0] + ':**')
    f.writelines('\n' + ', '.join(favoriteGames[g][1]))
    f.writelines('\n')
f.writelines('\n<a href="#white-black-list">Back to top</a>')
f.writelines('\n## Whitelist:')
f.writelines('\n')
for w in range(len(wishlisted)):
    f.writelines('\n**' + wishlisted[w][0] + ':**')
    f.writelines('\n' + ', '.join(wishlisted[w][1]))
    f.writelines('\n')
f.writelines('\n<a href="#white-black-list">Back to top</a>')
f.writelines('\n## Blacklist:')
f.writelines('\n')
for b in range(len(blacklist)):
    f.writelines('\n**' + blacklist[b][0] + ':**')
    blacklistedGames = []
    for g in range(len(blacklist[b][1])):
        blacklistedGames.append(blacklist[b][1][g][0])
    f.writelines('\n' + ', '.join(blacklistedGames))
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
    elif testing:
        print("Raw streamed games are: " + str(len(topGameIds)) + " " + str(topGameNames))


def getMoreStreams(i):
    try:
        global pagination
        global gameViewers
        global gameStreams
        global medianList
        global dropsGames
        urlMore = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[i] + "&after=" + pagination
        paramsMore = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        r = requests.get(urlMore, headers=paramsMore).json()
        if not r['pagination'] == {}:
            pagination = r['pagination']['cursor']
            gameStreams[i] = str(int(gameStreams[i]) + int(len(r['data'])))
            for e in r['data']:
                if testing:
                    if e['game_id'] == 'Lineage 2':
                        print(e['user_name'])
                startedAt = e['started_at']
                year, month, day, hour, minute, second = int(startedAt[0:4]), int(startedAt[5:7]), int(startedAt[8:10]), int(startedAt[11:13]), int(startedAt[14:16]), int(startedAt[17:19])
                startedAt = datetime.datetime(year, month, day, hour, minute, second)
                now = datetime.datetime.now()
                hours, minutes, seconds = convert_timedelta(now - startedAt)
                if not e['tag_ids'] is None:
                    for h in range(len(e['tag_ids'])):
                        if not e['tag_ids'][h] in tagIds:
                            tagIds.append(e['tag_ids'][h])
                if not hours > 18:
                    if not e['user_name'] in blacklistedStreams:
                        blacklisted = False
                        if not e['tag_ids'] is None:
                            for b in range(len(blacklistedTags)):
                                if e['tag_ids'] == blacklistedTags[b][1]:
                                    blacklisted = True
                                    break
                            if 'c2542d6d-cd10-4532-919b-3d19f30a768b' in e['tag_ids']:
                                if not e['game_id'] in dropsGames:
                                    dropsGames.append(e['game_id'])
                        for b in range(len(blacklistedTitles)):
                            if b == 0:
                                for t in range(len(blacklistedTitles[b][1])):
                                    if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                        blacklisted = True
                                        break
                            elif e['game_name'] == blacklistedTitles[b][0]:
                                for t in range(len(blacklistedTitles[b][1])):
                                    if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                        blacklisted = True
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
                        if not blacklisted:
                            gameViewers[i] = str(int(gameViewers[i]) + int(e['viewer_count']))
                            medianList[i].append(int(e['viewer_count']))
                            if testing:
                                if e['game_name'].lower() == testGame:
                                    print(e['game_name'] + " streamer " + e['user_name'].lower() + " has " + str(
                                        e['viewer_count']) + " viewers  for a total of " + str(gameViewers[i]) + " viewers so far")
            getMoreStreams(i)
    except Exception as x:
        print(x)
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
    if testing:
        print("Before math has been done")
        print(len(topGameNames), topGameNames)
        print(len(topGameIds), topGameIds)
        print(len(hostGamesLooped), hostGamesLooped)
        print(len(topGameIdsLooped), topGameIdsLooped)
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
    if testing:
        print("After math has been done")
        print(testExist, testNonExist)
        print(len(topGameNames), topGameNames)
        print(len(topGameIds), topGameIds)
        print(len(hostGamesLooped), hostGamesLooped)
        print(len(topGameIdsLooped), topGameIdsLooped)


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
                elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 300:
                    print('\033[32m' + printString + '\033[0m')
                else:
                    print(printString)
            elif viewerRatioMedianRatioLoopedAverage > 0:
                newGameLooped = False
                printed = False
                favoriteGame = False
                wishlistedGame = False
                for f in range(len(favoriteGames)):
                    if hostGamesLoopedPrinted[i - viewAmount] in favoriteGames[f][1]:
                        if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                            print('\033[34m' + printString + '\033[0m')  # Blue
                        else:
                            print('\033[32m' + printString + '\033[0m')  # Green
                        favoriteGame = True
                        break
                if not favoriteGame:
                    for w in range(len(wishlisted)):
                        if hostGamesLoopedPrinted[i - viewAmount] in wishlisted[w][1]:
                            if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                print('\033[34m' + printString + '\033[0m')  # Blue
                            else:
                                print('\033[33m' + printString + '\033[0m')  # Yellow
                            wishlistedGame = True
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
            elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 300:
                print('\033[32m' + printString + '\033[0m')
            else:
                print(printString)
        elif viewerRatioMedianRatioLoopedAverage > 0:
            for f in range(len(favoriteGames)):
                if hostGamesLoopedPrinted[i - viewAmount] in favoriteGames[f][1]:
                    if viewerRatioMedianRatioLoopedAverage >= 1000:
                        print('\033[34m' + printString + '\033[0m')
                    elif 1000 > viewerRatioMedianRatioLoopedAverage > 300:
                        print('\033[32m' + printString + '\033[0m')
                    else:
                        print(printString)
                    break
            for w in range(len(favoriteGames)):
                if hostGamesLoopedPrinted[i - viewAmount] in wishlisted[w][1] and viewerRatioMedianRatioLoopedAverage > 300:
                    print('\033[33m' + printString + '\033[0m')
                    break
    print(str(totalGames) + 'g have ' + str(totalViewers) + 'v watching s ' + str(totalStreams) + ' with an avgvrat of: ' + str(round(totalViewerRatio / totalGames, 2)) + ", the s at " + str(casterPercentage) + "% of the cat has an avg of " + str(round(totalViewersMedian / totalGames)) + "v and an avgvmrat of: " + str(round(totalViewerRatioMedianRatio / totalGames)))
    if newGames:
        newGamesReversed = newGames[:]
        newGamesReversed.reverse()
        print("The new games are: " + str(newGamesReversed))
    if combinedTags:
        print("New tags are: " + str(combinedTags))

    hostGamesLoopedPrintedReversed = hostGamesLoopedPrinted[:]
    hostGamesLoopedPrintedReversed.reverse()
    # Write games to a txt file
    f = open("tmpfile.py", "w", encoding='utf-8')
    f.writelines("# !/usr/bin/env python")
    f.writelines("\n# -*- coding: utf-8 -*-")
    f.writelines("\n# output.py")
    f.writelines("\nhostGames = " + str(hostGamesLoopedPrintedReversed))
    f.writelines("\nnewGames = " + str(newGames))
    f.writelines("\ncombinedTags = " + str(combinedTags))
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
            blacklistedGameAmount = blacklistedGameAmount + len(blacklist[b][1])
        for f in range(len(favoriteGames)):
            favoriteGameAmount = favoriteGameAmount + len(favoriteGames[f][1])
        for w in range(len(wishlisted)):
            wishlistedGameAmount = wishlistedGameAmount + len(wishlisted[w][1])
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
                quit()
    if newBlacklistAdditions:
        print("New blacklist additions are: " + str(newBlacklistAdditions))
else:
    if testing:
        print("No new blacklist additions")
        url = "https://api.twitch.tv/helix/games?name=KartRider"
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
            for a in range(len(blacklist[i][1])):
                blacklistIds.append(blacklist[i][1][a][1])

        # Remove blacklisted games
        topGameIdsTemp = []
        topGameNamesTemp = []
        for i in range(len(topGameIds)):
            if not topGameIds[i] in blacklistIds:
                topGameIdsTemp.append(topGameIds[i])
                topGameNamesTemp.append(topGameNames[i])
        topGameIds = topGameIdsTemp
        topGameNames = topGameNamesTemp

        # Add games that were not included
        existingGame = False
        if loops > 0:
            if testing:
                print("The new top game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
                print("The old top game names are: " + str(len(hostGamesLooped)) + " " + str(hostGamesLooped))
                print("The new top game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
                print("The old top game ids are: " + str(len(topGameIdsLooped)) + " " + str(topGameIdsLooped))
            for i in range(len(topGameIdsLooped)):
                for t in range(len(topGameIds)):
                    if topGameIdsLooped[i] == topGameIds[t]:
                        existingGame = True
                if not existingGame:
                    topGameIds.append(topGameIdsLooped[i])
                    topGameNames.append(hostGamesLooped[i])

        if testing:
            print("The added game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
            print("The added game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
        try:
            for i in range(len(topGameIds)):
                if testing:
                    if i == 0:
                        print('Getting info for games')
                    if topGameNames[i] == testGame:
                        print("Getting info for " + testGame)
                url = "https://api.twitch.tv/helix/streams?first=100&language=en&language=other&game_id=" + topGameIds[i]
                params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
                r = requests.get(url, headers=params).json()
                gameStreams.append("0")
                gameViewers.append("0")
                medianList.append([])
                if r['pagination'] == {}:
                    gameStreams[i] = str(int(gameStreams[i]) + len(r['data']))
                    for e in r['data']:
                        startedAt = e['started_at']
                        year, month, day, hour, minute, second = int(startedAt[0:4]), int(startedAt[5:7]), int(startedAt[8:10]), int(startedAt[11:13]), int(startedAt[14:16]), int(startedAt[17:19])
                        startedAt = datetime.datetime(year, month, day, hour, minute, second)
                        now = datetime.datetime.now()
                        hours, minutes, seconds = convert_timedelta(now - startedAt)
                        if not hours > 18:
                            if not e['user_name'] in blacklistedStreams:
                                blacklisted = False
                                if not e['tag_ids'] is None:
                                    for b in range(len(blacklistedTags)):
                                        if e['tag_ids'] == blacklistedTags[b][1]:
                                            blacklisted = True
                                            break
                                    if 'c2542d6d-cd10-4532-919b-3d19f30a768b' in e['tag_ids']:
                                        if not e['game_id'] in dropsGames:
                                            dropsGames.append(e['game_id'])
                                for b in range(len(blacklistedTitles)):
                                    if b == 0:
                                        for t in range(len(blacklistedTitles[b][1])):
                                            if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                                blacklisted = True
                                                break
                                    elif e['game_name'] == blacklistedTitles[b][0]:
                                        for t in range(len(blacklistedTitles[b][1])):
                                            if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
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
                                            if re.search('(' + blacklistedPartialStreams[b][1][t][0].lower() + ').*(' + blacklistedPartialStreams[b][1][t][1].lower() + ')', e['user_name'].lower()):
                                                blacklisted = True
                                                break
                                if not blacklisted:
                                    gameViewers[i] = str(int(gameViewers[i]) + int(e['viewer_count']))
                                    medianList[i].append(int(e['viewer_count']))
                                    if testing:
                                        if e['game_name'].lower() == testGame:
                                            print(e['game_name'] + " streamer " + e['user_name'].lower() + " has " + str(e['viewer_count']) + " viewers for a total of " + str(gameViewers[i]) + " viewers so far")
                else:
                    gameStreams[i] = str(int(gameStreams[i]) + len(r['data']))
                    for e in r['data']:
                        startedAt = e['started_at']
                        year, month, day, hour, minute, second = int(startedAt[0:4]), int(startedAt[5:7]), int(startedAt[8:10]), int(startedAt[11:13]), int(startedAt[14:16]), int(startedAt[17:19])
                        startedAt = datetime.datetime(year, month, day, hour, minute, second)
                        now = datetime.datetime.now()
                        hours, minutes, seconds = convert_timedelta(now - startedAt)
                        if not hours > 18:
                            if not e['user_name'] in blacklistedStreams:
                                blacklisted = False
                                if not e['tag_ids'] is None:
                                    for b in range(len(blacklistedTags)):
                                        if e['tag_ids'] == blacklistedTags[b][1]:
                                            blacklisted = True
                                            break
                                    if 'c2542d6d-cd10-4532-919b-3d19f30a768b' in e['tag_ids']:
                                        if not e['game_id'] in dropsGames:
                                            dropsGames.append(e['game_id'])
                                for b in range(len(blacklistedTitles)):
                                    if b == 0:
                                        for t in range(len(blacklistedTitles[b][1])):
                                            if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
                                                blacklisted = True
                                                break
                                    elif e['game_name'] == blacklistedTitles[b][0]:
                                        for t in range(len(blacklistedTitles[b][1])):
                                            if re.search(blacklistedTitles[b][1][t].lower(), e['title'].lower()):
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
                                                        if topGameNames[i] == 'Tibia':
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
                                    if testing:
                                        if e['game_name'].lower() == testGame:
                                            print(e['game_name'] + " streamer " + e['user_name'].lower() + " has " + str(e['viewer_count']) + " viewers for a total of " + str(gameViewers[i]) + " viewers so far")
                    pagination = r['pagination']['cursor']
                    getMoreStreams(i)
                if testing:
                    if topGameNames[i] == 'Minecraft':
                        print("Info for Minecraft has been gotten")
                    if topGameNames[i] == testGame:
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
    except Exception as x:
        print(x)
    except requests.exceptions.ConnectTimeout:
        print("timeout", url)
    except KeyboardInterrupt:
        print('Keyboard interrupt exception is caught')

    if testing:
        print("Before drop removal")
        print(len(topGameNames), topGameNames)
        print(len(gameViewers), gameViewers)
        print(len(topGameIds), topGameIds)
        for g in range(len(topGameIds)):
            if topGameNames[g] == 'Minecraft':
                print(topGameNames[g] + " has: " + str(gameViewers[g]) + " viewers")
            if topGameNames[g] == testGame:
                print(topGameNames[g] + " has: " + str(gameViewers[g]) + " viewers")

    newKeys = []
    newTags = []
    for t in range(len(tagIds)):
        newTag = True
        for w in range(len(whitelistedTags)):
            if tagIds[t] == whitelistedTags[w][1]:
                newTag = False
        if newTag:
            for b in range(len(blacklistedTags)):
                if tagIds[t] == blacklistedTags[b][1]:
                    newTag = False
        if newTag:
            for c in range(len(combinedTags)):
                if tagIds[t] == combinedTags[c][1]:
                    newTag = False
        if newTag:
            urlTags = "https://api.twitch.tv/helix/tags/streams?tag_id=" + tagIds[t]
            paramsTags = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
            r = requests.get(urlTags, headers=paramsTags).json()
            newTags.append(tagIds[t])
            newKeys.append(r['data'][0]['localization_names']['en-us'])
    for i in range(len(newKeys)):
        combinedTags.append([newKeys[i], newTags[i]])

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
        print(len(topGameNames), topGameNames)
        print(len(gameViewers), gameViewers)
        print(len(topGameIds), topGameIds)
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

        if testing:
            print(topGameNames)
            print(gameViewers)
            print(gameStreams)

        # Sort by all lists by viewerRatioMedianRatio
        dummy = []
        dummy[:], topGameNames[:] = zip(*sorted(zip(viewerRatioMedianRatio, topGameNames), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewers[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameViewers), key=lambda p: (p[0], p[1])))
        dummy[:], gameStreams[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameStreams), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewerRatio[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameViewerRatio), key=lambda p: (p[0], p[1])))
        dummy[:], gameViewersMedian[:] = zip(*sorted(zip(viewerRatioMedianRatio, gameViewersMedian), key=lambda p: (p[0], p[1])))
        viewerRatioMedianRatioSorted[:] = sorted(viewerRatioMedianRatioSorted)
        if testing:
            print(topGameNames)
            print(gameViewers)
            print(gameStreams)
            print(viewerRatioMedianRatio)

        if testing:
            print("After sorting")
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")
                if topGameNames[i] == testGame:
                    print(topGameNames[i] + " has: " + str(gameViewers[i]) + " viewers")

        if firstRun:
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
                        if topGameNames[i - viewAmount] in favoriteGames[f][1]:
                            print('\033[32m' + printString + '\033[0m')
                            favoriteGame = True
                            break
                    if not favoriteGame:
                        for w in range(len(wishlisted)):
                            if topGameNames[i - viewAmount] in wishlisted[w][1]:
                                print('\033[33m' + printString + '\033[0m')
                                wishlistedGame = True
                                break
                    if not favoriteGame and not wishlistedGame:
                        newGame = True
                        for n in range(len(newGames)):
                            if newGames[n] == topGameNames[i - viewAmount]:
                                newGame = False
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
                    elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 300:
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
                        if topGameNames[i - viewAmount] in favoriteGames[f][1]:
                            if round(viewerRatioMedianRatioSorted[i - viewAmount]) >= 1000:
                                print('\033[34m' + printString + '\033[0m')
                            elif 1000 > round(viewerRatioMedianRatioSorted[i - viewAmount]) > 300:
                                print('\033[32m' + printString + '\033[0m')
                            else:
                                print(printString)
                            favoriteGame = True
                            break
                    if not favoriteGame:
                        for w in range(len(wishlisted)):
                            if topGameNames[i - viewAmount] in wishlisted[w][1] and round(viewerRatioMedianRatioSorted[i - viewAmount]) > 300:
                                print('\033[33m' + printString + '\033[0m')
                                break
            print(str(totalGames) + 'g have ' + str(totalViewers) + 'v watching s ' + str(totalStreams) + ' with an avgvrat of: ' + str(round(totalViewerRatio / totalGames, 2)) + ", the s at " + str(casterPercentage) + "% of the cat has an avg of " + str(round(totalViewersMedian / totalGames)) + "v and an avgvmrat of: " + str(round(totalViewerRatioMedianRatio / totalGames)))
            if newGames:
                newGamesReversed = newGames[:]
                newGamesReversed.reverse()
                print("The new games are: " + str(newGamesReversed))
            if combinedTags:
                print("New tags are: " + str(combinedTags))
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
