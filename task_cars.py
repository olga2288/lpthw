
class Car(object):
    def __init__(self, mark, colour, speed_max, speed_up):
        self.mark = mark
        self.colour = colour
        self.speed_max = speed_max
        self.speed_up = speed_up

    def distance(self, t_max):
        t_sec = 1
        dis = 0.0
        speed = 0
        while t_sec <= t_max:
            print "t %d, dis %f, speed %d" % (t_sec, dis, speed)
            if speed < self.speed_max:
                mean_speed = (speed + (speed +self.speed_up)) / 2
                dis = dis + (mean_speed *1000)/3600.0
            else:
                dis = dis + (self.speed_max * 1000)/3600.0

            speed += self.speed_up
            print "t %d, dis %f, speed %d" % (t_sec, dis, speed)
            print "Next sec"
            t_sec += 1
        return dis

    def time_race(self, dist):
        t_sec = 1
        dist_min = 0
        speed = 0
        while dist_min < dist:
            print "t %d, dis %f, speed %d" % (t_sec, dist_min, speed)
            if speed < self.speed_max:
                mean_speed = (speed + (speed +self.speed_up)) / 2
                dist_min += (mean_speed *1000)/3600.0
            else:
                dist_min += (self.speed_max * 1000)/3600.0

            speed += self.speed_up
            print "t %d, dis %f, dist_min %f, speed %d" % (t_sec, dist, dist_min, speed)
            print "Next sec"
            t_sec += 1
        return t_sec

class Race(object):
    def __init__(self, time, dist):
        self.cars = []
        self.diss = []
        self.times = []
        self.time = time
        self.dist = dist

    def add_car(self, car):
        self.cars.append(car)

    def print_result(self):
            for i in range(0, len(self.cars)):
                car = self.cars[i]
                dis = self.diss[i]
                print " \n Car: %s  colour: %s " % (car.mark, car.colour),
                print " speed = %d    distance = %f meters" % (car.speed_max, dis)

class DistanceRace(Race):
    def run_race(self):
        for car in self.cars:
            dis = car.distance(self.dist)
            self.times.append(t_sec)


class TimeRace(Race):
    def run_race(self):
        for car in self.cars:
            dis = car.distance(self.time)
            self.diss.append(dis)

print "Which race do you want: 1 - distance race, 2- time race? "
choice = raw_input('> ')
if choice == '1':
    race = DistanceRace(0, 1000)
else:
    race = TimeRace(10, 0)

race.add_car(Car('bmv', 'green', 180, 20))
race.add_car(Car('vw', 'blue', 160, 30))
race.add_car(Car('au', 'white', 170, 25))

race.run_race()
race.print_result()
