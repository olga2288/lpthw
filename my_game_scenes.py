# -*- coding: utf-8 -*-
from sys import exit
from random import randint

class Scene(object):
    def enter(self, hero):
        print ' This scene is not yet conficured. '
        exit(1)

class GameLoss(Scene):
    consolation = [
    "You can try once again",
    "You are loser!!! Try once again!",
    "Don't go away!  Try once again!",
    "Goodbye!!! See you soon!"
    ]
    def enter(self, hero):
        print GameLoss.consolation[randint(0, len(self.consolation)-1)]
        exit(1)

class Corridor(Scene):

    def enter(self, hero):
        print "\nYou have to visit some rooms and find three keys and some atributes."
        print "You have to bring the atributes to library to get prize and win the game."
        print "You stand in front of first foom. Come on!"
        return 'room_1'

class Room1(Scene):

    def enter(self, hero):
        print "\nFind a key of second room and find semiprecious stone in this room."
        print "You go to: 1. window; 2. wardrobe; 3. other"
        a = raw_input("> ")
        if a == '1':
            print "Your choice isn't right. Look for things..."
            return 'room_1'
        elif a == '2':
            print "You get second key and semiprecious stone #1"
            #hero =
            room = 2
            game_key = "key 2"
            game_prize = 'opal'
            hero.hero_prize(room, game_key, game_prize)
            return "room_2"
        else:
            return 'game_loss'

class Room2(Scene):
    def enter(self, hero):
        print "You need to find a key of third room and find semiprecious stone in this room."
        print "You go to: 1.shelf ; 2. wardrobe; 3. other"
        a = raw_input("> ")
        if a == '1':
            print "Your choice isn't right. Look for things..."
            return 'room_2'
        elif a == '2':
            print "You get second key and semiprecious stone #2"
            #hero =
            room = 3
            game_key = "key 3"
            game_prize = 'coral'
            hero.hero_prize(room, game_key, game_prize)
            return "room_3"
        else:
            return 'game_loss'

class Room3(Scene):
    def enter(self, hero):
        print "You need to find a key of fourth room and find semiprecious stone in this room."
        print "You go to: 1. window; 2. shelf; 3. other"
        a = raw_input("> ")
        if a == '1':
            print "Your choice isn't right. Look for things..."
            return 'room_3'
        elif a == '2':
            print "You get second key and semiprecious stone #2"
            #hero =
            room = 4
            game_key = "key 4"
            game_prize = 'amber'
            hero.hero_prize(room, game_key, game_prize)
            return 'game_library'
        else:
            return 'game_loss'

class GameLibrary(Scene):

    def enter(self, hero):
        a = len(hero.game_keys.keys())
        b = len(hero.game_stones.keys())
        if a == 3 and b == 3:
            print "You have won!!!"
            print " you get prize!!!"
            return 'finished'
        else:
            return 'game_loss'

class Finished(Scene):

    def enter(self, hero):
        print "\nyou colleced keys:",
        print hero.game_keys.values()
        print "\nyou colleced stones:",
        print hero.game_stones.values()
        print "You have won!!!"
        return 'finished'
