from __future__ import print_function
import random
import time
import sys



print ("Greetings, adventurer! We welcome you to this fantasy land of wonder filled with legacies of courage, wisdom, and power. But among XXXXXXXXXX")
name = raw_input('"What is your title?" | ')
print ("A strong name. You will require a weapon of similar caliber to match. Come this way.")
print ('You follow XXXXXXXX and before you are XXXXXXXXX')
weapon_choice = input('1 - Blade | 2 - Shield | 3 - Staff | ')
if weapon_choice == 1:
    print ('cool magic destiny stuff blade blah blah blah XXXXXX')
elif weapon_choice == 2:
    print ('cool magic destiny stuff shield blah blah blah XXXXXX')
elif weapon_choice == 3:
    print ('cool magic destiny stuff staff blah blah blah XXXXXX')
if weapon_choice == 1 or 2 or 3:
    print ('you have zone choices XXXXXX')
    zone_choice = input('1 - Forest | 2 - Castle Ruins | ')
    if zone_choice == 1:
        print ('You walk into the forest XXXXXXXX')
        print ('You come upon a fork in the root-ridden path of the forest ground. On the left, the path is strewn with many rocks and twigs and other trip hazards, but the broken trees allow for more sunlight to shine through.')
        print ('Alternatively, the path to your right carries less objects to trip on and appears neater. But, your vision capabilities are at the mercy of the full, thick layers of leaves hanging overhead.')
        print ('You choose to take the path on the left. You walk down the left XXXXXX')
        print ('But before you get far, you hear faintly the sound of a wolf howling somewhere deep in the forest of mostly-dead trees and rotten shrubs.')
        print ('You tighten your grip on the sword, hurry your pace, and hope to avoid having a dangerous encounter with a fabled lone DIRE WOLF.')
        print ('And before long, you hear a brushing in the rotten leaves of the vegetation, and much to your terror a DIRE WOLF approaches you from the bushes.')
        print ('But you catch yourself and remember: You are the BLADE. Courage and bravery. You fearlessly approach the DIRE WOLF and begin combat.')
        print ('(To fight, type "fight1()")')
        def fight1():
            fdmg1 = int(random.randint(1,6))
            edmg1 = int(random.randint(1,2))
            time.sleep(1)
            if edmg1 > fdmg1:
                print ('Poor adventurer, how unlucky. You trip, and the DIRE WOLF jumps on top of you and you never manage to overpower it.')
                print ('The DIRE WOLF defeats you.')
                print ('Maybe next time, brave adventurer.')
            elif edmg1 < fdmg1 or edmg == fdmg:
                    print ('The DIRE WOLF leaps out at you after a few seconds of deadly silence, but you dodge it at just the right moment and thrust your blade into its side, inflicting a mortal wound, forever silencing the beast.')
                    print ('You slay the DIRE WOLF.')
                    print ('You continue your journey meet the bear blah blah XXXXXXXXXX')
                    print ('Fight bear blah blah XXXXXXXXXXXX')
                    print ('(To fight, type "fight2()")')
        def fight2():
                fdmg1 = int(random.randint(2,8))
                edmg1 = int(random.randint(1,4))
                time.sleep(1)
                if edmg1 > fdmg1:
                    print ('XXXXXXXXX.')
                    print ('The RABID BEAR defeats you.')
                    print ('Maybe next time, brave adventurer.')
                elif edmg1 < fdmg1 or edmg == fdmg:
                    print ('The RABID BEAR XXXXXXXXX.')
                    print ('You slay the RABID BEAR.')
                    print ('You keep walking in forest blah blah XXXXXX')
                    print ('Theres a troll lol guess a number XXXXX')
                    print ('(To guess a number, type "guess()")')
        def guess():
                print('"guess a number XXXXX"')
                number = random.randint(1,10)
                guess = int(raw_input())
                tries = 1
                while guess != number and tries < 3:
                    tries += 0
                    if guess<number:
                        print('"', guess, 'is too low, stupid, guess again."')
                        print ('"You have ', 3 - tries, ' more tries, human."')
                    else:
                        print('"', guess, 'is too high, idiot, guess again."')
                    guess = int(raw_input())
                if guess == number:
                    print ("UGHHHHHHHHHHHHHHH NOW I CAN'T EAT YOU. GO AHEAD.")
                    print ('You go and find the dragon XXXXXXX')
                    print ('UwU you found dargon')
                    print ('Fancy dragon introduction XXXXXX')
                    print ('(To fight, type "fight3()")')
        def fight3():
                fdmg1 = int(random.randint(2,8))
                edmg1 = int(random.randint(1,4))
                time.sleep(1)
                if edmg1 > fdmg1:
                    print ('XXXXXXXXX.')
                    print ('The DRAGON defeats you.')
                    print ('Maybe next time, brave adventurer. Or maybe not. Take a break if this is, like, your fourth try.')
                elif edmg1 < fdmg1 or edmg == fdmg:
                    print ('The DRAGON XXXXXXXXX.')
                    print ('You slay the DRAGON XXXXXX.')
                    print ('YAAAAAAAAAAAAAAAAAAAY XXXXXX')
                    print ('You have shown courage and bravery and whatever.')
                    
    if zone_choice ==2:
        print ('you walk to a castle blah blah XXXXX')
        print ('put other stuff here too XXXXX')
        print ('(type "fight1a()")')
        def fight1a():
             fdmg1 = int(random.randint(2,8))
             edmg1 = int(random.randint(1,4))
             time.sleep(1)
             if edmg1 > fdmg1:
                print ('XXXXXXXXX.')
                print ('The ASH ZOMBIE defeats you.')
                print ('Maybe next time, brave adventurer.')
             elif edmg1 < fdmg1 or edmg == fdmg:
                 print ('The ASH ZOMBIE XXXXXXXXX.')
                 print ('You slay the ASH ZOMBIE XXXXXX.')
                 print ('You continue your journey meet the bear blah blah XXXXXXXXXX')
                 print ('Fight bear blah blah XXXXXXXXXXXX')
                 print ('(To fight, type "fight2a()")')
        def fight2a():
                fdmg1 = int(random.randint(2,8))
                edmg1 = int(random.randint(1,4))
                time.sleep(1)
                if edmg1 > fdmg1:
                    print ('XXXXXXXXX.')
                    print ('The GHOUL defeats you.')
                    print ('Maybe next time, brave adventurer.')
                elif edmg1 < fdmg1 or edmg == fdmg:
                    print ('The GHOUL XXXXXXXXX.')
                    print ('You slay the GHOUL.')
                    print ('You keep walking in forest blah blah XXXXXX')
                    print ('Theres a troll lol guess a number XXXXX')
                    print ('(To guess a number, type "guess2()")')
        def guess2():
                print('"guess a number XXXXX"')
                number = random.randint(1,10)
                guess = int(raw_input())
                tries = 0
                while guess != number and tries < 3:
                    tries += 1
                    if guess<number:
                        print('"', guess, 'is too low, stupid, guess again."')
                        print ('"You have', 3 - tries, 'more tries, human."')
                    else:
                        print('"', guess, 'is too high, idiot, guess again."')
                    guess = int(raw_input())
                if guess == number:
                    print ("UGHHHHHHHHHHHHHHH NOW I CAN'T EAT YOU. GO AHEAD.")
                    print ('You go and find the adventurer XXXXXXX')
                    print ('UwU you found dargon')
                    print ('Fancy dragon introduction XXXXXX')
                    print ('(To fight, type "fight3a()")')
        def fight3a():
                fdmg1 = int(random.randint(2,8))
                edmg1 = int(random.randint(1,4))
                time.sleep(1)
                if edmg1 > fdmg1:
                    print ('XXXXXXXXX.')
                    print ('The ORC BARBARIAN defeats you and the other adventurer XXXXXXX.')
                    print ('Maybe next time, brave adventurer. Or maybe not. Take a break if this is, like, your fourth try.')
                elif edmg1 < fdmg1 or edmg == fdmg:
                    print ('The ORC BARBARIAN XXXXXXXXX.')
                    print ('You slay the ORC BARBARIAN XXXXXX.')
                    print ('YAAAAAAAAAAAAAAAAAAAY XXXXXX')
                    print ('You have shown courage and bravery and whatever.')