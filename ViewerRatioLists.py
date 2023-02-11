#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ViewerRatioLists.py

# Games I don't want to play mostly because they are violent, competitive or skill based
# The id in the blacklist is the twitch category id used for api calls
blacklist = [
    # Shooter games
    ['Fashion Police Squad', '829294318'], ['Deep Rock Galactic', '494839'], ['HITMAN 2', '506342'], ['gtfo', '500627'],
    ['The Last of Us Part I', '294724507'], ['GoldenEye 007', '829248383'], ['Alan Wake', '19156'], ['Vigor', '506489'],
    ['Gears of War: Ultimate Edition', '490354'], ['Metro Exodus: Enhanced Edition', '517865034'], ['Warface', '29918'],
    ['Mass Effect 3', '26992'], ['S.T.A.L.K.E.R.: Anomaly', '1549167076'], ['Signalis', '508685'], ['Synced', '515633'],
    ['Enlisted', '505257'], ['Killing Floor 2', '460508'], ['BioShock Remastered', '2009742488'], ['Destiny', '280721'],
    ['Evil West', '1488417149'], ['The Callisto Protocol', '838226069'], ['Stalcraft', '516866'], ['1v1.lol', '515978'],
    ['the last of us', '33180'], ['the last of us part ii', '494552'], ['Watch_Dogs', '65953'], ['Task Force', '10627'],
    ['Earth Defense Force 4.1: The Shadow of New Despair', '476437'], ['Mafia III', '490432'], ['Isonzo', '2044247183'],
    ['Fallout 3', '18763'], ['Earth Defense Force 5', '493080'], ['Counter-Strike', '10710'], ['Crossfire X', '512985'],
    ['apex legends', '511224'], ['quake', '7348'], ['Metro: Last Light Redux', '2098897146'], ['PlanetSide 2', '26175'],
    ['Watch Dogs 2', '492930'], ['Zombie Army 4: Dead War', '512968'], ['hitman', '491471'], ['Deadlink', '2079264738'],
    ['Hyper Demon', '1350012934'], ['Gundam Evolution', '584047654'], ['gears 5', '506407'], ['Ready or Not', '511701'],
    ['Predator: Hunting Grounds', '512551'], ['Deadside', '516097'], ['Prodeus', '512629'], ["Sector's Edge", '513252'],
    ['hell let loose', '497440'], ['hunt: showdown', '500188'], ['hyper scape', '518306'], ['Rollerdrome', '772915712'],
    ['Shatterline', '528918758'], ['The Greatest Penguin Heist of All Time', '635251134'], ['World Boss', '1558011199'],
    ['fallout 76', '506246'], ['f.e.a.r. perseus mandate', '14310'], ['Cold War', '2732'], ['Gran Turismo 7', '518014'],
    ['splitgate', '499310'], ['squad', '488479'], ['star wars battlefront ii', '492546'], ['Sker Ritual', '1017537377'],
    ['Gears of War 3', '27596'], ['Gears of War 3', '27596'], ['APB Reloaded', '19157'], ['Unreal Tournament', '16007'],
    ['SUPERHOT', '313566'], ['theHunter Classic', '23171'], ['Deceive Inc.', '512232'], ['Gungrave G.O.R.E.', '501087'],
    ['returnal', '518019'], ['rogue company', '514194'], ['sniper elite 5', '511743'], ['Watch Dogs: Legion', '512895'],
    ['T3 Arena', '1731084649'], ['STG Shmups', '519380'], ['STG Shmups', '519380'], ['Earth Defense Force 6', '518402'],
    ['Warhammer 40,000: Space Marine', '21495'], ['Duke Nukem Forever', '18944'], ['Rising Storm 2: Vietnam', '492763'],
    ['metro exodus', '497410'], ['mass effect legendary edition', '1568081763'], ['Holdfast: Nations At War', '498983'],
    ['BioShock 2 Remastered', '2143844298'], ['Metro 2033 Redux', '1388848972'], ['The First Descendant', '2104758320'],
    ['Crossfire', '27101'], ['Overwatch 2', '515025'], ['battlebit', '496916'], ['F.E.A.R. 2: Project Origin', '18886'],
    ['Gunner, HEAT, PC!', '1688112273'], ['Terminator: Resistance', '514426'], ['Aliens: Fireteam Elite', '1585949885'],
    ['Family Battle: Tag Arena', '1871077473'], ['Zero Sievert', '324194362'], ['Wolfenstein: The New Order', '369259'],
    ['Metro: Last Light', '31836'], ['Alan Wake Remastered', '1293419931'], ['The Last of Us Remastered', '1200871695'],
    ['aim gods', '516967'], ['aim lab', '503456'],  ['anthem', '460696'], ['counter-strike: global offensive', '32399'],
    ['Counter-Strike: Source', '10407'], ['Sudden Attack', '29068'], ['Bioshock Infinite', '29099'], ['Prey', '15013'],
    ['S.T.A.L.K.E.R.: Shadow of Chernobyl', '10775'], ['SCUM', '495811'], ['BioShock', '15866'], ['Vanquish', '26960'],
    ['The Outer Worlds', '510580'], ['Star Valor', '508764'], ['cruelty squad', '977894696'], ['Cultic', '1055115891'],
    ['Wolfenstein II: The New Colossus', '497439'], ['The Cycle: Frontier', '470840663'], ['team fortress 2', '16676'],
    ['Way of the Hunter', '489308483'], ['Mafia II: Definitive Edition', '2058566581'], ['Chop Goblins', '2075219039'],
    ['Fallout: New Vegas', '23453'], ['APEX', '1848487811'], ['Quake Live', '19490'], ['Xmas Apocalypse', '170702509'],
    ['theHunter: Call of the Wild', '494683'], ['Evil Dead: The Game', '1022719138'], ['Hell is Others', '1048673384'],
    ['Fallout 4', '489776'], ['quake champions', '496253'], ['Adaca', '544704748'], ['Star Wars: Squadrons', '518059'],
    ['World War Z: Aftermath', '1280358639'], ['Road to Vostok', '461934448'], ['Mafia: Definitive Edition', '517769'],
    ['Arma Reforger', '478407715'], ['payday 2', '65997'], ['outriders', '512930'], ['Perfect Heist 2', '1255642391'],
    ['Alliance of Valiant Arms', '26569'], ['Generation Zero', '33389'], ['hitman 3', '518011'], ['Deus Ex', '16082'],
    ['destiny 2', '497057'], ['deathloop', '512983'], ['Mass Effect: Andromeda', '460695'],  ['Skyscraper', '512206'],
    ['Company of Heroes', '17343'], ['Ring Of Elysium', '504954'], ['F.E.A.R.', '4392'], ['Sniper Elite 4', '491769'],
    ['Paladins', '491115'], ['Hypercharge: Unboxed', '497769'], ['Half-Life 2', '1420'], ['gunfire reborn', '517645'],
    ['totally accurate battlegrounds', '506344'], ['true crime: new york city', '3077'], ['Gears of War 4', '459382'],
    ['Midair 2', '517069'], ['Severed Steel', '1172476700'], ['MetaOps', '1220570282'], ['Gears of War 2', '18884'],
    ['Krunker', '508391'], ['Let It Die', '460641'], ['Mass Effect', '15510'], ['Big Buck Hunter Arcade', '505226'],
    ['insurgency: sandstorm', '491705'], ['max payne 3', '21222'], ['Fabular: Once upon a Spacetime', '1977257893'],
    ['Aliens vs. Predator', '23979'], ['gunz: the duel', '513567'], ['HITMAN World of Assassination', '1780647523'],
    ['Days Gone', '497456'], ['ULTRAKILL', '514166'], ['Quake II', '2955'], ['Star Wars: Battlefront II', '6490'],
    ['Deadpool', '509509'], ['BIGFOOT', '6675'], ['Company of Heroes 3', '1931776829'], ['BioShock 2', '19030'],
    ['Arma 3', '31750'], ['Mafia', '14562'], ['High on Life', '1910324696'], ["KovaaK's Aim Trainer", '510911'],
    ['Killer7', '16823'], ['Death in the Water 2', '940111995'], ['DUSK', '493813'], ['Deadrop', '124244595'],
    ['Firewall Zero Hour', '500644'], ['Mass Effect 2', '19676'], ['Natural Selection 2', '22038'],
    ['Perfect Dark', '2686'],
    # Shooter - Mech
    ['Armored Core', '15267'], ['Mech Arena: Robot Showdown', '685005254'], ['MechWarrior 5: Mercenaries', '494684'],
    ['Mobile Suit Gundam: Extreme Vs. Maxi Boost', '490808'], ['Mobile Suit Gundam Battle Operation 2', '499526'],
    ['titanfall 2', '489201'], ['Super Mecha Champions', '512844'], ['SD Gundam Battle Alliance', '1179447665'],
    ['MechWarrior Online', '24623'], ['Roboquest', '518178'],
    # Shooter - Borderlands
    ['Borderlands 2', '32345'], ['Borderlands', '18734'], ['Borderlands: Game of the Year Enhanced', '1579552694'],
    ['New Tales from the Borderlands', '1407310739'], ['Borderlands: The Pre-Sequel', '460041'],
    ["Tiny Tina's Wonderlands", '1318043161'], ['Tales from the Borderlands', '458778'],
    # Shooter - Saint's Row
    ['Saints Row', '1067345253'], ['Saints Row: The Third Remastered', '747702304'], ['Saints Row: The Third', '23268'],
    ['Saints Row 2', '18906'], ['Saints Row IV', '33086'],
    # Shooter - Doom
    ['doom eternal', '506442'], ['DOOM 3', '13342'], ['DOOM 64', '15389'], ['DOOM II: Hell on Earth', '584'],
    ['DOOM', '6715'],
    # Shooter - Uncharted
    ['Uncharted: The Lost Legacy - Remastered', '1573450322'], ["Uncharted 4: A Thief's End - Remastered", '230322618'],
    ["Uncharted 4: A Thief's End", '458641'], ["Uncharted: Drake's Fortune", '12845'],
    ['Uncharted: The Lost Legacy', '494558'], ['Uncharted 2: Among Thieves', '20357'],
    # Shooter - Call of Duty
    ['Call of Duty: Advanced Warfare', '417973'], ['Call of Duty 4: Modern Warfare', '1964'], ['Call of Duty', '1494'],
    ['Call of Duty: World at War', '19006'], ['call of duty: black ops 4', '504462'], ['call of duty: wwii', '496712'],
    ['call of duty: black ops iii', '489401'], ['Call of Duty: Ghosts', '118200'], ['call of duty: warzone', '512710'],
    ['Call of Duty: Infinite Warfare', '491437'], ['call of duty: black ops ii', '34134'], ['Call of Duty 2', '2162'],
    ['Call of Duty: Modern Warfare 3', '31551'], ['Call of Duty: Modern Warfare 2 Campaign Remastered', '478314500'],
    ['call of duty: modern warfare remastered', '494155'], ['Call of Duty: Modern Warfare II', '1678052513'],
    ['call of duty: modern warfare', '1614555304'], ['call of duty: black ops cold war', '512709'],
    ['call of duty: vanguard', '492778073'], ['call of duty: modern warfare 2', '22393'],
    ['Call of Duty: Warzone 2.0', '1704092816'], ['Call of Duty: Black Ops', '23894'],
    ['Call of Duty: Black Ops III - Zombies Chronicles', '266199487'],
    # Shooter - Grand Theft Auto
    ['Grand Theft Auto: Vice City', '15631'], ['Grand Theft Auto: San Andreas – The Definitive Edition', '89250567'],
    ['Grand Theft Auto', '12453'], ['Grand Theft Auto III', '3412'], ['Grand Theft Auto: San Andreas', '6521'],
    ['Grand Theft Auto: Vice City – The Definitive Edition', '957103328'], ['Grand Theft Auto IV', '18707'],
    ['grand theft auto iv: the ballad of gay tony', '2113221108'], ['GTA: La Heist', '41272850'],
    ['grand theft auto v', '32982'],
    # Shooter - Metal gear
    ['metal gear solid', '14805'], ['metal gear solid 2: sons of liberty', '11386'], ['Metal Gear Survive', '498026'],
    ['metal gear solid 4: guns of the patriots', '18893'], ['metal gear solid 3: snake eater', '16582'],
    ['metal gear rising: revengeance', '24208'], ['Metal Gear Solid V: The Phantom Pain', '91419'],
    ['Metal Gear Acid', '8798'],
    # Shooter - Halo
    ['Halo Wars 2', '490446'], ['Halo 3', '9178'], ['Halo 5: Guardians', '369567'], ['Halo: Combat Evolved', '2397'],
    ['halo: the master chief collection', '417969'], ['halo infinite', '506416'], ['halo: reach', '24203'],
    ['halo 2', '6511'], ['Halo 4', '31879'],
    # Shooter - Tom Clancy
    ["Tom Clancy's Ghost Recon: Breakpoint", '512534'], ["Tom Clancy's Ghost Recon: Wildlands", '490379'],
    ["Tom Clancy's Rainbow Six Extraction", '513004'], ["tom clancy's rainbow six: siege", '460630'],
    ["tom clancy's the division 2", '504463'], ["tom clancy's rainbow six siege", '460630'],
    ["tom clancy's the division", '369579'], ["Tom Clancy's Rainbow Six", '7228'],
    # Shooter - Battlefield
    ['battlefield: bad company 2', '22851'], ['battlefield 3', '24394'], ['battlefield 4', '66402'],
    ['battlefield v', '504199'], ['battlefield 1', '488500'], ['battlefield 2', '15467'],
    ['battlefield 2042', '514974'],
    # Shooter - Far cry
    ['Far Cry 3', '29635'], ['far cry', '13564'], ['Far Cry: Primal', '490919'], ['far cry 6', '518692'],
    ['Far Cry New Dawn', '510586'], ['Far Cry 5', '497078'], ['Far Cry 4', '460384'],
    # Bossfights
    ['Elden Ring', '512953'], ["demon's souls", '21812'], ['Wo Long: Fallen Dynasty', '1450386257'], ['Nioh', '24872'],
    ['bloodborne', '460636'], ['dark souls', '29433'], ['dark souls iii', '490292'], ['Ninja Gaiden Sigma 2', '23134'],
    ['sekiro: shadows die twice', '506415'], ['the surge', '496233'], ['black mesa', '68016'], ['nioh 2', '506468'],
    ['Company of Heroes 2', '65663'], ['Evolve Stage 2', '1893365738'], ['Dark Souls: Remastered', '1122982998'],
    ['Steelrising', '518621'], ['hellpoint', '496421'], ['Left 4 Dead', '18916'], ["Asura's Wrath", '29420'],
    ['mortal shell', '516915'], ['Kingdom Hearts III', '369585'], ['Star Wars Jedi: Fallen Order', '503446'],
    ['dark souls ii', '91423'], ['nioh 2: the complete edition', '160136078'], ['left 4 dead 2', '24193'],
    ['The Last Hero of Nostalgaia', '943590253'], ['Dark Souls: Prepare to Die Edition', '924683477'],
    ['Ninja Gaiden Sigma', '17000'],
    # Medieval fights
    ["Conqueror's Blade", '498523'], ['Mortal Online 2', '517282'], ['chivalry 2', '512971'], ['for honor', '490382'],
    ['Dark and Darker', '2009321156'], ['Warlander', '1557946295'], ["Joe Dever's Lone Wolf: HD Remastered", '493192'],
    ['The Last Oricru', '313407471'], ['Totally Accurate Battle Simulator', '493069'], ['Warhaven', '197105496'],
    ['Warhammer: Vermintide 2', '498668'], ['mordhau', '498859'], ['We Who Are About To Die', '1533045811'],
    ['Ryse: Son of Rome', '28557'],
    # Swordfight
    ['No More Heroes III', '513000'], ['sifu', '506089309'], ["Ghost of Tsushima: Director's Cut", '350892884'],
    ['ghost of tsushima', '499856'], ['No More Heroes', '5123'],
    # Violent Survival - Looter shooter
    ['dayz', '65632'], ['SurrounDead', '750209762'], ['Lost Light', '1706428735'], ['escape from tarkov', '491931'],
    ['Dying Light 2: Stay Human', '506410'], ['Dying Light', '369380'], ['State of Decay 2', '495122'],
    ['Dead Island', '19622'], ['Mad Max', '8271'], ['Unturned', '417932'], ['Marauders', '556660222'],
    ['DeadPoly', '1688925820'], ['Dead Island: Riptide', '65967'], ['Dead Frontier 2', '509128'],
    ['Just Survive', '491480'],
    # Fist fighting
    ['Teenage Mutant Ninja Turtles: The Cowabunga Collection', '273325610'], ['Midnight Fight Express', '519493'],
    ['Teenage Mutant Ninja Turtles', '1864659375'], ['River City Girls', '513359'], ['Judgment', '509482'],
    ['lost judgment', '2120403770'], ['River City Girls 2', '559934641'], ['sleeping dogs', '26547'],
    ['Teenage Mutant Ninja Turtles: Cowabunga', '140101465'],
    ['Sleeping Dogs: Definitive Edition', '322063165'],
    # Fist fighting - Yakuza
    ['Yakuza 3 Remastered', '870905192'], ['Yakuza Kiwami 2', '498510'], ['yakuza', '6571'], ['yakuza 0', '476269'],
    ['Yakuza Kiwami', '490702'], ['Yakuza 5 Remastered', '1844151778'], ['yakuza: like a dragon', '512121'],
    ['yakuza 6: the song of life', '490701'], ['Yakuza 4 Remastered', '445444679'], ['yakuza 5', '32541'],
    ['Yakuza 3', '20250'],
    # Drama
    ['West Hunt', '603089883'], ['Unfortunate Spacemen', '492529'], ['Is It You?', '172861049'], ['SpyParty', '27449'],
    ['Deducto', '866701566'], ['Dubium', '1420830956'], ['Project Winter', '509893'], ['Goose Goose Duck', '14333696'],
    ['among us', '510218'], ['Politics', '515214'], ['Gang Beasts', '459527'], ['Midnight Ghost Hunt', '1262894464'],
    ['Town of Salem', '417694'], ['Eville', '517143'], ['Dread Hunger', '511181708'], ['As Dusk Falls', '518875'],
    ['PULSAR: Lost Colony', '417919'], ['The Matriarch', '699374847'], ['Traitors in Salem', '330878476'],
    ['Clue/Cluedo: The Classic Mystery Game', '508322'], ['Among Us', '1089438810'],
    # Drama - The Walking Dead
    ['The Walking Dead: Survivors', '47011541'], ['The Walking Dead: The Telltale Series Collection', '499987'],
    ['The Walking Dead: A New Frontier', '461246'], ['The Walking Dead: The Final Season', '497916'],
    ['The Walking Dead: Season Two', '66410'], ['The Walking Dead: Saints %26 Sinners', '515862'],
    ['The Walking Dead: Saints %26 Sinners - Ch 2: Retribution', '855045563'],
    ['The Walking Dead: Season One', '30740'],
    # Horror - Psychological - Jump scares - Gore
    ['Amnesia: The Dark Descent', '27127'], ['Layers of Fear', '490537'], ['Forsake', '1617126896'], ['SOMA', '458224'],
    ['Remnant: From the Ashes', '509066'], ['The Dark Pictures Anthology: Little Hope', '514207'], ['Deceit', '493244'],
    ['Vampire: The Masquerade', '492963'], ['Haunted PS1 Demo Disc: Spectral Mall', '608712516'], ['Luto', '486610138'],
    ['Alien: Isolation', '458443'], ['The Quarry', '1937599489'], ['Simulacra 3', '1831336412'], ['Darkwood', '313146'],
    ['The Mortuary Assistant', '1945673289'], ['madison', '1535635666'], ['Pacify', '511134'], ['Dino Crisis', '10945'],
    ['Hellseed', '1650671675'], ['Dead Rising 4', '493389'], ['Scarlet Hollow', '1310224550'], ['Tattletail', '494869'],
    ['Fear Therapy', '819777302'], ['Dead Space', '1338005147'], ['Lunch Lady', '477532253'], ['Rule of Rose', '11743'],
    ['Alisa', '516354'], ['Born Into Fear', '1984206929'], ['Slender: The Arrival', '68074'], ['Stranger', '228183669'],
    ['At Dead Of Night', '1180890490'], ['Scathe', '513761526'], ['Lost in Vivo', '510024'], ['Maid of Sker', '510106'],
    ['White Day: A Labyrinth Named School', '13425'], ['Refund Me If You Can', '866831809'], ['Bullet Force', '502060'],
    ['Vampire: The Masquerade - Bloodlines', '15062'], ['The Convenience Store', '517030'], ['Dead Rising 3', '369565'],
    ['Heavy Rain', '19423'], ['The Dark Pictures Anthology: House of Ashes', '1274531553'], ['Borderlands 3', '491318'],
    ["Maurice: In The Predator's Nest", '1342707206'], ['Garten of Banban', '1804964602'], ['Who Knocks', '1163498175'],
    ["Happy's Humble Burger Farm", '1893523506'], ['Bendy and the Ink Machine', '496431'], ['Song of Horror', '514930'],
    ['Labyrinthine', '517528'], ['Ghost Watchers', '790163050'], ['DEVOUR', '836519689'], ['Call of Cthulhu', '459262'],
    ['Tormented Souls', '519192'], ['Forewarned', '783609948'], ['The Medium', '517401'], ['Deadly Night', '913013812'],
    ['Friday the 13th', '19562'], ['the evil within 2', '497437'], ['Visage', '494082'], ['Murder House', '1646904797'],
    ['Fatal Frame', '16570'], ['Nighthunt', '1268832494'], ['Ghost Exile', '289552769'], ['Amnesia: Rebirth', '516624'],
    ['JR’s', '623775229'], ['Blair Witch', '512981'], ['Remnant Records', '1869189136'], ['Layers of Fear 2', '510090'],
    ['The Joy of Creation', '498160'], ['Bloodstained: Ritual of the Night', '489642'], ['The Bathhouse', '1584532157'],
    ['Parasite Eve', '8464'], ["Summer of '58", '2080474707'], ['SIMULACRA', '499910'], ['Endoparasitic', '1090256367'],
    ['Thymesia', '64300975'], ['Until Dawn', '67637'], ['Broken Pieces', '850501121'], ['Martha Is Dead', '1691026305'],
    ['The Park', '490984'], ['Iron Lung', '1297345368'], ['back 4 blood', '511746'], ['Phantom Hysteria', '1472119142'],
    ['Dead Space 2', '23017'], ['Dead Space', '19009'], ['Outlast II', '510117'], ['Ghost Exorcism Inc.', '1239774436'],
    ['Friday the 13th: The Game', '488518'], ['The Backrooms 1998', '624848592'], ["I'm on Observation Duty", '510773'],
    ['SCP: Pandemic', '516702'], ['Dead Space 3', '65706'], ['ObsCure', '3408'], ['Dread X Collection 5', '1362590789'],
    ['Standoff 2', '513501'], ['In Sound Mind', '518088'], ['Scorn', '494081'], ['Condemned: Criminal Origins', '8068'],
    ['Horror Game Collection', '560237920'], ['This is a Ghost', '861867398'], ['Doki Doki Literature Club!', '497527'],
    ['From the Darkness', '220074709'], ['Christmas Massacre', '2014004194'], ['FOBIA: St. Dinfna Hotel', '2037799395'],
    ['Poppy Playtime', '2058220722'], ['Nightmare of Decay', '1034527557'], ['Night At the Gates of Hell', '325280449'],
    ['Inside the Backrooms', '1144809661'], ['Amnesia: Rebirth', '516624'], ["I'm on Observation Duty 5", '1654421360'],
    ['The Escape: Together', '1122801725'], ['SCP: Labrat', '390159386'], ['Fears to Fathom: Home Alone', '1399681620'],
    ['Yomawari: Night Alone', '491581'], ['Horror Tycoon', '273983591'], ['Hello Puppets: Midnight Show', '1509911901'],
    ['The Evil Within', '68000'], ['The Evil Within 2', '497437'], ['Chernobylite', '513597'], ['Dead Rising', '7995'],
    ['Stay Out of the House', '1029754927'], ['Ghostbusters: Spirits Unleashed', '783596487'], ['Psych', '1114000446'],
    ['The Dark Pictures Anthology: The Devil in Me', '654543582'], ['Devour', '836519689'], ['Dead Rising 2', '22797'],
    ['Metal: Hellsinger', '517999'], ['Cry of Fear', '115546'], ['S.P.A.T.', '1690176578'], ['Phasmophobia', '518184'],
    ['Yomawari: Lost in the Dark', '2051835775'], ['Yomawari: Midnight Shadows', '497763'], ['Nun Massacre', '509959'],
    ["Spooky's Jump Scare Mansion: HD Renovation", '496499'], ['Boo Men', '1137292380'], ['Secret Neighbor', '509065'],
    ['The Fridge is Red', '289024523'], ["Spooky's Jump Scare Mansion", '489555'], ['The Closing Shift', '1419063656'],
    ['SCP: Containment Breach', '65745'], ['SCP: Secret Laboratory', '498744'], ['Escape the Backrooms', '2066107586'],
    ['Obsideo', '1171273884'], ['The Complex: Found Footage', '1850434022'], ['The Backrooms: Survival', '1461285830'],
    ['Amnesia: A Machine for Pigs', '33692'], ['Deathwatch', '435007956'], ["I'm on Observation Duty 4", '1677489258'],
    ['The Chant', '928614244'], ['Vade Retro: Exorcist', '1674030944'], ["Zero Escape: Virtue's Last Reward", '32506'],
    ['Fears to Fathom: Norwood Hitchhike', '2099118364'], ['The Madvent Calendar', '329627642'], ['Outlast', '73586'],
    ['Devour', '836519689'], ['Faith', '136173336'], ['FAITH: Chapter II', '511640'], ['Find Yourself', '1724063925'],
    ['Fatal Frame III: The Tormented', '6604'], ['Haunting Ground', '2607'], ['Bendy and the Dark Revival', '516089'],
    ['World of Horror', '501951'], ['Home Sweet Home', '8828'], ['The Bridge Curse: Road To Salvation', '2081287761'],
    ['SIMULACRA 3', '1831336412'], ['Lunch Lady', '477532253'], ['Vampire: The Masquerade - Bloodhunt', '1411398523'],
    ['The Dark Pictures Anthology: Man of Medan', '509249'], ['Mirror Forge', '1984401775'], ['Mad Father', '126312'],
    ['SCP: Secret Files', '983939782'], ['The Infected', '519272'], ['Fatal Frame: Maiden of Black Water', '460160'],
    ['Is Simon There?', '443409039'], ['Fatal Frame II: Crimson Butterfly', '8483'], ['The Beast Inside', '504389'],
    ['Melty Blood: Type Lumina', '936945829'], ['Dark Deception', '460018'], ['Video Horror Society', '642328546'],
    ['Fears to Fathom: Carson House', '976324957'], ["Father's Day", '1311006114'], ['MetaPhysical', '593336080'],
    ['The Death: Than Trung', '129113862'], ['September 7th', '1327012121'], ['FAITH: Chapter III', '2005106062'],
    ['Crimson Snow', '766247336'], ['Krampus is Home', '508995'], ["Eternal Darkness: Sanity's Requiem", '6888'],
    ['Krampus Kills', '1296236974'], ['Cthulhu Saves Christmas', '513992'], ['Project: Playtime', '1727187055'],
    ['The Forgotten Tapes: Analog Nightmares', '1710778930'], ['Doki Doki Literature Club Plus!', '543795917'],
    ['Welcome to the Game II', '499507'], ['Dead Space', '980679052'],
    # Horror - Resident evil
    ['Resident Evil Code: Veronica', '12789'], ['Resident Evil Code: Veronica X HD', '7690'], ['Resident Evil', '5360'],
    ['Resident Evil Re:Verse', '1407147388'], ['Resident Evil 5 Remastered', '256804748'], ['Resident Evil 5', '18808'],
    ['Resident Evil Survivor', '14528'], ['Resident Evil 4: Otome Edition', '1638636362'], ['Resident Evil 4', '1468'],
    ['resident evil 7 biohazard', '492934'], ['Resident Evil Resistance', '514308'], ['Resident Evil Outbreak', '535'],
    ['Resident Evil Zero', '9402'], ["Resident Evil: Director's Cut", '9348'], ['Resident Evil: Revelations', '28576'],
    ['Resident Evil 4 HD', '784020615'], ['Resident Evil 0', '489721'], ['Resident Evil Outbreak File %232', '13961'],
    ['resident evil village', '518017'], ['Resident Evil: Deadly Silence', '352'], ['Resident Evil 3', '649775967'],
    ['resident evil 2', '8645'], ['resident evil 3: nemesis', '5126'], ['Resident Evil: Revelations 2', '461522'],
    ['Resident Evil 6', '33437'],
    # Horror - Five Nights at Freddy's
    ['Ultimate Custom Night', '508445'], ["Five Nights at Freddy's 2", '488559'], ["Five Nights at Freddy's", '418063'],
    ["Five Nights at Freddy's: Sister Location", '492810'], ["Five Nights at Freddy's: Help Wanted", '511841'],
    ["Five Nights at Freddy's: Security Breach", '2143096682'], ["Five Nights at Freddy's 4", '489567'],
    ['The Glitched Attraction', '1723109546'],
    # Horror - Silent Hill
    ['Silent Hill', '3947'], ['Silent Hill: Downpour', '27626'], ['Silent Hill 2', '9891'], ['Silent Hill 3', '9522'],
    ['Silent Hill 4: The Room', '5804'], ['Silent Hill: Homecoming', '18864'], ['Silent Hill: Origins', '13206'],
    ['Silent Hill 3', '1459558487'],
    # Murder mystery
    ["Conrad Stevenson's Paranormal P.I.", '862489808'], ["Handy Harry's Haunted House Services", '1450669133'],
    ['gone home', '65752'], ['What Remains of Edith Finch', '490174'],
    # Underwater
    ['Maneater', '506452'],
    # Story
    ['half-life', '2755'], ['red dead redemption 2', '493959'], ['Just Cause 3', '488564'], ['Just Cause 4', '506384'],
    ['crysis', '10818'], ['death stranding', '494364'], ['Evoland', '140005'], ['Red Dead Redemption', '22848'],
    # Story - Tomb Raider
    ['Tomb Raider III: Adventures of Lara Croft', '17945'], ['Tomb Raider Level Editor', '515584'],
    ['Rise of the Tomb Raider', '460620'], ['Tomb Raider', '2770'], ['Tomb Raider II', '317'],
    ['Shadow of the Tomb Raider', '504735'], ['Tomb Raider: Definitive Edition', '868689686'],
    # Story - God of War
    ['God of War Ragnarök', '102007682'], ['God of War', '6369'], ['God of War III: Remastered', '1938435210'],
    ['God of War III', '18703'], ['God of War II', '10384'], ['God of War HD', '995720898'],
    # Roguelites / dungeon crawlers
    ['There Is No Light', '898087921'], ['Dark Cloud 2', '9182'], ['Devil May Cry', '283386'], ['Rounds', '1747174592'],
    ['Loop Hero', '1535565784'], ['Castle Crashers', '18950'], ['Risk of Rain 2', '509110'], ['Soulstice', '358302053'],
    ['No Place For Bravery', '518094'], ['Tiny Rogues', '1760477474'], ['Helldivers', '313521'], ['Spelunky', '22619'],
    ['Hades', '510590'], ["Despot's Game", '2069330253'], ['Ship of Fools', '1547266159'], ['Pokémon Rumble', '24305'],
    ['path of exile', '29307'], ['warframe', '66170'], ['Enter the Gungeon', '488632'], ['Darkest Dungeon', '458353'],
    ['Gauntlet: Slayer Edition', '184615409'], ['UNDECEMBER', '145787409'], ['Warhammer 40,000: Darktide', '518873'],
    ['Devil May Cry 4: Special Edition', '488974'], ['Darkest Dungeon II', '511471'], ['Dome Keeper', '1771631982'],
    ['Torchlight: Infinite', '890558948'], ['Last Epoch', '503932'], ['The Binding of Isaac: Repentance', '491080'],
    ['Code Vein', '496697'], ['Boyfriend Dungeon', '499821'], ['Dark Cloud', '1705'], ['Sea of Thieves', '490377'],
    ['Devil May Cry 5', '506412'], ['Have a Nice Death', '375960865'], ['The Binding of Isaac: Rebirth', '94073'],
    ['Warhammer 40,000: Inquisitor - Martyr', '496021'], ["Despot's Game: Dystopian Army Builder", '991521214'],
    ['Bravery and Greed', '676925111'], ['Endless Dungeon', '2145566326'], ['DmC: Devil May Cry', '12004'],
    ['Brotato', '743214338'], ['Spelunky 2', '499859'], ['Scott Pilgrim vs. the World: The Game', '26599'],
    ['The Binding of Isaac', '32207'], ["Devil May Cry 3: Dante's Awakening – Special Edition", '488844'],
    ['The Binding of Isaac: Repentance', '1414860634'], ['Titan Quest Anniversary Edition', '500585'],
    ['Devil May Cry 5: Special Edition', '1367248546'],
    # Roguelite - Turn based
    ['Inkbound', '82779299'], ['Golfie', '1265387454'],
    # Roguelite - Diablo
    ['Diablo', '5492'], ['diablo ii', '1041'], ['diablo iii', '313558'], ['diablo iii: reaper of souls', '313558'],
    ['Diablo II: Resurrected', '1788326126'], ['diablo immortal', '510150'], ['Diablo IV', '515024'],
    # Roguelite - Hack and slash - Level up character to unlock new characters - Beat 'em up - Run 'n' gun
    ['Hero Siege', '416015'], ['Realm of the Mad God', '28834'], ['Nobody Saves the World', '1723092203'], ['Neon Abyss', '512017'],
    # Dialogue game
    ['VA-11 HALL-A: Cyberpunk Bartender Action', '461529'], ['Persona 3 FES', '18908'],
    # Hide and seek
    ['Propnight', '1342987707'], ['Somni', '1878649756'], ['Witch It', '494792'], ['Killer in the Cabin', '1051016179'],
    ["garry's mod", '18846'], ['dead by daylight', '491487'], ['Monstrum 2', '519309'], ['Among the Sleep', '65871'],
    ['Identity V', '508662'], ['Prop and Seek', '516287'], ['Just Act Natural', '1100117120'],
    # VR
    ['POPULATION: ONE', '1900396348'], ['VAIL VR', '1405679224'], ['VAIL VR', '1405679224'], ['Synth Riders', '508865'],
    ['Hot Dogs, Horseshoes %26 Hand Grenades', '492164'], ['Gorilla Tag', '665425234'], ['Blade %26 Sorcery', '510100'],
    ['BONEWORKS', '511773'], ['Echo Arena', '497461'], ['Contractors VR', '1331100283'], ['After the Fall', '513010'],
    ['Rec Room', '493280'], ['vrchat', '499003'], ['Bonelab', '1227893925'], ['Zenith: The Last City', '1618840991'],
    ['beat saber', '503116'], ['Pavlov VR', '496142'], ['half-life: alyx', '515195'], ['Into the Radius', '511922'],
    ['DCS World', '313331'], ['Among Us VR', '62760102'], ['Contractors', '510095'], ['VTOL VR', '497816'],
    ['Resident Evil 4 VR', '1310524846'],
    # Stealth
    ['Magic Spellslingers', '516538'], ['Dishonored', '32156'], ['Dishonored 2', '490348'], ['Gloomwood', '518084'],
    ['this land is my land', '512842'], ['Middle-earth: Shadow of Mordor', '458619'], ['Aragami 2', '519497'],
    ['Serial Cleaners', '1949432105'], ['Hello Neighbor', '493618'], ['Hello Neighbor 2', '518878'],
    # Money
    ['Undead Blocks', '1912435287'], ['Pokémon Trading Card Game Online', '32634'], ['Stocks And Bonds', '5899'],
    ['Lottery Simulator', '497156'], ['Pokémon Trading Card Game', '9618'], ['Coin Pusher World', '530998549'],
    ['Wheel of Fortune', '2126'], ['Day Trader', '10953'], ['Pokémon Trading Card Game Live', '155409827'],
    ['crypto', '499634'], ['horse racing', '6891'], ['rFactor 2', '24636'], ['Bitcoin', '515880'],
    # Money - Casino
    ['Prominence Poker', '492287'], ['virtual casino', '29452'], ['slots', '498566'], ['poker quest', '308324368'],
    ['poker', '488190'], ['Casino', '582382910'], ['Blackjack', '2030294088'], ['Luck be a Landlord', '543194321'],
    # Money - Includes NFT's
    ['MetalCore', '1457260524'], ['Axie Infinity', '508967'], ['Splinterlands', '589569308'], ['Illuvium', '503221810'],
    ['Lost Relics', '889640923'],
    # Money - Subscription based
    ['Dual Universe', '493826'], ['World of Warcraft', '18122'], ['World of Warcraft Classic', '190105045'],
    # Weird Sexual
    ['In Silence', '2010603021'], ['ValiDate: Struggling Singles in your Area', '1566076397'], ['Bayonetta 2', '68015'],
    ['Beauty & Body Art', '509669'], ["Love, Money, Rock'n'Roll", '517967'], ['Monster Prom 2: Monster Camp', '513819'],
    ['Monster Prom', '498345'], ['Just Dance 2022', '413353439'], ['Monster Prom 3: Monster Roadtrip', '2097451607'],
    ['Hooked on You: A Dead by Daylight Dating Sim', '160028919'], ['Just Dance', '25122'], ['Bayonetta', '18933'],
    ['asmr', '509659'], ['pools, hot tubs, and beaches', '116747788'], ['Just Dance 2023 Edition', '1113191219'],
    ['Bayonetta 3', '500621'], ['Entropia Universe', '19714'],
    # Weird - IRL - Controversial - Rude
    ['Talk To Me', '50925173'], ['Gaming Late at Night', '2133075861'], ['Quiz Show', '17085'], ['Family Feud', '9815'],
    ["I'm Only Sleeping", '498592'], ['just chatting', '509658'], ['twitch plays', '491180'], ['Fishing', '1110106829'],
    ['Test, Test', '2070714813'], ['McPixel 3', '1421724731'], ['Minicraft', '752209654'], ['Special Events', '509663'],
    ['Sleep', '154096350'], ['Tarot', '83418'], ['Food%20%26%20Drink', '509667'], ['Talk Shows %26 Podcasts', '417752'],
    ['The Ship: Remasted', '492683'], ['Cultivation', '19741'], ['Theology', '1317721335'], ['Reaction', '1559544038'],
    ['Bad Guys at School', '1087376848'], ['Lost in Play', '181659447'], ['Animals, Aquariums, and Zoos', '272263131'],
    ['Bully', '9440'], ['Bully: Scholarship Edition', '4667'], ['IRL: The Game', '1063483442'], ['Others', '512354'],
    ['Christmas', '1947006064'], ['Games %2B Demos', '66082'], ['Playing Games', '491032618'], ['Steam', '11530'],
    ['Travel %26 Outdoors', '509672'], ['The Simpsons: Hit %26 Run', '2897'], ['EZ2ON REBOOT : R', '2057185004'],
    ['Pokémon Community Game', '329951934'], ['Coffee Talk', '512306'], ['Live', '508402'], ['Chill', '28838'],
    ['watch parties', '515467'],
    # Weird DMCA - Shows/movies - Radio
    ['FUSER', '516513'], ['DJ Life', '24504'], ['Sexy Sniper', '643318802'], ['One Piece', '30012'], ['Music', '26936'],
    ['Anime World', '637756067'], ['Always On', '499973'], ['Sexy Miss', '1129360291'], ['The Simpsons', '2046821115'],
    ['Relaxing Waves', '872742502'], ['South Park', '8105'], ['Nothing', '1709696975'], ['TV Station Manager', '8259'],
    ['Rock Band 4', '489136'], ['South Park: The Stick of Truth', '33175'], ['Disney Dreamlight Valley', '1515862749'],
    ['The Spongebob Squarepants Movie', '503749'], ['Dragon Ball', '317912951'], ['Rocksmith%2b', '2023547331'],
    ['Watch TV', '1865070091'], ['World Cup', '2119643460'], ['South Park: The Fractured But Whole', '490378'],
    ['Artifact', '16937'], ['El Chavo', '34054'], ['Movie Night', '753325070'], ['The Polar Express', '4130'],
    ['SpongeBob SquarePants: Battle for Bikini Bottom - Rehydrated', '513020'], ['MUSIC ROOM', '965935360'],
    ['Series Makers', '700055046'], ['Radio Station', '2128929587'], ['Karaoke Party', '488782'],
    ['The TV Show', '498153'],
    # Space
    ["Marvel's Guardians of the Galaxy", '1540116959'], ['Star Trek Online', '19858'], ['Juno: New Origins', '510271'],
    ['FTL: Faster Than Light', '33882'], ['Star Trek Fleet Command', '510530'], ['Star Citizen', '71375'],
    ['elite: dangerous', '80607'], ['kerbal space program', '32742'], ['Starsector', '33416'],
    ['Occupy Mars: The Game', '510193'],
    # Platformer
    ['Astlibra Revision', '595232525'], ['Super Mario Bros.: The Lost Levels', '852456640'], ['Timespinner', '461206'],
    ['ENDER LILIES: Quietus of the Knights', '519579'], ['The Darkest Tales', '519580'], ['Chenso Club', '22065949'],
    ['Touhou Project', '448375'], ['The Knight Witch', '156296054'], ['New Super Mario Bros. U Deluxe', '366613364'],
    ['Legends of IdleOn', '1935520090'], ['Shovel Knight Dig', '514089'], ['Persona 4 Arena Ultimax', '313464'],
    ['Super Mario Bros. 3', '9455'], ['Shovel Knight', '138583'], ['Skul: The Hero Slayer', '515386'],
    ['Warhammer 40,000: Shootas, Blood %26 Teef', '1720712325'], ['Super Mario Bros.', '509508'],
    # Platformer - Bad: Fighting - Hack and slash____good: Exploration - Non-linear - Skill jumps
    ['Grand Chase Classic', '1233312672'], ['MapleStory', '19976'], ['Neon Abyss', '512017'],
    # Platformer - Bad: Fighting____good: Exploration - Non-linear - Skill jumps
    ['F.I.S.T.: Forged In Shadow Torch', '511666'], ['Ori and the Blind Forest', '460619'], ['Dead Cells', '495961'],
    ['Ori and the Will of the Wisps', '497412'], ['Hollow Knight', '490147'],
    # Platformer - Bad: Fighting____good: Non-linear - Skill jumps
    ['Axiom Verge 2', '515458'],
    # Platformer - Bad: Fighting Linear____good: Skill jumps
    ['Vengeful Guardian: Moonrider', '337396402'], ['Pizza Tower', '1774510513'],
    # Platformer - Arena multiplayer brawl pick up weapon
    ['Nickelodeon All-Star Brawl', '1140748845'], ['Stick Fight: The Game', '499379'], ['Divine Knockout', '330358169'],
    ['SpiderHeck', '1722376710'], ['MultiVersus', '950189725'], ['Rivals of Aether', '488436'], ['Runbow', '488444'],
    ['super smash bros. ultimate', '504461'], ['Super Smash Bros.', '17516'], ['Super Smash Bros. Brawl', '18833'],
    ['super smash bros. melee', '16282'], ['SMASH LEGENDS', '519080'], ['brawlhalla', '460316'],
    ['Multiverse', '206089050'], ['Crash Bash', '14625'], ['Fraymakers', '1731003802'],
    # Platformer - 1v1 flat fighter
    ['BlazBlue: Cross Tag Battle', '497877'], ['Marvel vs. Capcom 2: New Age of Heroes', '2400'], ['Dino Rex', '27887'],
    ['Ultra Kaiju Monster Rancher', '591032671'], ['Granblue Fantasy: Versus', '510799'], ['Rushdown Revolt', '519171'],
    ['Street Fighter III: 3rd Strike', '1476'], ['Ultra Street Fighter IV', '313164'], ['Street Fighter 6', '55453844'],
    ['mortal kombat 11', '510578'], ['Mortal Kombat XL', '2072543734'], ['Guilty Gear XX Accent Core Plus R', '491467'],
    ['Skullgirls', '30639'], ['Killer Instinct', '16951'], ['JoJo’s Bizarre Adventure: All-Star Battle R', '704979750'],
    ["The King of Fighters '98", '9747'], ['Lethal League Blaze', '505619'], ['Melty Blood: Type Lumina', '936945829'],
    ['Tekken 8', '538054672'], ['The Rumble Fish 2', '29480'], ["JoJo's Bizarre Adventure: All Star Battle", '66275'],
    ['Breakers Collection', '716786005'], ["My Hero One's Justice 2", '514620'], ['Guilty Gear Xrd: Rev 2', '496464'],
    ['Punch Planet', '494352'], ['The King of Fighters XV', '513753'], ['Ultimate Marvel vs. Capcom 3', '1336067913'],
    ['DNF Duel', '108763890'], ['Injustice 2', '494995'], ['Elsword', '68018'], ['Ultimate Mortal Kombat 3', '1999'],
    ['Power Rangers: Battle for the Grid', '496203'], ['street fighter v', '488615'], ['Mortal Kombat X', '460521'],
    ['Streets of Rage 4', '509356'], ['m.u.g.e.n', '271231'], ['Virtua Fighter 5: Ultimate Showdown', '1802933584'],
    ['SoulCalibur VI', '500626'], ['Under Night In-Birth Exe:Late[cl-r]', '513751'], ['Dead or Alive 6', '506376'],
    ['Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles', '1414748474'], ["Them's Fightin' Herds", '494126'],
    ['guilty gear: strive', '517159'], ['Dead or Alive 6', '506376'], ['Skullgirls: 2nd Encore', '764537219'],
    ['tekken 7', '461067'], ['Tekken Tag Tournament 2', '29448'], ['Marvel vs. Capcom: Infinite', '494544'],
    ['BlazBlue: Central Fiction', '490500'], ['M.U.G.E.N', '39532650'],
    # Sports
    ['Nintendo Switch Sports', '2044170173'], ['Fitness%20%26%20Health', '509671'], ['Zwift', '490959'],
    ['sports', '518203'],
    # Sports - Golf
    ['pga tour 2k21', '517397'], ['Turbo Golf Racing', '1350267695'], ['PGA Tour 2K23', '468880140'],
    # Sports - Soccer
    ['efootball pes 2021 season update', '1520501777'], ['eFootball 2023', '2071983320'], ['Soccer Story', '478775568'],
    ['football manager 2021', '1271244884'], ['eFootball 2022', '1061323687'], ['Football Manager 2023', '1047410718'],
    ['football manager 2022', '586622463'], ['mario strikers: battle league', '1769394593'], ['Italia 1990', '14824'],
    ['fifa 19', '506103'], ['Freestyle Football R', '1566992650'], ['World Soccer Cup 2022', '1777886928'],
    ['Anstoss 3', '498350675'], ['Fantasy Sports', '1573920501'], ['fifa 22', '1869092879'],
    ['Pro Soccer Online', '1286420756'],
    # Sports - Soccer - Fifa
    ['fifa 23', '1745202732'], ['FIFA Online 4', '504798'], ['fifa 18', '495589'], ['fifa 17', '493091'],
    ['fifa 16', '489608'], ['fifa 21', '518204'], ['fifa 20', '512804'],
    # Sports - Basketball
    ['nba 2k21', '518023'], ['slam dunk', '517301'], ['nba 2k22', '1371363232'], ['NBA Live 19', '506406'],
    ['NBA 2K23', '772421245'], ['Out of the Park Baseball 23', '123403711'], ['3on3 Freestyle', '494769'],
    # Sports - American Football
    ['madden nfl 21', '517406'], ['madden nfl 22', '966064811'], ['Madden NFL 23', '862021340'],
    ['NCAA Football 14', '271198'], ['Blood Bowl 2', '490177'], ['NFL Football', '1028492867'],
    # Sports - Baseball
    ['MLB 9 Innings 22', '2038575831'], ['MLB The Show 22', '1820819463'], ['mlb the show 21', '1160459167'],
    ['Captain Tsubasa II: Super Striker', '579601296'], ['eBaseball Powerful Pro Yakyuu 2022', '405215881'],
    ['Super Mega Baseball 3', '516728'],
    # Sports - Fishing
    ['Russian Fishing 4', '497304'], ['Fishing Planet', '491117'], ['Ultimate Fishing Simulator 2', '1825784314'],
    ['Ultimate Fishing Simulator', '500518'], ['Call of the Wild: The Angler', '487237675'],
    # Sports - Wrestling
    ['ea sports ufc 4', '518711'], ['wwe 2k19', '508289'], ['wwe 2k20', '513681'], ['Wrestling Empire', '638072230'],
    ['UFC', '866175498'], ['EA Sports UFC 2', '491220'], ['WWE', '9421829'], ['Fire Pro Wrestling World', '496098'],
    ['WWE SuperCard', '461427'], ['WWE Champions', '491560'], ['wwe 2k22', '1199725270'],
    # Sports - Boxing
    ['Fight Night Champion', '28924'], ['Boxing', '1173'], ['Boxing Fight', '369432'], ['Boxing Star', '510965'],
    ['Undisputed', '1244970157'],
    # Sports - Hockey
    ['nhl 21', '519329'], ['NHL 22', '13932618'], ['NHL 23', '731327454'],
    # Sports - Cricket
    ['cricket 19', '512623'], ['Cricket 22', '875869495'],
    # Vehicles - Build vehicle then fight with it
    ['Guns of Icarus Alliance', '490981'], ['My Summer Car', '493125'], ['Microsoft Flight Simulator', '7193'],
    ['Ace Combat 7: Skies Unknown', '492605'], ['Cosmoteer: Starship Architect %26 Commander', '497906'],
    ['The Long Drive', '514661'], ['Motorsport Manager', '490393'],
    # Vehicles - Racing
    ['f1 2020', '517174'], ['f1 2021', '752590871'], ['iracing', '19554'], ['Assetto Corsa Competizione', '1348809580'],
    ['BeamNG.drive', '491878'], ['DiRT Rally 2.0', '509698'], ['GRID Legends', '1402483528'], ['The Crew 2', '497118'],
    ['Automobilista 2', '516921'], ['Wreckfest', '370472'], ['Forza Horizon 4', '506413'], ['Assetto Corsa', '313197'],
    ['F1 22', '1705795372'], ['RaceRoom Racing Experience', '723544889'], ['Crash Team Racing Nitro-Fueled', '510579'],
    ['Forza Horizon 5', '1757732267'], ['Stuntfest Worldtour', '1582771097'], ['NASCAR Racing 2003 Season', '5368'],
    ['Asphalt 9: Legends', '1960201900'], ['WRC Generations', '1982326230'], ['Dakar Desert Rally', '1980128527'],
    ['CarX Drift Racing Online', '498289'], ['Diddy Kong Racing', '14660'], ['Hot Lap League', '1962997464'],
    ['NASCAR Heat 5', '517409'], ['Hot Wheels Unleashed', '1716516651'], ['Forza Motorsport 7', '497411'],
    ['F1 Manager 2022', '489490035'], ['Trail Out', '175665548'],
    # Vehicles - Racing - Fake cars
    ['KartRider: Drift', '515160'], ['You Suck at Parking', '519604'], ['World of Outlaws: Dirt Racing', '1336887325'],
    ['Mario Kart 64', '9250'], ['Trackmania', '687129551'], ['Circuit Superstars', '513012'], ['Kartrider', '491334'],
    ['Sonic Robo Blast 2 Kart', '1652216715'], ['Garfield Kart: Furious Racing', '513640'],
    # Vehicles - Racing - Need for speed
    ['Need for Speed Heat', '512782'], ['Need for Speed: Underground 2', '8855'], ['Need For Speed: Payback', '492547'],
    ['Need for Speed: Underground', '11258'], ['Need for Speed: Most Wanted', '495711'], ['Need for Speed', '489611'],
    ['Need for Speed Unbound', '928412879'], ['Need for Speed: Hot Pursuit - Remastered', '522224787'],
    ['Need for Speed: Carbon', '8110'],
    # Speedrun - Metroidvania
    ['Rayman Legends', '26315408'], ['Crash Bandicoot: Warped', '11854'], ['MediEvil', '332934265'], ['Jak II', '9531'],
    ['Ratchet %26 Clank: Up Your Arsenal', '4540'], ['Crash Bandicoot: The Wrath of Cortex', '69'], ['Rayman', '16933'],
    ['Crash Bandicoot 2: Cortex Strikes Back', '1461160776'], ['Metroid Prime', '14198'], ['Cutthroat Island', '14464'],
    ['Jak and Daxter: The Precursor Legacy', '13420'], ['Shadow the Hedgehog', '17794'], ['Super Kiwi 64', '148897831'],
    ["Donkey Kong Country 2: Diddy's Kong Quest", '15483'], ['Super Metroid', '7595'], ['Star Fox Adventures', '17424'],
    ['Crash Bandicoot', '2092563353'], ['Castlevania', '6108'], ['Final Fantasy IV', '19023'], ['Psychonauts', '2673'],
    ["Donkey Kong Country 3: Dixie Kong's Double Trouble!", '4162'], ['Ghost Song', '313363'], ['EarthBound', '30367'],
    ['Digimon World', '3564'], ["Conker's Bad Fur Day", '9664'], ['Dragon Quest', '14951'], ['Banjo-Kazooie', '10033'],
    ['Sly 2: Band of Thieves', '556097834'], ['Ratchet %26 Clank: Going Commando', '4230'], ['SpeedRunners', '370345'],
    ['Banjo-Tooie', '2634'], ["Luigi's Mansion", '10090'], ['Psychonauts 2', '499111'], ['Metroid Dread', '212029556'],
    ['Ratchet %26 Clank', '16791'], ['Final Fantasy XII: The Zodiac Age', '493926'], ['Final Fantasy VI', '858043689'],
    ["Crash Bandicoot 4: It's About Time", '518222'], ['Super Meat Boy', '22720'], ['Sly 2: Band of Thieves', '14286'],
    ["Kirby's Dream Land", '18104'], ['Sly Cooper and the Thievius Raccoonus', '14081'], ['Amok Runner', '815501255'],
    ['metroid prime 2: echoes', '1459'], ['Moonscars', '1850336454'], ['Hot Lava', '498346'], ['The Grinch', '7212'],
    ['Freedom Planet 2', '495022'], ['Klonoa: Door to Phantomile', '8753'], ['Final Fantasy: Mystic Quest', '3331'],
    ['Final Fantasy: Mystic Quest', '3331'], ['Castlevania: Symphony of the Night', '13050'], ['Koudelka', '4784'],
    ['Ratchet %26 Clank: Rift Apart', '518016'], ['Donkey Kong Country', '165338793'], ['Donkey Kong 64', '13765'],
    ['Kirby and the Forgotten Land', '496321134'], ['Control', '506462'], ['Castlevania: Aria of Sorrow', '11065'],
    ['Dragon Quest VIII: Journey of the Cursed King', '590233873'], ['Ratchet %26 Clank: Going Commando', '4230'],
    ['Scooby-Doo! Night of 100 Frights', '13868'], ['Pokémon Puzzle League', '7382'], ['Metroid Fusion', '9479'],
    ['Dragon Warrior', '1565834559'], ['Lufia II: Rise of the Sinistrals', '5262'], ['The Messenger', '4185'],
    ['ToeJam %26 Earl', '12206'], ["Castlevania II: Simon's Quest", '10854'], ['Golden Sun', '252'],
    ['Ratchet %26 Clank: Going Commando', '4230'],
    # Speedrun - Timed - Stressful - Chased - Finish level before the thing gets you
    ['Catherine', '29143'],
    # Speedrun - Spyro
    ['Spyro the Dragon: Reignited Trilogy', '1885901697'], ['Spyro: Year of the Dragon Reignited', '1916268396'],
    ['Spyro the Dragon', '7182'], ["Spyro 2: Ripto's Rage!", '1434'], ['Spyro: Year of the Dragon', '1598'],
    ["Spyro 2: Ripto's Rage! Reignited", '725811421'],
    # Speedrun - Zelda
    ['The Legend of Zelda: A Link to the Past', '899559811'], ['The Legend of Zelda: Ocarina of Time 3D', '28613'],
    ['The Legend of Zelda: A Link to the Past', '9435'], ['The Legend of Zelda: The Wind Waker HD', '368205'],
    ['The Legend of Zelda: Ocarina of Time', '11557'], ["The Legend of Zelda: Link's Awakening", '3337'],
    ['The Legend of Zelda: The Wind Waker', '16967'], ['The Legend of Zelda: Spirit Tracks', '23195'],
    ["The Legend of Zelda: Majora's Mask", '12482'], ['Zelda II: The Adventure of Link', '14890'],
    ['The Legend of Zelda: Skyward Sword', '24324'], ['The Legend of Zelda', '10979'],
    ['The Legend of Zelda: The Minish Cap', '5635'],
    # Speedrun - Mario
    ['Paper Mario: The Thousand-Year Door', '6855'], ['Mario Golf: Toadstool Tour', '1458'], ['Paper Mario', '18231'],
    ['Super Mario RPG: Legend of the Seven Stars', '6737'], ['Mario Golf', '18042'], ['Super Mario Sunshine', '6086'],
    ['Super Mario Maker', '490608'], ['Paper Mario: The Origami King', '517534'], ['Super Mario Maker 2', '511399'],
    ["Super Mario World 2: Yoshi's Island", '2635'], ['Super Mario Galaxy 2', '24239'], ['Super Mario 64', '2692'],
    ['Mario %26 Luigi: Superstar Saga', '8543'], ['Super Mario Galaxy', '14766'], ['Super Mario World', '1229'],
    ['Super Paper Mario', '11705'],
    # Speedrun - Sonic
    ['Sonic Adventure', '7195'], ['Sonic Heroes', '8734'], ['Sonic Mania', '493877'], ['Sonic the Hedgehog 3', '4240'],
    ['Sonic Generations', '31284'], ['Sonic Frontiers', '1732431919'], ["Sonic Adventure DX: Director's Cut", '12078'],
    ['Sonic Adventure 2: Battle', '6263'], ['Sonic the Hedgehog', '2271'], ['Christmas NiGHTS into Dreams', '7453'],
    ['Sonic Adventure 2', '17464'], ['Sonic Origins', '914065119'], ['Sonic Unleashed', '1601389319'],
    # Speedrun - Mega Man
    ['Mega Man Maker', '1267688912'], ['Mega Man 2', '12870'], ['Mega Man', '4815'], ['Mega Man X2', '18114'],
    ['Mega Man X Dive', '516791'], ['Mega Man X', '8676'], ['Mega Man 3', '4133'], ['Mega Man 11', '500560'],
    # Battle Royale
    ['super people', '19620578'], ['warzone', '25416'], ['Stumble Guys', '1312214340'], ['Mad Adventures', '482429167'],
    ['Realm Royale', '505845'], ['Rush Royale', '633454324'], ['Rumbleverse', '161880494'], ['HypeSquad', '867013405'],
    ['pubg: battlegrounds', '493057'], ["playerunknown's battlegrounds", '493057'], ['Super Animal Royale', '509529'],
    ['fortnite', '33214'], ['fall guys', '512980'], ['Garena Free Fire', '502732'], ['Naraka: Bladepoint', '515474'],
    ['Z1: Battle Royale', '417892'], ['CRSED: F.O.A.D.', '506491'], ['Super Bomberman R Online', '1884783031'],
    ['Deathverse: Let It Die', '1425397746'], ['Bombergrounds: Reborn', '513364'], ['Crab Game', '673760473'],
    ['Rubber Bandits', '892799604'], ['Spellbreak', '509614'], ['My Hero Ultra Rumble', '451007760'],
    ['Zombs Royale', '505939'],
    # Old
    ['Ape Escape', '12270'],  ['Retro', '27284'],
    # War
    ['war thunder', '66366'], ['world of tanks', '27546'], ['world of warships', '32502'], ['Foxhole', '493388'],
    ['World of Tanks Console', '499551'], ['World of tanks: Blitz', '140035'], ['Heroes %26 Generals', '32895'],
    ['Post Scriptum', '497441'], ['World War 3', '505956'], ['Destroyer: The U-Boat Hunter', '1103439091'],
    ['Steel Division 2', '511940'], ['World of Warships: Legends', '512226'], ['Regiments', '946617000'],
    ['Battalion 1944', '491704'], ['BATTLETECH', '490757'], ['Middle-earth: Shadow of War', '496000'],
    ['crossout', '492113'],
    # Minigames with or without chat
    ['Kukoro: Stream Chat Games', '518764'], ['Words On Stream', '512821'], ['Jackbox Party Packs', '493174'],
    ['Kahoot!', '1127100998'], ['Wordle', '879648744'], ['What The Dub?!', '752874500'],
    ['The Jackbox Party Pack 9', '1219652274'], ['Viewergames Racing', '42004081'],
    # Anime fighter
    ['Dragon Ball Z: Kakarot', '511195'], ['Naruto to Boruto: Shinobi Striker', '496503'], ['Jump Force', '506411'],
    ['Naruto Shippuden: Ultimate Ninja Storm 4', '488635'], ['One Piece: Pirate Warriors 4', '513366'],
    ['Dragon Ball: The Breakers', '1657670363'], ['Dragon Ball: Xenoverse 2', '492731'],
    ['DRAGON BALL Z DOKKAN BATTLE', '489405'], ['dragon ball fighterz', '497385'],
    # Competitive - Moving groups of units towards eachother
    ['Age of Empires III', '7830'], ['Age of Empires IV', '498482'], ['S4 League', '21563'], ['StarCraft II', '490422'],
    ['overwatch', '488552'], ['Total War: Warhammer II', '497434'], ['Age of Empires', '9623'], ['StarCraft', '11989'],
    ['Warcraft III', '12924'], ['valorant', '516575'], ['Age of Empires II', '13389'], ['Total War: Rome II', '66246'],
    ['EVE Online', '13263'], ['Warhammer 40,000: Dawn of War II', '19329'], ['StarCraft: Remastered', '1664649323'],
    ['The Lord of the Rings: The Battle for Middle-earth II', '4449'], ['Total War: Warhammer III', '1913410799'],
    ['Warhammer Online: Age of Reckoning', '18888'], ['Fault: Elder Orb', '514152'],
    # Competitive - Non violent
    ['Splatoon 3', '1158884259'], ['Splatoon', '460649'], ['Rawmen', '510638'], ['Omega Strikers', '1600495710'],
    ['Super Buckyball Tournament', '514169'], ['Phantom Abyss', '1812167143'], ['Roller Champions', '512991'],
    ['Splatoon 2', '495064'], ['Knockout City', '1924769596'], ['Expedition Agartha', '1853203196'],
    ['Puyo Puyo Tetris 2', '519358'], ['Pac-Man 99', '1079150006'], ['Rocket League', '30921'],
    # Competitive - Deck builders
    ['Gods Unchained', '508716'], ['Skyweaver', '512913'], ['Warsaken', '1808969818'], ['Magic: The Gathering', '2748'],
    ['Across the Obelisk', '807746316'], ['Cardfight!! Vanguard', '1170471980'], ['Yu-Gi-Oh! Cross Duel', '1376558717'],
    ['Yu-Gi-Oh! TRADING CARD GAME', '497248'], ['Yu-Gi-Oh! Duel Links', '494508'], ['Vault of the Void', '1691435108'],
    ['Yu-Gi-Oh! Forbidden Memories', '207'], ['Yu-Gi-Oh! Master Duel', '1119642287'], ['Eternal Card Game', '491403'],
    ['Hellfire Tactics', '4536672'], ['Voice of Cards: The Beasts of Burden', '28655792'], ['Shadowverse', '492925'],
    ["Evony: The King's Return", '1129869117'], ['Duelyst', '459741'], ['Ascension: Deckbuilding Game', '535155317'],
    ['Digimon Digital Card Battle', '11088'], ['Legends of Runeterra', '514790'], ['Storybook Brawl', '1210837377'],
    ['Gwent: The Witcher Card Game', '493217'], ['Hearthstone', '138585'],
    ['Cardfight!! Vanguard: Dear Days', '1859470728'],
    # Competitive - Weird - Board games etc.
    ['Bloons TD Battles 2', '1740011318'], ['Go', '65360'], ['Mahjong Soul', '512708'], ['8 Ball Pool', '491851'],
    ['Chess.com', '2106453313'], ['Clubhouse Games: 51 Worldwide Classics', '516867'], ['Darts', '1331855755'],
    ['Chess', '743'], ['Riichi City', '84504405'], ['Scrabble', '3014'],
    # Turn based combat
    ['The Legend of Dragoon', '12101'], ['Chrono Cross', '3963'], ['Jack Move', '517965'], ['Sunday Gold', '725193289'],
    ['Danganronpa V3: Killing Harmony', '489164'], ['Deltarune', '965771331'], ['Digimon Story Cyber Sleuth', '458900'],
    ['West of Loathing', '495932'], ['Digimon Survive', '508776'], ['Symphony of War: The Nephilim Saga', '1781853522'],
    ['Chrono Trigger', '8489'], ['Blue Archive', '95998382'], ['Slice %26 Dice', '1519193002'], ['Xenogears', '16782'],
    ['Costume Quest 2', '459731'], ['Xenoblade Chronicles: Definitive Edition', '514245'], ['Pokémon Stadium', '6657'],
    ['Shadows Over Loathing', '1812391707'], ['Arcane Waters', '662884141'], ['Star Wars: Galaxy of Heroes', '496853'],
    ['Infinite Magicraid', '1283475051'], ['Pokémon Showdown', '850490686'], ['Fear %26 Hunger: Termina', '514595515'],
    ['Dragon Quest XI S: Echoes of an Elusive Age - Definitive Edition', '486102336'], ['Pokémon Colosseum', '11879'],
    ['Xenoblade Chronicles 3', '1584758405'], ['Tales of Arise', '512957'], ['Super Lesbian Animal RPG', '519336'],
    ['Pokémon Colosseum', '11879'], ['Monster Rancher 2 DX', '2025163961'], ['One Piece: Odyssey', '1842715404'],
    ['Monster Sanctuary', '505788'], ['Xenoblade Chronicles 2', '495061'], ['One Piece Odyssey', '1842715404'],
    ['The Outbound Ghost', '2183385'], ['Shin Megami Tensei V', '499825'], ['Circus Electrique', '455953031'],
    ['Pokémon Stadium', '1918702860'], ['Bravely Default II', '515469'], ['Dungeon Fighter Online', '25367'],
    ['Monochrome Mobius: Rights and Wrongs Forgotten', '1373542404'], ['Backpack hero', '1023917542'],
    ['Octopath Traveler', '495062'], ['Soul Hackers 2', '18070083'], ['Valkyrie Profile', '10651'],
    ['Shin Megami Tensei III: Nocturne - HD Remaster', '673382043'], ['Costume Quest', '29091'],
    ['Toontown Online', '1281'], ['Chained Echoes', '519302'],
    # Turn based combat - Moving one unit up to a max distance then tell it what actions to perform
    ['Pokémon Mystery Dungeon: Gates to Infinity', '107539'], ['Valkyria Chronicles', '19153'], ['Demeo', '2100353806'],
    ['Battle Brothers', '490771'], ['The DioField Chronicle', '249366108'], ['Front Mission 1st: Remake', '938305608'],
    ['Wasteland 3', '494710'], ['Tactics Ogre: Reborn', '2066834255'], ['Warhammer 40,000 Rogue Trader', '1173887206'],
    ['Warhammer 40,000: Gladius - Relics of War', '501157'], ['Duelyst II', '15674700'], ['Phoenix Point', '491909'],
    ["King Arthur: Knight's Tale", '417145015'], ['XCOM: Enemy Unknown', '33331'], ['Triangle Strategy', '96418879'],
    ['Warhammer 40,000: Chaos Gate - Daemonhunters', '2047407036'], ['Wartales', '749092120'], ['XCOM 2', '489767'],
    ['La Pucelle: Ragnarok', '2071568212'], ['The Last Spell', '513769'], ['Lost Eidolons', '459138204'],
    ['Wildermyth', '511724'], ['Moonbreaker', '1155636003'], ["Tortuga: A Pirate's Tale", '1375570613'],
    ['Stolen Realm', '124407790'],
    # Turn based combat - Moving max distance tell actions - Fire Emblem
    ['Fire Emblem Warriors: Three Hopes', '183330426'], ['Fire Emblem: The Sacred Stones', '1055'],
    ['Fire Emblem: Path of Radiance', '210'], ['Fire Emblem: The Blazing Blade', '1396'],
    ['Fire Emblem: Three Houses', '495202'], ['Fire Emblem: Radiant Dawn', '13299'],
    ['Fire Emblem Engage', '1242184979'],
    # Turn based combat - Competitive multiplayer RTS conquering territory - War simulation - Glorified RISK
    ['Halo Wars', '18758'], ['Old World', '517077'], ['Star Wars: Empire at War', '4222'], ['Mahokenshi', '1354494872'],
    ['For The King', '494903'], ['Crusader Kings III', '514888'], ['Master of Magic', '6006'], ['HUMANKIND', '514071'],
    ['Command & Conquer: Red Alert', '235'], ['Knights of Honor II – Sovereign', '514133'], ['8-Bit Hordes', '494856'],
    ['Command & Conquer 3: Tiberium Wars', '16106'], ['Crossfire: Legion', '759550556'], ['Victoria 3', '1768423951'],
    ['Command & Conquer: Red Alert 2', '16580'], ['Hearts of Iron IV', '459327'], ['Europa Universalis IV', '67584'],
    ['Age of Mythology', '1260'], ["Sid Meier's Civilization VI", '492553'], ["Sid Meier's Civilization V", '27103'],
    ['Dune: Spice Wars', '1482819933'], ['Age of Mythology: Extended Edition', '421115841'], ['Armello', '68063'],
    ['Heroes of Might and Magic III: The Restoration of Erathia', '12839'], ['Terra Invicta', '349626339'],
    ['Command %26 Conquer: Remastered', '1095419511'],
    # Turn based combat - Playing cards to do abilities
    ['Beneath Oresa', '1106691740'], ['Fresh Start', '1445819052'], ['Yi Xian: The Cultivation Card Game', '757121053'],
    ['Alina of the Arena', '1523832419'], ['Rungore: Beginner Experience', '1819169686'], ['Slay the Spire', '496902'],
    ["Marvel's Midnight Suns", '735602708'], ['Library Of Ruina', '517515'], ['Monster Train', '516096'],
    # Turn based combat - The Legend of Heroes
    ['The Legend of Heroes: Trails of Cold Steel III', '499560'], ['The Legend of Heroes: Trails from Zero', '31809'],
    ['The Legend of Heroes: Kuro no Kiseki II - Crimson Sin', '1454243467'],
    ['The Legend of Heroes: Trails of Cold Steel II', '459341'],
    ['The Legend of Heroes: Trails of Cold Steel', '94084'],
    # Turn based combat - Final Fantasy
    ['Final Fantasy', '7689'], ['Final Fantasy II', '1918'], ['Dissidia Final Fantasy Opera Omnia', '503561'],
    ['Final Fantasy XI Online', '10229'], ['Final Fantasy V', '1692274562'], ['Final Fantasy IX', '8090'],
    ['Final Fantasy III', '19549'], ['Final Fantasy III', '1302233663'],
    # Turn based combat - Kingdom Hearts
    ['Kingdom Hearts Birth by Sleep Final Mix', '496475877'], ['Kingdom Hearts Birth by Sleep Final Mix', '1853454333'],
    ['Kingdom Hearts II', '4375'], ['Kingdom Hearts', '10081'], ['Kingdom Hearts II Final Mix', '116910466'],
    ['Kingdom Hearts HD 1.5 %2B 2.5 ReMIX', '494099'], ['Kingdom Hearts Dark Road', '516085'],
    ['Kingdom Hearts Final Mix', '597712627'],
    # Games for 2
    ['Gartic Phone', '278888515'], ['It Takes Two', '518213'], ['Tabletop RPGs', '509664'], ['Pummel Party', '509549'],
    ['We Were Here Forever', '428452832'], ['Codenames', '508509'], ['Keep Talking and Nobody Explodes', '461492'],
    ['A Way Out', '497388'], ['We Were Here', '495723'], ['We Were Here Too', '502825'], ['Moving Out', '511656'],
    ['We Need to Go Deeper', '494020'], ['We Were Here Together', '509862'], ['Operation: Tango', '1582767179'],
    ['BattleBlock Theater', '25087'], ['We Need to Go Deeper', '494020'], ['The Past Within', '1933145458'],
    ['PHOGS!', '508529'],
    # Games for groups - Party games
    ['Monopoly Plus', '493159'], ['PlateUp!', '1115711128'], ['Gloomhaven', '509009'], ['The Game of Life 2', '492879'],
    ['Dungeons%20%26%20Dragons', '509577'], ['Music Quiz', '24786'], ['Mafia LIVE!', '22761'], ['Ravenfall', '519528'],
    ['Trivia', '569869366'], ['Gartic On Stream', '1414617745'], ['Mario Party 2', '11176'], ['Mario Party 7', '6874'],
    ['RISK: The Game of Global Domination', '520083701'], ['First Class Trouble', '515486'], ['Mario Party 6', '7673'],
    ['Overcooked! 2', '506458'], ['UNO', '11103'], ['Pathfinder', '508513'], ['Masks Of Deception', '519297364'],
    ['Mario Party', '5887'], ['Ultimate Chicken Horse', '490438'], ['DND', '14846'], ['Starfinder', '508514'],
    ['RiffTrax: The Game', '1892955924'], ['Overcooked! All You Can Eat', '518847'], ['skribbl.io', '496983'],
    ['Scribble It!', '513789'], ['Cards Against Insanity', '339403363'], ['Whatsamusic', '1019674856'],
    ['Mario Party 5', '3130'],
    # Systems - Mobile general
    ['Goddess of Victory: Nikke', '512033'], ['Epic Seven', '510056'], ["Girls' Frontline: Neural Cloud", '1891690553'],
    ['Final Fantasy Tactics', '18181'], ['Dungeon %26 Fighter Mobile', '1013109068'], ['langrisser mobile', '509986'],
    ['Granblue Fantasy', '489668'], ['Azur Lane', '498434'], ['Ring of Pain', '516806'], ['Clash of Clans', '73914'],
    ['Rise of Kingdoms', '511882'], ['The Lord of the Rings: Rise to War', '602368913'], ['Counter: Side', '516690'],
    ['Cookie Run: Kingdom', '103252334'], ['Fire Emblem Heroes', '492354'], ['Punishing: Gray Raven', '516564'],
    ['Dislyte', '436453013'], ['Last Day on Earth: Survival', '497697'], ['Ni no Kuni: Cross Worlds', '519394'],
    ['Neural Cloud', '165333975'], ['Rocket League Sideswipe', '1270322937'], ['Dragalia Lost', '505774'],
    ['Clash Royale', '491168'], ['NEW STATE MOBILE', '1737225095'], ['Saint Seiya: Awakening', '511850'],
    ['MIR4', '966704637'], ['Sky: Children of the Light', '513553'], ['Minion Masters', '494327'],
    ['Black Survival', '491170'], ['State of Survival', '516800'], ['Flash Party', '488336777'],
    ['Guardian Tales', '517357'], ['Memento Mori', '1446757577'], ['Brawl stars', '497497'],
    # Systems - Mobile - Manga/Anime/Comics
    ['Dragon Ball Legends', '504921'], ['One Piece: Treasure Cruise', '489169'], ['Bleach: Brave Souls', '492984'],
    ['Marvel Snap', '1743359147'], ['MARVEL Strike Force', '504651'], ['MARVEL Contest of Champions', '461221'],
    ['Fate%2FGrand Order', '493048'], ['Umamusume: Pretty Derby', '505084'], ['Eversoul', '455534054'],
    ['The Seven Deadly Sins: Grand Cross', '512887'], ['The Seven Deadly Sins: Grand Cross', '512887'],
    # Systems - Mobile - Turn based combat - Competitive
    ['Path to Nowhere', '460767488'], ['Raid: Shadow Legends', '508948'], ['Summoners War: Sky Arena', '489111'],
    ['Summoners War: Chronicles', '1885922279'], ['Princess Connect! Re:Dive', '503988'],
    # Systems - Mobile - Hide and seek
    ['Dead by Daylight Mobile', '517072'],
    # Systems - Mobile - MOBA
    ['Mobile Legends: Bang Bang', '494184'], ['AutoChess Moba', '1078929938'], ['Honor of Kings', '497301'],
    ['league of legends: wild rift', '514858'], ['Arena of Valor', '498302'],
    # Systems - Mobile - Shooter
    ['Call of Duty: Black Ops Zombies', '65801'], ['Apex Legends Mobile', '170987874'],
    # Systems - Mobile Shooter
    ['pubg mobile', '505884'], ['call of duty: mobile', '512818'],
    # Systems - Mobile Sports
    ['FIFA Mobile', '496320'], ['Madden NFL Mobile', '476388'],
    # Systems - Playstation 4
    ['Dreams', '490373'],
    # Systems - Playstation 5
    ["Astro's Playroom", '518022'],
    # Systems - Playsation Portable
    ['Persona 3 Portable', '25130'],
    # Systems - Nintendo Switch
    ['The Legend of Zelda: Twilight Princess', '17828'], ['Pokémon Shield', '1249600852'], ["Who's Who?", '792526757'],
    ["Kirby's Dream Buffet", '284482065'], ['Pokémon Scarlet', '670867987'], ["Pokémon: Let's Go, Pikachu!", '506237'],
    ['Pokémon Brilliant Diamond%2FShining Pearl', '1584745140'], ['Pokémon Unite', '518379'], ['Miitopia', '494160'],
    ['Super Mario Odyssey', '493997'], ["Luigi's Mansion 3", '509541'],  ['Animal Crossing: New Horizons', '509538'],
    ['New Pokémon Snap', '518188'], ['Hyrule Warriors: Age of Calamity', '519545'], ['Pokémon Violet', '173843625'],
    ['Super Mario Party', '506454'], ['Mario Party Superstars', '1068239917'], ['Pokémon Sword%2FShield', '497451'],
    ['The Legend of Zelda: Twilight Princess HD', '491327'], ['The Legend of Zelda: Breath of the Wild', '110758'],
    ["Pokémon: Let's Go, Eevee!", '2103556522'], ['Mario Kart 8', '369588'], ['Mario Kart 8 Deluxe', '941530474'],
    ["Super Mario 3D World %2B Bowser's Fury", '1446426412'], ['Mario %2B Rabbids Kingdom Battle', '497148'],
    ['The Legend of Zelda: Skyward Sword HD', '1829367372'], ['Pokémon Legends: Arceus', '561013832'],
    ['Mario Golf: Super Rush', '339386743'], ['Mario %2b Rabbids Sparks of Hope', '582372781'],
    ['Live A Live', '149991938'],
    # Systems - Nintendo WII
    ['Mario Kart Wii', '18871'], ['StepMania', '6415'], ['Wii Sports Resort', '19259'],
    ['Ring Fit Adventure', '514313'], ['New Super Mario Bros. Wii', '24238'],
    # Systems - Xbox
    ['Phantom Dust', '994344636'],
    # Systems - Other
    ['SOUND VOLTEX EXCEED GEAR', '1259504587']
]

# Here you put games that you own or really, really want to play
favoriteGames = [
    # Survival
    'Minecraft', 'Terraria', 'Vintage Story', 'Valheim', 'Icarus', 'Atlas', 'Ark', 'Creativerse', 'Forager',
    'Ark: Survival Evolved', 'Subsistence', 'Salt 2: Shores of Gold', 'Dwarf Fortress',
    # Survival - Wasteland
    'Rust',
    # Survival - Ocean
    'Raft',
    # Survival - Space
    'Astroneer', 'Starbound', 'Planet Crafter',
    # Survival - Zombies
    'Project Zomboid',
    # Puzzle
    'Portal 2',
    # City building
    'Cities: Skylines', 'SimCity', 'Farthest Frontier',
    # Management - Automation
    'Factorio', 'Hydroneer', 'Space Engineers', 'Mindustry', 'Satisfactory',
    # Management - Traffic
    'Snowrunner', 'Mini Motorways',
    # Management
    'RollerCoaster Tycoon 2', 'Timberborn', 'RimWorld',
    # Tile games
    'Dorfromantik', 'Unrailed!',
    # Roguelite that interacts with environment
    'Noita',
    # Management - Villagers
    'Stardew Valley', 'Dinkum', 'Animal Crossing: New Horizons', 'Kynseed',
    # Management - Simulation
    'The Sims 4', 'The Sims 3', 'The Sims 2', 'The Universim', 'Oxygen Not Included', 'PowerWash Simulator',
    'Game Dev Tycoon',
    # Strategy
    'Going medieval', 'Teamfight Tactics', 'Auto Chess', 'They Are Billions', 'Shell Shockers',
    # Weird
    'Reading Fun', 'Roblox', 'Duolingo', 'Viscera Cleanup Detail', 'Tetris 99', 'GeoGuessr', 'Tower Unite',
    'Blankos Block Party', "Viscera Cleanup Detail: Santa's Rampage",
    # Board games
    'Tabletop Simulator', 'Card Games', 'Board Games',
    # Special
    'Art', 'Makers & Crafting', 'Software and Game Development', 'Science & Technology', 'Roblox Studio',
    # Sports
    'Golf With Your Friends', "Tony Hawk's Pro Skater 1+2", 'Skater XL', 'Skate 3', 'Cursed to Golf', 'Golf Gang',
    # Simulation - Vehicles
    'American Truck Simulator', 'Euro Truck Simulator 2',
    # Community games
    'Marbles On Stream', 'Stream Raiders', 'Stream Racer', 'Stream Pirates', 'Cult of the Lamb',
    # Defence games
    'Soulstone Survivors',
    # Platformer - Skill jumps
    'Jump King', 'Pac-Man World Re-Pac', 'Rogue Legacy 2', 'Getting Over It with Bennett Foddy',
    # Moba
    'League of Legends', 'Heroes of the Storm', 'Dota 2',
    # RPG
    'Gothic', 'Gothic II', 'Old School RuneScape', 'TERA', 'Tibia', 'RuneScape', 'The Elder Scrolls Online', 'Dofus',
    'Trove', 'Grim Dawn', 'Neverwinter', 'Dungeons & Dragons Online', 'New World', 'Guild Wars 2', 'Frozen Flame',
    # RPG - 2D
    'Core Keeper',
    # JP/KR RPG
    'Aion', 'Lost Ark', 'Final Fantasy XIV Online', 'Genshin Impact', 'Metin2', 'Black Desert',
    # Mobile
    'Pokémon GO',
    # Historical RPG
    "Assassin's Creed Odyssey", "Assassin's Creed Origins", "Assassin's Creed IV Black Flag", "Assassin's Creed",
    "Assassin's Creed Valhalla", "Assassin's Creed Unity", "Assassin's Creed II", "Assassin's Creed Brotherhood",
    "Assassin's Creed Syndicate", "Assassin's Creed Revelations", "Assassin's Creed III Remastered",
    "Assassin's Creed III", 'Asterigos: Curse of the Stars',
    # Story
    'A Plague Tale: Innocence',
    # Turn based games nuzlocke! ironmon
    'Pokémon FireRed/LeafGreen', 'Pokémon Crystal', 'Crystalis', 'Pokémon HeartGold/SoulSilver',
    # Idle games
    'Idle Champions of the Forgotten Realms', 'Cookie Clicker', 'Idle skilling', 'Leaf Blower Resolution: Idle Game',
]

# Games that I could see myself playing


wishlisted = [
    # Survival
    'Conan Exiles', 'Barony', 'My Time at Sandrock', 'Eco', 'Breakwaters', 'The Warhorn', 'Cataclysm: Dark Days Ahead',
    'Medieval Dynasty', 'Dragon Quest Builders 2', 'Volcanoids', 'Rune Factory 5', 'Dredge', 'The Oregon Trail',
    'Made in Abyss: Binary Star Falling into Darkness', 'Craftopia', 'Alba: A Wildlife Adventure',
    'The Ascent', 'ARK: Survival Of The Fittest', 'Atrio: The Dark Wild', 'Wytchwood',
    # Survival - Wasteland
    'No One Survived',
    # Survival - Forest
    'The Forest', 'Green Hell', 'Grounded', "Len's Island", 'Ancestors: The Humankind Odyssey',
    # Survival - Space
    'Breathedge', 'Empyrion - Galactic Survival', 'Stars End',
    # Survival - Ocean
    'Subnautica', 'Raft', 'Stranded Deep', 'Subnautica: Below Zero', 'Sail Forth',
    # Survival - Zombies
    'Death Road to Canada', '7 Days to Die', 'Mist Survival', 'Night of the Dead',
    # Automotive
    'Scrap Mechanic', 'The Long Drive',
    # Puzzle
    "Baldi's Basics Classic Remastered", 'The Entropy Centre', 'Lonesome Village', 'A Little To The Left', 'I Am Fish',
    'Baba is You', 'Taiji', 'Garden Simulator', 'Peglin', 'Pikmin', 'Pikmin 2', 'FAR: Changing tides', 'Jigsaw Puzzle',
    'Peggle', 'Superliminal', 'Portal', 'Are You Smarter Than a 5th Grader?', 'Escape Simulator', 'Puzzles & Survival',
    'Dr. Mario', 'Untitled Goose Game', 'Submerged: Hidden Depths', 'The Last Guardian', 'The Last Campfire', 'KeyWe',
    'Chicory: A Colorful Tale', 'Sackboy: A Big Adventure', 'Limbo', 'Kill It With Fire', 'The Witness', 'Brewmaster',
    "Rubik's Cube", 'The Room', 'Tetris: The Grand Master', 'JellyCar Worlds', 'Wavetale', 'Tetris Effect: Connected',
    'Escape Memoirs: Mini Stories', 'Apsulov: End of Gods', 'Crosswords', 'Ghostbusters: The Video Game Remastered',
    'TETR.IO', 'Tetris', 'Pinball', 'Human: Fall Flat', 'Escape Academy', 'The Forgotten City', 'The Pedestrian',
    "LEGO Builder's Journey", 'The Room Two', 'The House of Da Vinci 3',
    # RPG - Story, item quality
    'Dragon Age: Inquisition', 'Outward', 'Flyff Universe', 'Vindictus', 'Space Station 13', 'Chimeraland', 'Dauntless',
    'SpongeBob SquarePants: Battle For Bikini Bottom', 'Chibi-Robo!', "Baldur's Gate II: Enhanced Edition", 'MU Online',
    'Medieval Dynasty', 'Divinity: Original Sin II', 'Kingdom Come: Deliverance', 'Dark Age of Camelot', 'CABAL Online',
    'Blacktail', 'Sports Story', "Baldur's Gate: Enhanced Edition", 'Pillars of Eternity II: Deadfire', 'Dragon Age II',
    'EverQuest II', 'City of Heroes', 'Kingdoms of Amalur: Re-Reckoning', 'Last Oasis', 'The Witcher: Enhanced Edition',
    'Tower of Fantasy', 'Immortals Fenyx Rising', 'Mabinogi', 'Biomutant', 'Guild Wars', "Baldur's Gate 3", 'Fable II',
    "Dragon's Dogma: Dark Arisen", 'Knight Online', 'Turnip Boy Commits Tax Evasion', 'Turnip Boy Commits Tax Evasion',
    'Shadow of the Colossus', 'Solasta: Crown of the Magister', 'Disco Elysium', 'Perfect World', 'EverCraft Online',
    'Bless Unleashed', 'Medivia Online', 'Embers Adrift', "Baldur's Gate: Dark Alliance II", 'Ashes of Creation',
    'Horizon Forbidden West', 'Ravenfall', 'Pathfinder: Wrath of the Righteous', 'Path of Titans', 'EverQuest',
    'Ultima Online', 'Fractured Online', 'Fable III', 'Fable Anniversary', 'Pathfinder: Kingmaker', 'Big Time',
    'Dragon Age: Origins',
    # RPG - MMO
    'R2 Online: Reign of Revolution', 'Silkroad Online', 'ROSE Online', 'V Rising', 'Wizard101',
    # RPG - Single player
    'The Witcher 3: Wild Hunt', 'The Witcher 2: Assassins of Kings', 'Kenshi', 'Horizon Zero Dawn', 'I Am Jesus Christ',
    'Cyberpunk 2077',
    # RPG - Japanese - JRPG -  Good
    'Phantasy Star Online Episode I + II', 'Re:Legend', 'Blue Protocol', 'Digimon Masters Online', 'Persona 5 Strikers',
    'Phantasy Star Online 2 New Genesis', 'Persona 4 Golden', 'Persona 5 Royal', 'Phantasy Star Online Episode I & II',
    'Tales of Zestiria', 'Little Witch Nobeta', 'Death Stranding: Director’s Cut', 'Persona 5', 'Tales of Symphonia',
    'Ghostwire: Tokyo', 'Phantasy Star Online 2', 'Honkai Impact 3rd', 'Dragon Quest Treasures', 'GhostWire: Tokyo',
    'Phantasy Star Online 2 New Genesis', 'Tales of Berseria', 'Ni no Kuni: Wrath of the White Witch Remastered',
    'Tales of Vesperia: Definitive Edition',
    # RPG - Japanese - Good - Square Enix
    'Forspoken', 'NieR Replicant ver.1.22474487139...', 'NieR: Automata', 'NEO: The World Ends with You',
    'Romancing SaGa: Minstrel Song Remastered',
    # RPG - Japanese - Good - Monster Hunter
    'Monster Hunter 4 Ultimate', 'Monster Hunter Stories 2: Wings of Ruin', 'Monster Hunter Frontier G',
    'Monster Hunter Rise', 'Monster Hunter Generations Ultimate', 'Monster Hunter: World',
    # RPG - Japanese - Good - Final Fantasy
    'Final Fantasy VIII Remastered', 'Final Fantasy VII: The First Soldier', 'Final Fantasy XIII-2', 'Final Fantasy X',
    'Final Fantasy IV: Oblivion', 'Final Fantasy X-2', 'Crisis Core: Final Fantasy VII - Reunion', 'Final Fantasy VII',
    'Final Fantasy X HD', 'Final Fantasy XV', 'Stranger of Paradise: Final Fantasy Origin', 'Final Fantasy VII Remake',
    'Final Fantasy X HD Remaster', 'Final Fantasy VIII', 'Final Fantasy XIII', 'Crisis Core: Final Fantasy VII',
    'Final Fantasy X-2 HD Remaster',
    # RPG - Japanese - JRPG - Average - Mostly about dialogue - No interesting combat - Can have good artwork
    '.hack//G.U. Vol. 1: Rebirth', 'Star Ocean: The Divine Force', 'Corpse Party', 'Valkyrie Elysium', 'Scarlet Nexus',
    'Samurai Maiden', 'Neptunia: Sisters vs. Sisters',
    # RPG - Korean
    'Blade & Soul', 'MIR4', 'Lineage 2', 'ArcheAge: Unchained', 'ArcheAge', 'Ragnarok Online',
    # RPG - The Elder Scrolls
    'The Elder Scrolls V: Skyrim - Special Edition', 'The Elder Scrolls V: Skyrim Special Edition',
    'The Elder Scrolls II: Daggerfall', 'The Elder Scrolls III: Morrowind', 'The Elder Scrolls V: Skyrim',
    'The Elder Scrolls IV: Oblivion',
    # RPG - Lowpoly - Cartoonish
    "Swords 'n Magic and Stuff", 'Muck', 'Tunic', 'Gedonia', 'Genfanad', 'Bugsnax', 'Lil Gator Game', 'Aka',
    # RPG - 2D
    'CrossCode', 'Stoneshard', 'Potion Permit', 'Growtopia', 'Eastward', 'Little Witch in the Woods',
    # RPG - Furry
    'Spirit of the North', 'Stray', 'Shelter 2', 'The Spirit and the Mouse', 'Star Stable', 'Calico',
    # RPG - Villagers
    'Wylde Flowers', 'Hokko Life', 'No Place Like Home', 'Coral Island', 'Sun Haven', 'Ooblets',
    'Story of Seasons: A Wonderful Life',
    # Turn based combat
    'Temtem', 'Omori', 'Super Auto Pets', 'Into the Breach', 'Inscryption', 'Coromon',
    # Turn based combat - Pokémon DS and older or fan-based
    'Pokémon Mystery Dungeon: Explorers of Sky', 'Pokémon Omega Ruby/Alpha Sapphire', 'Pokémon Ultra Sun/Ultra Moon',
    'Pokémon Red/Blue', 'Pokémon X/Y', 'Pokémon Ruby/Sapphire', 'Pokémon Black/White Version 2', 'Pokémon Yellow',
    'Pokémon XD: Gale of Darkness', 'Pokémon Platinum', 'Pokémon Emerald', 'Pokémon MMO 3D', 'Pokémon Insurgence',
    'Pokémon Black/White', 'Pokémon Red', 'Pokémon Uranium', 'Pokémon White', 'Pokémon Infinite Fusion',
    'Pokémon Planet',
    # Comic universes
    'Harry Potter and the Chamber of Secrets', "Harry Potter and the Sorcerer's Stone", 'LEGO Harry Potter: Years 1-4',
    'Batman: Return to Arkham - Arkham City', 'Batman: Return to Arkham - Arkham Asylum', 'Batman: Arkham Asylum',
    'Batman: Arkham City', 'The Lord of the Rings Online', 'Gotham Knights', "Marvel's Spider-Man: Miles Morales",
    'Shin-chan: Me and the Professor on Summer Vacation - The Endless Seven-Day Journey', "Marvel's Spider-Man",
    "Teenage Mutant Ninja Turtles: Shredder's Revenge", "Marvel's Avengers", "Marvel's Spider-Man Remastered",
    'Batman: Arkham Origins', 'Batman: The Telltale Series', 'DC Universe Online', 'Batman: Arkham Knight',
    'Hogwarts Legacy',
    # Comic universes - Star Wars
    'LEGO Star Wars: The Complete Saga', 'Star Wars: Knights of the Old Republic', 'LEGO Star Wars: The Skywalker Saga',
    'Star Wars: The Old Republic', 'Star Wars: Knights of the Old Republic II - The Sith Lords',
    'Star Wars Galaxies: An Empire Divided',
    # Simulation
    'Heavenly Bodies', 'Little Inferno', 'Bratz: Flaunt Your Fashion', 'Surgeon Simulator 2', 'PC Building Simulator',
    'Drug Dealer Simulator', 'Cozy Grove', 'Police Simulator: Patrol Officers', 'SuchArt: Genius Artist Simulator',
    'PC Building Simulator 2', 'Late Night Mop', 'Little Inferno', 'Thief Simulator',
    # Simulation - Vehicles
    'X-Plane 12', 'Train Sim World 3', 'Car Mechanic Simulator 2021', 'Train Sim World 2', 'Transport Fever 2',
    'Train Simulator Classic', 'X-Plane 11', 'Railroads Online!', 'SimRail 2021: The Railway Simulator',
    # Simulation - Consume objects
    'Katamari Damacy REROLL', 'Destroy All Humans! 2', 'Donut County', 'Destroy All Humans! 2: Reprobed',
    'Destroy All Humans!', 'Fireworks Mania', 'Katamari Damacy Reroll',
    # Simulation - Animals
    'Beasts of Bermuda', 'Hamster Playground', 'Placid Plastic Duck Simulator', 'The Isle', 'Goat Simulator 3',
    # Simulation - Hospitality - Single building - shopkeep
    'Cafe Owner Simulator', 'Tavern Master', 'Bear & Breakfast', 'Papers, Please', 'Dave the Diver', 'Potion Craft',
    'One-Armed Cook', 'Cooking Simulator', 'Food Truck Simulator', 'Barista Simulator', 'Gas Station Simulator',
    'Strange Horticulture', 'My Time at Portia', 'Potionomics', 'APICO', 'Arcade Paradise',
    'Definitely Not Fried Chicken',
    # Simulation - Building
    "Landlord's Super", 'Construction Simulator',  'Lawn Mowing Simulator', 'House Flipper', 'Electrician Simulator',
    'WW2 Rebuilder',
    # Platformer - No combat - Not so sure about these
    'A Hat in Time', 'Ōkami HD', 'Ōkami', 'Blasphemous', 'Islets', 'Night in the Woods', 'Pico Park', 'Ghostrunner',
    'PICO PARK', 'Curse Crackers: For Whom the Belle Toils', 'Rain World',
    'Worms W.M.D', 'INSIDE', 'ALTF4', 'Weed Shop 3',
    # Platformer - puzzles
    'Pumpkin Jack', 'Little Nightmares', 'Little Nightmares II', 'Somerville',
    # Platformer - Skill jumps only - No combat
    'Geometry Dash', 'I Wanna Be The Guy', 'Pogostuck: Rage With Your Friends', 'The Professional', 'Celeste', 'GRIS',
    'Cuphead', 'Geometry Dash', 'Last Command', 'Super Bunny Man',
    # Management - General
    'Kingdom Two Crowns', 'Railgrade', 'Travellers Rest', 'Lobotomy Corporation', 'Hundred Days', 'Choo-Choo Charles',
    'Stellaris', 'Frostpunk', 'Wobbledogs', 'Hardspace: Shipbreaker', 'Barotrauma', 'Stormworks: Build and Rescue',
    'Two Point Hospital', 'Going Medieval', 'Captain of industry', 'Teardown', 'Captain of Industry', 'Unpacking',
    # Management - Caretaker - farm etc.
    'Harvestella', 'Ranch Simulator', 'Slime Rancher 2', 'Graveyard Keeper', 'Slime Rancher', 'Farming Simulator 19',
    'Farming Simulator 22',
    # Management - Colony survival
    'Stranded: Alien Dawn', 'The Wandering Village', 'Sapiens', 'Northgard', 'Stardeus', 'Spore', 'Against the Storm',
    'The Eternal Cylinder', 'Land of the Vikings', 'Anno 1800', 'Catizens', 'Floodland', 'Zombie Cure Lab', 'Aquatico',
    'Surviving the Abyss', 'Farlanders', 'SteamWorld Build',
    # Management - Theme park/animals/prison/hospital/cult
    'Jurassic World Evolution 2', 'Planet Coaster', 'My Free Zoo', 'Planet Zoo', 'Jurassic World Evolution',
    "Let's Build a Zoo", 'The Escapists 2', 'Two Point Campus', 'Prison Architect', 'Parkitect',
    'Honey, I Joined a Cult',
    # Management - City builder
    'Kingdoms Reborn', 'Manor Lords', 'Workers & Resources: Soviet Republic',
    # Tile games
    'orx', 'Orx', 'Colonist', '100% Orange Juice', 'Railbound', 'Garden Galaxy',
    # Automation
    'Shapez', 'Astro Colony', 'Autonauts', 'Stationeers', 'Ixion', 'Dyson Sphere Program',
    # Dialogue - Voice acting - Choices with multiple endings
    'AI: The Somnium Files', 'Zero Escape: Nine Hours, Nine Persons, Nine Doors', 'Life is Strange: Before the Storm',
    'Vampyr', 'Life is Strange: True Colors', 'Life is Strange', "Deadly Premonition: Director's Cut", 'Tell Me Why',
    'Beyond: Two Souls', 'Danganronpa: Trigger Happy Havoc', 'Life is Strange 2', 'The Wolf Among Us', 'Immortality',
    'Brok the Investigator', 'I Was a Teenage Exocolonist', 'Danganronpa 2: Goodbye Despair', 'Once Upon a Jester',
    'Neon White', 'Ai: The Sodium Files', 'AI: The Somnium Files - Nirvana Initiative', 'We Are OFK', 'Pentiment',
    'Detroit: Become Human', 'Undertale', 'The Stanley Parable: Ultra Deluxe', 'Sucker for Love: First Date',
    'Life is Strange Remastered', "Project: Eden's Garden", 'Bug Fables: The Everlasting Sapling',
    '13 Sentinels: Aegis Rim', 'Citizen Sleeper', 'Needy Streamer Overload',
    # Dialogue - Dating sim
    'Dream Daddy: A Dad Dating Simulator',
    # Dialogue - Detective
    'Frog Detective 2: The Case of the Invisible Wizard', 'L.A. Noire', 'Return of the Obra Dinn',
    # Point and click - Side scroller
    'The Secret of Monkey Island: Special Edition', 'Ib', "The Excavation of Hob's Barrow", 'The Great Ace Attorney',
    'Phoenix Wright: Ace Attorney − Trials and Tribulations', 'Fran Bow', 'The Artful Escape', 'Little Misfortune',
    'Unusual Findings', 'Frog Detective 3: Corruption at Cowboy County', 'Burnhouse Lane', 'Children of Silentown',
    'Mysterium', 'TOEM', 'Little Orpheus', 'Return to Monkey Island', 'Witchy Life Story', "The Witch's House MV",
    'Broken Age', 'The Great Ace Attorney Chronicles', 'Phoenix Wright: Ace Attorney', 'Beacon Pines', 'Oxenfree',
    'Phoenix Wright: Ace Attorney - Trials and Tribulations', 'The Case of the Golden Idol', 'Sally Face',
    'Phoenix Wright: Ace Attorney Trilogy', 'A Space for the Unbound',
    # Oneshot adventures - short linear games that let you roleplay a bit
    'OneShot: World Machine Edition', 'OneShot', 'Twelve Minutes',
    # Competitive
    'Legion TD 2', 'The Machines Arena', 'Eternal Return', 'Supreme Commander: Forged Alliance', 'Wormate.io', 'TagPro',
    'Kingshunt',
    # Moba
    'Century: Age of Ashes', 'Heroes of Newerth', 'Fangs', 'smite', 'Paragon: The Overprime', 'Paragon', 'Smite',
    'Predecessor',
    # Weird
    "Who's Your Daddy", 'Writers', 'Education',
    # Creative
    'Warhammer', 'The Sandbox', 'LEGO Bricktales',
    # Music - Rythm
    'osu!', 'Hatsune Miku: Project DIVA Mega Mix+', "FRIDAY NIGHT FUNKIN'", 'Clone Hero', 'Muse Dash', 'Melatonin',
    'Rocksmith 2014 Edition - Remastered', 'Hatsune Miku: Colorful Stage!', 'Hatsune Miku: Project DIVA Mega Mix',
    'Crypt of the NecroDancer', 'Trombone Champ', 'DJMAX RESPECT V', "Friday Night Funkin'", 'DJMax Respect V',
    'Everhood', 'Hi-Fi Rush',
    # Vehicles
    'SnowRunner', 'Trials Rising', 'MX Bikes', 'Descenders',
    # Defence games
    'Plants vs. Zombies', 'Vampire Survivors', 'Bloons TD 6', 'Arknights', 'Isle of Arrows', 'Holocure: Save the Fans!',
    'Plants vs. Zombies: Garden Warfare 2', 'Rogue: Genesia', 'Orcs Must Die! 3', 'Dungeon Defenders: Awakened',
    'Dungeon Defenders II', 'Element TD 2', 'Gatewalkers', 'Epistory: Typing Chronicles',
    # Exploration
    "No Man's Sky", 'The Long Dark', 'Outer Wilds', 'Kena: Bridge of Spirits', 'Spiritfarer', 'Road 96', 'Trifox',
    'Mount & Blade II: Bannerlord', 'Mount & Blade: Warband', 'Sable', 'trailmakers', 'X4: Foundations', 'A Short Hike',
    # Sports
    'Golf It!', 'Riders Republic', 'Session: Skate Sim',
    # Story - Cool elements like parkour - little to no fighting - Puzzle elements
    "Mirror's Edge Catalyst", 'Firewatch', "Hellblade: Senua's Sacrifice", 'The Sinking City', '20 Minutes Till Dawn',
    'Lost in Random', 'Quantum Break', 'We Happy Few', 'Alice: Madness Returns', 'Tinykin', 'Restless Soul', 'Journey',
    'A Plague Tale: Requiem', "Mirror's Edge", 'inFAMOUS: Second Son',
    # Roguelite that interact with environment or where you have a static place to come back to that you can upgrade
    "Don't Starve Together", 'Nuclear Throne', 'Minecraft Dungeons', 'Tower Princess', 'Moonlighter',
    'Tribes of Midgard', 'Ember Knights', "Death's Door", "Don't Starve"
    # Idle games
    'Stacklands',
]
