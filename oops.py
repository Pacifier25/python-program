class PlayerCharacter:
  def __init__(self,name):
    self.name = name

  def run(self):
   print('run')

player1 = PlayerCharacter('Piyush')
player2 = PlayerCharacter('messi')
player1.attack = 50

print(player1.run())
print(player1.attack)
print(player2.run())
