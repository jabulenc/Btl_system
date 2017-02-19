label storage:
    # List of Status' (As of 5/12 I'm seriously going to cry omfg I LOST SO MUCH DATA):
    # Steady Stats: Heal | Brn | Psn | Frz | Prlz | Con | Slp | ConstHeal | AttAndHeal
    # Self Stats: PsnDD | SpdUp_Self | DefUp_Self | AtkUp_Self | CritUp | EvaUp_Self | 
    # Move-Specific Stats: SCKO (Sheer Cold KO) | DefCurl | Rollout | HelpHand | Superpower |
    #                   Roar | Autotomize | HSlam | MetBurst |  ChipAway | Thrash | HealWish |
    #                   Payback | EQ | CritPrevention | CalmMind | Imprison | FSight | DEater |
    #                   SPower | FuryCut | BreakProtect | 1HP | 
    # Special Stats: Recoil | Flinch | TwoTurn | Recharge | Flee | Protect |
    # Opponent Stats: SpdD_Opp | SpecDD_Opp | DefD_Opp | AtkD_Opp | AccD_Opp | 
    # Weakening Stats: FireType_Down 
    # Weather Effects: Raining | Sandstorm | Misty
    
    # Skill = [ Skill Name, Power, Status, Type ]
    $ SolarBeam = ["Solar Beam", 24, "None", "Grass"]
    $ SleepPowder = ["Sleep Powder", 0, "Slp", "Grass"]
    $ Venoshock = ["Venoshock", 12, "PsnDD", "Poison"]
    $ BlastBurn = ["Blast Burn", 30, "None", "Fire"]
    $ DragonClaw = ["Dragon Claw", 15, "None", "Dragon"]
    $ Roost = ["Roost", 30, "Heal", "Flying"]
    $ Hydrocannon = ["Hydrocannon", 30, "None", "Water"]
    $ FocusBlast = ["Focus Blast", 24, "None", "Fighting"]
    $ Recover = ["Recover", 78, "Heal", "Normal"]
    $ ShadowBall = ["Shadow Ball", 16, "None", "Ghost"]
    $ AuraSphere = ["Aura Sphere", 18, "None", "Fighting"]
    $ Thunder = ["Thunder", 30, "Prlz", "Electric"]
    $ Agility = ["Agility", 0, "SpdUp_Self", "Psychic"]
    $ Slam = ["Slam", 20, "None", "Normal"]
    $ WildCharge = ["Wild Charge", 25, "Recoil", "Electric"]
    $ SheerCold = ["Sheer Cold", 0, "SCKO", "Ice"] #Formula for accuracy: [(Level of user - level of target) + 30] %
    $ ZenHeadbutt = ["Zen Headbutt", 25, "Flinch", "Psychic"] 
    $ IceBeam = ["Ice Beam", 28, "Frz", "Ice"]
    $ Crunch = ["Crunch", 24, "SpecDD_Opp", "Dark"]
    $ BodySlam = ["Body Slam", 25, "Prlz", "Normal"]
    $ Thunderbolt = ["Thunder Bolt", 25, "Prlz", "Electric"]
    $ Ember = ["Ember", 20, "None", "Fire"]
    
    #Marill family skills
    $ Tackle = ["Tackle", 25, "None", "Normal"]
    $ Bubble = ["Bubble", 20, "SpdD_Opp", "Water"]
    $ WaterGun = ["Water Gun", 20, "None", "Water"]
    $ TailWhip = ["Tail Whip", 0, "DefD_Opp", "Normal"]
    $ WaterSport = ["Water Sport", 0, "FireType_Down", "Water"]
    $ DefenseCurl = ["Defense Curl", 0, "DefCurl", "Normal"]
    $ Rollout = ["Rollout", 15, "Rollout", "Rock"]
    $ Bubblebeam = ["Bubble Beam", 10, "SpdD_Opp", "Water"]
    $ HelpingHand = ["Helping Hand", 0, "HelpHand", "Normal"]
    $ AquaTail = ["Aqua Tail", 45, "None", "Water"]
    $ PlayRough = ["Play Rough", 45, "AtkD_Opp", "Fairy"]
    $ RainDance = ["Rain Dance", 0, "Raining", "Water"]
    $ Superpower = ["Superpower", 60, "Superpower", "Fight"]
    $ DoubleEdge = ["Double Edge", 60, "Recoil", "Normal"]
    $ HydroPump = ["Hydropump", 55, "None", "Water"]
    $ Splash = ["Splash", 0, "None", "Normal"]
    $ Charm = ["Charm", 0, "AtkD_Opp", "Fairy"]
    $ Slam = ["Slam", 40, "None", "Normal"]
    $ Bounce = ["Bounce", 43, "TwoTurn", "Flying"]
    $ AquaRing = ["Aqua Ring", 0, "ConstHeal", "Water"]
    
    #Aron family skills
    $ Harden = ["Harden", 0, "DefUp_Self", "Normal"]
    $ MudSlap = ["Mud-Slap", 10, "AccD_Opp", "Ground"]
    $ Headbutt = ["Headbutt", 35, "Flinch", "Normal"]
    $ MetalClaw = ["Metal Claw", 25, "AtkUp_Self", "Steel"]
    $ RockTomb = ["Rock Tomb", 30, "SpdD_Opp", "Rock"]
    $ Protect = ["Protect", 0, "Protect", "Normal"]
    $ Roar = ["Roar", 0, "Roar", "Normal"]
    $ IronHead = ["Iron Head", 0, "Flinch", "Steel"]
    $ RockSlide = ["Rock Slide", 37, "Flinch", "Rock"]
    $ TakeDown = ["Take Down", 45, "Recoil", "Normal"]
    $ MetalSound = ["Metal Sound", 0, "SpecDD_Opp", "Steel"]
    $ IronTail = ["Iron Tail", 50, "DefD_Opp", "Steel"]
    $ IronDefense = ["Iron Defense", 0, "DefUp_Self", "Steel"]
    $ Autotomize = ["Autotomize", 0, "Autotomize", "Steel"]
    $ HeavySlam = ["Heavy Slam", 0, "HSlam", "Steel"]
    $ MetalBurst = ["Metal Burst", 0, "MetBurst", "Steel"]
    
    #Larvitar family skills
    $ Bite = ["Bite", 30, "Flinch", "Normal"]
    $ Leer = ["Leer", 0, "DefD_Opp", "Normal"]
    $ Sandstorm = ["Sandstorm", 0, "Sandstorm", "Rock"]
    $ Screech = ["Screech", 0, "DefD_Opp", "Normal"]
    $ ChipAway = ["Chip Away", 35, "ChipAway", "Normal"]
    $ ScaryFace = ["ScaryFace", 0, "SpdD_Opp", "Normal"]
    $ Thrash = ["Thrash", 60, "Thrash", "Normal"]
    $ DarkPulse = ["Dark Pulse", 40, "Flinch", "Dark"]
    $ Payback = ["Payback", 25, "Payback", "Dark"]
    $ Crunch = ["Crunch", 40, "DefD_Opp", "Dark"]
    $ Earthquake = ["Earthquake", 50, "EQ", "Ground"]
    $ StoneEdge = ["Stone Edge", 40, "CritUp", "Rock"]
    $ HyperBeam = ["Hyper Beam", 75, "Recharge", "Normal"]
    $ GigaImpact = ["Giga Impact", 75, "Recharge", "Normal"]
    $ ThunderFang = ["Thunder Fang", 33, "Prlz", "Electric"]
    $ IceFang = ["Ice Fang", 33, "Frz", "Ice"]
    $ FireFang = ["Fire Fang", 33, "Brn", "Fire"]
    
    #Ralts family skills
    $ Growl = ["Growl", 0, "AtkD_Opp", "Normal"]
    $ Confusion = ["Confusion", 25, "Con", "Psychic"]
    $ DoubleTeam = ["Double Team", 0, "EvaUp_Self", "Normal"]
    $ Teleport = ["Teleport", 0, "Flee", "Psychic"]
    $ DisarmingVoice = ["Disarming Voice", 20, "None", "Fairy"]
    $ LuckyChant = ["Lucky Chant", 0, "CritPrevention", "Normal"]
    $ MagicalLeaf = ["Magical Leaf", 30, "None", "Grass"]
    $ HealPulse = ["Heal Pulse", 50, "Heal", "Psychic"] #actually percentage based
    $ DrainingKiss = ["Draining Kiss", 25, "AttAndHeal", "Fairy"]
    $ CalmMind = ["Calm Mind", 0, "CalmMind", "Psychic"]
    $ Psychic = ["Psychic", 45, "SpecDD_Opp", "Psychic"]
    $ Imprison = ["Imprison", 0, "Imprison", "Psychic"]
    $ FutureSight = ["Future Sight", 60, "FSight", "Psychic"]
    $ Hypnosis = ["Hypnosis", 0, "Slp", "Psychic"]
    $ DreamEater = ["Dream Eater", 50, "DEater", "Psychic"]
    $ StoredPower = ["Stored Power", 10, "SPower", "Psychic"]
    $ MoonBlast = ["Moon Blast", 43, "SpecDD_Opp", "Fairy"]
    $ MistyTerrain = ["Misty Terrain", 0, "Misty", "Fairy"]
    $ HealingWish = ["Healing Wish", 0, "HealWish", "Psychic"]
    $ Wish = ["Wish", 50, "Heal", "Normal"]
    $ Captivate = ["Captivate", 0, "SpecDD_Opp", "Normal"]
    $ CloseCombat = ["Close Combat", 60, "DefD_Opp", "Fighting"]
    $ LeafBlade = ["Leaf Blade", 45, "CritUp", "Grass"]
    $ NightSlash = ["Night Slash", 35, "CritUp", "Dark"]
    $ Leer = ["Leer", 0, "DefD_Opp", "Normal"]
    $ QuickGuard = ["Quick Guard", 0, "Protect", "Fighting"]
    $ FuryCutter = ["Fury Cutter", 20, "FuryCut", "Bug"]
    $ Slash = ["Slash", 35, "CritUp", "Normal"]
    $ WideGuard = ["Wide Guard", 0, "Protect", "Rock"]
    $ SwordsDance = ["Swords Dance", 0, "AtkUp_Self", "Normal"]
    $ PsychoCut = ["Psycho Cut", 35, "CritUp", "Psychic"]
    $ Feint = ["Feint", 15, "BreakProtect", "Normal"]
    $ FalseSwipe = ["False Swipe", 20, "1HP", "Normal"]
    
    
     
    # Pokemon Skill Sets
    $ VenaSkill = [SolarBeam, GigaImpact, SleepPowder, Venoshock]
    $ CharZSkill = [BlastBurn, DragonClaw, Roost, HyperBeam]
    $ BlastSkill = [Hydrocannon, FocusBlast, IronDefense, DarkPulse]
    $ Mew2Skill = [Psychic, Recover, ShadowBall, AuraSphere]
    $ PikaSkill = [Thunder, Agility, Slam, WildCharge]
    $ LapSkill = [HydroPump, SheerCold, ZenHeadbutt, IceBeam]
    $ SnorSkill = [GigaImpact, Crunch, BodySlam, Thunderbolt]
    
    #(1/22) {Lines 38 - 93}
    #Used Python's Dictionary (http://www.tutorialspoint.com/python/python_dictionary.htm) as reference
    #Still need to implement typing
    $ Vena = {'Name' : "Venasaur", 
        'T1' : "Grass", 'T2' : "Poison", 
        'Skill_1' : VenaSkill[0][0], 'Skill_1_dmg' : VenaSkill[0][1], 'S1_Status' : VenaSkill[0][2], 'Skill_1_T' : VenaSkill[0][3], 
        'Skill_2' : VenaSkill[1][0], 'Skill_2_dmg' : VenaSkill[1][1], 'S2_Status' : VenaSkill[1][2], 'Skill_2_T' : VenaSkill[1][3], 
        'Skill_3' : VenaSkill[2][0], 'Skill_3_dmg' : VenaSkill[2][1], 'S3_Status' : VenaSkill[2][2], 'Skill_3_T' : VenaSkill[2][3], 
        'Skill_4' : VenaSkill[3][0], 'Skill_4_dmg' : VenaSkill[3][1], 'S4_Status' : VenaSkill[3][2], 'Skill_4_T' : VenaSkill[3][3], 
        'Attack' : 30, 
        'Defense' : 40, 
        'Speed' : 3, 
        'MaxHP' : 122, 'CurrHP' : 122, 'Image' : "venasaur.png"};
    
    $ CharZ = {'Name' : "Charizard", 
        'T1' : "Fire", 'T2' : "Flying", 
        'Skill_1' : CharZSkill[0][0], 'Skill_1_dmg' : CharZSkill[0][1], 'S1_Status' : CharZSkill[0][2], 'Skill_1_T' : CharZSkill[0][3], 
        'Skill_2' : CharZSkill[1][0], 'Skill_2_dmg' : CharZSkill[1][1], 'S2_Status' : CharZSkill[1][2], 'Skill_2_T' : CharZSkill[1][3], 
        'Skill_3' : CharZSkill[2][0], 'Skill_3_dmg' : CharZSkill[2][1], 'S3_Status' : CharZSkill[2][2], 'Skill_3_T' : CharZSkill[2][3], 
        'Skill_4' : CharZSkill[3][0], 'Skill_4_dmg' : CharZSkill[3][1], 'S4_Status' : CharZSkill[3][2], 'Skill_4_T' : CharZSkill[3][3], 
        'Attack' : 40, 
        'Defense' : 30, 
        'Speed' : 4, 
        'MaxHP' : 112, 'CurrHP' : 112, 'Image': "charizard.png"};
    
    $ Blast = {'Name' : "Blastoise", 
        'T1' : "Water", 'T2' : "NULL", 
        'Skill_1' : BlastSkill[0][0], 'Skill_1_dmg' : BlastSkill[0][1], 'S1_Status' : BlastSkill[0][2], 'Skill_1_T' : BlastSkill[0][3], 
        'Skill_2' : BlastSkill[1][0], 'Skill_2_dmg' : BlastSkill[1][1], 'S2_Status' : BlastSkill[1][2], 'Skill_2_T' : BlastSkill[1][3], 
        'Skill_3' : BlastSkill[2][0], 'Skill_3_dmg' : BlastSkill[2][1], 'S3_Status' : BlastSkill[2][2], 'Skill_3_T' : BlastSkill[2][3], 
        'Skill_4' : BlastSkill[3][0], 'Skill_4_dmg' : BlastSkill[3][1], 'S4_Status' : BlastSkill[3][2], 'Skill_4_T' : BlastSkill[3][3], 
        'Attack' : 35, 
        'Defense' : 45, 
        'Speed' : 2, 
        'MaxHP' : 118, 'CurrHP' : 118, 'Image' : "blastoise.png"};
    
    $ Mew2 = {'Name' : "Mewtwo", 
        'T1' : "Psychic", 'T2' : "NULL", 
        'Skill_1' : Mew2Skill[0][0], 'Skill_1_dmg' : Mew2Skill[0][1], 'S1_Status' : Mew2Skill[0][2], 'Skill_1_T' : Mew2Skill[0][3], 
        'Skill_2' : Mew2Skill[1][0], 'Skill_2_dmg' : Mew2Skill[1][1], 'S2_Status' : Mew2Skill[1][2], 'Skill_2_T' : Mew2Skill[1][3], 
        'Skill_3' : Mew2Skill[2][0], 'Skill_3_dmg' : Mew2Skill[2][1], 'S3_Status' : Mew2Skill[2][2], 'Skill_3_T' : Mew2Skill[2][3], 
        'Skill_4' : Mew2Skill[3][0], 'Skill_4_dmg' : Mew2Skill[3][1], 'S4_Status' : Mew2Skill[3][2], 'Skill_4_T' : Mew2Skill[3][3],
        'Attack' : 40, 
        'Defense' : 40, 
        'Speed' : 3, 
        'MaxHP' : 156, 'CurrHP' : 156, 'Image' : "mewtwo.png"};

    $ Pika = {'Name' : "Pikachu", 
        'T1' : "Electric", 'T2' : "NULL", 
        'Skill_1' : PikaSkill[0][0], 'Skill_1_dmg' : PikaSkill[0][1], 'S1_Status' : PikaSkill[0][2], 'Skill_1_T' : PikaSkill[0][3], 
        'Skill_2' : PikaSkill[1][0], 'Skill_2_dmg' : PikaSkill[1][1], 'S2_Status' : PikaSkill[1][2], 'Skill_2_T' : PikaSkill[1][3], 
        'Skill_3' : PikaSkill[2][0], 'Skill_3_dmg' : PikaSkill[2][1], 'S3_Status' : PikaSkill[2][2], 'Skill_3_T' : PikaSkill[2][3], 
        'Skill_4' : PikaSkill[3][0], 'Skill_4_dmg' : PikaSkill[3][1], 'S4_Status' : PikaSkill[3][2], 'Skill_4_T' : PikaSkill[3][3],
        'Attack' : 45, 
        'Defense' : 35, 
        'Speed' : 5, 
        'MaxHP' : 100, 'CurrHP' : 100};

    $ Lap = {'Name' : "Lapras", 
        'T1' : "Water", 'T2' : "Ice", 
        'Skill_1' : LapSkill[0][0], 'Skill_1_dmg' : LapSkill[0][1], 'S1_Status' : LapSkill[0][2], 'Skill_1_T' : LapSkill[0][3], 
        'Skill_2' : LapSkill[1][0], 'Skill_2_dmg' : LapSkill[1][1], 'S2_Status' : LapSkill[1][2], 'Skill_2_T' : LapSkill[1][3], 
        'Skill_3' : LapSkill[2][0], 'Skill_3_dmg' : LapSkill[2][1], 'S3_Status' : LapSkill[2][2], 'Skill_3_T' : LapSkill[2][3], 
        'Skill_4' : LapSkill[3][0], 'Skill_4_dmg' : LapSkill[3][1], 'S4_Status' : LapSkill[3][2], 'Skill_4_T' : LapSkill[3][3],
        'Attack' : 35, 
        'Defense' : 30, 
        'Speed' : 3, 
        'MaxHP' : 145, 'CurrHP' : 145};

    $ Snor = {'Name' : "Snorlax", 
        'T1' : "Water", 'T2' : "Ice", 
        'Skill_1' : SnorSkill[0][0], 'Skill_1_dmg' : SnorSkill[0][1], 'S1_Status' : SnorSkill[0][2], 'Skill_1_T' : SnorSkill[0][3], 
        'Skill_2' : SnorSkill[1][0], 'Skill_2_dmg' : SnorSkill[1][1], 'S2_Status' : SnorSkill[1][2], 'Skill_2_T' : SnorSkill[1][3], 
        'Skill_3' : SnorSkill[2][0], 'Skill_3_dmg' : SnorSkill[2][1], 'S3_Status' : SnorSkill[2][2], 'Skill_3_T' : SnorSkill[2][3], 
        'Skill_4' : SnorSkill[3][0], 'Skill_4_dmg' : SnorSkill[3][1], 'S4_Status' : SnorSkill[3][2], 'Skill_4_T' : SnorSkill[3][3],
        'Attack' : 40, 
        'Defense' : 45, 
        'Speed' : 1, 
        'MaxHP' : 160, 'CurrHP' : 160};
    
    return

label typeSetup:
    $ p_DefWeak = []
    $ p_DefStrong = []
    $ p_DefNone = []
    $ p_DefVeryWeak = []
    $ p_DefVeryStrong = []
    
    if type1 == "Normal":
        $ p_DefWeak.append("Fighting")
        $ p_DefNone.append("Ghost")
    if type1 == "Fire":
        $ p_DefWeak.extend(("Water", "Ground", "Rock"))
        $ p_DefStrong.extend(("Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"))
    if type1 == "Water":
        $ p_DefWeak.extend(("Electric", "Grass"))
        $ p_DefStrong.extend(("Fire", "Water", "Ice", "Steel"))
    if type1 == "Electric":
        $ p_DefWeak.extend(("Ground"))
        $ p_DefStrong.extend(("Electric", "Flying", "Steel"))
    if type1 == "Grass":
        $ p_DefWeak.extend(("Fire", "Ice", "Poison", "Flying", "Bug"))
        $ p_DefStrong.extend(("Water", "Electric", "Grass", "Ground"))
    if type1 == "Ice":
        $ p_DefWeak.extend(("Fire", "Fighting", "Rock", "Steel"))
        $ p_DefStrong.extend(("Ice"))
    if type1 == "Fighting":
        $ p_DefWeak.extend(("Flying", "Psychic", "Fairy"))
        $ p_DefStrong.extend(("Bug", "Rock", "Dark"))
    if type1 == "Poison":
        $ p_DefWeak.extend(("Ground", "Psychic"))
        $ p_DefStrong.extend(("Grass", "Fighting", "Poison", "Bug", "Fairy"))
    if type1 == "Ground":
        $ p_DefWeak.extend(("Water", "Grass", "Ice"))
        $ p_DefStrong.extend(("Poison", "Rock"))
        $ p_DefNone.extend(("Electric"))
    if type1 == "Flying":
        $ p_DefWeak.extend(("Electric", "Ice", "Rock"))
        $ p_DefStrong.extend(("Grass", "Fighting", "Bug"))
        $ p_DefNone.extend(("Ground"))
    if type1 == "Psychic":
        $ p_DefWeak.extend(("Bug", "Ghost", "Dark"))
        $ p_DefStrong.extend(("Fighting", "Psychic"))
    if type1 == "Bug":
        $ p_DefWeak.extend(("Fire", "Flying", "Rock"))
        $ p_DefStrong.extend(("Grass", "Fighting", "Ground"))
    if type1 == "Rock":
        $ p_DefWeak.extend(("Water", "Grass", "Fighting", "Ground", "Steel"))
        $ p_DefStrong.extend(("Normal", "Fire", "Poison", "Flying"))
    if type1 == "Ghost":
        $ p_DefWeak.extend(("Ghost", "Dark"))
        $ p_DefStrong.extend(("Poison", "Bug"))
        $ p_DefNone.extend(("Normal", "Fighting"))
    if type1 == "Dragon":
        $ p_DefWeak.extend(("Ice", "Dragon", "Fairy"))
        $ p_DefStrong.extend(("Fire", "Water", "Electric", "Grass"))
    if type1 == "Dark":
        $ p_DefWeak.extend(("Fighting", "Bug", "Fairy"))
        $ p_DefStrong.extend(("Ghost", "Dark"))
        $ p_DefNone.extend(("Psychic"))
    if type1 == "Steel":
        $ p_DefWeak.extend(("Fire", "Fighting", "Ground"))
        $ p_DefStrong.extend(("Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"))
    if type1 == "Fairy":
        $ p_DefWeak.extend(("Poison", "Steel"))
        $ p_DefStrong.extend(("Fighting", "Bug", "Dark"))
        $ p_DefNone.extend(("Dragon"))
        
    if type2 == "Normal":
        if p_DefWeak.count("Ghost") > 0:
            $ p_DefWeak.remove("Ghost")
            $ p_DefNone.extend(("Ghost"))
        if p_DefStrong.count("Fighting") > 0:
            $ p_DefWeak.remove("Fighting")
            
    if type2 == "Fire":
        #1/4 Weakness
        if p_DefStrong.count("Fire") > 0:
            $ p_DefStrong.remove("Fire")
            $ p_DefVeryStrong.extend(("Fire"))
        if p_DefStrong.count("Grass") > 0:
            $ p_DefStrong.remove("Grass")
            $ p_DefVeryStrong.extend(("Grass"))
        if p_DefStrong.count("Ice") > 0:
            $ p_DefStrong.remove("Ice")
            $ p_DefVeryStrong.extend(("Ice"))
        if p_DefStrong.count("Bug") > 0:
            $ p_DefStrong.remove("Bug")
            $ p_DefVeryStrong.extend(("Bug"))
        if p_DefStrong.count("Steel") > 0:
            $ p_DefStrong.remove("Steel")
            $ p_DefVeryStrong.extend(("Steel"))
        if p_DefStrong.count("Fairy") > 0:
            $ p_DefStrong.remove("Fairy")
            $ p_DefVeryStrong.extend(("Fairy"))
        
        #Quad Weakness
        if p_DefWeak.count("Water") > 0:
            $ p_DefWeak.remove("Water")
            $ p_DefVeryWeak.extend(("Water"))
        if p_DefWeak.count("Ground") > 0:
            $ p_DefWeak.remove("Ground")
            $ p_DefVeryWeak.extend(("Ground"))
        if p_DefWeak.count("Rock") > 0:
            $ p_DefWeak.remove("Rock")
            $ p_DefVeryWeak.extend(("Rock"))
        
        #Normal/ 1/2 damage/ double damage
        if p_DefWeak.count("Fire") > 0:
            $ p_DefWeak.remove("Fire")
        else:
            if p_DefVeryStrong.count("Fire") = 0:
                $ p_DefStrong.extend(("Fire"))
                
        if p_DefWeak.count("Grass") > 0:
            $ p_DefWeak.remove("Grass")
        else:
            if p_DefVeryStrong.count("Grass") = 0:
                $ p_DefStrong.extend(("Grass"))
                
        if p_DefWeak.count("Ice") > 0:
            $ p_DefWeak.remove("Ice")
        else:
            if p_DefVeryStrong.count("Ice") = 0:
                $ p_DefStrong.extend(("Ice"))
    
        if p_DefWeak.count("Bug") > 0:
            $ p_DefWeak.remove("Bug")
        else:
            if p_DefVeryStrong.count("Bug") = 0:
                $ p_DefStrong.extend(("Bug"))
                
        if p_DefWeak.count("Steel") > 0:
            $ p_DefWeak.remove("Steel")
        else:
            if p_DefVeryStrong.count("Steel") = 0:
                $ p_DefStrong.extend(("Steel"))
                
        if p_DefWeak.count("Fairy") > 0:
            $ p_DefWeak.remove("Fairy")
        else:
            if p_DefVeryStrong.count("Fairy") = 0:
                $ p_DefStrong.extend(("Fairy"))
                
        if p_DefStrong.count("Water") > 0:
            $ p_DefStrong.remove("Water")
        else:
            if p_DefVeryWeak.count("Water") = 0:
                $ p_DefWeak.extend(("Water"))
                
        if p_DefStrong.count("Ground") > 0:
            $ p_DefStrong.remove("Ground")
        else:
            if p_DefVeryStrong.count("Ground") = 0:
                $ p_DefWeak.extend(("Ground"))
                
        if p_DefStrong.count("Rock") > 0:
            $ p_DefStrong.remove("Rock")
        else:
            if p_DefVeryStrong.count("Rock") = 0:
                $ p_DefWeak.extend(("Rock"))
        
    if type2 == "Water":
        #1/4 Weakness
        if p_DefStrong.count("Fire") > 0:
            $ p_DefStrong.remove("Fire")
            $ p_DefVeryStrong.extend(("Fire"))
        if p_DefStrong.count("Water") > 0:
            $ p_DefStrong.remove("Water")
            $ p_DefVeryStrong.extend(("Water"))
        if p_DefStrong.count("Ice") > 0:
            $ p_DefStrong.remove("Ice")
            $ p_DefVeryStrong.extend(("Ice"))
        if p_DefStrong.count("Steel") > 0:
            $ p_DefStrong.remove("Steel")
            $ p_DefVeryStrong.extend(("Steel"))
        
        #Quad Weakness
        if p_DefWeak.count("Electric") > 0:
            $ p_DefWeak.remove("Electric")
            $ p_DefVeryWeak.extend(("Electric"))
        if p_DefWeak.count("Grass") > 0:
            $ p_DefWeak.remove("Grass")
            $ p_DefVeryWeak.extend(("Grass"))
        
        #Normal/ 1/2 damage/ double damage
        if p_DefWeak.count("Fire") > 0:
            $ p_DefWeak.remove("Fire")
        else:
            if p_DefVeryStrong.count("Fire") = 0:
                $ p_DefStrong.extend(("Fire"))
                
        if p_DefWeak.count("Water") > 0:
            $ p_DefWeak.remove("Water")
        else:
            if p_DefVeryStrong.count("Water") = 0:
                $ p_DefStrong.extend(("Water"))
                
        if p_DefWeak.count("Ice") > 0:
            $ p_DefWeak.remove("Ice")
        else:
            if p_DefVeryStrong.count("Ice") = 0:
                $ p_DefStrong.extend(("Ice"))
                
        if p_DefWeak.remove("Steel") > 0:
            $ p_DefWeak.remove("Steel")
        else:
            if p_DefVeryStrong.count("Steel") = 0:
                $ p_DefStrong.extends(("Steel"))
                
        if p_DefStrong.count("Electric") > 0:
            $ p_DefStrong.remove("Electric")
        else:
            if p_DefVeryWeak.count("Electric") = 0:
                $ p_DefWeak.extend(("Electric"))
                
        if p_DefStrong.count("Grass") > 0:
            $ p_DefStrong.remove("Grass")
        else:
            if p_DefVeryStrong.count("Grass") = 0:
                $ p_DefWeak.extend(("Grass"))
        
    if type2 == "Electric":
        #1/4 Weakness
        if p_DefStrong.count("Electric") > 0:
            $ p_DefStrong.remove("Electric")
            $ p_DefVeryStrong.extend(("Electric"))
        if p_DefStrong.count("Flying") > 0:
            $ p_DefStrong.remove("Flying")
            $ p_DefVeryStrong.extend(("Flying"))
        if p_DefStrong.count("Steel") > 0:
            $ p_DefStrong.remove("Steel")
            $ p_DefVeryStrong.extend(("Steel"))
        
        #Quad Weakness
        if p_DefWeak.count("Ground") > 0:
            $ p_DefWeak.remove("Ground")
            $ p_DefVeryWeak.extend(("Ground"))
        
        #Normal/ 1/2 damage/ double damage
        if p_DefWeak.count("Electric") > 0:
            $ p_DefWeak.remove("Electric")
        else:
            if p_DefVeryStrong.count("Electric") = 0:
                $ p_DefStrong.extend(("Electric"))
                
        if p_DefWeak.count("Flying") > 0:
            $ p_DefWeak.remove("Flying")
        else:
            if p_DefVeryStrong.count("Flying") = 0:
                $ p_DefStrong.extend(("Flying"))
                
        if p_DefWeak.count("Steel") > 0:
            $ p_DefWeak.remove("Steel")
        else:
            if p_DefVeryStrong.count("Steel") = 0:
                $ p_DefStrong.extend(("Steel"))
        
        if p_DefStrong.count("Ground") > 0:
            $ p_DefStrong.remove("Ground")
        else:
            if p_DefVeryWeak.count("Ground") = 0:
                $ p_DefWeak.extend(("Ground"))
                
    if type2 == "Grass":  
        #1/4 Weakness
        if p_DefStrong.count("Water") > 0:
            $ p_DefStrong.remove("Water")
            $ p_DefVeryStrong.extend(("Water"))
        if p_DefStrong.count("Electric") > 0:
            $ p_DefStrong.remove("Electric")
            $ p_DefVeryStrong.extend(("Electric"))
        if p_DefStrong.count("Grass") > 0:
            $ p_DefStrong.remove("Grass")
            $ p_DefVeryStrong.extend(("Grass"))
        if p_DefStrong.count("Ground") > 0:
            $ p_DefStrong.remove("Ground")
            $ p_DefVeryStrong.extend(("Ground"))
        
        #Quad Weakness
        if p_DefWeak.count("Fire") > 0:
            $ p_DefWeak.remove("Fire")
            $ p_DefVeryWeak.extend(("Fire"))
        if p_DefWeak.count("Ice") > 0:
            $ p_DefWeak.remove("Ice")
            $ p_DefVeryWeak.extend(("Ice"))
        if p_DefWeak.count("Poison") > 0:
            $ p_DefWeak.remove("Poison")
            $ p_DefVeryWeak.extend(("Poison"))
        if p_DefWeak.count("Flying") > 0:
            $ p_DefWeak.remove("Flying")
            $ p_DefVeryWeak.extend(("Flying"))
        if p_DefWeak.count("Bug") > 0:
            $ p_DefWeak.remove("Bug")
            $ p_DefVeryWeak.extend(("Bug"))
        
        #Normal/ 1/2 damage/ double damage
        if p_DefWeak.count("Water") > 0:
            $ p_DefWeak.remove("Water")
        else:
            if p_DefVeryStrong.count("Water") = 0:
                $ p_DefStrong.extend(("Water"))
        
        if p_DefWeak.count("Electric") > 0:
            $ p_DefWeak.remove("Electric")
        else:
            if p_DefVeryStrong.count("Electric") = 0:
                $ p_DefStrong.extend(("Electric"))
        
        if p_DefWeak.count("Grass") > 0:
            $ p_DefWeak.remove("Grass")
        else:
            if p_DefVeryStrong.count("Grass") = 0:
                $ p_DefStrong.extend(("Grass"))
        
        if p_DefWeak.count("Ground") > 0:
            $ p_DefWeak.remove("Ground")
        else:
            if p_DefVeryStrong.count("Ground") = 0:
                $ p_DefStrong.extend(("Ground"))
        
        if p_DefStrong.count("Fire") > 0:
            $ p_DefStrong.remove("Fire")
        else:
            if p_DefVeryWeak.count("Fire") = 0:
                $ p_DefWeak.extend(("Fire"))
        
        if p_DefStrong.count("Ice") > 0:
            $ p_DefStrong.remove("Ice")
        else:
            if p_DefVeryWeak.count("Ice") = 0:
                $ p_DefWeak.extend(("Ice"))
        
        if p_DefStrong.count("Poison") > 0:
            $ p_DefStrong.remove("Poison")
        else:
            if p_DefVeryWeak.count("Poison") = 0:
                $ p_DefWeak.extend(("Poison"))
        
        if p_DefStrong.count("Flying") > 0:
            $ p_DefStrong.remove("Flying")
        else:
            if p_DefVeryWeak.count("Flying") = 0:
                $ p_DefWeak.extend(("Flying"))
        
        if p_DefStrong.count("Bug") = 0:
            $ p_DefStrong.remove("Bug")
        else:
            if p_DefVeryWeak.count("Bug") = 0:
                $ p_DefWeak.extend(("Bug"))
        
#    if type2 == "Ice":
#    if type2 == "Fighting":    
#    if type2 == "Poison":
#    if type2 == "Ground":
#    if type2 == "Flying":
#    if type2 == "Psychic":
#    if type2 == "Bug":
#    if type2 == "Rock":
#    if type2 == "Ghost":
#    if type2 == "Dragon":
#    if type2 == "Dark":
#    if type2 == "Steel":
#    if type2 == "Fairy":
    
    return
