class Robot:
    """表示有一个带有名字的机器人"""
    # 一个类变量，用来计数机器人的书来数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initialization {})".format(self.name))

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destoryed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("there are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候

        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

    def xx(self):
        pass

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

print(Robot.xx.__doc__)