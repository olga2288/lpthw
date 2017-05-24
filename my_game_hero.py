# -*- coding: utf-8 -*-
from sys import exit
from random import randint

class GameHero(object):

    def __init__(self):
        self.game_keys = {}
        self.game_stones = {}

    def hero_prize(self, room, game_key, game_prize):
        self.game_keys[room] = game_key
        self.game_stones[room] = game_prize
