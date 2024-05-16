import sys

def Play():
    print("TYPE PLAY TO BEGIN")
    if Prompt() == "PLAY":
        Start() 
    else:
        print("Type Play")
        Play()
    
def Start():
    print("\n")
    print("Welcome To Ty and Nick's Temple of Doom!")
    print("To see what commands you can do or how to play type HELP")
    print("Collect 2 aritfacts as you explore to unlock the door and win!")
    print("You have 3 lives, be careful and learn from your mistakes.")
    print("\n . . . \n")
    print("As you walk down the ancient stone steps into the temple you notice that no one has been here for more than a thousand years")
    print("Battered tapestries hang from the ceiling their bright red color lost to time and heiroglyphs are written across the wall telling stories of a civilization long past. \n")
    print("Remember to type in CAPS LOCK")
    global gold
    global lives
    global search
    global torch 
    global one_up 
    global climb_gear 
    global map1

    torch = 0
    climb_gear = 0
    search = 0
    gold = 0
    lives = 3
    map1 = 0
    artifacts = 0
    Chamber_of_souls()


def print_map():
    print("\n")
    print("      |_______________WEST________________________")
    print("      |                                         |")
    print("      |                                         |")
    print("      |          hallway - puzzle 1             |")
    print("      |           |                             |")
    print("SOUTH Entrance - throne - end room              | NORTH") 
    print("      |           |                             |")
    print("      |         bedroom                         |")
    print("      |           |                             |")
    print("      |         hallway -- puzzle 2             |")
    print("      |                                         |")
    print("      |                                         |")
    print("      |________________EAST______________________")
    print("\n")

def Prompt():
    x = input('>>>')
    print("\n") 
    if x == "EXIT":
        print("Thanks for Playing!")
        sys.exit()
    return x
  
def countgold(): 
    global gold
    print(f"current gold = {gold}")
    
def countlives(): 
    global lives
    print(f"lives reamaning = {lives}") 

def countartifacts():
    global artifacts
    print(f"artifacts found = {artifacts}")
    
def help():
    print("I see you've found the help menu!\n")
    print("Commands include, HELP, *cough this menu *cough")
    print("Room commands, CLIMB, SEARCH")
    print("Movement commands, NORTH, EAST, WEST, SOUTH, MAP")
    print("To check certain stats type, GOLD, LIVES or ARTIFACTS")
    print("If you want to access the shop go to the Throne room and type SPEAK to rico")
    print("to restart type, RESTART")
    print("to exit type, EXIT \n")
    
global lives 
lives = 3
global Search 
Search = 0 
global artifacts 
artifacts = 0 
global map1
map1 = 0

def cow_level(): 
    global gold
    global lives
    global artifacts
    global torch
    global climb_gear
    global map1
    print("You have found the cow level!")
    print("The room is filled with the stench of cow feces.")
    print("Maybe there is something in the cow feces?")
    command = Prompt()
    
    if command == "SEARCH":
        print("As you trudge through the goop you find a note on a cow, it reads, THERE IS NO COW LEVEL, you smell the awful stench and sense your body mutating, gold rains from the ceiling . . . ")
        print("You gained invincibility and 5000 GOLD!") 
        lives = 1000000000000000 
        gold = 5000
        Chamber_of_souls()
        
    else:
        print("no")    
        cow_level()
        
def Chamber_of_souls():
    global gold 
    global lives 
    global artifacts 
    global torch 
    global climb_gear 
    global map1
    print("You are in the Chamber of souls!")
    print("There are vines that look climbable on the walls and a narrow doorway to the NORTH")
    command = Prompt()
    
    if command == "NORTH":
        print("You make your way into the Throne room, there is a mysterious bag in the corner and 3 doorways one to the East one to the West and one to the North")
        print("You see a skeleton sitting in a stall. Type SPEAK to talk with him ")
        Throne_room()
        
    if command == "BEEEEF":
        cow_level()
        
    elif command == "EAST":
        print("You find a note telling you to try the command BEEEEF")
        Chamber_of_souls()
        
    elif command == "ARTIFACTS":
        countartifacts()
        Chamber_of_souls() 
        
    elif command == "EXIT":
        print("Thanks for playing!")
        
    elif command == "SOUTH":
        print("You ran into a wall! There is a doorway to the North")
        Chamber_of_souls() 
        
    elif command == "WEST":
        print("You ran into a wall! There is a doorway to the North")   
        Chamber_of_souls() 
        
    elif command == "2001GOD":
        print("YOU GAINED 100000000000000000000 gold!")
        print("YOU HAVE ALL ARTIFACTS")
        artifacts = artifacts + 2
        gold += 10000000000000000
        Endroom()
        
    elif command == "CLIMB":
        print("It looks like there is tresure in a outlet high up on the wall. You try to climb but when you get to the top you lose your footing and fall to your death.")
        lives = lives - 1 
        
    if lives == 0:
        print("GAME OVER")
        Start()
        Chamber_of_souls()
        
    elif command == "HELP": 
        help()
        Chamber_of_souls() 
        
    elif command == "MAP":
        if map1 == 1: 
            print_map()
            Chamber_of_souls()
        else:
            print("You need to buy a map")
            Chamber_of_souls()
            
    elif command == "LIVES": 
        countlives()
        Chamber_of_souls() 
        
    elif command == "SEARCH":
        print("You dont find anything here.")
        Chamber_of_souls() 
        
    elif command == "RESTART":
        lives = 3
        gold = 0
        artifacts = 0
        Start()
        
    elif command == "GOLD": 
        countgold()
        Chamber_of_souls() 
        
    else:
        print("Type a command if you need help type HELP")
        Chamber_of_souls()
        

def Throne_room(): 
    global gold
    global Search 
    global lives 
    global artifacts 
    global torch 
    global climb_gear 
    global map1
    print("You are in the Throne room.")
    print("To speak to Rico enter the command SPEAK")
    command = Prompt()
    
    if command == "SOUTH":
        Chamber_of_souls() 
        
    elif command == "EAST":
        print("As you walk through the ornate stone doorway you notice that this room was once a bedroom. A four post bed lies in the corner of the room, a tile lies loose on the ground and an old statue lies to the north")
        print("A small hole in the wall is hidden behind the curtain to the EAST")
        Bedroom()
        
    elif command == "SPEAK":
        print(""">>>HEY YOU! YEA YOU! GUY WITH THE HAT OR WHATEVER! MY FIRST CUSTOMER! YOU CAN BUY COOL ITEMS FROM ME, RICO, TO HELP YOU ON YOUR QUEST FOR GOLD! """)
        print("TYPE SHOP AND CHECK MY STOCK AND BUY WHAT YOU LIKE! NYEH NYEH NYEH")
        Rico()
        
    elif command == "RESTART":
            lives = 3
            gold = 0
            artifacts = 0
            Start()
            
    elif command == "EXIT":
        print("Thanks for playing!")
        
    elif command == "WEST":
        print("You find a hallway lined with vines with several holes in the walls, in front of you lies a door to the west.")
        Hallway1()
        
    elif command == "NORTH":
        print("Through the ruined pillars massive double doors tower above you with three artifact slots")
        print("Find and enter the artifacts to open the door")
        Endroom()
        
    elif command == "ARTIFACTS":
        countartifacts()
        Throne_room()
        
    elif command == "LIVES":
        countlives()
        Throne_room()
        
    elif command == "HELP":
        help()
        Throne_room() 
        
    elif command == "MAP":
        if map1 == 1:
            print_map()
        else:
            print("You need to buy a map")
            Throne_room()
            
    elif command == "SEARCH": 
        if Search == 0:
            print("You found 30 gold coins in a small pouch on the Throne") 
            gold = gold + 30
            Search = Search + 1
            Throne_room()
        else:
            print("You have found everything in this room") 
            Throne_room()

    elif command == "GOLD": 
        countgold()
        Throne_room() 
    else:
        print("Type a command if you need help type HELP") 
        Throne_room()
        
def Hallway1(): 
    global gold
    global Search 
    global lives 
    global artifacts 
    global torch 
    global climb_gear 
    global map1
    print("You are in a hallway") 
    command = Prompt()

    if command == "NORTH":
        print("You ran into a wall!") 
        
    elif command == "EAST":
        print("You make your way back towards the large throne with rico standing next to it")
        Throne_room()
        
    elif command == "WEST":
        print("You ran into a wall")
        Hallway1()
        
    elif command == "SOUTH":
        print("You ran into a wall")
        Hallway1()
        
    elif command == "EXIT":
        print("Thanks for playing!")
        
    elif command == "SEARCH":
        if Search == 0 or Search == 1 or Search == 2:
            print("you climb up the vines to find a treasure chest with 50 gold coins")
            gold = gold + 50
            Search = Search + 1
            Hallway1()
        else:
            print("You already found everything")
            Hallway1()
            
    elif command == "ARTIFACTS": 
        countartifacts()
        Hallway1()
        
    elif command == "LIVES":
        countlives()
        Hallway1()
        
    elif command == "HELP":
        help()
        Hallway1()
        
    elif command == "MAP":
        if map1 == 1:
            print_map()
            Hallway1()
        else:
            print("You need to buy a map")
            Hallway1()

    elif command == "CLIMB": 
        if climb_gear == 1:
            print("You climb your way into a room with a great bridge with a water fall, blocked by a great big door with a strange puzzel engraved on it")
            puzzle1room() 
        else:
            print("looks like you need some advanced climbing gear to get to this room")
            Hallway1()
            
    elif command == "RESTART":
            lives = 3
            gold = 0
            artifacts = 0
            Start()
            
    elif command == "GOLD": 
        countgold()
        Hallway1() 
        
    else:
        print("Type the command HELP if you need help")
        Hallway1()
        
def puzzle1room(): 
    global gold
    global Search 
    global lives 
    global artifacts 
    global torch 
    global climb_gear 
    global map1
    print("You are in a puzzle room")
    print("When you walk to the door blocking the bridge there is a strange puzzle engraved on the door")
    print("You notice a little note next do the door with a 1 on it")
    print("The way back is to the SOUTH")
    print("\sssssssssssssssssssssssss/")
    print("s\sssssssssssssssssssssss/")
    print("ss\sssssssssssssssssssss/s")
    print("sss\sssssssssssssssssss/ss")
    print("ssss\sssssssssssssssss/sss")
    print("ssssss\sssssssssssss/sssss")
    print("ssssssss\sssssssss/sssssss")
    print("ssssssssss\sssss/sssssssss")
    print("ssssssssssss\s/sssssssssss")
    print("What letter is hidden")
    command = Prompt()
    if artifacts == 0:
        if command == "V":
            print("CORRECT!")
            print("The large door slides open with a artifact laying peacefully on a table")
            print("You walk over and pick it up")
            print("the second puzzle room is now open")
            artifacts = artifacts + 1
            Hallway1()
            
        elif command == "LIVES": 
            countlives()
            puzzle1room() 
            
        else:
            print("Thats not correct")
            print("spikes shoot from the walls and impale you!")
            print("You lost a life")
            lives = lives - 1
            if lives == 0:
                print("GAME OVER") 
                lives = 3
                Start()
            puzzle1room() 
            
    elif command == "RESTART":
        lives = 3
        gold = 0
        artifacts = 0
        Start()
    elif command == "EXIT":
        print("Thanks for playing!")
    elif command == "SEARCH":
        print("You find a note stained with blood with the word SUN barely visible")
        print("Just as you pick up the note a toxic gas releases from the ceiling and you die")
        print("You lost a life")
        if lives == 0:
            print("GAME OVER") 
            Start()
        else:
            lives = lives - 1 
            puzzle1room()
        puzzle1room() 
    else:
        print("You have already claimed this artifact") 
        Hallway1()
        
        
def Endroom():
    global artifacts
    print("You are in the Final chamber")
    print("INSERT You artifacts to open the door")
    command = Prompt()
    if command == "INSERT":
        if artifacts == 2:
            print("You insert 2 artifacts.")
            print("The gigantic doors slide open making a thoundourous noise echo through the entire temple")
            print("As the dust settles you see a heaping pile of treasure coins upon coins stacked on top of each other")
            print("YOU SURVIVED THE TEMPLE")
            print("PROGRAMMERS")
            print("TY WENRICK")
            print("NICK R - F")
            print("DESIGNERS")
            print("TY WENRICK")
            print("NICK R - F")
            print("THANKS FOR PLAYING EXPLORE!!!!!!!!") 
        else:
            print("collect more artifacts to unlock this door")
            Endroom()
    elif command == "SOUTH":
        print("You walk back into the grand Throne room")
        Throne_room()
    elif command == "EXIT":
        print("Thanks for playing!")
    else:
        print("Type the command HELP if you need help")
        print("The way back is south")
        Endroom()
        
        
def Bedroom(): 
    global gold
    global Search 
    global lives 
    global artifacts 
    global torch 
    global climb_gear 
    global map1
    print("You are in the bedroom.")
    command = Prompt()
    if command == "SOUTH":
        print("You ran into a wall!")
        Bedroom()
    elif command == "EAST":
        print("You crawl through a hole in the wall leading to a dark hallway")
        if torch >= 1:
            print("You take out your torch and light your way through the hallway")
            Hallway2() 
        else:
            print("its too dark you need a torch to explore this area")
            Bedroom()
    elif command == "LIVES":
        countlives()
        Bedroom()
    elif command == "ARTIFACTS":
        countartifacts()
        Bedroom()
    elif command == "HELP":
        help()
        Bedroom()
    elif command == "EXIT":
        print("Thanks for playing!") 
    elif command == "NORTH":
        print("You walk towards the Statue, but suddenly it falls on top of you and you die.")
        print("You have been revived!") 
        lives = lives - 1
        if lives == 0:
            print("GAME OVER")
            lives = 3
            Start()
            Bedroom()
    elif command == "MAP":
        if map1 == 1: 
            print_map()
        else:
            print("You need to buy a map") 
            Bedroom()
    elif command == "RESTART":
        lives = 3
        gold = 0
        Start()
    elif command == "CLIMB":
        print("There are no vines on any of the walls to climb. There is a doorway to the west.")
        Bedroom()
    elif command == "WEST":
        print("You go back into the Throne room")
        Throne_room()
    elif command == "SEARCH":
        if Search == 0 or Search == 1:
            print("You found a massive gold coin under a broken tile on the floor") 
            gold = gold + 75
            Search = Search + 1
            Bedroom()
        else:
            print("You have found everything in this room")
            Bedroom()
    elif command == "GOLD": 
        countgold()
        Bedroom() 
    else:
        print("Type a command if you need help type HELP") 
        Bedroom()
        
        
def Hallway2(): 
    global gold
    global Search 
    global lives 
    global artifacts 
    global torch 
    global climb_gear 
    global map1
    print("You are in a Hallway")
    print("The hallway continues to the north") 
    command = Prompt()
    if command == "EAST":
        print("You ran into a wall!")
        Hallway2()
    elif command == "WEST":
        print("You make your way back towards the bedroom")
        Bedroom()
    elif command == "NORTH":
        print("You Walk across a narrow bridge water rushing below you")
        print("Continue north to the shrine")
        puzzle2()
    elif command == "SOUTH":
        print("You ran into a wall!")
        Hallway2()
    elif command == "EXIT":
        print("Thanks for playing!")
    elif command == "SEARCH":
        if Search <= 3:
            print("You found 100 gold! in a small chest in the corner.")
            gold = gold + 100
            Hallway2()
        else:
            print("You have already searched this area") 
            Hallway2()
        Hallway2()
    elif command == "ClIMB":
        print("There is nothing to climb")
        Hallway2()
    elif command == "MAP":
        if map1 == 1: 
            print_map()
        else:
            print("You need to buy a map") 
            Hallway2()
    elif command == "LIVES": 
        countlives()
        Hallway2()
    elif command == "RESTART":
        lives = 3
        gold = 0
        Search = 0
        Start()
    elif command == "ARTIFACTS": 
        countartifacts()
        Hallway2()
    elif command == "GOLD":
        countgold()
        Hallway2() 
    else:
        print("Type a command if you need help type HELP") 
        Hallway2()
        
        
def puzzle2(): 
    global gold
    global torch 
    global lives 
    global climb_gear 
    global map1
    global artifacts
    command = Prompt()
    print("You walk up to a door on a narrow bridge with a river far below, the door has a riddle incribed on it")
    print("The riddle is...")
    print("I cover cities, I make men blind, yet help them see .") 
    if artifacts == 1:
        if command == "SOUTH":
            print("you head back towards the hallway") 
            Hallway2()
        elif command == "NORTH": 
            puzzle2()
        elif command == "LIVES": 
            countlives()
            puzzle2()
        elif command == "MAP":
            if map1 == 1: 
                print_map()
            else:
                print("You need to buy a map") 
                puzzle2()
        elif command == "RESTART": 
            lives = 3
            gold = 0
            Search = 0
            artifacts = 0
            Start()
        elif command == "GOLD": 
            countgold()
            puzzle2()
        elif command == "ARTIFACTS":
            countartifacts()
            puzzle2()
        elif command == "WEST":
            print("You fall into the huge river and hit your head, as you struggle to reach the top of the water you feel your body weeken and your vision goes dark.")
            lives = lives - 1 
            if lives == 0:
                print("GAME OVER")
                lives = 3
                Start()
                puzzle2()

        elif command == "SUN":
            print("CORRECT!!!!")
            print("The door opens and the artifact sits calmly on the table a strange light rippling off it.")
            artifacts = artifacts + 1
            Hallway2()
        else:
            print("Thats wrong the floor disappers from under you and you fall to your death")
            lives = lives - 1 
            if lives == 0:
                print("GAME OVER")
                lives = 3
                Start()
                puzzle2() 
            else:
                print("Collect the first artifact to continue") 
                Hallway2()
                
def Rico(): 
    global gold
    global torch 
    global lives 
    global climb_gear 
    global map1
    print("I used to be an adventurer like you... until i died")
    print("Waddya Buyin")
    print("Items include...")
    print("TORCH - allows you to search dark rooms! 20 gold ")
    print("ONE_UP - gives you another life! 50 gold ")
    print("CLIMB_GEAR - climb more surfaces! 50 gold ")
    print("MAP - uncover the layout of the temple! 70 gold") 
    command = Prompt()
    if command == "TORCH":
        if gold == gold >= 20:
            print("Now you have a Torch")
            print(">>>Thanks for doin buisness pal!") 
            torch = 1
            gold = gold - 20
        else:
            print("You dont have enough gold")
            Throne_room()
    elif command == "ONE_UP":
        if gold == gold >= 50:
            print("You gained a extra life!") 
            print(">>>Thanks for doin buisness!") 
            lives = lives + 1
            gold = gold - 50
        else:
            print("You dont have enough gold")
            Throne_room() 
    elif command == "MAP":
        if gold == gold >= 50:
            print("Now you have a map")
            print("type the command map to see the map") 
            map1 = 1
            gold = gold - 50
        else:
            print("You dont have enough gold")
            Throne_room()
    elif command == "CLIMB_GEAR":
        if gold == gold >= 50:
            print("Now you have climbing gear")
            print(">>>Thanks for doin buisness amigo!")
            climb_gear = 1
            gold = gold - 50
        else:
            print("You dont have enough gold")
            Throne_room()
    elif command == "EXIT":
        print("Thanks for playing!")
    else:
        Throne_room()
        
        
    

if __name__ =='__main__':
    Play()