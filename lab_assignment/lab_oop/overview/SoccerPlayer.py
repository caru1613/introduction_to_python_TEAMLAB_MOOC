class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, new_number):
        print("Change back number from %d to %d" % (self.back_number, new_number))
        self.back_number = new_number
    def __str__(self):
        return "Hello, My name is %s. I play in %s in center. My back number is %d." % (self.name, self.position, self.back_number)
    
jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
print("Current back number:", jinhyun.back_number)
jinhyun.change_back_number(5)
print("Current back number:", jinhyun.back_number)

names = ["Jin", "Sungchul", "Ronaldo", "Hong", "Seo"]
positions = ["MF", "DF", "CF", "WF", "GK"]
numbers = [10, 15, 20, 3, 1]

player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
for players in player_objects:
    print(players)