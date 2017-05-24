# -*- coding: utf-8 -*-
from sys import exit
from random import randint

import my_game_scenes
import my_game_hero


class Engine(object):
#сюда присвоился объект класса Map, т.е. загрузилась созданная карта
    def __init__(self, scene_map, hero):
        self.scene_map = scene_map
        self.hero = hero

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            #запускается тукущая сцена на выполнение
            # и возвращает в переменную next_scene_name название след. сцены(ключ от словаря)
            next_scene_name = current_scene.enter(self.hero)
            current_scene = self.scene_map.next_scene(next_scene_name)
        #выполняется последняя сцена
        current_scene.enter(self.hero)


class Map(object):
#создаются сцены карты, создаются объекты: Corridor()...
    scenes = {
    'corridor': my_game_scenes.Corridor(),
    'room_1': my_game_scenes.Room1(),
    'room_2': my_game_scenes.Room2(),
    'room_3': my_game_scenes.Room3(),
    'game_library': my_game_scenes.GameLibrary(),
    'game_loss': my_game_scenes.GameLoss(),
    'finished': my_game_scenes.Finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    #возвращает уже созданный объект из словаря scene по ключу scene_name: scene[scene_name]
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    #возвращает значение 'corridor'
    def opening_scene(self):
        ret = self.next_scene(self.start_scene)
        return ret

a_map = Map('corridor')
a_hero = my_game_hero.GameHero()
a_game = Engine(a_map, a_hero)
a_game.play()
