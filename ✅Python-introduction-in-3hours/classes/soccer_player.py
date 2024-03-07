class Player:
    def __init__(self, name, age, team, injured):
        self.name = name
        self.age = age
        self.team = team
        self.injured = injured

    def get_status(self):
        print(self.name + ': ' + str(self.age) + "\n Injured: " + str(self.injured))