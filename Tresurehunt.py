#!/usr/bin/env python 

#Welcome to my version of AQA Tresure Hunt. By Dylan Spriddle. Started 26/09/2016
#You start the game on the menu where you have a choice between playing ('1') or options('2')
#The options allows you to change icons, map size, icon x_y_width (player icon size). Ps. have a look at GameBot :D
#basic game controls are (u1 = up 1)(r1 = right 1)(l1 = left 1)(d1 = down 1) 
#Ignore the spelling mistake, i study programming not english :)

# RUN ON A LINUX TERMINAL IF POSSIBLE! ELSE OPEN IN A PYTHON CMD WINDOWN (idle works fine, it just dosn't support the os.system('clear') function)






def aga():
    from random import randint
    from sys import platform
    import os
    import time
    global x
    global z
    global Game_activation
    global error_message
    global land_icon
    global used_land_icon
    global bandit_icon
    global player_icon 
    global chest_icon
    global Map_Size_X_Y
    global Chests_Bandits
    global player_score
    global d3bug
    global bot_speed
    global clear
    global win
    global bot_memory
    global print_board
    global max_step
    global re_use



    def d3bug_bot(bot_speed):
        global bot_memory
        global print_board
        global max_step
        global Chests_Bandits
        global re_use
        if bot_speed >= 0.1:
            thinking = ["  ^", "    ^", "    ^", "    ^"]
            thinker = True
        else:
            thinking = []
            thinker = False
        think_count = 0
        ticker = True
        while True:
            thoughts = []
            is_re_use = False
            if re_use != "":
                thoughts.append(re_use) 
                is_re_use = 1
            else:
                is_re_use = 0
            for out in range((bot_memory) - is_re_use):
                # I'm pretty dumb but I can play the game for you!
                rand_udlr = randint(0, 3)
                rand_step = randint(1, max_step)
                out = ""
                if rand_udlr == 0:
                    out += 'u'
                elif rand_udlr == 1:
                    out += 'd'
                elif rand_udlr == 2:
                    out += 'l'
                elif rand_udlr == 3:
                    out += 'r'
                out += str(rand_step)
                #print out, "+",
                thoughts.append(out)
            #print out,
            #bot_speed = 0.01
            if thinker and ticker:
                print thoughts
            #time.sleep(1)
            ischest = False
            #if bot_speed > 0.05:
                #print thoughts
            land_left = 0
            for map in playerboard:
                for spot in map:
                    if spot == land_icon:
                        land_left += 1



            if not thinker:
                time.sleep(float(bot_speed) * 0.3)
            if land_left > 0:
                for out in thoughts:
                    if thinker and ticker:
                        print thinking[think_count],
                    if think_count == 3:
                        think_count = 1
                    else:
                        think_count += 1
                    time.sleep(float(bot_speed) * 0.3)

                    if out[0] == "u":
                        if player_location[0] - int(out[1]) >= 0: # UP (-X, 0)
                            if playerboard[(player_location[0] - int(out[1]))][player_location[1]]in (land_icon): # Is generated move == land_icon
                                re_use = out
                                return out
                                break
                    elif out[0] == "d":
                        if (player_location[0] + int(out[1])) < (len(object_board)): # DOWN (+X, 0)
                            if playerboard[(player_location[0] + int(out[1]))][player_location[1]]in (land_icon):
                                re_use = out
                                return out
                                break
                    elif out[0] == "r":
                        if player_location[1] + int(out[1]) < (len(object_board)): # RIGHT (0, +X)
                            if playerboard[player_location[0]][(player_location[1] + int(out[1]))] in (land_icon):
                                re_use = out
                                return out
                                break

                    elif out[0] == "l":
                        if player_location[1] - int(out[1]) >= 0: # LEFT (0, -X)
                            if playerboard[player_location[0]][(player_location[1] - int(out[1]))] in (land_icon):
                                re_use = out
                                return out
                                break

            think_count = 0
            print ""
            if not thinker:
                time.sleep(float(bot_speed) * 0.3)

            for out in thoughts: # is chest?
                if thinker and ticker:
                    print thinking[think_count],
                    if think_count == 3:
                        think_count = 1
                    else:
                        think_count += 1
                    time.sleep(float(bot_speed) * 0.3)
                        
                if out[0] == "u":
                    if player_location[0] - int(out[1]) >= 0: # UP (-X, 0)
                        if playerboard[(player_location[0] - int(out[1]))][player_location[1]] in (chest):
                            re_use = ""
                            print "A chest!!!!"
                            return out
                            break
                
                if out[0] == "d":
                    if (player_location[0] + int(out[1])) < (len(object_board)): # DOWN (+X, 0)
                        if playerboard[(player_location[0] + int(out[1]))][player_location[1]] in (chest):
                            re_use = ""
                            print "A chest!!!!"
                            return out
                            break

                if out[0] == "r":
                    if player_location[1] + int(out[1]) < (len(object_board)): # RIGHT (0, +X)
                        if playerboard[player_location[0]][(player_location[1] + int(out[1]))] in (chest):
                            re_use = ""
                            print "A chest!!!!"
                            return out
                            break

            else: # is safe move?
                if thinker == True:
                    print thinking[think_count],
                    if think_count == 3:
                        think_count = 1
                    else:
                        think_count += 1
                    time.sleep(float(bot_speed) * 0.3)
                if out[0] == "l":
                    if player_location[1] - int(out[1]) >= 0: # LEFT (0, -X)
                        if playerboard[player_location[0]][(player_location[1] - int(out[1]))] in (chest):
                            re_use = ""
                            print "A chest!!!!"
                            return out
                            break

                if out[0] == "u":
                    if player_location[0] - int(out[1]) >= 0: # UP (-X, 0)
                        if playerboard[(player_location[0] - int(out[1]))][player_location[1]] not in (bandit):
                            re_use = ""
                            return out
                            break
                elif out[0] == "d":
                    if (player_location[0] + int(out[1])) < (len(object_board)): # DOWN (+X, 0)
                        if playerboard[(player_location[0] + int(out[1]))][player_location[1]] not in (bandit):
                            re_use = ""
                            return out
                            break
                elif out[0] == "r":
                    if player_location[1] + int(out[1]) < (len(object_board)): # RIGHT (0, +X)
                        if playerboard[player_location[0]][(player_location[1] + int(out[1]))] not in (bandit):
                            re_use = ""
                            return out
                            break

                elif out[0] == "l":
                    if player_location[1] - int(out[1]) >= 0: # LEFT (0, -X)
                        if playerboard[player_location[0]][(player_location[1] - int(out[1]))] not in (bandit):
                            re_use = ""
                            return out
                            break
                ticker = False

        else:
            em = "What?"

    if platform == "linux" or platform == "linux2":
        clear = lambda: os.system('clear')
    elif platform == "darwin":
        clear = lambda: os.system('clear')
    elif platform == "win32":
        clear = lambda: os.system('cls')

    print "Test"

    clear()


    #------------------------------------------------------------------------------------------------------- Varibles
    Chests_Bandits = {    
        "chests": 10,
        "bandit": 5
    }

    #boring varibles
    player_score = 0
    Used_coordinates = []
    object_board = []
    memory_board = []
    playerboard = []
    error_message = ""
    Game_activation = False

    #other varibles
    win = 100
    Map_Size_X_Y = 8
    re_use = "u1"

    #bot varibles
    d3bug = False
    bot_speed = 0.5
    bot_memory = 8
    max_step = 2

    #Icons
    land_icon = ' '
    used_land_icon = '~'
    player_icon = '#'
    bandit_icon = 'X'
    chest_icon = '$'

    #------------------------------------------------------------------------------------------------------- Options
    def options():
        global land_icon
        global used_land_icon
        global bandit_icon
        global player_icon
        global chest_icon
        global Map_Size_X_Y
        global Chests_Bandits
        global d3bug
        global win
        global bot_speed
        global bot_memory
        global clear
        global error_message
        
        while True:
            clear()
            print error_message
            error_message = ""
            print ""
            print "Select option to edit:"
            print "1 - Map size"
            print "2 - Chests"
            print "3 - Bandits"
            print "4 - Object Icons"
            print "5 - Gold to win"
            print "6 - Exit"
            print "7 - GameBot"
            Option = raw_input("Enter now: ")

            if Option == '1':
                clear()
                print "Map size currently", Map_Size_X_Y, '*', Map_Size_X_Y
                New_size = raw_input("Enter Map X*Y size: ")
                if len(New_size) >= 1:
                    New_size = int(New_size)
                    Map_Size_X_Y = New_size
                else:
                    error_message = "Map size not changed."
            elif Option == '2':
                clear()
                print "There are currently", Chests_Bandits['chests'], "chests."
                New_chests = raw_input("Enter new chest amount: ")
                if len(New_chests) >= 1:
                    New_chests = int(New_chests)
                    Chests_Bandits['chests'] = New_chests
                else:
                    error_message = "Chest amount not changed"
            elif Option == '3':
                clear()
                print "There are currently", Chests_Bandits['bandit'], "bandits."
                New_Bandits = raw_input("Enter new bandit amount: ")
                if len(New_Bandits) >= 1:
                    New_Bandits = int(New_Bandits)
                    Chests_Bandits['bandit'] = New_Bandits
                else:
                    error_message = "Bandit amount not changed"  
            elif Option == '4':
                    while True:
                        clear()
                        print error_message
                        error_message = ""
                        print ""
                        print "Select an icon to edit:"
                        print "1 - player (Warning! global Icon size will match new player icon length)"
                        print "2 - chests"
                        print "3 - bandit"
                        print "4 - untouched land"
                        print "5 - touched land"
                        print "6 - Exit"
                        option2 = raw_input("Enter now: ")
                        if option2 == '1':
                            clear()
                            print "Player icon currently: ", player_icon
                            new_player_icon = raw_input("Enter new icon now: ")
                            if len(new_player_icon) > 0:
                                player_icon = new_player_icon
                            else:
                                error_message = "Value not changed"
                        elif option2 == '2':
                            clear()
                            print "Chest icon currently: ", chest_icon
                            new_chest_icon = raw_input("Enter new icon now: ")
                            if len(new_chest_icon) > 0:
                                chest_icon = new_chest_icon
                            else:
                                error_message = "Value not changed"
                        elif option2 == '3':
                            clear()
                            print "Bandit icon currently: ", bandit_icon
                            new_bandit_icon = raw_input("Enter new icon now: ")
                            if len(new_bandit_icon) > 0:
                                bandit_icon = new_bandit_icon
                            else:
                                error_message = "Value not changed"
                        elif option2 == '4':
                            clear()
                            print "Untouched land icon currently: ", land_icon
                            new_used_land_icon = raw_input("Enter new icon now: ")
                            if len(new_used_land_icon) > 0:
                                land_icon = new_used_land_icon
                            else:
                                error_message = "Value not changed"
                        elif option2 == '5':
                            clear()
                            print "Touched land currently: ", used_land_icon
                            new_land_icon = raw_input("Enter new icon now: ")
                            if len(new_land_icon) > 0:
                                used_land_icon = new_land_icon
                            else:
                                error_message = "Value not changed"
                        elif option2 == '6':
                            break
                        else:
                            "What?"       
            elif Option == '5':
                clear()
                print "You currently need", win, "Gold to win the game."
                new_win = raw_input("Enter new win amount: ")
                if len(new_win) > 1:
                    if  new_win < 1:
                        error_message = "Value too low! Re-setting to 1.."
                        win = 1
                    else:
                        new_win = int(new_win)
                        win = new_win 
                else:
                    error_message = "Value not changed"
                      
            elif Option == '6':
                if (int(Map_Size_X_Y) ** 2 - 1) < (Chests_Bandits['chests'] + Chests_Bandits['bandit']):
                    print ""
                    clear()
                    print "INVALID SETTINGS! Map Size =", Map_Size_X_Y, "*", Map_Size_X_Y, "(", (Map_Size_X_Y ** 2), "Squares", ")", "Bandits + Chests =", (Chests_Bandits['chests'] + Chests_Bandits['bandit']), "Squares"
                    while (Map_Size_X_Y ** 2) < ((Chests_Bandits['chests'] + Chests_Bandits['bandit']) + 25):
                        Map_Size_X_Y += 1
                    else:
                        print "Map Size Has Been Reconfigured To", Map_Size_X_Y, '*', Map_Size_X_Y, "(", (Map_Size_X_Y**2), "Squares", ")"
                        print ""
                        break
                else:
                    clear()
                    break
            elif Option == '7':
                while True:
                    clear()
                    print ""
                    print "GameBot will play the game for you!"
                    print "Select setting to change:"
                    print "1 - ON/OFF"
                    print "2 - Bot speed"
                    print "3 - Bot Intelligence"
                    print "6 - Exit"
                    bot_option = raw_input("Enter now: ")

                    if bot_option == "1":
                        clear()
                        print ""
                        print "Select ON/OFF:"
                        print "1 - ON"
                        print "2 - OFF" 
                        ONOFF = raw_input("Enter now: ")
                        if ONOFF == "1":
                            d3bug = True
                            print ""
                            error_message = "# GameBot activated*"
                        elif ONOFF == "2":
                            d3bug = False
                            print ""
                            error_message = "# GameBot de-activated*"
                    elif bot_option == "2":
                        clear()
                        print ""
                        print "BotSpeed currently :", bot_speed*10, "(Lower is faster :))"
                        new_speed = raw_input("enter new bot speed :")
                        if len(new_speed) >= 1:
                            new_speed = float(new_speed)
                            new_speed *= 0.1
                            bot_speed = new_speed
                        else:
                            error_message = "Speed not changed"
                    elif bot_option == "3":
                        clear()
                        print ""
                        print "Bot Intelligence currently", bot_memory, "/ 8."
                        bot_intelligence = raw_input("Enter bot intelligence now: ")
                        if len(bot_intelligence) >= 1:
                            bot_intelligence = int(bot_intelligence)
                            if bot_intelligence > 0:
                                if bot_intelligence < 8:
                                    bot_memory = bot_intelligence
                                else:
                                    error_message = "Bot intelligence too High! It might become self aware and kill you!"
                            else:
                                error_message = "Bot intelligence too low"
                        else:
                            error_message = "Bot intelligence not changed."

                    elif bot_option == "6":
                        break


            else:
                print "What?"

        global Game_activation
        print "Welcome to Bandits & Gold!"
        print "Enter navigation number:"
        print "Start = '1'"
        print "Options = '2'"
        start = raw_input('Enter: ')
        if start == "1":
            Game_activation = True
        elif start == "2":
            options()
    #------------------------------------------------------------------------------------------------------- Menu
    def menu():
        global Game_activation
        global error_message
        global timer0
        while Game_activation != True:       
            clear()
            print error_message
            error_message = ""
            print "Welcome to Bandits & Gold!"
            print "Enter navigation number:"
            print "Start = '1'"
            print "Options = '2'"
            start = raw_input('Enter: ')
            if start == '1':
                Game_activation = True
                print Game_activation

                break
            elif start == '2':
                print ""
                options()
      
            else:
                print 'What?'
    menu()

    #------------------------------------------------------------------------------------------------------- Icon length
    icon_length = len(player_icon)
    bandit = bandit_icon*icon_length
    chest = chest_icon*icon_length
    #------------------------------------------------------------------------------------------------------- Map writer
    for click in range(Map_Size_X_Y):
        object_board.append([used_land_icon*icon_length] * Map_Size_X_Y)
        playerboard.append([land_icon*icon_length] * Map_Size_X_Y)
        memory_board.append([0*icon_length] * Map_Size_X_Y)
    

    #------------------------------------------------------------------------------------------------------- Player start location
    player_location = [(len(object_board)-1), 0]
    Used_coordinates.append(str(player_location[0]) + str(player_location[1]))

    #------------------------------------------------------------------------------------------------------- Random object to map placer
    def Object_Placement(ran_len, WHO):
        spot = []
        for x in range(ran_len): # How many random numbers?
            x, z = 0, 0        
            def baker():
                global x
                global z
                x, z = randint(0, (len(object_board)-1)), randint(0, (len(object_board)-1))            
                if (str(x) + str(z)) in Used_coordinates: # or (str(x) + str(z)) in Used_coordinates:
                    #print "XZ FOUND IN SPOT", (str(x) + str(z))
                    baker()
                elif (str(x) + str(z)) in spot:
                    #print "XZ FOUND IN USED COORDINATES", (str(x) + str(z))
                    baker()
                else:
                    object_board[x][z] = WHO
                    Used_coordinates.append(str(x) + str(z))
                    spot.append(str(x) + str(z))
                           
            baker()

        if len(spot) > ran_len:
            print "OVERFLOW!"
        return spot
        Used_coordinates.append(spot)
    Chests_Bandits['chests'] = Object_Placement(Chests_Bandits['chests'], chest)
    Chests_Bandits['bandit'] = Object_Placement(Chests_Bandits['bandit'], bandit)



    #random_gen(5) #Debug
    '''print stuff['chests']
    print stuff['bandit']'''

    #------------------------------------------------------------------------------------------------------- Print board
    def print_board(board):
        for row in board:
            for x in range(icon_length):
                print "  ".join(row)
            print ""

    def print_board2(board):
        for row in board:
            for x in range(icon_length):
                print "".join(str(row))
            print ""
    #print_board(board)

    s0 = 0
    s1 = 0
    s2 = 0

    '''for x in object_board:
        for z in x:
            if z == '0':
                s0 += 1
            elif z == '1':
                s1 += 1
            elif z == '2':
                s2 += 1
            else:
                print "idk what happened"

    print ""
    print "Blank :", s0, "chest's :", s1, "bandit's :", s2'''



    #------------------------------------------------------------------------------------------------------- Board transport
    def board_transport(move_choice, em):
        global error_message
        global player_score
        global clear
        clear()

        if move_choice == "d3bug":
            player_score = 15766
        em = move_choice
        if len(move_choice) == 2 and move_choice[0] in ('u', 'd', 'l', 'r') and move_choice[1] in str(range(0, len(object_board))): 
            if move_choice[0] == "u":
                if player_location[0] - int(move_choice[1]) < 0: #UP
                    em = "You can't move there!"
                else:
                    player_location[0] -= int(move_choice[1]) 

            elif move_choice[0] == "d":
                if (player_location[0] + int(move_choice[1])) > (len(object_board)-1): #DOWN

                    em = "You can't move there!"
                else:
                    player_location[0] += int(move_choice[1])
            elif move_choice[0] == "r":
                if player_location[1] + int(move_choice[1]) > (len(object_board)-1): #RIGHT

                    em = "You can't move there!"
                else:
                    player_location[1] += int(move_choice[1])
            elif move_choice[0] == "l":
                if player_location[1] - int(move_choice[1]) < 0: #LEFT

                    em = "You can't move there!"
                else:
                    player_location[1] -= int(move_choice[1])
            else:
                em = "What?"
        else:
            em = "Unreadable input"
        error_message = em
        return player_location

    clear()

    #------------------------------------------------------------------------------------------------------- Game loop
    while player_score < win:

        icon_length = len(player_icon)
        bandit = bandit_icon*icon_length
        chest = chest_icon*icon_length
        #print_board(object_board)
        #time.sleep(1)
        while Game_activation:

            ban = 0
            che = 0
            for objects in object_board:
                for item in objects:
                    if item == bandit:
                        ban += 1
                    if item == chest:
                        che += 1
            if player_score >= win:
                print "you won!"
                break
            elif che == 0:
                print "No chests left! You've lost!"
                break
            clear()
            #os.system('clear') #FOR LINUX  




            print error_message
            error_message = ""
            oldposision = player_location
            playerboard[player_location[0]][player_location[1]] = player_icon # Make me Multiple choice!
            print_board(playerboard)
            print ""

            playerboard[oldposision[0]][oldposision[1]] = object_board[oldposision[0]][oldposision[1]] # Make old posision == object
            memory_board[oldposision[0]][oldposision[1]] += 1 #Block usage counter (You have stepped on this square x times)



            if object_board[oldposision[0]][oldposision[1]] == bandit:
                player_score = 0
            if object_board[oldposision[0]][oldposision[1]] == chest:
                if memory_board[oldposision[0]][oldposision[1]] == 3:
                    player_score += 10
                    playerboard[oldposision[0]][oldposision[1]], object_board[oldposision[0]][oldposision[1]] = bandit, bandit # Make chest into bandit

                else:
                    player_score += 10
            



            print "You have", player_score, "Gold"
            print "There are", ban, "Bandit[s] and", che, "chest[s] left"




            print ""
            if d3bug != True:
                W = raw_input("Where to move?")
            else:
                W = d3bug_bot(bot_speed)
            board_transport(W, error_message)
        break
aga()
    #------------------------------------------------------------------------------------------------------- Restart?
def again():
    while True:
        print ""
        again = 'y'# raw_input("Play again? y/n")
        if again == 'y':
            aga()
        elif again == 'n':
            print "Thanks for playing!"
            break
again()






#------------------------------------------------------------------------------------------------------- #715L TH True smartbot (new memory config)