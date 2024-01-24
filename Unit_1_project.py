from dataclasses import dataclass

import random

from colorama import Back, Fore

@dataclass
class Boss:
  boss_health: int
  name: str
  weakness: str
  resistance: str 

bosslist = [Boss(200, "Werewolf", "Silver-Bullet", "None"), Boss(150, "Killer Clown","Magic", "Fire-Potion"), Boss(200, "Witch", "Fire-Potion", "Magic" ), Boss(100, "Troll", "Gold", "None"), Boss(100, "Skeleton", "Bare-Handed", "None" )]

monster = random.choice(bosslist)

@dataclass
class Player:
  health: int
  gold: bool 
  silver_bullet: bool
  wand: bool 
  sword: bool
  fire_potion: bool
  

 #############  RANDOM ITEMS  ########################## 
def pick_up_item(player1: Player):
  itemlist = ["gun with one bullet", "wand", "potion", "sword", "gold coin"]
  itemplacement = random.choice(itemlist)
  item_option = validate_pickup_item(input(f"There is a {itemplacement} on the ground. Do you pick it up? [Y] or [N]? ")).upper()
  if item_option == "Y":
    if itemplacement == "wand":
      player1.wand = True
      print("You picked up the wand.")
    elif itemplacement == "potion":
      player1.fire_potion = True
      print("You picked up the potion.")
    elif itemplacement == "sword":
      player1.sword = True
      print("You picked up the sword.")
    elif itemplacement == "gold coin":
      player1.gold = True
    elif itemplacement == "gun with one bullet":
      player1.silver_bullet = True
      print("You picked up the gun")
  elif item_option == "N":
    print(f"You decide not to pick up the {itemplacement}.")


 ############  Monster Battle ##########################
def monster_damages_player(player1: Player, monster: Boss):
    monsterdamage = random.randint(15, 25)
    if monster.name == "Werewolf":
      monsterdamage += 5
    elif monster.name == "Troll":
      monsterdamage += 7 
    elif monster.name == "Killer Clown":
      monsterdamage += 10
    elif monster.name == "Witch":
      monsterdamage += 15
    else:
      monsterdamage += 6
    print (f"The {monster.name} attacks you for {monsterdamage} damage.\n")
    player1.health -= monsterdamage
def player_damages_monster(player1: Player, monster: Boss):
  #one_hit_ko_boss_weaknesses_true(player1, monster)
  items = [player1.sword, player1.wand, player1.silver_bullet,]
  if monster.name == "Werewolf" and player1.silver_bullet == True:
    monster.boss_health = 0
    print (Fore.RED +"You shot it." + Fore.RESET)
  else:
    playerdamage = random.randint(20,40)
  if monster.name == "Witch" and player1.fire_potion == True:
    monster.boss_health = 0
    print (Fore.RED + "You set it on fire"+ Fore.RESET)
  else:
    playerdamage = random.randint(20,40)
  if monster.name == "Killer-Clown" and  player1.wand == True:
    monster.boss_health = 0 
    print(Fore.RED +"You cast a spell that pops the clown like a balloon. "+ Fore.RESET)
  else:
    playerdamage = random.randint(20,40)
  if monster.name == "Troll" and player1.gold == True:
    print(Fore.RED + "The Troll stole your gold but spared you life. Keep walking."+ Fore.RESET)
    monster.boss_health = 0
    player1.gold = False
  else:
    playerdamage = random.randint(20,40)
  
  if monster.name == "Skeleton" and not items: 
    monster.boss_health = 0
    print(Back.WHITE + "Boxed with skeleton and emerged triumphant" + Back.RESET)
  else:
    playerdamage = random.randint(20,40)

  
  if monster.boss_health > 0:
    misschance = random.randint (1, 10) == 10
    critchance = random.randint(1, 10) == 7
    playerdamage = random.randint(20,40)
    if misschance:
      playerdamage *= 0
      print("You swing your sword at the Monster but completely miss.\n")
    elif critchance:
      playerdamage *= 5
      print(Fore.RED + f"Critical hit! You hit {monster.name} for {playerdamage} damage!\n"+ Fore.RESET)
    else:
      print(f"You hit the {monster.name} for {playerdamage} damage!\n")
    monster.boss_health -= playerdamage
def is_game_over(player1: Player, monster: Boss) -> bool:
  if player1.health == 0 or monster.boss_health == 0:
    return True
  return False
def battle_monster(player1: Player, monster: Boss):
  while not is_game_over(player1, monster):
    monster_damages_player(player1, monster)
    player1.health = 0 if player1.health <= 0 else player1.health
    player_damages_monster(player1, monster)
    monster.boss_health = 0 if monster.boss_health <= 0 else monster.boss_health
    
    if player1.health > 0 and monster.boss_health > 0:
      print (f"Player health: {player1.health}\nBoss health: {monster.boss_health}\n")
    else:
      if player1.health == 0:
        print (Back.RED + Fore. BLACK +f"You were defeated by the {monster.name}, and yet another person falls victim to the maze..." + Back.RESET + Fore.RESET)
      elif monster.boss_health == 0:
        print (f"You defeated the {monster.name}!")

 ###########  Validations ####################
def validateinput_LS(direction: str) -> str:
    running = True
    while running:
      if direction == "L" or direction == "S" or direction == "l" or direction == "s":
        running = False
      else:
        direction = input("You can not go that way. Please choose a valid path.  ").upper()
    return direction
def validateinput_LR(direction: str) -> str:
  running = True
  while running:
    if direction == "L" or direction == "R" or direction == "l" or direction == "r":
      running = False
    else:
      direction = input("You can not go that way. Please choose a valid path. ").upper()
  return direction
def validateinput_LRS(direction: str) -> str:
  running = True
  while running:
    if direction == "L" or direction == "R" or direction == "S" or direction == "l" or direction == "r" or direction == "s":
      running = False
    else:
      direction = input("You can not go that way. Please choose a valid path.  ").upper()
  return direction
def validateinput_RS(direction: str) -> str:
  running = True
  while running:
    if direction == "R" or direction == "S" or direction == "r" or direction == "s":
      running = False
    else:
      direction = input("You can not go that way. Please choose a valid path.  ").upper()
  return direction
def validate_path_choice(choice: str) -> str:
  running = True
  while running:
    if choice == "N" or choice == "E" or choice == "W" or choice == "S" or choice =="n" or choice =="e" or choice =="w" or choice =="s":
      running = False
    else:
      choice = input("You can not go that way. Please choose a valid path. ").upper()
  return choice
def validate_enter_maze(entermaze: str) -> str:
  running = True
  while running:
    if entermaze == "Y" or entermaze == "N" or entermaze == "n" or entermaze == "y":
      running = False
    else:
      entermaze = input ("You can not go that way. Please choose a valid path. ").upper()
  return entermaze
def validate_pickup_item(getitem: str) -> str:
  running = True
  while running:
    if getitem == "Y" or getitem == "y" or getitem == "N" or getitem == "n":
      running = False
    else:
      getitem = input("That was not an option. Pick again. [Y] or [N]? ")
  return getitem

 ##########  Directions ######################
  
def fork_in_road_right_or_straight() -> str:
  print (Fore.BLUE + "\nThe path forks before you."+ Fore.RESET)
  direction = validateinput_RS(input ("Do you wish to take the [S]traight or [R]ight path? ")).upper()
  if direction == "R":
    print ("You take the right path.\n")
  elif direction == "S":
    print ("You take the straight path.\n")
  return direction
def fork_in_road_left_or_straight():
  print (Fore.BLUE +"\nThe path forks before you."+Fore.RESET)
  direction = validateinput_LS(input("Do you wish to take the [L]eft or [S]traight path? ")).upper()
  if direction == "L":
    print ("You take the left path.\n")
  elif direction == "S":
    print ("You take the straight path.\n")
  return direction
def fork_in_road_left_or_right():
  print (Fore.BLUE + "\nThe path forks before you."+ Fore.RESET)
  direction = validateinput_LR(input("Do you wish to take the [L]eft or [R]ight path? ")).upper()
  if direction == "L":
    print ("You take the left path.\n")
  elif direction == "R":
    print ("You take the right path.\n")
  return direction
def fork_in_road_left_or_right_or_straight():
  print (Fore.BLUE + "\nThe path forks before you."+ Fore.RESET)
  direction = validateinput_LRS(input("""Do you wish to take the [L]eft, [R]ight, or [S]traight path? """)).upper()
  if direction == "L":
    print ("You take the left path.\n")
  elif direction == "R":
    print ("You take the right path.\n")
  elif direction == "S":
    print ("You take the straight path.\n")
  return direction
  
 ############ Commentary ########################

def user_path_commentary(choose_name): 
  path1 =(Fore.GREEN + Back.BLACK +"""
 You hear the rustle of bushes and the snapping of twigs…. Is 
 there… something in here
 with you?\n """ +Fore.RESET + Back.RESET)
  
  path2 = (Fore.GREEN + Back.BLACK +"""
 The shadows encroach upon you as you make your way down the path… 
 its like they're trying to consume you…\n """+Fore.RESET + 
 Back.RESET)

  path3 = (Fore.GREEN + Back.BLACK +"""
 The crunch of gravel behinds you startles you into turning, but 
 you find no one\n behind you. You turn and continue walking but 
 you hear the crunch of gravel again. 
 You don't dare to turn around.
 \n"""+Fore.RESET + Back.RESET)
  
  path4 = (Fore.GREEN + Back.BLACK +f"""
 You come across a small cemetery. An entire cemetery inside the 
 maze? As you make 
 your way through, you pause at the only open grave and stare at 
 the tombstone. 
 It says...Here lies {choose_name}\n"""+Fore.RESET + Back.RESET)
 

  path5 = (Fore.GREEN + Back.BLACK +"""
 The maze seems to be alive at the prospect of prey inside of it. 
 The shrubs that\n construct the walls shimmer in an imaginary wind 
 as you make your way down the path.\n"""+Fore.RESET + Back.RESET)

  path6 = (Fore.GREEN + Back.BLACK + """
 You come across a small cemetery. An entire cemetery inside the 
 maze? As you make 
 your way through, you pause at the only open grave and stare at 
 the tombstone. 
 It says...Here lies... who the hell is Kerbar?\n"""+Fore.RESET + 
 Back.RESET)
  
  pathlist = [path1, path2, path3, path4, path5, path6]

  commentary = random.choice(pathlist)
  return print(commentary)

def monster_commentary(monster:Boss):
    if monster.name == "Werewolf":
      print(Fore.CYAN + Back.BLACK +"The sound of howling in the distance… that wasn't the wind….\n"+ Fore.RESET + Back.RESET)
    elif monster.name == "Killer Clown":
      print(Back. WHITE + Fore.RED +"""
You take a step, only to find your foot stuck to something. You yank at your leg, eventually managing to pull yourself free. You stare at the thin, silk-like threads that formed a web of some sort. Is that… cotton candy? \n""" + Back.RESET + Fore.RESET)
    elif monster.name == "Witch":
      print(Fore.MAGENTA + """
You turn the corner, your foot coming down on something soft and furry. A yowl has you jumping away. The black cat you just stepped on hisses at you before disappearing into the underbrush.
\n""" + Fore.RESET)
    elif monster.name == "Troll":
      print(Back.GREEN + """
You come across broken portions of hedges, like something had crashed through the walls of the maze. You take a step, only to catch yourself as you almost fall face first... into the massive foot-print.\n""" + Back. RESET)
    elif monster.name == "Skeleton":
       print(Back.YELLOW + """
You hear a rattling sound in the distance, like bones striking bone. Just what else is waiting for you in this maze?....\n""" + Back.RESET)     

 ############ Dead End or Boss ##################
def deadend_trap_or_boss(player1: Player, monster: Boss) -> None: 
  traptriggered = False
  trapchance, escapechance, bosschance = random.randint(1, 15), random.randint(1, 7), random.randint(1,15)
  while not traptriggered:
      if trapchance == 1 or trapchance == 7:
          player1.health = 0
          print(Back.RED + Fore.BLACK +"""The floor opens and before the sound of your scream can escape your mouth... it 
gobbles you whole and your adventure ended before it even began.
""" + Back.RESET + Fore.RESET)
          traptriggered = True 
      else:
          if bosschance < escapechance:
              print("You have run into a deadend.")
              tryagain = validate_enter_maze(input("Try again? [Y] or [N] ").upper())
              if tryagain == "Y":
                  print("You backtrack to the entrance in confusion... Where exactly did you get turned around?")
                  traptriggered = True
              else:
                print("You backtrack to the entrance and decide to walk away from the maze.")
                player1.health = 0
                traptriggered = True

          else:
            if monster.boss_health > 0:
              monster_commentary(monster)
              battle_monster(player1,monster)
              if monster.boss_health == 0:
                tryagain = validate_enter_maze(input("Would you like to continue? [Y] or [N] ").upper())
                if tryagain == "Y":
                  print("You backtrack to the entrance in confusion... Where exactly did you get turned around?")
                  traptriggered = True
                else:
                  print("You backtrack to the entrance and decide to walk away from the maze.")
                  traptriggered = True
                  player1.health = 0
              elif player1.health == 0: 
                traptriggered = True
            else:
              print (f"You've stumbled upon the carcass of the {monster.name}. Have you been this way already?")
              tryagain = validate_enter_maze(input("Try again? [Y] or [N] ").upper())
              if tryagain == "Y":
                print("You backtrack to the entrance in confusion... Where exactly did you get turned around?")
                traptriggered = True
              else:
                print("You backtrack to the entrance and decide to walk away from the maze.")
                traptriggered = True
                player1.health = 0

 ######################### Player Paths'##########################

 #############Bailey's Path###########
def North_path(player1):
  while player1.health > 0:
    user_path_commentary(choose_name)
    user_input = fork_in_road_left_or_right()
    if user_input == "L":
      deadend_trap_or_boss(player1, monster)
    elif user_input == "R":
      user_path_commentary(choose_name)
      pick_up_item(player1)
      user_input = fork_in_road_left_or_right_or_straight()
      if user_input == "R" or user_input == "L":
        user_path_commentary(choose_name)
        deadend_trap_or_boss(player1, monster)
      elif user_input == "S":
        user_path_commentary(choose_name)
        user_input = fork_in_road_left_or_right()
        if user_input == "R":
          user_path_commentary(choose_name)
          deadend_trap_or_boss(player1, monster)
        elif user_input == "L":
          user_path_commentary(choose_name)   
          
          user_input = fork_in_road_left_or_right()
          if user_input == "R":
            user_path_commentary(choose_name)
            deadend_trap_or_boss(player1, monster)
          elif user_input == "L":
            user_path_commentary(choose_name)
            print(Back.CYAN +"""
You’ve made it, through monsters and horror and shadows that reach for you like starving vagrants, to the center of the maze. You’d almost forgotten what awaited you: Eternal Youth. You find yourself amid a garden of statues, 
searching desperately for the prize you’d been promised. The sound of scraping stone has you spinning, only to find the statue behind you suddenly very close, arms out-stretched as if to cradle your face. You take a step back only 
to hear more scraping behind you. Another statue has moved, this time its face twisted in malice as it reaches for you.You quickly back away, keeping both statues in your sight. This maze, this god-forsaken maze!
You freeze, feeling stone hands surround your throat-""" )
            print("""\nAmid the statues in the center of the maze, rests a new angel. Their hands hold theirface as they scream in horror, frozen in time. They are but one in a long line of 
victims. And now, they await the next; Hungry. Frozen. Eternal""")
            player1.health = 0 
        
 ######## Briana's Path ###########
# 2 forks, 3 dead ends
def West_path(player1):
  while player1.health >0:
    user_path_commentary(choose_name)
    action = fork_in_road_left_or_right()
    if action == "L":
      print( "You have fallen to your death")
      player1.health = 0 
    elif action == "R":
      user_path_commentary(choose_name)
      action = fork_in_road_right_or_straight()
      if action == "S":
        # monster_commentary(witch)
        deadend_trap_or_boss(player1,monster)
      elif action == "R":
        user_path_commentary(choose_name)
        # monster_commentary(clown)
        deadend_trap_or_boss(player1,monster)
      
 ############ KERA'S PATH##############
def South_path(player1):  
  user_path_commentary(choose_name)
  while player1.health > 0:
    user_input = fork_in_road_left_or_right_or_straight()
    if user_input == "L":
      user_path_commentary(choose_name)
      pick_up_item(player1)
      user_input = fork_in_road_left_or_straight()
      if user_input == "L":
        deadend_trap_or_boss(player1, monster)
      elif user_input == "S":
        user_input = fork_in_road_left_or_right()
        pick_up_item(player1)
        if user_input == "S" or user_input == "L":
          deadend_trap_or_boss(player1, monster)
    elif user_input == "R":
      deadend_trap_or_boss(player1, monster)
    elif user_input == "S":
      user_path_commentary(choose_name)
      pick_up_item(player1)
      user_input = fork_in_road_left_or_right()
      if user_input == "R":
        deadend_trap_or_boss(player1,monster)
      elif user_input == "L":
        user_path_commentary(choose_name)
        user_input= fork_in_road_left_or_right()
        if user_input == "R":
          deadend_trap_or_boss(player1, monster)
        elif user_input == "L":
            print(Back.CYAN +"""
You’ve made it, through monsters and horror and shadows that reach for you like starving vagrants, to the center of the maze. You’d almost forgotten what awaited you: Eternal Youth. You find yourself amid a garden of statues, 
searching desperately for the prize you’d been promised. The sound of scraping stone has you spinning, only to find the statue behind you suddenly very close, arms out-stretched as if to cradle your face. You take a step back only 
to hear more scraping behind you. Another statue has moved, this time its face twisted in malice as it reaches for you.You quickly back away, keeping both statues in your sight. This maze, this god-forsaken maze!
You freeze, feeling stone hands surround your throat-""" )
            print("""\nAmid the statues in the center of the maze, rests a new angel. Their hands hold theirface as they scream in horror, frozen in time. They are but one in a long line of 
victims. And now, they await the next; Hungry. Frozen. Eternal""")
            player1.health = 0 
  
 ############ Kariel'S PATH##############
def East_path(player1):
  while player1.health > 0:
      choice = fork_in_road_left_or_right_or_straight()
      if choice == "L":
        user_path_commentary(choose_name)
        deadend_trap_or_boss(player1, monster)
        break
      elif choice == "R":
          user_path_commentary(choose_name)
          pick_up_item(player1)
          choice = fork_in_road_right_or_straight()
          if choice == "S":
            user_path_commentary(choose_name)
            deadend_trap_or_boss(player1, monster)
          elif choice == "R":
            user_path_commentary(choose_name)
            pick_up_item(player1)
            choice = fork_in_road_right_or_straight()
            if choice == "S":
              user_path_commentary(choose_name)
              deadend_trap_or_boss(player1, monster)
            elif choice == "R":
              user_path_commentary(choose_name)
              choice = fork_in_road_left_or_straight()
              if choice == "S":
                user_path_commentary(choose_name)
                deadend_trap_or_boss(player1, monster)
              elif choice == "L":
                user_path_commentary(choose_name)
                choice = fork_in_road_left_or_straight()
                if choice == "L":
                  user_path_commentary(choose_name)
                  deadend_trap_or_boss(player1, monster)
                else:
                  user_path_commentary(choose_name)
                  choice = fork_in_road_left_or_straight()
                  if choice == "L" or choice == "S":
                    user_path_commentary(choose_name)
                    deadend_trap_or_boss(player1, monster) 
      else:
        user_path_commentary(choose_name)
        pick_up_item(player1)
        choice = fork_in_road_left_or_straight()
        if choice == "L":
          user_path_commentary(choose_name)
          deadend_trap_or_boss(player1, monster)
        elif choice == "S":
          user_path_commentary(choose_name)
          choice = fork_in_road_left_or_straight()
          if choice == "L":
            user_path_commentary(choose_name)
            deadend_trap_or_boss(player1, monster)
          elif choice == "S":
            user_path_commentary(choose_name)
            choice = fork_in_road_left_or_straight()
            if choice == "L" or choice == "S":
              user_path_commentary(choose_name)
              deadend_trap_or_boss(player1, monster)



 ############################ MAIN ##############################
choose_name = input("What is your name? ")
def main() -> None:
  player1 = Player(100, False, False, False, False,False)

  while player1.health > 0:
    print( """
You stand in front of a towering, ghastly maze.\nWho knows what horrors await inside...
""")
    user_input=validate_enter_maze(input("Do you wish to enter? [Y] or [N]? ")).upper()
    if user_input == "Y":
      print("There are 4 paths.")
      user_path = validate_path_choice(input("Which do you choose: [N]orth, [E]ast, [S]outh, or [W]est? ")).upper()
      if user_path == "N":
        North_path(player1)
      elif user_path == "E":
        East_path(player1)
      elif user_path == "W":
        West_path(player1)
      elif user_path =="S":
        South_path(player1)
    else:
      print("You walk away from the maze")

  

if __name__ == "__main__":
  main()