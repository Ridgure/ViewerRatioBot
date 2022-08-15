#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioBot.py

import datetime
import math
import requests
from ViewerRatioConfig import *
from ViewerRatioLists import *
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

# Debug variable
testing = False

def getMoreGameViewers():
    global pagination
    global topGameViewers
    urlGameViewers = "https://api.twitch.tv/helix/streams?first=100&language=en&game_id=" + topGameIds[-1] + "&after=" + pagination
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
        print("raw streamed games are: " + str(len(topGameIds)) + " " + str(topGameNames))


def getMoreStreams(i):
    try:
        global pagination
        global gameViewers
        global gameStreams
        global medianList
        global dropsGames
        urlMore = "https://api.twitch.tv/helix/streams?first=100&language=en&game_id=" + topGameIds[i] + "&after=" + pagination
        paramsMore = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        r = requests.get(urlMore, headers=paramsMore).json()
        if not r['pagination'] == {}:
            pagination = r['pagination']['cursor']
            gameStreams[i] = str(int(gameStreams[i]) + int(len(r['data'])))
            for a in r['data']:
                gameViewers[i] = str(int(gameViewers[i]) + int(a['viewer_count']))
                medianList[i].append(int(a['viewer_count']))
                if not a['tag_ids'] is None:
                    if 'c2542d6d-cd10-4532-919b-3d19f30a768b' in a['tag_ids']:
                        if not a['game_id'] in dropsGames:
                            dropsGames.append(e['game_id'])
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
    for i in range(len(topGameIds)):
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
                if (int(gameStreamsLooped[h]) / loops) < minStreams:
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
        if not existingGame:
            gameViewersLooped.append(gameViewers[i])
            if (int(gameViewersLooped[-1]) / loops) < minViewers:
                gameViewersLooped[-1] = "0"
            gameStreamsLooped.append(gameStreams[i])
            if (int(gameStreamsLooped[-1]) / loops) < minStreams:
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
            if viewerRatioMedianRatioLoopedAverage > 0:
                worthGames = worthGames + 1
                printString = (str(viewAmount - i) + ". " + hostGamesLoopedPrinted[i - viewAmount] + " has " +
                               str(round(gameViewersLoopedAverage)) + " viewers watching " +
                               str(round(gameStreamsLoopedAverage)) + " streams with a viewer ratio of: " +
                               str(round(gameViewerRatioLoopedAverage, 2)) + " and the stream at " + str(casterPercentage) + "% of the category has " +
                               str(round(gameViewersMedianLoopedAverage, 2)) + " viewers and a viewer to median ratio of: " +
                               str(round(viewerRatioMedianRatioLoopedAverage)))
                if hostGamesLoopedPrinted[i - viewAmount] in favoriteGames:
                    print('\033[1m' + printString + '\033[0m')
                else:
                    print(printString)
    print("Favorite games:")
    for i in range(viewAmount):
        if hostGamesLoopedPrinted[i - viewAmount] in favoriteGames:
            gameViewersLoopedAverage = int(gameViewersLoopedPrinted[i - viewAmount]) / loops
            gameStreamsLoopedAverage = int(gameStreamsLoopedPrinted[i - viewAmount]) / loops
            gameViewerRatioLoopedAverage = gameViewerRatioLoopedPrinted[i - viewAmount]
            gameViewersMedianLoopedAverage = gameViewersMedianLoopedPrinted[i - viewAmount] / loops
            if gameViewersMedianLoopedAverage == 0:
                viewerRatioMedianRatioLoopedAverage = 0
            else:
                viewerRatioMedianRatioLoopedAverage = viewerRatioMedianRatioLoopedSorted[i - viewAmount] / loops
            if viewerRatioMedianRatioLoopedAverage > 0:
                print(
                    str(viewAmount - i) + ". " + hostGamesLoopedPrinted[i - viewAmount] + " has " +
                    str(round(gameViewersLoopedAverage)) + " viewers watching " +
                    str(round(gameStreamsLoopedAverage)) + " streams with a viewer ratio of: " +
                    str(round(gameViewerRatioLoopedAverage, 2)) + " and the stream at " + str(casterPercentage) + "% of the category has " +
                    str(round(gameViewersMedianLoopedAverage, 2)) + " viewers and a viewer to median ratio of: " +
                    str(round(viewerRatioMedianRatioLoopedAverage))
                )
    print(str(worthGames) + ' games worth streaming')


def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds

# Print new blacklist additions
if not newBlacklistAdditions == []:
    if testing:
        print("Getting blacklist game ids")
    for i in range(len(newBlacklistAdditions)):
        url = "https://api.twitch.tv/helix/games?name=" + newBlacklistAdditions[i]
        params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
        r = requests.get(url, headers=params).json()
        newBlacklistAdditions[i] = [newBlacklistAdditions[i], r['data'][0]['id']]
    if newBlacklistAdditions:
        print("New blacklist additions are: " + str(newBlacklistAdditions))
else:
    if testing:
        print("Blacklist is empty")

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

        print("Getting streamed games")
        if loops == 0:
            loopStart = datetime.datetime.now()
        getMoreGames()
        if testing:
            print("Streamed games have been gotten")

        # Extract id from blacklist
        blacklistIds = []
        for i in range(len(blacklist)):
            blacklistIds.append(blacklist[i][1])

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
        if loops > 0:
            if testing:
                print("The top game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
                print("The top game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
            for i in range(len(topGameIdsLooped)):
                if not topGameIdsLooped[i] in topGameIds:
                    topGameIds.append(topGameIdsLooped[i])
                    topGameNames.append(hostGamesLooped[i])

        if testing:
            print("The top game names are: " + str(len(topGameNames)) + " " + str(topGameNames))
            print("The top game ids are: " + str(len(topGameIds)) + " " + str(topGameIds))
        try:
            for i in range(len(topGameIds)):
                if testing:
                    if i == 0:
                        print('Getting info for games')
                    if topGameNames[i] == 'Minecraft':
                        print("Getting info for Minecraft")
                url = "https://api.twitch.tv/helix/streams?first=100&language=en&game_id=" + topGameIds[i]
                params = {"Client-ID": "" + ClientID + "", "Authorization": "Bearer " + FollowerToken}
                r = requests.get(url, headers=params).json()
                gameStreams.append("0")
                gameViewers.append("0")
                medianList.append([])
                if r['pagination'] == {}:
                    gameStreams[i] = str(int(gameStreams[i]) + len(r['data']))
                    for e in r['data']:
                        gameViewers[i] = str(int(gameViewers[i]) + int(e['viewer_count']))
                        medianList[i].append(int(e['viewer_count']))
                        if not e['tag_ids'] is None:
                            if 'c2542d6d-cd10-4532-919b-3d19f30a768b' in e['tag_ids']:
                                if not e['game_id'] in dropsGames:
                                    dropsGames.append(e['game_id'])
                else:
                    gameStreams[i] = str(int(gameStreams[i]) + len(r['data']))
                    for e in r['data']:
                        gameViewers[i] = str(int(gameViewers[i]) + int(e['viewer_count']))
                        medianList[i].append(int(e['viewer_count']))
                        if not e['tag_ids'] is None:
                            if 'c2542d6d-cd10-4532-919b-3d19f30a768b' in e['tag_ids']:
                                if not e['game_id'] in dropsGames:
                                    dropsGames.append(e['game_id'])
                    pagination = r['pagination']['cursor']
                    getMoreStreams(i)
                if testing:
                    if topGameNames[i] == 'Minecraft':
                        print("Info for Minecraft has been gotten")
                if int(gameStreams[i]) < minStreams:
                    gameViewersMedian.append(0)
                else:
                    casterPercentile = (len(medianList[i]) - (math.trunc(len(medianList[i]) * (casterPercentage / 100))))
                    if len(medianList[i]) < minStreams:
                        median = 0
                    else:
                        median = medianList[i][casterPercentile]
                    gameViewersMedian.append(median)
                if firstRun:
                    if i % 50 == 0:
                        print(str(i) + " of " + str(len(topGameIds)))
                    if (i + 1) == len(topGameIds):
                        print(str(len(topGameIds)) + " of " + str(len(topGameIds)))
                else:
                    if i % 100 == 0:
                        print(str(i) + " of " + str(len(topGameIds)))
                    if (i + 1) == len(topGameIds):
                        print(str(len(topGameIds)) + " of " + str(len(topGameIds)))
        except Exception as e:
            print("Error in getting streamed games")
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
        if testing:
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print("Minecraft has: " + str(gameViewers[i]) + " viewers")

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
        if testing:
            for i in range(len(topGameIds)):
                if topGameNames[i] == 'Minecraft':
                    print("Minecraft has: " + str(gameViewers[i]) + " viewers")

    for i in range(len(topGameIds)):
            if int(gameViewers[i]) < minViewers:
                gameViewers[i] = "0"
            if int(gameStreams[i]) < minStreams:
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
    loopAmount = 3
    loops = loops + 1
    worthGames = 0
    now = datetime.datetime.now()
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
                    print("Minecraft has: " + str(gameViewers[i]) + " viewers")

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
                    print("Minecraft has: " + str(gameViewers[i]) + " viewers")

        if firstRun:
            for i in range(viewAmount):
                if viewerRatioMedianRatioSorted[i - viewAmount] > 0:
                    worthGames = worthGames + 1
                    printString = (str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                                   str(round(int(gameViewers[i - viewAmount]))) + " viewers watching " +
                                   str(round(int(gameStreams[i - viewAmount]))) + " streams with a viewer ratio of: " +
                                   str(round(gameViewerRatio[i - viewAmount], 2)) + " and the stream at " + str(casterPercentage) + "% of the category has " +
                                   str(round(gameViewersMedian[i - viewAmount], 2)) + " viewers and a viewer to median ratio of: " +
                                   str(round(viewerRatioMedianRatioSorted[i - viewAmount])))
                    if topGameNames[i - viewAmount] in favoriteGames:
                        print('\033[1m' + printString + '\033[0m')
                    else:
                        print(printString)
            print("Favorite games:")
            for i in range(viewAmount):
                if viewerRatioMedianRatioSorted[i - viewAmount] > 0:
                    if topGameNames[i - viewAmount] in favoriteGames:
                        print(
                            str(viewAmount - i) + ". " + topGameNames[i - viewAmount] + " has " +
                            str(round(int(gameViewers[i - viewAmount]))) + " viewers watching " +
                            str(round(int(gameStreams[i - viewAmount]))) + " streams with a viewer ratio of: " +
                            str(round(gameViewerRatio[i - viewAmount], 2)) + " and the stream at " + str(casterPercentage) + "% of the category has " +
                            str(round(gameViewersMedian[i - viewAmount], 2)) + " viewers and a viewer to median ratio of: " +
                            str(round(viewerRatioMedianRatioSorted[i - viewAmount]))
                        )
            print(str(worthGames) + ' games worth streaming')
    elif 0 < loops < loopAmount:
        printData()
        if firstRun:
            printStrings()
    elif loops == loopAmount:
        printData()
        printStrings()
        firstRun = False
        loops = 0
    hours, minutes, seconds = convert_timedelta(now - loopStart)
    print('Data from the last {} minute{}, {} seconds{}'.format(minutes, 's' if seconds != 1 else '',seconds, 's' if seconds != 1 else ''))
    print("Current time: " + str(now.strftime('%H:%M:%S')))
