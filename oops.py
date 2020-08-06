#class PlayerCharacter:
  #membership = True
  #def __init__(self,name = 'hello',age = 55):
#    if(self.membership):
#      self.name = name#attribute
#      self.age = age
#  def run(self):
#   print('run')

#player1 = PlayerCharacter()
#player2 = PlayerCharacter()
#player2.attack = 50

#print(player1.run())
#print(player1.membership)
#print(player1.age)
#print(player2.attack)
#print(player2.run())
#print(player2.age)

class user:
    def sign_in(self):
        print('logged in')

class wizard(user):
  def __init__(self,name,power):
      self.name = name
      self.power = power
  def attack(self):
   print(f'attacking with power of {self.power}')

class archer(user):
     def __init__(self,name,num_arrows):
         self.name = name
         self.num_arrows = num_arrows
     def attack(self):
      print(f'attacking with arrows of {self.num_arrows}')

wizard1 = wizard('merlin',50)
archer1 = archer('robin',100)
print(wizard1.sign_in())
wizard1.attack()
archer1.attack()

class Toy():
    def __init__(self,colour,age):
        self.colour = colour
        self.age = age
        self.my_dict ={
          'name':'yoyo',
          'has_pets':False
        }
    def __str__(self):
        return f'{self.colour}'
    def __len__(self):
        return 5
    def __getitem__(self,i):
        return self.my_dict[i]

action_figure = Toy('red',0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure['name'])
