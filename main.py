class Hero:
  def __init__(self, name, live, mana):
    self.name = name
    self.live = live
    self.mana = mana

class Human(Hero):
  def say_man(self):
    print('I"m Human!')

class Orc(Hero):
  def say_orc(self):
    print('I"m Orc!')



if __name__ == "__main__":


  man = Human('Миша', 100, 50)

  orc = Orc('Вася', 120, 70)

  print(man.name, man.live, man.mana)

  print(orc.name, orc.live, orc.mana)

  man.say_man()

  orc.say_orc()

