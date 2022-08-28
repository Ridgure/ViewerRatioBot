#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioLists.py

# If you want to blacklist a game, put it in here to get its id and add it to the blacklist
newBlacklistAdditions = []

# Games you don't want to play
blacklist = [
    # Shooter games
    ['aim gods', '516967'], ['aim lab', '503456'],  ['anthem', '460696'],  ['Call of Duty', '1494'],
    ['apex legends', '511224'], ['battlefield 1', '488500'], ['battlefield 2', '15467'], ['battlefield 2042', '514974'],
    ['battlefield 3', '24394'], ['battlefield 4', '66402'], ['battlefield v', '504199'],
    ['battlefield: bad company 2', '22851'], ['call of duty: black ops 4', '504462'],  ['Grand Theft Auto', '12453'],
    ['call of duty: black ops cold war', '512709'], ['Grand Theft Auto IV', '18707'],
    ['call of duty: black ops iii', '489401'], ['Aliens: Fireteam Elite', '1585949885'], ['cruelty squad', '977894696'],
    ['call of duty: modern warfare', '1614555304'], ['call of duty: modern warfare 2', '22393'], ['Destiny', '280721'],
    ['call of duty: modern warfare remastered', '494155'], ['call of duty: vanguard', '492778073'],
    ['call of duty: warzone', '512710'], ['call of duty: wwii', '496712'], ['Vigor', '506489'],
    ['call of duty: black ops ii', '34134'], ['counter-strike: global offensive', '32399'], ['battlebit', '496916'],
    ['destiny 2', '497057'], ['doom eternal', '506442'], ['deathloop', '512983'], ['Rollerdrome', '772915712'],
    ['fallout 76', '506246'], ['f.e.a.r. perseus mandate', '14310'], ['gears 5', '506407'], ['Fallout 4', '489776'],
    ['grand theft auto iv: the ballad of gay tony', '2113221108'], ['grand theft auto v', '32982'], ['gtfo', '500627'],
    ['gunfire reborn', '517645'], ['gunz: the duel', '513567'], ['hitman', '491471'], ['hitman 3', '518011'],
    ['hell let loose', '497440'], ['hunt: showdown', '500188'], ['hyper scape', '518306'], ['Crossfire X', '512985'],
    ['insurgency: sandstorm', '491705'], ['max payne 3', '21222'], ['metal gear rising: revengeance', '24208'],
    ['metal gear solid', '14805'], ['metal gear solid 2: sons of liberty', '11386'], ['Metal Gear Acid', '8798'],
    ['metal gear solid 3: snake eater', '16582'], ['metal gear solid 4: guns of the patriots', '18893'],
    ['metro exodus', '497410'], ['mass effect legendary edition', '1568081763'], ['metroid prime 2: echoes', '1459'],
    ['payday 2', '65997'], ['outriders', '512930'], ['quake', '7348'], ['quake champions', '496253'],
    ['splitgate', '499310'], ['squad', '488479'], ['star wars battlefront ii', '492546'], ['Gears of War 4', '459382'],
    ['returnal', '518019'], ['rogue company', '514194'], ['sniper elite 5', '511743'], ['team fortress 2', '16676'],
    ['the last of us', '33180'], ['the last of us part ii', '494552'], ["tom clancy's rainbow six siege", '460630'],
    ["tom clancy's rainbow six: siege", '460630'], ["tom clancy's the division", '369579'],
    ["tom clancy's the division 2", '504463'], ['titanfall 2', '489201'], ['Quake Live', '19490'],
    ['totally accurate battlegrounds', '506344'], ['true crime: new york city', '3077'], ['Adaca', '544704748'],
    ['Grand Theft Auto: San Andreas', '6521'], ['Uncharted 2: Among Thieves', '20357'], ['BIGFOOT', '6675'],
    ['Mass Effect 3', '26992'], ['S.T.A.L.K.E.R.: Anomaly', '1549167076'], ['Mass Effect: Andromeda', '460695'],
    ['DOOM II: Hell on Earth', '584'], ['Fallout: New Vegas', '23453'], ['Grand Theft Auto: Vice City', '15631'],
    ['Call of Duty: Black Ops', '23894'], ['Mafia II: Definitive Edition', '2058566581'], ['Gran Turismo 7', '518014'],
    ['Arma 3', '31750'], ['Far Cry 5', '497078'], ["Tom Clancy's Ghost Recon: Wildlands", '490379'], ['DOOM', '6715'],
    ['Grand Theft Auto III', '3412'], ['Crossfire', '27101'], ['Overwatch 2', '515025'], ['BioShock 2', '19030'],
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
    ['Call of Duty 2', '2162'], ['Saints Row 2', '18906'], ['The Outer Worlds', '510580'], ['Star Valor', '508764'],
    ['Fashion Police Squad', '829294318'], ['Deep Rock Galactic', '494839'], ['Bioshock Infinite', '29099'],
    ['Enlisted', '505257'], ['Killing Floor 2', '460508'], ['BioShock Remastered', '2009742488'], ['Warface', '29918'],
    ['Watch Dogs 2', '492930'], ['Saints Row IV', '33086'], ['GTA: La Heist', '41272850'], ['PlanetSide 2', '26175'],
    ['Saints Row', '1067345253'], ['Mafia: Definitive Edition', '517769'], ['Saints Row: The Third', '23268'],
    ['Earth Defense Force 4.1: The Shadow of New Despair', '476437'], ['Metro 2033 Redux', '1388848972'],
    ['Saints Row: The Third Remastered', '747702304'], ['Aliens vs. Predator', '23979'], ['Halo 3', '9178'],
    ['Predator: Hunting Grounds', '512551'], ['Deadside', '516097'], ['BioShock', '15866'], ['Paladins', '491115'],
    ['Wolfenstein: The New Order', '369259'], ['Shatterline', '528918758'], ['Earth Defense Force 6', '518402'],
    ['Wolfenstein II: The New Colossus', '497439'], ['The Cycle: Frontier', '470840663'],
    ['Alliance of Valiant Arms', '26569'], ['Generation Zero', '33389'], ["Tiny Tina's Wonderlands", '1318043161'],
    ['Fallout 3', '18763'], ['Halo Wars 2', '490446'], ['Earth Defense Force 5', '493080'],
    # Bossfights
    ['bloodborne', '460636'], ['dark souls', '29433'], ['dark souls iii', '490292'], ['dark souls ii', '91423'],
    ['Elden Ring', '512953'], ["demon's souls", '21812'], ['hellpoint', '496421'], ['left 4 dead 2', '24193'],
    ['mortal shell', '516915'], ['nioh 2', '506468'], ['nioh 2: the complete edition', '160136078'],
    ['sekiro: shadows die twice', '506415'], ['the surge', '496233'], ['black mesa', '68016'],
    ['Company of Heroes 2', '65663'], ['Evolve Stage 2', '1893365738'], ['Metro: Last Light', '31836'],
    ['Dark Souls: Remastered', '1122982998'],
    ['Nioh', '24872'], ['Kingdom Hearts III', '369585'], ['Star Wars Jedi: Fallen Order', '503446'],
    # Medieval fights
    ['chivalry 2', '512971'], ['for honor', '490382'], ['ghost of tsushima', '499856'], ['mordhau', '498859'],
    ['sifu', '506089309'], ['Warhammer: Vermintide 2', '498668'], ['Mortal Online 2', '517282'],
    ["Conqueror's Blade", '498523'], ["Ghost of Tsushima: Director's Cut", '350892884'],
    ['Dark and Darker', '2009321156'],
    # Violent Survival
    ['dayz', '65632'], ['SurrounDead', '750209762'], ['Lost Light', '1706428735'], ['escape from tarkov', '491931'],
    ['Dying Light 2: Stay Human', '506410'], ['Dying Light', '369380'], ['State of Decay 2', '495122'],
    ['Dead Island', '19622'], ['Mad Max', '8271'], ['Unturned', '417932'],
    # Fist fighting
    ['yakuza', '6571'], ['yakuza 0', '476269'], ['yakuza 5', '32541'], ['yakuza 6: the song of life', '490701'],
    ['yakuza: like a dragon', '512121'], ['lost judgment', '2120403770'], ['sleeping dogs', '26547'],
    ['Yakuza Kiwami 2', '498510'], ['Judgment', '509482'], ['Yakuza Kiwami', '490702'],
    ['Midnight Fight Express', '519493'],
    # Drama
    ['among us', '510218'], ['Politics', '515214'], ['Gang Beasts', '459527'], ['Dread Hunger', '511181708'],
    ['The Walking Dead: The Telltale Series Collection', '499987'], ['As Dusk Falls', '518875'],
    ['The Walking Dead: Season One', '30740'], ['Is It You?', '172861049'], ['The Walking Dead: Season Two', '66410'],
    ['The Walking Dead: A New Frontier', '461246'], ['The Walking Dead: The Final Season', '497916'],
    ['Project Winter', '509893'], ['The Walking Dead: Saints %26 Sinners', '515862'], ['Goose Goose Duck', '14333696'],
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
    ['Resident Evil 0', '489721'], ['Labyrinthine', '517528'], ['Ghost Watchers', '790163050'], ['DEVOUR', '836519689'],
    ['Resident Evil 4: Otome Edition', '1638636362'], ['Phasmophobia', '518184'], ['The Beast Inside', '504389'],
    ['Refund Me If You Can', '866831809'], ["I'm on Observation Duty 5", '1654421360'], ['Deceit', '493244'],
    ['Ghost Exile', '289552769'], ['Silent Hill 3', '9522'], ['Resident Evil 4 HD', '784020615'], ['DOOM 64', '15389'],
    ['Is Simon There?', '443409039'], ['Silent Hill: Origins', '13206'], ['FOBIA: St. Dinfna Hotel', '2037799395'],
    ['Inside the Backrooms', '1144809661'], ['Amnesia: Rebirth', '516624'], ['Resident Evil Survivor', '14528'],
    ['The Evil Within', '68000'], ['The Evil Within 2', '497437'], ['Escape the Backrooms', '2066107586'],
    ['Resident Evil Resistance', '514308'], ['Song of Horror', '514930'], ['Darkwood', '313146'],
    ['Fear Therapy', '819777302'], ['Silent Hill', '3947'], ['Lunch Lady', '477532253'], ['Pacify', '511134'],
    ['Resident Evil: Revelations', '28576'], ['Standoff 2', '513501'], ['In Sound Mind', '518088'],
    ['Dead Space 2', '23017'], ['Dead Space', '19009'], ['Outlast II', '510117'], ['Nighthunt', '1268832494'],
    ['Resident Evil: Revelations 2', '461522'], ['Thymesia', '64300975'], ['Call of Duty: Ghosts', '118200'],
    ['Remnant: From the Ashes', '509066'], ['The Dark Pictures Anthology: Little Hope', '514207'],
    ['Ghost Exorcism Inc.', '1239774436'], ["Five Nights at Freddy's: Security Breach", '2143096682'],
    ['SCP: Containment Breach', '65745'], ['SCP: Secret Laboratory', '498744'], ['Until Dawn', '67637'],
    ['Amnesia: The Dark Descent', '27127'], ['Layers of Fear', '490537'], ['Call of Duty: World at War', '19006'],
    ['SCP: Pandemic', '516702'], ['Dead Space 3', '65706'], ['The Bridge Curse: Road To Salvation', '2081287761'],
    ['JR’s', '623775229'], ['Blair Witch', '512981'], ['Remnant Records', '1869189136'],
    # Murder mystery
    ['gone home', '65752'], ["Handy Harry's Haunted House Services", '1450669133'],
    # Underwater
    ['Maneater', '506452'],
    # Story
    ['crysis', '10818'], ['death stranding', '494364'], ['far cry', '13564'], ['far cry 6', '518692'],
    ['halo infinite', '506416'], ['halo: reach', '24203'], ['halo: the master chief collection', '417969'],
    ['half-life', '2755'], ['red dead redemption 2', '493959'], ['halo 2', '6511'], ['Tomb Raider', '2770'],
    ['Far Cry: Primal', '490919'], ['Far Cry 3', '29635'], ['Rise of the Tomb Raider', '460620'],
    ['Tomb Raider II', '317'], ['Shadow of the Tomb Raider', '504735'], ['God of War', '6369'], ['Watch_Dogs', '65953'],
    ['Halo 5: Guardians', '369567'], ['God of War II', '10384'], ['God of War HD', '995720898'],
    ['Halo: Combat Evolved', '2397'], ['Red Dead Redemption', '22848'],
    # Roguelikes
    ['diablo ii', '1041'], ['diablo iii', '313558'], ['diablo iii: reaper of souls', '313558'],
    ['diablo immortal', '510150'], ['path of exile', '29307'], ['warframe', '66170'], ['Enter the Gungeon', '488632'],
    ['Diablo II: Resurrected', '1788326126'], ['Devil May Cry 5', '506412'], ['Devil May Cry', '283386'],
    ['Code Vein', '496697'], ['Boyfriend Dungeon', '499821'], ['Dark Cloud', '1705'],
    ["Devil May Cry 3: Dante's Awakening – Special Edition", '488844'], ['Darkest Dungeon', '458353'],
    ['Devil May Cry 4: Special Edition', '488974'],
    # Dialogue game
    ['VA-11 HALL-A: Cyberpunk Bartender Action', '461529'], ['Persona 3 FES', '18908'],
    # Hide and seek
    ["garry's mod", '18846'], ['dead by daylight', '491487'], ['Monstrum 2', '519309'], ['Identity V', '508662'],
    ['Propnight', '1342987707'],
    # VR
    ['beat saber', '503116'], ['vrchat', '499003'], ['half-life: alyx', '515195'], ['DCS World', '313331'],
    ['Rec Room', '493280'], ['Pavlov VR', '496142'], ['Echo Arena', '497461'], ['Into the Radius', '511922'],
    ['POPULATION: ONE', '1900396348'], ['VAIL VR', '1405679224'], ['VAIL VR', '1405679224'],
    ['Hot Dogs, Horseshoes %26 Hand Grenades', '492164'],
    # Stealth
    ['this land is my land', '512842'], ['Middle-earth: Shadow of Mordor', '458619'],
    # Money
    ['crypto', '499634'], ['horse racing', '6891'], ['poker quest', '308324368'], ['poker', '488190'],
    ['slots', '498566'], ['virtual casino', '29452'], ['Pokémon Trading Card Game Online', '32634'],
    ['Axie Infinity', '508967'], ['Stocks And Bonds', '5899'], ['Pokémon Trading Card Game', '9618'],
    ['Bitcoin', '515880'], ['Casino', '582382910'], ['Blackjack', '2030294088'], ['rFactor 2', '24636'],
    ['Lottery Simulator', '497156'], ['Prominence Poker', '492287'], ['Coin Pusher World', '530998549'],
    ['Undead Blocks', '1912435287'],
    # Weird Sexual
    ['asmr', '509659'], ['pools, hot tubs, and beaches', '116747788'], ['Just Dance 2022', '413353439'],
    ['Hooked on You: A Dead by Daylight Dating Sim', '160028919'], ['Just Dance', '25122'], ['Bayonetta', '18933'],
    ['Beauty & Body Art', '509669'], ["Love, Money, Rock'n'Roll", '517967'], ['Entropia Universe', '19714'],
    ['Monster Prom', '498345'],
    # Weird
    ["I'm Only Sleeping", '498592'], ['just chatting', '509658'], ['twitch plays', '491180'], ['Others', '512354'],
    ['watch parties', '515467'], ['Special Events', '509663'], ['Animals, Aquariums, and Zoos', '272263131'],
    ['Travel %26 Outdoors', '509672'], ['Games %2B Demos', '66082'], ['Talk Shows %26 Podcasts', '417752'],
    ['Sleep', '154096350'], ['Tarot', '83418'], ['Food%20%26%20Drink', '509667'], ['EZ2ON REBOOT : R', '2057185004'],
    ['Test, Test', '2070714813'], ['Lost in Play', '181659447'], ['The Simpsons: Hit %26 Run', '2897'],
    ['Pokémon Community Game', '329951934'], ['Coffee Talk', '512306'], ['Live', '508402'], ['Chill', '28838'],
    ['Bully', '9440'], ['Bully: Scholarship Edition', '4667'], ['IRL: The Game', '1063483442'],
    # Weird DMCA
    ['Artifact', '16937'], ['El Chavo', '34054'], ['Movie Night', '753325070'], ['Music', '26936'],
    ['Anime World', '637756067'], ['Always On', '499973'], ['Sexy Miss', '1129360291'], ['The Simpsons', '2046821115'],
    ['Series Makers', '700055046'], ['Radio Station', '2128929587'], ['Karaoke Party', '488782'],
    ['Relaxing Waves', '872742502'], ['South Park', '8105'], ['Nothing', '1709696975'], ['TV Station Manager', '8259'],
    ['Rock Band 4', '489136'], ['South Park: The Stick of Truth', '33175'],
    ['The Spongebob Squarepants Movie', '503749'], ['South Park: The Fractured But Whole', '490378'],
    # Space
    ['elite: dangerous', '80607'], ['kerbal space program', '32742'], ['Starsector', '33416'],
    ['FTL: Faster Than Light', '33882'], ['Star Trek Fleet Command', '510530'], ['Star Citizen', '71375'],
    ["Marvel's Guardians of the Galaxy", '1540116959'], ['Star Trek Online', '19858'],
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
    ['MapleStory', '19976'], ["The King of Fighters '98", '9747'], ['Skul: The Hero Slayer', '515386'],
    ['Mortal Kombat X', '460521'], ['Dragon Ball: Xenoverse 2', '492731'], ['Elsword', '68018'],
    ['Streets of Rage 4', '509356'], ['Marvel vs. Capcom 2: New Age of Heroes', '2400'], ['Injustice 2', '494995'],
    ['Super Mario Bros. 3', '9455'], ['Persona 4 Arena Ultimax', '313464'], ['Street Fighter III: 3rd Strike', '1476'],
    ['BlazBlue: Central Fiction', '490500'], ['Mortal Kombat XL', '2072543734'], ['Super Mario Bros.', '509508'],
    ['Street Fighter 6', '55453844'],
    # Sports
    ['cricket 19', '512623'], ['pga tour 2k21', '517397'], ['sports', '518203'], ['Fitness%20%26%20Health', '509671'],
    ['Zwift', '490959'], ['Nintendo Switch Sports', '2044170173'],
    # Soccer
    ['efootball pes 2021 season update', '1520501777'], ['eFootball 2022', '1061323687'],
    ['football manager 2021', '1271244884'], ['fifa 16', '489608'], ['fifa 17', '493091'], ['fifa 18', '495589'],
    ['fifa 19', '506103'], ['fifa 20', '512804'], ['fifa 21', '518204'], ['fifa 22', '1869092879'],
    ['fifa 23', '1745202732'], ['Pro Soccer Online', '1286420756'], ['FIFA Online 4', '504798'],
    ['football manager 2022', '586622463'], ['mario strikers: battle league', '1769394593'], ['Italia 1990', '14824'],
    ['Anstoss 3', '498350675'],
    # Basketball
    ['nba 2k21', '518023'], ['Out of the Park Baseball 23', '123403711'], ['slam dunk', '517301'],
    ['nba 2k22', '1371363232'], ['NBA Live 19', '506406'],
    # American Football
    ['madden nfl 21', '517406'], ['madden nfl 22', '966064811'], ['Madden NFL 23', '862021340'],
    ['NCAA Football 14', '271198'], ['Blood Bowl 2', '490177'],
    # Baseball
    ['eBaseball Powerful Pro Yakyuu 2022', '405215881'], ['MLB 9 Innings 22', '2038575831'],
    ['MLB The Show 22', '1820819463'], ['mlb the show 21', '1160459167'],
    ['Captain Tsubasa II: Super Striker', '579601296'],
    # Hockey
    ['nhl 21', '519329'], ['NHL 22', '13932618'],
    # Fishing
    ['Russian Fishing 4', '497304'], ['Fishing Planet', '491117'], ['Ultimate Fishing Simulator 2', '1825784314'],
    ['Ultimate Fishing Simulator', '500518'], ['Call of the Wild: The Angler', '487237675'],
    # Wrestling
    ['ea sports ufc 4', '518711'], ['wwe 2k19', '508289'], ['wwe 2k20', '513681'], ['wwe 2k22', '1199725270'],
    ['WWE SuperCard', '461427'], ['WWE Champions', '491560'], ['Fire Pro Wrestling World', '496098'],
    # Boxing
    ['Fight Night Champion', '28924'], ['Boxing', '1173'], ['Boxing Fight', '369432'], ['Boxing Star', '510965'],
    # Vehicles
    ['Microsoft Flight Simulator', '7193'], ['SD Gundam Battle Alliance', '1179447665'], ['My Summer Car', '493125'],
    ['Mobile Suit Gundam Battle Operation 2', '499526'], ['The Long Drive', '514661'],
    ['Ace Combat 7: Skies Unknown', '492605'],
    # Racing
    ['f1 2020', '517174'], ['f1 2021', '752590871'], ['iracing', '19554'], ['Assetto Corsa Competizione', '1348809580'],
    ['F1 22', '1705795372'], ['CarX Drift Racing Online', '498289'], ['Need for Speed: Underground', '11258'],
    ['F1 22', '1705795372'], ['CarX Drift Racing Online', '498289'], ['Need for Speed: Underground', '11258'],
    ['Forza Horizon 5', '1757732267'], ['Stuntfest Worldtour', '1582771097'], ['The Crew 2', '497118'],
    ['NASCAR Heat 5', '517409'], ['Need for Speed Heat', '512782'], ['Need for Speed: Underground 2', '8855'],
    ['BeamNG.drive', '491878'], ['Mario Kart 8 Deluxe', '941530474'], ['DiRT Rally 2.0', '509698'],
    ['Automobilista 2', '516921'], ['Mario Kart 8', '369588'], ['Wreckfest', '370472'], ['Forza Horizon 4', '506413'],
    ['Need For Speed: Payback', '492547'], ['F1 Manager 2022', '489490035'], ['Assetto Corsa', '313197'],
    # Speedrun
    ['Hot Lava', '498346'], ['Spyro the Dragon', '7182'], ['Super Mario 64', '2692'], ['Super Metroid', '7595'],
    ['Metroid Prime', '14198'], ['Sonic the Hedgehog', '2271'], ['The Legend of Zelda: A Link to the Past', '9435'],
    ['Spyro the Dragon: Reignited Trilogy', '1885901697'], ["The Legend of Zelda: Majora's Mask", '12482'],
    ['Sonic Origins', '914065119'], ['Castlevania: Symphony of the Night', '13050'], ['Super Mario Maker 2', '511399'],
    ['Ratchet %26 Clank', '16791'], ['Final Fantasy XII: The Zodiac Age', '493926'], ['Final Fantasy VI', '858043689'],
    ['Jak and Daxter: The Precursor Legacy', '13420'], ['Banjo-Kazooie', '10033'], ['Donkey Kong 64', '13765'],
    ['The Legend of Zelda: Ocarina of Time', '11557'], ['Super Mario Galaxy', '14766'], ['SpeedRunners', '370345'],
    ['Sonic Adventure 2: Battle', '6263'], ['Shadow the Hedgehog', '17794'], ['The Legend of Zelda', '10979'],
    ['Crash Bandicoot', '2092563353'], ['Castlevania', '6108'], ['Final Fantasy IV', '19023'],
    ["Crash Bandicoot 4: It's About Time", '518222'], ['Super Mario Sunshine', '6086'], ['Sonic Adventure', '7195'],
    ['Kirby and the Forgotten Land', '496321134'], ['Control', '506462'], ['Super Mario Galaxy 2', '24239'],
    ['The Legend of Zelda: The Wind Waker', '16967'], ['The Legend of Zelda: Skyward Sword', '24324'],
    ['The Legend of Zelda: The Wind Waker HD', '368205'], ["The Legend of Zelda: Link's Awakening", '3337'],
    ['Crash Bandicoot 2: Cortex Strikes Back', '1461160776'], ['Final Fantasy: Mystic Quest', '3331'],
    ['Final Fantasy: Mystic Quest', '3331'], ['Super Mario RPG: Legend of the Seven Stars', '6737'],
    ['Metroid Dread', '212029556'], ['Mega Man 2', '12870'], ['Sonic Mania', '493877'], ['Metroid Fusion', '9479'],
    ['Mega Man X', '8676'], ['Digimon World', '3564'], ['Paper Mario', '18231'], ['Sonic Heroes', '8734'],
    ['Paper Mario: The Thousand-Year Door', '6855'], ['The Legend of Zelda: The Minish Cap', '5635'],
    ['EarthBound', '30367'], ['Castlevania: Aria of Sorrow', '11065'], ['Mario Golf: Toadstool Tour', '1458'],
    ['Mega Man Maker', '1267688912'], ['Zelda II: The Adventure of Link', '14890'],
    ['Ratchet %26 Clank: Rift Apart', '518016'],
    # Battle Royale
    ['fortnite', '33214'], ['fall guys', '512980'], ['Garena Free Fire', '502732'], ['Naraka: Bladepoint', '515474'],
    ['pubg: battlegrounds', '493057'], ["playerunknown's battlegrounds", '493057'], ['Super Animal Royale', '509529'],
    ['super people', '19620578'], ['warzone', '25416'], ['Stumble Guys', '1312214340'], ['Crab Game', '673760473'],
    ['Realm Royale', '505845'], ['Rush Royale', '633454324'], ['Rumbleverse', '161880494'],
    ['Z1: Battle Royale', '417892'], ['CRSED: F.O.A.D.', '506491'], ['My Hero Ultra Rumble', '451007760'],
    # Old
    ['Ape Escape', '12270'],  ['Retro', '27284'],
    # War
    ['war thunder', '66366'], ['world of tanks', '27546'], ['world of warships', '32502'], ['Foxhole', '493388'],
    ['World of Tanks Console', '499551'], ['World of tanks: Blitz', '140035'], ['crossout', '492113'],
    ['Steel Division 2', '511940'], ['World of Warships: Legends', '512226'], ['Regiments', '946617000'],
    ['Battalion 1944', '491704'], ['BATTLETECH', '490757'], ['Middle-earth: Shadow of War', '496000'],
    # Minigames with or without chat
    ['Kukoro: Stream Chat Games', '518764'], ['Words On Stream', '512821'], ['Jackbox Party Packs', '493174'],
    ['Kahoot!', '1127100998'], ['Wordle', '879648744'], ['What The Dub?!', '752874500'],
    ['The Jackbox Party Pack 9', '1219652274'],
    # Anime fighter
    ['Dragon Ball Z: Kakarot', '511195'], ['Naruto to Boruto: Shinobi Striker', '496503'],
    ['Naruto Shippuden: Ultimate Ninja Storm 4', '488635'],
    # Competitive
    ['smite', '32507'], ['overwatch', '488552'], ['Smite', '32507'], ['starcraft ii', '490422'],
    ['StarCraft', '11989'], ['Warcraft III', '12924'], ['valorant', '516575'], ['Age of Empires II', '13389'],
    ['Total War: Warhammer III', '1913410799'], ['EVE Online', '13263'], ['Fault: Elder Orb', '514152'],
    ['Age of Empires III', '7830'], ['Age of Empires IV', '498482'], ['Total War: Warhammer II', '497434'],
    ['Warhammer Online: Age of Reckoning', '18888'], ['World of Warcraft', '18122'],
    # Competitive non violent
    ['Splatoon 2', '495064'], ['Knockout City', '1924769596'], ['Expedition Agartha', '1853203196'],
    ['Splatoon 3', '1158884259'],
    # Competitive deck builders
    ['Gwent: The Witcher Card Game', '493217'], ['Hearthstone', '138585'], ['Magic: The Gathering', '2748'],
    ['Yu-Gi-Oh! TRADING CARD GAME', '497248'], ['Yu-Gi-Oh! Duel Links', '494508'], ['Storybook Brawl', '1210837377'],
    ['Yu-Gi-Oh! Forbidden Memories', '207'], ['Yu-Gi-Oh! Master Duel', '1119642287'], ['Eternal Card Game', '491403'],
    ['Digimon Digital Card Battle', '11088'], ['Legends of Runeterra', '514790'], ['Gods Unchained', '508716'],
    ['Shadowverse', '492925'], ['Across the Obelisk', '807746316'], ['Ascension: Deckbuilding Game', '535155317'],
    ["Evony: The King's Return", '1129869117'],
    # Competitive weird
    ['Bloons TD Battles 2', '1740011318'], ['Chess', '743'], ['Go', '65360'], ['Mahjong Soul', '512708'],
    ['Chess.com', '2106453313'],
    # Turn based combat
    ['Heroes of Might and Magic III: The Restoration of Erathia', '12839'], ['XCOM 2', '489767'],
    ["Sid Meier's Civilization VI", '492553'], ['XCOM: Enemy Unknown', '33331'], ['Hearts of Iron IV', '459327'],
    ['Europa Universalis IV', '67584'], ['Slay the Spire', '496902'],
    ['Chrono Trigger', '8489'], ['Crusader Kings III', '514888'], ['Kingdom Hearts HD 1.5 %2B 2.5 ReMIX', '494099'],
    ['Age of Mythology', '1260'], ['Age of Mythology: Extended Edition', '421115841'], ['Monster Train', '516096'],
    ['Xenoblade Chronicles: Definitive Edition', '514245'], ['Final Fantasy IX', '8090'],
    ['Xenoblade Chronicles 3', '1584758405'], ['Tales of Arise', '512957'], ['Digimon Survive', '508776'],
    ['Final Fantasy V', '1692274562'], ['Backpack hero', '1023917542'], ['Fire Emblem: Three Houses', '495202'],
    ["Sid Meier's Civilization V", '27103'], ['Command %26 Conquer: Red Alert 2', '16580'], ['HUMANKIND', '514071'],
    ['Battle Brothers', '490771'], ['Octopath Traveler', '495062'], ['Dungeon Fighter Online', '25367'],
    ['Final Fantasy XI Online', '10229'], ['Toontown Online', '1281'], ['Star Wars: Galaxy of Heroes', '496853'],
    ['Dragon Quest XI S: Echoes of an Elusive Age - Definitive Edition', '486102336'], ['Final Fantasy', '7689'],
    ['Pokémon Showdown', '850490686'], ['Xenoblade Chronicles 2', '495061'], ['Kingdom Hearts', '10081'],
    ['The Legend of Dragoon', '12101'], ['Wildermyth', '511724'], ['For The King', '494903'], ['Chrono Cross', '3963'],
    ['Dragon Quest', '14951'], ['Digimon Story Cyber Sleuth', '458900'], ['Kingdom Hearts Dark Road', '516085'],
    ['Fire Emblem Warriors: Three Hopes', '183330426'], ['Soul Hackers 2', '18070083'], ['Final Fantasy II', '1918'],
    # Games for 2
    ['We Were Here Forever', '428452832'], ['Codenames', '508509'], ['Keep Talking and Nobody Explodes', '461492'],
    ['Gartic Phone', '278888515'], ['It Takes Two', '518213'], ['Tabletop RPGs', '509664'], ['Pummel Party', '509549'],
    ['A Way Out', '497388'], ['We Were Here', '495723'],
    # Games for groups
    ['Dungeons%20%26%20Dragons', '509577'], ['Music Quiz', '24786'], ['Mafia LIVE!', '22761'], ['Ravenfall', '519528'],
    ['Monopoly Plus', '493159'], ['Masks Of Deception', '519297364'], ['PlateUp!', '1115711128'],
    ['Overcooked! 2', '506458'], ['UNO', '11103'], ['Pathfinder', '508513'], ['skribbl.io', '496983'],
    ['RISK: The Game of Global Domination', '520083701'], ['First Class Trouble', '515486'], ['Mario Party 6', '7673'],
    ['RiffTrax: The Game', '1892955924'], ['Overcooked! All You Can Eat', '518847'],
    # Mobile general
    ['langrisser mobile', '509986'], ['Dragon Ball Legends', '504921'],
    ['Mobile Legends: Bang Bang', '494184'], ['MARVEL Strike Force', '504651'], ['Epic Seven', '510056'],
    ['Fate%2FGrand Order', '493048'], ['One Piece: Treasure Cruise', '489169'], ['Marvel Snap', '1743359147'],
    ['MARVEL Contest of Champions', '461221'], ['Last Day on Earth: Survival', '497697'],
    ['Apex Legends Mobile', '170987874'], ['Saint Seiya: Awakening', '511850'], ['Brawl stars', '497497'],
    ['Final Fantasy Tactics', '18181'], ['Dungeon %26 Fighter Mobile', '1013109068'], ['Bleach: Brave Souls', '492984'],
    ['Dead by Daylight Mobile', '517072'], ['pubg mobile', '505884'], ['FIFA Mobile', '496320'],
    ['Summoners War: Sky Arena', '489111'], ['Clash Royale', '491168'], ['Clash of Clans', '73914'],
    ['Raid: Shadow Legends', '508948'], ['Ni no Kuni: Cross Worlds', '519394'], ['Punishing: Gray Raven', '516564'],
    ['Sky: Children of the Light', '513553'], ['The Seven Deadly Sins: Grand Cross', '512887'],
    ['call of duty: mobile', '512818'], ['The Seven Deadly Sins: Grand Cross', '512887'], ['Minion Masters', '494327'],
    ['Granblue Fantasy', '489668'], ['Azur Lane', '498434'], ['MIR4', '966704637'], ['Ring of Pain', '516806'],
    # Mobile MOBA
    ['league of legends: wild rift', '514858'], ['Arena of Valor', '498302'],
    # Playstation 4
    ['Dreams', '490373'],
    # Nintendo Switch
    ['The Legend of Zelda: Skyward Sword HD', '1829367372'], ['Pokémon Legends: Arceus', '561013832'],
    ['Super Mario Odyssey', '493997'], ["Luigi's Mansion 3", '509541'], ['Pokémon Sword%2FShield', '497451'],
    ['Pokémon Brilliant Diamond%2FShining Pearl', '1584745140'], ['Pokémon Unite', '518379'],
    ["Kirby's Dream Buffet", '284482065'], ['The Legend of Zelda: Breath of the Wild', '110758'],
    ['The Legend of Zelda: Twilight Princess', '17828'], ["Pokémon: Let's Go, Pikachu!", '506237'],
    ['Super Mario Party', '506454'], ['Mario Party Superstars', '1068239917'], ['Pokémon Shield', '1249600852'],
    ["Super Mario 3D World %2B Bowser's Fury", '1446426412'], ['Animal Crossing: New Horizons', '509538'],
    # Nintendo WII
    ['Mario Kart Wii', '18871'], ['StepMania', '6415'], ['Wii Sports Resort', '19259'],
    # Xbox
    ['Phantom Dust', '994344636'],
    # Other equipment
    ['SOUND VOLTEX EXCEED GEAR', '1259504587']
]

# Here you put games that you own or really, really want to play
favoriteGames = [
    # Games I enjoy the most at the moment
    'Satisfactory',
    # Survival
    'Minecraft', 'Terraria', 'Vintage Story', 'Valheim', 'Icarus', 'Raft', 'Atlas', 'Ark', 'Creativerse',
    'Ark: Survival Evolved', 'Rust', 'Starbound', 'Planet Crafter', 'Subsistence',
    # City building
    'Cities: Skylines', 'SimCity',
    # Automation
    'Factorio', 'Hydroneer', 'Captain of industry', 'Rimworld', 'Dorfromantik', 'Snowrunner', 'Mini Motorways',
    'Space Engineers', 'Captain of Industry',
    # Villagers
    'Stardew Valley', 'Dinkum', 'Animal Crossing: New Horizons',
    # Simulation
    'The Sims 4', 'The Sims 3', 'The Sims 2', 'The Universim', 'Oxygen Not Included',
    # Strategy
    'Going medieval', 'Teamfight Tactics', 'Auto Chess', 'They Are Billions', 'Shell Shockers',
    # Weird
    'Reading Fun', 'Roblox', 'Duolingo', 'Viscera Cleanup Detail', 'Tetris 99', 'GeoGuessr', 'Tower Unite',
    'Blankos Block Party',
    # Board games
    'Chess', 'Tabletop Simulator', 'Card Games', 'Board Games',
    # Racing with fake cars
    'Trackmania', 'Rocket League', 'Turbo Golf Racing',
    # Special
    'Art', 'Makers & Crafting', 'Software and Game Development', 'Science & Technology', 'Roblox Studio',
    # Sports
    'Golf With Your Friends', "Tony Hawk's Pro Skater 1+2", 'Skater XL', 'Skate 3',
    # Community games
    'Marbles On Stream', 'Stream Raiders', 'Stream Racer', 'Stream Pirates', 'Cult of the Lamb',
    # Platformer
    'Super Meat Boy', 'Cursed to Golf', 'Jump King', 'Pac-Man World Re-Pac', 'Rogue Legacy 2',
    # Hate but love
    'League of Legends', 'Heroes of the Storm', 'Dota 2', 'Century: Age of Ashes',
    # RPG
    'Gothic', 'Gothic II', 'Lost Ark', 'Old School RuneScape', 'TERA', 'Final Fantasy XIV Online', 'Tibia', 'RuneScape',
    'The Elder Scrolls Online', 'Dofus',
    # Mobile
    'Pokémon GO',
    # Story
    "Assassin's Creed Odyssey", "Assassin's Creed Origins", "Assassin's Creed IV Black Flag", "Assassin's Creed",
    "Assassin's Creed Valhalla", "Assassin's Creed Unity", "Assassin's Creed II", "Assassin's Creed Brotherhood",
    "Assassin's Creed Syndicate",
    # Turn based games nuzlocke! ironmon
    'Pokémon FireRed/LeafGreen',
]

# Games that I could see myself playing
wishlisted = [
    # Survival
    '7 Days to Die', 'Project Zomboid', 'The Forest', 'Green Hell', 'Raft', 'Conan Exiles', 'Subnautica',
    'Subnautica: Below Zero', 'Astroneer', 'The Long Drive', 'Stranded Deep', 'Wormate.io',
    'Mist Survival', 'Grounded', 'The Ascent', 'Empyrion - Galactic Survival',
    # Puzzle
    'Portal 2', 'TETR.IO', 'Tetris', 'Pinball', 'Human: Fall Flat', 'Escape Academy', 'Tetris Effect: Connected',
    'Twelve Minutes', 'Peggle', 'Superliminal', 'Portal', 'Are You Smarter Than a 5th Grader?', 'Escape Simulator',
    'Dr. Mario',
    # RPG
    'The Elder Scrolls IV: Oblivion', 'Final Fantasy IV: Oblivion', 'The Witcher 3: Wild Hunt', 'Final Fantasy X',
    'Final Fantasy VIII Remastered', 'The Elder Scrolls V: Skyrim', 'Death Stranding: Director’s Cut', 'Growtopia',
    'Final Fantasy XIII', 'Final Fantasy VII Remake', 'NieR: Automata', 'V Rising', 'Monster Hunter: World',
    'Horizon Zero Dawn', 'NieR Replicant ver.1.22474487139...', 'EverQuest', 'GhostWire: Tokyo', 'Ghostwire: Tokyo',
    'The Elder Scrolls V: Skyrim Special Edition', 'Monster Hunter Rise', 'Phantasy Star Online 2', 'Ultima Online',
    'Final Fantasy XV', 'Honkai Impact 3rd', 'Dragon Age: Origins', 'Realm of the Mad God', 'Aion', 'Path of Titans',
    'Horizon Forbidden West', 'Phantasy Star Online 2 New Genesis', 'Grim Dawn', 'Ravenfall', 'Tunic', 'MU Online',
    'Medieval Dynasty', 'Divinity: Original Sin II', 'Kingdom Come: Deliverance', 'Dark Age of Camelot', 'CABAL Online',
    'Core Keeper', 'Dungeons & Dragons Online', 'Dauntless', 'Stoneshard', 'Guild Wars 2', 'Guild Wars', 'Muck',
    'Fable Anniversary', 'Last Oasis', 'Live A Live', 'Genshin Impact', 'Neverwinter', 'Big Time', 'Ragnarok Online',
    'Shadow of the Colossus', 'Cyberpunk 2077', 'Bugsnax', 'Solasta: Crown of the Magister', 'Disco Elysium', 'Kenshi',
    "Dragon's Dogma: Dark Arisen", 'Knight Online', 'Final Fantasy VIII', 'The Elder Scrolls III: Morrowind',
    'Dragon Age: Inquisition', 'Outward', 'Flyff Universe', 'Sea of Thieves', 'Digimon Masters Online', 'Vindictus',
    'Final Fantasy X HD', 'MIR4', 'Lineage 2', 'Tower of Fantasy', 'Immortals Fenyx Rising', 'Mabinogi', 'Blade & Soul',
    'Wizard101', 'Stray', 'Stranger of Paradise: Final Fantasy Origin', 'Metin2', 'The Elder Scrolls II: Daggerfall',
    'Final Fantasy VII: The First Soldier', 'Final Fantasy VII',
    # Turn based combat
    'Temtem', 'Pokémon HeartGold/SoulSilver', 'Pokémon Ultra Sun/Ultra Moon', 'Pokémon Black/White', 'Pokémon Crystal',
    'Pokémon Black/White Version 2', 'Pokémon XD: Gale of Darkness', 'Pokémon Platinum', 'Pokémon Emerald',
    'Super Auto Pets', 'Into the Breach', 'Inscryption', 'Pokémon MMO 3D', 'Coromon', 'Pokémon Yellow',
    'Pokémon Omega Ruby/Alpha Sapphire', 'Pokémon Red/Blue', 'Omori', 'Pokémon X/Y',
    # Comic universes
    'Batman: Arkham Knight', "Marvel's Avengers", 'Star Wars: The Old Republic', "Marvel's Spider-Man Remastered",
    "Marvel's Spider-Man", "Marvel's Spider-Man: Miles Morales", 'The Lord of the Rings Online',
    'LEGO Star Wars: The Skywalker Saga', 'DC Universe Online', "Teenage Mutant Ninja Turtles: Shredder's Revenge",
    'Batman: Arkham City', 'Batman: Arkham Asylum', 'Star Wars: Knights of the Old Republic',
    # Simulation
    'American Truck Simulator', 'Euro Truck Simulator 2', 'Ori and the Will of the Wisps', 'Farming Simulator 22',
    'Cooking Simulator', 'House Flipper', 'PowerWash Simulator', 'Lawn Mowing Simulator', 'The Isle',
    'Train Sim World 2', 'PC Building Simulator', 'Destroy All Humans! 2: Reprobed',
    # Platformer
    'Getting Over It with Bennett Foddy', 'Cuphead', 'Ori and the Blind Forest', 'Geometry Dash',
    'Worms W.M.D', 'Celeste', 'Little Nightmares', 'Little Nightmares II', 'INSIDE',
    'PICO PARK', 'Hollow Knight', 'Night in the Woods', 'Pico Park',
    'A Hat in Time', 'I Wanna Be The Guy', 'Ōkami HD', 'Ōkami', 'Blasphemous', 'Islets',
    # Management
    'Catizens', 'RimWorld', 'Two Point Hospital', 'Sapiens', 'Farthest Frontier', 'Bear & Breakfast', 'Slime Rancher',
    'Two Point Campus', 'Unrailed!', 'My Free Zoo', 'Planet Zoo', 'Lobotomy Corporation', 'Unpacking', 'Barotrauma',
    'Graveyard Keeper', 'Stellaris', 'Gas Station Simulator', 'Frostpunk', 'Wobbledogs', 'Hardspace: Shipbreaker',
    'Planet Coaster', 'Arcade Paradise', 'Going Medieval', 'Spore',
    # Dialogue
    'Vampyr', 'Life is Strange: True Colors', 'Life is Strange', 'Persona 4 Golden',
    'Persona 5 Strikers', 'Detroit: Become Human', 'Undertale', 'The Stanley Parable: Ultra Deluxe', 'Persona 5 Royal',
    'Beyond: Two Souls', 'Danganronpa: Trigger Happy Havoc', 'Life is Strange 2',
    'L.A. Noire', 'Neon White', 'Ai: The Sodium Files', 'AI: The Somnium Files - Nirvana Initiative',
    'AI: The Somnium Files', 'Doki Doki Literature Club!', 'Danganronpa 2: Goodbye Despair',
    'Phoenix Wright: Ace Attorney − Trials and Tribulations', 'Phoenix Wright: Ace Attorney', 'The Great Ace Attorney',
    'The Great Ace Attorney Chronicles', 'Brok the Investigator',
    # Competitive
    'Legion TD 2', 'Smite', 'The Machines Arena',
    # Weird
    "Who's Your Daddy",
    # Creative
    'Warhammer', 'The Sandbox',
    # Music
    'osu!', 'Hatsune Miku: Project DIVA Mega Mix+', "FRIDAY NIGHT FUNKIN'", 'Clone Hero',
    'Rocksmith 2014 Edition - Remastered', 'Hatsune Miku: Colorful Stage!',
    # Vehicles
    'SnowRunner', 'Trials Rising',
    # Defence games
    'Plants vs. Zombies', 'Vampire Survivors', 'Bloons TD 6', 'Arknights',
    # Exploration
    "No Man's Sky", 'The Long Dark', 'Outer Wilds', 'Kena: Bridge of Spirits', 'Spiritfarer', 'Road 96',
    'Mount & Blade II: Bannerlord', 'Mount & Blade: Warband',
    # Stealth
    'Dishonored', 'Dishonored 2',
    # Sports
    'Golf It!', 'Riders Republic',
    # Story
    'A Plague Tale: Innocence', 'Lost in Random', 'Quantum Break', 'We Happy Few', 'Alice: Madness Returns',
    "Mirror's Edge Catalyst",
    "Hellblade: Senua's Sacrifice",
    # Roguelite
    'Noita', 'Risk of Rain 2', 'Tribes of Midgard', 'Spelunky', 'Spelunky 2', 'The Binding of Isaac: Repentance',
    "Don't Starve Together", 'Crypt of the NecroDancer', 'Nuclear Throne', 'Dead Cells', 'Minecraft Dungeons', 'Hades',
    "Death's Door"
]
