'''Implement a class called player that represents a cricker player.The player class should have a
methods called play() which prints "The player is playing criket.Derive two classes, Batsman and
Bowler,from the player class. Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling" respectively. Write a program to create objects of both the
Batsman and bowler classes and call the play() method for each object.'''


# Define the base class player
class player:
  def play(self):
      print("The player is playing cricket.")

# Define the derived class Batsman
class batsman(player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class Bowler
class bowler(player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = batsman()
bowler = bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
