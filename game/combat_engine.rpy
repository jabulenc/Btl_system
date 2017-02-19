init python:

    def stats_frame(name, level, hp, maxhp, **properties):

        ui.frame(xfill=False, yminimum=None, **properties)

        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)

        ui.text(name, size=20)

        ui.hbox() # "HP" from bar
        ui.text("HP", size=20)
        ui.bar(maxhp, hp,
               xmaximum=150)

        ui.close()
        ui.close()

        ui.vbox() # Level from (hp/maxhp)

        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)

        ui.close()
        ui.close()
        
init 1 python:
    from random import randint
    chance = 0
    def rand_enemy(chance):
        chance = randint(1,3)
        return chance
        
init:
    $ nopoisonE = True
    $ nopoisonP = True
    $ noBurnP = True
    $ noBurnE = True
    $ sleepCounterE = 3
    $ sleepingE = False
    $ sleepCounterP = 3
    $ sleepingP = False
    $ pauseGame = False
    $ partyPokemon = None
    $ switchPoke = False
    
    call storage
    
    #Dictionaries stored in List for flexibility/ease of use
    
    if partyPokemon is None:
        $ pokelist = [Vena, CharZ, Blast]
    else:
        $ pokelist = partyPokemon
    $ ePoke = [Mew2, CharZ]
    
    $ combat_turn = 0
    $ curEPoke = 0
    $ numEPoke = len(ePoke)
    $ numPoke = len(pokelist)

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
    
image enemy_cyan:
    xalign .98
    yalign .02
    "e2.png"
    
image enemy_green:
    xalign .98
    yalign .02
    "e3.png"
    
image poisoned:
    "poison.png"

#This label controls Enemy and Player stats' screen
label fight:
    
    $ critroll = renpy.random.randint(1, 4)
    
    $ d4roll = renpy.random.randint(1, 4)

    # Player Stats Frame
    $ stats_frame(pname, plevel, php, pmaxhp, xalign=.02, yalign=.7)
        
    # Enemy Stats Frame
    $ stats_frame(ename, elevel, ehp, emaxhp, xalign=.98, yalign=.7)
    return


#(1/22) Labels: combat, pokemon, skillsetup
label combat:
    $ iter = 0
    $ names = []
    
    #Unable to create menu using pokelist[n]['Name']. Will need to look into this
    while iter != numPoke:
        $ names.append(pokelist[iter]['Name'])
        $ iter += 1
    
    #Choosing initial pokemon
    if combat_turn == 0:
        menu:
            "Choose your Pokemon."
            "[names[0]]" if numPoke >= 1:
                $ curPoke = 0
            "[names[1]]" if numPoke >= 2:
                $ curPoke = 1
            "[names[2]]" if numPoke >= 3:
                $ curPoke = 2
            "[names[3]]" if numPoke >= 4:
                $ curPoke = 3
            "[names[4]]" if numPoke >= 5:
                $ curPoke = 4
            "[names[5]]" if numPoke >= 6:
                $ curPoke = 5
        jump pokemon
    #Switching pokemon
    else:
        call fight
        menu:
            "Choose your Pokemon."
            "[names[0]]" if numPoke >= 1:
                call hideImage
                $ curPoke = 0
            "[names[1]]" if numPoke >= 2:
                call hideImage
                $ curPoke = 1
            "[names[2]]" if numPoke >= 3:
                call hideImage
                $ curPoke = 2
            "[names[3]]" if numPoke >= 4:
                call hideImage
                $ curPoke = 3
            "[names[4]]" if numPoke >= 5:
                call hideImage
                $ curPoke = 4
            "[names[5]]" if numPoke >= 6:
                call hideImage
                $ curPoke = 5
            "Back":
                jump battle
        jump pokemon

label pokemon:
    #Setting up all data with the pokemon's "Current HP"
    
    if pauseGame:
        "[ename] has fainted!"
        menu:
            "Would you like to change Pokemon?"
            "[pname]'s done enough! Let's switch them out!":
                $ pauseGame = False
                jump combat
            "[pname]'s still got fight left!":
                $ pauseGame = False
                jump battle
        jump pokemon
    else:
        #HP
        $ php = pokelist[curPoke]['CurrHP']
        $ ehp = ePoke[curEPoke]['CurrHP']
        
        # Player/Fighter image
        image playerPokemon:
            xalign .02
            yalign .02
            pokelist[curPoke]['Image']
        show playerPokemon
        
        #Pokemon Setup
        if php != 0:
            $ pname = pokelist[curPoke]['Name']
            $ plevel = 50
            $ pmaxhp = pokelist[curPoke]['MaxHP']
            $ skill_1 = pokelist[curPoke]['Skill_1']
            $ skill_1_dam = pokelist[curPoke]['Skill_1_dmg']
            $ skill_1_stat = pokelist[curPoke]['S1_Status']
            
            $ skill_2 = pokelist[curPoke]['Skill_2']
            $ skill_2_dam = pokelist[curPoke]['Skill_2_dmg']
            $ skill_2_stat = pokelist[curPoke]['S2_Status']
            
            $ skill_3 = pokelist[curPoke]['Skill_3']
            $ skill_3_dam = pokelist[curPoke]['Skill_3_dmg']
            $ skill_3_stat = pokelist[curPoke]['S3_Status']
            
            $ skill_4 = pokelist[curPoke]['Skill_4']
            $ skill_4_dam = pokelist[curPoke]['Skill_4_dmg']
            $ skill_4_stat = pokelist[curPoke]['S4_Status']
            
            $ type1 = pokelist[curPoke]['T1']
            $ type2 = pokelist[curPoke]['T2']
            
            call typeSetup
        
        #Enemy Setup
        if ehp != 0:
            $ ename = ePoke[curEPoke]['Name']
            $ elevel = 54
            $ emaxhp = ePoke[curEPoke]['MaxHP']
            
            $ e_skill1_Name = ePoke[curEPoke]['Skill_1']
            $ e_skill1 = ePoke[curEPoke]['Skill_1_dmg']
            $ e_skill1_stat = ePoke[curEPoke]['S1_Status']
            
            $ e_skill2_Name = ePoke[curEPoke]['Skill_2']
            $ e_skill2 = ePoke[curEPoke]['Skill_2_dmg']
            $ e_skill2_stat = ePoke[curEPoke]['S2_Status']
            
            $ e_skill3_Name = ePoke[curEPoke]['Skill_3']
            $ e_skill3 = ePoke[curEPoke]['Skill_3_dmg']
            $ e_skill3_stat = ePoke[curEPoke]['S3_Status']
            
            $ e_skill4_Name = ePoke[curEPoke]['Skill_4']
            $ e_skill4 = ePoke[curEPoke]['Skill_4_dmg']
            $ e_skill4_stat = ePoke[curEPoke]['S4_Status']
            
            $ e_type1 = ePoke[curEPoke]['T1']
            $ e_type2 = ePoke[curEPoke]['T2']
                
            image enemyPokemon:
                xalign .98
                yalign .02
                ePoke[curEPoke]['Image']
            show enemyPokemon
            
        jump battle

label battle:
    call fight
    $ combat_turn += 1
    $ numSkill = 0
    
    #Battle Menu
    menu:
        "What would you like to do?"
        "Fight":
            call fight 
            menu:
                "What should [pname] do?"
                "[skill_1]":
                    $ numSkill = 1
                "[skill_2]":
                    $ numSkill = 2
                "[skill_3]":
                    $ numSkill = 3
                "[skill_4]":
                    $ numSkill = 4
            jump use_skill
        "Run":
            jump p_defeat
        "Team":
            #Storing current HP of pokemon in dictionary
            $ pokelist[curPoke]['CurrHP'] = php
            jump combat

label use_skill:
    call fight 
    
    if sleepingP == False:
        $ skillDamage = 0
        $ skillStatus = "None"
        
        if numSkill == 1:
            "[pname] used [skill_1]!"
            $ skillDamage = skill_1_dam
            $ skillStatus = skill_1_stat
        elif numSkill == 2:
            "[pname] used [skill_2]!"
            $ skillDamage = skill_2_dam
            $ skillStatus = skill_2_stat
        elif numSkill == 3:
            "[pname] used [skill_3]!"
            $ skillDamage = skill_3_dam
            $ skillStatus = skill_3_stat
        elif numSkill == 4:
            "[pname] used [skill_4]!"
            $ skillDamage = skill_4_dam
            $ skillStatus = skill_4_stat
        
        if skillStatus == "None" or skillStatus == "Recharge":
            if critroll == 2:
                $ crit = True
                call fight
                "Critical hit!"
                $ ehp -= skillDamage*2
            else:
                $ ehp -= skillDamage
                $ crit = False
        elif skillStatus == "Heal":
            if (pmaxhp - php) <= skillDamage:
                $ php = pmaxhp
            else:
                $ php += skillDamage
            call fight
            "[pname]'s HP was restored."
        elif skillStatus == "Brn":
            "[ename] was burned"
            $ noBurnP = False;
        elif skillStatus == "Psn":
            "[ename] was poisoned"
            $ nopoisonE = False
        elif skillStatus == "Frz":
            "[ename] was frozen"
        elif skillStatus == "Prlz":
            "[ename] was paralyzed"
        elif skillStatus == "Con":
            "[ename] was confused"
        elif skillStatus == "Slp":
            "[ename] has fallen asleep!"
            $ sleepingE = True
        elif skillStatus == "PsnDD":
            if nopoisonE == False:
                if critroll == 2:
                    call fight
                    "Critical hit!"
                    $ ehp -= skillDamage*4
                else:
                    $ ehp -= skillDamage*2
            elif nopoisonE == True:
                if critroll == 2:
                    call fight
                    "Critical hit!"
                    $ ehp -= skillDamage*2
                else:
                    $ ehp -= skillDamage
        
        if nopoisonP == False:
            call fight
            $ php -= 1+(combat_turn)
            "[pname] was hurt from the poison!"
        
        if noBurnP == False:
            call fight
            $ php = php - 2
            "[pname] was hurt from the burn!"
        
        if ehp <= 0:
            $ ehp = 0
            call fight
            "Enemy [ename] fainted!"
            $ nopoison = True;
            $ numEPoke = numEPoke - 1
            if numEPoke > 0:
                call enemyHideImage
                $ curEPoke = curEPoke + 1
                $ pokelist[curPoke]['CurrHP'] = php
                $ pauseGame = True
                call pokemon
            else:
                jump e_defeat
    else:
        $ sleepCounterP = sleepCounterP - 1
        if sleepCounterP == 0:
            $ sleepingP = False
            $ sleepCounterP = 3
            call fight
            "[pname] woke up!"
        
    jump eTurn
    
label eTurn:
    call fight
    
    if sleepingE == False:
        $ eSkillDam = 0
        $ eSkillStat = "None"
        
        if d4roll == 1:
            "[ename] used [e_skill1_Name]!"
            $ skillDamage = e_skill1
            $ skillStatus = e_skill1_stat
        elif d4roll == 2:
            "[ename] used [e_skill2_Name]!"
            $ skillDamage = e_skill2
            $ skillStatus = e_skill2_stat
        elif d4roll == 3:
            "[ename] used [e_skill3_Name]!"
            $ skillDamage = e_skill3
            $ skillStatus = e_skill3_stat
        elif d4roll == 4:
            "[ename] used [e_skill4_Name]!"
            $ skillDamage = e_skill4
            $ skillStatus = e_skill4_stat
        
        if skillStatus == "None" or skillStatus == "Recharge": #NOTE TO SELF: REMEMBER TO ADD MORE SKILL STAT'S OTHERWISE IT WON'T HIT
            if critroll == 2:
                call fight
                "Critical hit!"
                $ php -= skillDamage*2
            else:
                $ php -= e_skill1
        elif skillStatus == "Heal":
            if (emaxhp - ehp) <= skillDamage:
                $ ehp = emaxhp
            else:
                $ ehp += skillDamage
            call fight
            "[ename]'s HP was restored."
        elif skillStatus == "Brn":
            "[pname] was burned"
            $ noBurnE = False
        elif skillStatus == "Psn":
            "[pname] was poisoned"
            $ nopoisonP = False
        elif skillStatus == "Frz":
            "[pname] was frozen"
        elif skillStatus == "Prlz":
            "[pname] was paralyzed"
        elif skillStatus == "Con":
            "[pname] was confused"
        elif skillStatus == "Slp":
            "[ename] has fallen asleep!"
            $ sleepingP = True
        elif skillStatus == "PsnDD":
            if nopoisonP == False:
                if critroll == 2:
                    call fight
                    "Critical hit!"
                    $ php -= skillDamage*4
                else:
                    $ php -= skillDamage*2
            elif nopoisonP == True:
                if critroll == 2:
                    call fight
                    "Critical hit!"
                    $ php -= skillDamage*2
                else:
                    $ php -= skillDamage
        
        if nopoisonE == False:
            call fight
            $ ehp -= 1+(combat_turn)
            "[ename] was hurt from the poison!"
        
        if noBurnE == False:
            call fight
            $ ehp = ehp - 2
            "[pname] was hurt from the burn!"
        
        if php <= 0:
            $ php = 0
            call fight
            "[pname] fainted!"
            $ numPoke -= 1
            if numPoke > 0:
                call hideImage
                $ pokelist.pop(curPoke)
                $ combat_turn = 0
                $ ePoke[curEPoke]['CurrHP'] = ehp
                jump combat
            else:
                jump p_defeat
        else:
            call fight
            jump battle
    else:
        $ sleepCounterE = sleepCounterE - 1
        if sleepCounterE == 0:
            $ sleepingE = False
            $ sleepCounterE = 3
            call fight
            "[ename] woke up!"
            
    jump battle
                
label p_defeat:
    scene black with dissolve
    centered "You blacked out!"
    $ renpy.full_restart()
    
label e_defeat:
    scene black with dissolve
    centered "You win! Do you want a cookie?"
    $ renpy.full_restart()
    
label hideImage:
    hide playerPokemon

label enemyHideImage:
    hide enemyPokemon