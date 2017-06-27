
class Car(object):
    def __init__(self, mark, colour, speed_max, speed_up):
        self.mark = mark
        self.colour = colour
        self.speed_max = speed_max
        self.speed_up = speed_up

    def distance(self, t_max):
        """ calculates distance car goes for t_max seconds
        Args: t_max - seconds
        Returns: meters
        """
        t_sec = 1
        dis = 0.0
        speed = 0
        while t_sec <= t_max:
            print "t %d, dis %f, speed %d" % (t_sec, dis, speed)
            end_speed = speed + self.speed_up
            if end_speed > self.speed_max:
                end_speed = self.speed_max
            mean_speed = (speed + end_speed) / 2
            dis = dis + (mean_speed *1000)/3600.0
            speed = end_speed
            print "t %d, dis %f, speed %d" % (t_sec, dis, speed)
            print "Next sec"
            t_sec += 1
        return dis

class Race(object):
    def __init__(self, time):
        self.cars = []
        self.diss = []
        self.time = time

    def add_car(self, car):
        self.cars.append(car)

    def run_race(self):
        for car in self.cars:
            dis = car.distance(self.time)
            self.diss.append(dis)

    def print_result(self):
            for i in range(0, len(self.cars)):
                car = self.cars[i]
                dis = self.diss[i]
                print " \n Car: %s  colour: %s " % (car.mark, car.colour),
                print " speed = %d    distance = %f meters" % (car.speed_max, dis)



race = Race(10)

#race.add_car(Car('bmv', 'green', 180, 20))
race.add_car(Car('vw', 'blue', 160, 30))
#race.add_car(Car('au', 'white', 170, 25))

race.run_race()
race.print_result()
