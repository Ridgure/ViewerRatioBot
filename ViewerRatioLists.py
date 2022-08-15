#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioLists.py

blacklist = [
    # Shooter games
    ['aim gods', '516967'], ['aim lab', '503456'],  ['anthem', '460696'],
    ['apex legends', '511224'], ['battlefield 1', '488500'], ['battlefield 2', '15467'], ['battlefield 2042', '514974'],
    ['battlefield 3', '24394'], ['battlefield 4', '66402'], ['battlefield v', '504199'],
    ['battlefield: bad company 2', '22851'], ['call of duty: black ops 4', '504462'],
    ['call of duty: black ops cold war', '512709'], ['call of duty: black ops ii', '34134'],
    ['call of duty: black ops iii', '489401'], ['call of duty: mobile', '512818'],
    ['call of duty: modern warfare', '1614555304'], ['call of duty: modern warfare 2', '22393'],
    ['call of duty: modern warfare remastered', '494155'], ['call of duty: vanguard', '492778073'],
    ['call of duty: warzone', '512710'], ['call of duty: wwii', '496712'],
    ['counter-strike: global offensive', '32399'], ['battlebit', '496916'], ['cruelty squad', '977894696'],
    ['destiny 2', '497057'], ['doom eternal', '506442'], ['escape from tarkov', '491931'], ['deathloop', '512983'],
    ['fallout 76', '506246'], ['f.e.a.r. perseus mandate', '14310'], ['gears 5', '506407'], ['Fallout 4', '489776'],
    ['grand theft auto iv: the ballad of gay tony', '2113221108'], ['grand theft auto v', '32982'], ['gtfo', '500627'],
    ['gunfire reborn', '517645'], ['gunz: the duel', '513567'], ['hitman', '491471'], ['hitman 3', '518011'],
    ['hell let loose', '497440'], ['hunt: showdown', '500188'], ['hyper scape', '518306'],
    ['insurgency: sandstorm', '491705'], ['max payne 3', '21222'], ['metal gear rising: revengeance', '24208'],
    ['metal gear solid', '14805'], ['metal gear solid 2: sons of liberty', '11386'], ['Metal Gear Acid', '8798'],
    ['metal gear solid 3: snake eater', '16582'], ['metal gear solid 4: guns of the patriots', '18893'],
    ['metro exodus', '497410'], ['mass effect legendary edition', '1568081763'], ['metroid prime 2: echoes', '1459'],
    ['payday 2', '65997'], ['outriders', '512930'], ['quake', '7348'], ['quake champions', '496253'],
    ['splitgate', '499310'], ['squad', '488479'], ['star wars battlefront ii', '492546'],
    ['returnal', '518019'], ['rogue company', '514194'], ['sniper elite 5', '511743'], ['team fortress 2', '16676'],
    ['the last of us', '33180'], ['the last of us part ii', '494552'], ["tom clancy's rainbow six siege", '460630'],
    ["tom clancy's rainbow six: siege", '460630'], ["tom clancy's the division", '369579'],
    ["tom clancy's the division 2", '504463'], ['titanfall 2', '489201'], ['Quake Live', '19490'],
    ['totally accurate battlegrounds', '506344'], ['true crime: new york city', '3077'], ['Adaca', '544704748'],
    ['Grand Theft Auto: San Andreas', '6521'], ['Uncharted 2: Among Thieves', '20357'], ['BIGFOOT', '6675'],
    ['Mass Effect 3', '26992'], ['S.T.A.L.K.E.R.: Anomaly', '1549167076'], ['Destiny', '280721'],
    ['DOOM II: Hell on Earth', '584'], ['Fallout: New Vegas', '23453'], ['Grand Theft Auto: Vice City', '15631'],
    ['Call of Duty: Black Ops', '23894'], ['Mafia II: Definitive Edition', '2058566581'], ['Gran Turismo 7', '518014'],
    ['Arma 3', '31750'], ['Far Cry 5', '497078'], ["Tom Clancy's Ghost Recon: Wildlands", '490379'], ['DOOM', '6715'],
    ['Grand Theft Auto III', '3412'], ['Crossfire', '27101'], ['Overwatch 2', '515025'],
    ['Family Battle: Tag Arena', '1871077473'], ['Zero Sievert', '324194362'], ['SCUM', '495811'],
    ['The Last of Us Remastered', '1200871695'], ['MechWarrior Online', '24623'], ['MetaOps', '1220570282'],
    ['Call of Duty 4: Modern Warfare', '1964'], ['APB Reloaded', '19157'], ['Krunker', '508391'],
    ['theHunter: Call of the Wild', '494683'], ['Evil Dead: The Game', '1022719138'], ['Mafia III', '490432'],
    ['Counter-Strike: Source', '10407'], ['Sudden Attack', '29068'], ['Borderlands', '18734'],
    ['Grand Theft Auto: San Andreas – The Definitive Edition', '89250567'], ['Holdfast: Nations At War', '498983'],
    ["Tom Clancy's Ghost Recon: Breakpoint", '512534'], ['MechWarrior 5: Mercenaries', '494684'],
    ['Grand Theft Auto: Vice City – The Definitive Edition', '957103328'], ['Ready or Not', '511701'],
    ['Call of Duty: Infinite Warfare', '491437'], ['Way of the Hunter', '489308483'], ['Prey', '15013'],
    ["Tom Clancy's Rainbow Six Extraction", '513004'], ['Deadpool', '509509'], ['Half-Life 2', '1420'],
    ["KovaaK's Aim Trainer", '510911'], ['Metal Gear Survive', '498026'], ['Counter-Strike', '10710'],
    ['Uncharted: The Lost Legacy', '494558'], ['World War Z: Aftermath', '1280358639'], ['Borderlands 2', '32345'],
    ['Days Gone', '497456'], ['ULTRAKILL', '514166'], ['Quake II', '2955'], ["Uncharted 4: A Thief's End", '458641'],
    ['Call of Duty 2', '2162'],
    # Bossfights
    ['bloodborne', '460636'], ['dark souls', '29433'], ['dark souls iii', '490292'], ['dark souls ii', '91423'],
    ['Elden Ring', '512953'], ["demon's souls", '21812'], ['hellpoint', '496421'], ['left 4 dead 2', '24193'],
    ['mortal shell', '516915'], ['nioh 2', '506468'], ['nioh 2: the complete edition', '160136078'],
    ['sekiro: shadows die twice', '506415'], ['the surge', '496233'], ['black mesa', '68016'],
    ['Company of Heroes 2', '65663'], ['Evolve Stage 2', '1893365738'], ['Metro: Last Light', '31836'],
    ['Dark Souls: Remastered', '1122982998'], ['Grand Theft Auto IV', '18707'], ['Fallout 3', '18763'],
    # Medieval fights
    ['chivalry 2', '512971'], ['for honor', '490382'], ['ghost of tsushima', '499856'], ['mordhau', '498859'],
    ['sifu', '506089309'], ['Warhammer: Vermintide 2', '498668'], ['Mortal Online 2', '517282'],
    # Violent Survival
    ['dayz', '65632'], ['SurrounDead', '750209762'], ['Lost Light', '1706428735'],
    # Fist fighting
    ['yakuza', '6571'], ['yakuza 0', '476269'], ['yakuza 5', '32541'], ['yakuza 6: the song of life', '490701'],
    ['yakuza: like a dragon', '512121'], ['lost judgment', '2120403770'], ['sleeping dogs', '26547'],
    ['Yakuza Kiwami 2', '498510'], ['Judgment', '509482'], ['Yakuza Kiwami', '490702'],
    # Drama
    ['among us', '510218'], ['Politics', '515214'], ['Gang Beasts', '459527'],
    # Horror
    ['back 4 blood', '511746'], ['resident evil 2', '8645'], ['resident evil 3: nemesis', '5126'],
    ['resident evil 7 biohazard', '492934'], ['resident evil village', '518017'], ['the evil within 2', '497437'],
    ['The Mortuary Assistant', '1945673289'], ['madison', '1535635666'], ['Video Horror Society', '642328546'],
    ['Resident Evil 5', '18808'], ['Silent Hill 2', '9891'], ['Resident Evil 6', '33437'], ['SOMA', '458224'],
    ['Melty Blood: Type Lumina', '936945829'], ['Dark Deception', '460018'], ['Resident Evil 3', '649775967'],
    ['Friday the 13th: The Game', '488518'], ['The Backrooms 1998', '624848592'], ['Visage', '494082'],
    ['Resident Evil: Deadly Silence', '352'], ['Poppy Playtime', '2058220722'], ['Forewarned', '783609948'],
    ['Resident Evil 4', '1468'], ['Resident Evil', '5360'], ['The Quarry', '1937599489'], ['Outlast', '73586'],
    ['The Dark Pictures Anthology: Man of Medan', '509249'], ["Five Nights at Freddy's", '418063'],
    ['Heavy Rain', '19423'], ['The Dark Pictures Anthology: House of Ashes', '1274531553'], ['Borderlands 3', '491318'],
    ['Vampire: The Masquerade - Bloodlines', '15062'], ['The Medium', '517401'], ['Amnesia: Rebirth', '516624'],
    ['Alien: Isolation', '458443'], ["Five Nights at Freddy's 4", '489567'], ['Stranger', '228183669'],
    ['Metal Gear Solid V: The Phantom Pain', '91419'], ['Friday the 13th', '19562'], ['Bullet Force', '502060'],
    ['Resident Evil 0', '489721'], ['Labyrinthine', '517528'], ['Ghost Watchers', '790163050'],
    ['Resident Evil 4: Otome Edition', '1638636362'], ['Phasmophobia', '518184'], ['The Beast Inside', '504389'],
    ['Refund Me If You Can', '866831809'], ["I'm on Observation Duty 5", '1654421360'], ['Deceit', '493244'],
    ['Ghost Exile', '289552769'], ['Silent Hill 3', '9522'], ['Resident Evil 4 HD', '784020615'],
    ['Is Simon There?', '443409039'], ['Silent Hill: Origins', '13206'], ['FOBIA: St. Dinfna Hotel', '2037799395'],
    ['Inside the Backrooms', '1144809661'], ['Amnesia: Rebirth', '516624'], ['Resident Evil Survivor', '14528'],
    ['The Evil Within', '68000'], ['The Evil Within 2', '497437'], ['Escape the Backrooms', '2066107586'],
    ['Resident Evil Resistance', '514308'], ['Song of Horror', '514930'], ['Darkwood', '313146'],
    ['Fear Therapy', '819777302'], ['Silent Hill', '3947'], ['Lunch Lady', '477532253'], ['Pacify', '511134'],
    ['Resident Evil: Revelations', '28576'],
    # Murder mystery
    ['gone home', '65752'], ["Handy Harry's Haunted House Services", '1450669133'],
    # Underwater
    ['Maneater', '506452'],
    # Story
    ['crysis', '10818'], ['death stranding', '494364'], ['far cry', '13564'], ['far cry 6', '518692'],
    ['halo infinite', '506416'], ['halo: reach', '24203'], ['halo: the master chief collection', '417969'],
    ['half-life', '2755'], ['red dead redemption 2', '493959'], ['halo 2', '6511'], ['Tomb Raider', '2770'],
    ['Far Cry: Primal', '490919'], ['Far Cry 3', '29635'], ['Rise of the Tomb Raider', '460620'],
    # Dungeon Crawler
    ['diablo ii', '1041'], ['diablo iii', '313558'], ['diablo iii: reaper of souls', '313558'],
    ['diablo immortal', '510150'], ['path of exile', '29307'], ['warframe', '66170'],
    ['Diablo II: Resurrected', '1788326126'], ['Devil May Cry 5', '506412'],
    # Dialogue game
    ['VA-11 HALL-A: Cyberpunk Bartender Action', '461529'],
    # Hide and seek
    ["garry's mod", '18846'], ['dead by daylight', '491487'], ['Monstrum 2', '519309'], ['Identity V', '508662'],
    ['Propnight', '1342987707'],
    # VR
    ['beat saber', '503116'], ['vrchat', '499003'], ['half-life: alyx', '515195'], ['DCS World', '313331'],
    ['Rec Room', '493280'], ['Pavlov VR', '496142'],
    # Stealth
    ['this land is my land', '512842'],
    # Money
    ['crypto', '499634'], ['horse racing', '6891'], ['poker quest', '308324368'], ['poker', '488190'],
    ['slots', '498566'], ['virtual casino', '29452'], ['Pokémon Trading Card Game Online', '32634'],
    ['Axie Infinity', '508967'], ['Stocks And Bonds', '5899'], ['Pokémon Trading Card Game', '9618'],
    ['Bitcoin', '515880'], ['Casino', '582382910'], ['Blackjack', '2030294088'], ['rFactor 2', '24636'],
    ['Lottery Simulator', '497156'],
    # Weird Sexual
    ['asmr', '509659'], ['pools, hot tubs, and beaches', '116747788'], ['Just Dance 2022', '413353439'],
    ['Hooked on You: A Dead by Daylight Dating Sim', '160028919'], ['Just Dance', '25122'],
    ['Beauty & Body Art', '509669'], ["Love, Money, Rock'n'Roll", '517967'],
    # Weird
    ["I'm Only Sleeping", '498592'], ['just chatting', '509658'], ['twitch plays', '491180'],
    ['watch parties', '515467'], ['Special Events', '509663'], ['Animals, Aquariums, and Zoos', '272263131'],
    ['Travel %26 Outdoors', '509672'], ['Games %2B Demos', '66082'], ['Talk Shows %26 Podcasts', '417752'],
    ['Sleep', '154096350'], ['Tarot', '83418'], ['Food%20%26%20Drink', '509667'], ['EZ2ON REBOOT : R', '2057185004'],
    ['Test, Test', '2070714813'], ['Lost in Play', '181659447'], ['The Simpsons: Hit %26 Run', '2897'],
    ['Bully', '9440'],
    # Weird DMCA
    ['Artifact', '16937'], ['El Chavo', '34054'], ['Movie Night', '753325070'], ['Music', '26936'],
    ['Anime World', '637756067'], ['Always On', '499973'], ['Sexy Miss', '1129360291'], ['The Simpsons', '2046821115'],
    ['Series Makers', '700055046'], ['Radio Station', '2128929587'], ['Karaoke Party', '488782'],
    ['Relaxing Waves', '872742502'], ['South Park', '8105'],
    # Space
    ['elite: dangerous', '80607'], ['kerbal space program', '32742'], ['Starsector', '33416'],
    ['FTL: Faster Than Light', '33882'], ['Star Trek Fleet Command', '510530'],
    # Platformer and 2D fighting
    ['brawlhalla', '460316'], ['dragon ball fighterz', '497385'], ['guilty gear: strive', '517159'],
    ['m.u.g.e.n', '271231'], ['mortal kombat 11', '510578'], ['super smash bros. melee', '16282'],
    ['super smash bros. ultimate', '504461'], ['street fighter v', '488615'], ['tekken 7', '461067'],
    ['Legends of IdleOn', '1935520090'], ['Skullgirls: 2nd Encore', '764537219'], ['Touhou Project', '448375'],
    ['Granblue Fantasy: Versus', '510799'], ['Melty Blood: Type Lumina', '936945829'], ['MultiVersus', '950189725'],
    ['DRAGON BALL Z DOKKAN BATTLE', '489405'], ['SMASH LEGENDS', '519080'], ['DNF Duel', '108763890'],
    ['The King of Fighters XV', '513753'], ['Super Smash Bros. Brawl', '18833'], ['Dino Rex', '27887'],
    ['Super Smash Bros.', '17516'], ['Punch Planet', '494352'], ['Super Mario World', '1229'],
    ['Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles', '1414748474'], ['Skullgirls', '30639'],
    ['Ultimate Marvel vs. Capcom 3', '1336067913'], ['Guilty Gear XX Accent Core Plus R', '491467'],
    ['Ultra Street Fighter IV', '313164'], ['Ultimate Mortal Kombat 3', '1999'], ['SoulCalibur VI', '500626'],
    # Sports
    ['cricket 19', '512623'], ['ea sports ufc 4', '518711'], ['efootball pes 2021 season update', '1520501777'],
    ['fifa 16', '489608'], ['fifa 17', '493091'], ['fifa 18', '495589'], ['fifa 19', '506103'], ['fifa 20', '512804'],
    ['fifa 21', '518204'], ['fifa 22', '1869092879'], ['football manager 2021', '1271244884'],
    ['football manager 2022', '586622463'], ['madden nfl 21', '517406'], ['madden nfl 22', '966064811'],
    ['wwe 2k19', '508289'], ['wwe 2k20', '513681'], ['wwe 2k22', '1199725270'], ['nba 2k21', '518023'],
    ['nba 2k22', '1371363232'], ['nhl 21', '519329'], ['mlb the show 21', '1160459167'], ['pga tour 2k21', '517397'],
    ['slam dunk', '517301'], ['sports', '518203'], ["Tiny Tina's Wonderlands", '1318043161'], ['NHL 22', '13932618'],
    ['Blood Bowl 2', '490177'], ['Out of the Park Baseball 23', '123403711'], ['WWE SuperCard', '461427'],
    ['Fitness%20%26%20Health', '509671'], ['eFootball 2022', '1061323687'], ['MLB The Show 22', '1820819463'],
    ['Russian Fishing 4', '497304'], ['fifa 23', '1745202732'], ['MLB 9 Innings 22', '2038575831'],
    ['WWE Champions', '491560'], ['Fishing Planet', '491117'], ['Italia 1990', '14824'], ['Assetto Corsa', '313197'],
    ['Captain Tsubasa II: Super Striker', '579601296'], ['FIFA Online 4', '504798'],
    ['Pro Soccer Online', '1286420756'], ['NCAA Football 14', '271198'], ['Madden NFL 23', '862021340'],
    # Racing
    ['f1 2020', '517174'], ['f1 2021', '752590871'], ['iracing', '19554'], ['Assetto Corsa Competizione', '1348809580'],
    ['F1 22', '1705795372'], ['CarX Drift Racing Online', '498289'], ['Need for Speed: Underground', '11258'],
    ['Forza Horizon 5', '1757732267'], ['Stuntfest Worldtour', '1582771097'], ['The Crew 2', '497118'],
    ['NASCAR Heat 5', '517409'], ['Need for Speed Heat', '512782'],
    # Battle Royale
    ['fortnite', '33214'], ['fall guys', '512980'], ['Garena Free Fire', '502732'], ['Naraka: Bladepoint', '515474'],
    ['pubg: battlegrounds', '493057'], ["playerunknown's battlegrounds", '493057'], ['Super Animal Royale', '509529'],
    ['super people', '19620578'], ['warzone', '25416'], ['Stumble Guys', '1312214340'], ['Crab Game', '673760473'],
    ['Realm Royale', '505845'], ['Rush Royale', '633454324'],
    # Old
    ['Ape Escape', '12270'],  ['Retro', '27284'],
    # War
    ['war thunder', '66366'], ['world of tanks', '27546'], ['world of warships', '32502'], ['Foxhole', '493388'],
    ['World of Tanks Console', '499551'], ['World of tanks: Blitz', '140035'], ['crossout', '492113'],
    ['Steel Division 2', '511940'],
    # Minigames with or without chat
    ['Kukoro: Stream Chat Games', '518764'], ['Words On Stream', '512821'], ['Jackbox Party Packs', '493174'],
    ['Kahoot!', '1127100998'], ['Wordle', '879648744'], ['What The Dub?!', '752874500'],
    ['The Jackbox Party Pack 9', '1219652274'],
    # Competitive
    ['dota 2', '29595'], ['smite', '32507'], ['overwatch', '488552'], ['Smite', '32507'], ['starcraft ii', '490422'],
    ['StarCraft', '11989'], ['Warcraft III', '12924'], ['valorant', '516575'], ['Age of Empires II', '13389'],
    ['Total War: Warhammer III', '1913410799'], ['Heroes of Might and Magic III: The Restoration of Erathia', '12839'],
    ['Age of Empires III', '7830'], ['Age of Empires IV', '498482'], ['Total War: Warhammer II', '497434'],
    ['Warhammer Online: Age of Reckoning', '18888'], ['World of Warcraft', '18122'],
    # Games for 2
    ['We Were Here Forever', '428452832'], ['Codenames', '508509'], ['Keep Talking and Nobody Explodes', '461492'],
    ['Gartic Phone', '278888515'], ['It Takes Two', '518213'], ['Tabletop RPGs', '509664'], ['Pummel Party', '509549'],
    ['A Way Out', '497388'],
    # Games for groups
    ['Dungeons%20%26%20Dragons', '509577'], ['Music Quiz', '24786'], ['Mafia LIVE!', '22761'],
    # Mobile
    ['langrisser mobile', '509986'], ['league of legends: wild rift', '514858'], ['Dragon Ball Legends', '504921'],
    ['Mobile Legends: Bang Bang', '494184'], ['MARVEL Strike Force', '504651'], ['Epic Seven', '510056'],
    ['Fate%2FGrand Order', '493048'], ['One Piece: Treasure Cruise', '489169'], ['Marvel Snap', '1743359147'],
    ['MARVEL Contest of Champions', '461221'], ['Last Day on Earth: Survival', '497697'],
    ['Apex Legends Mobile', '170987874'], ['Saint Seiya: Awakening', '511850'], ['Brawl stars', '497497'],
    ['Final Fantasy Tactics', '18181'], ['Dungeon %26 Fighter Mobile', '1013109068'], ['Bleach: Brave Souls', '492984'],
    ['Dead by Daylight Mobile', '517072'], ['pubg mobile', '505884'], ['FIFA Mobile', '496320'],
    # Playstation 4
    ['Dreams', '490373'],
    # Nintendo Switch
    ['mario strikers: battle league', '1769394593'],
    # Nintendo WII
    ['Mario Kart Wii', '18871']
]

newBlacklistAdditions = ['Hot Lava', 'Standoff 2', 'Rumbleverse']

favoriteGames = [
    # Games I enjoy the most at the moment
    'Satisfactory',
    # Survival
    'Minecraft', 'Terraria', 'Vintage Story', 'Valheim', 'Icarus', 'Raft', 'Atlas', 'Ark', 'Creativerse',
    'Ark: Survival Evolved',
    # City bulding
    'Cities: Skylines', 'SimCity',
    # Villagers
    'Stardew Valley', 'Dinkum', 'Animal Crossing: New Horizons',
    # Automation
    'Factorio', 'Hydroneer', 'Captain of industry', 'Rimworld', 'Dorfromantik', 'Snowrunner', 'Mini Motorways',
    # Simulation
    'The Sims 4', 'The Sims 3', 'The Sims 2', 'The Universim', 'Oxygen Not Included',
    # Strategy
    'Going medieval', 'Civilization iv', 'Hearts of Iron IV', 'Mount & Blade: Warband', 'Mount & Blade II: Bannerlord',
    'Teamfight Tactics', 'Auto Chess'
    # Weird
    'Reading Fun', 'Roblox',
    # Board games
    'Chess', 'Tabletop Simulator', 'Card Games', 'Board Games',
    # Card games
    'Hearthstone',
    # Racing
    'Trackmania', 'Rocket League',
    # Special
    'Art', 'Makers & Crafting', 'Software and Game Development', 'Science & Technology',
    # Sports
    'Golf with your friends', "Tony Hawk's Pro Skater 1+2",
    # Story
    "Assassin's Creed Odyssey", "Assassin's Creed Origins", "Assassin's Creed IV Black Flag",
    "Assassin's Creed Valhalla", "Assassin's Creed Unity",
    # Games for 2
    'Overcooked! 2',
    # Platformer
    'Super Meat Boy',
    # Hate but love
    'League of Legends', 'Heroes of the Storm',
    # RPG
    'Gothic', 'Gothic II', 'Lost Ark', 'Old School RuneScape', 'TERA',
    # Mobile
    'Clash Royale', 'Clash of Clans', 'Pokémon GO', 'Summoners War: Sky Arena'
]
