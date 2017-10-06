
from math import *
from random import *



class someclass():


    
  def func():


    print ("Hello Bobby we know all about you...")
    x = 1

    if x == 1:
      print("You've entered the dead zone")
      print("Which weapon do you want?: Axe, Sword, Dagger")
      r = input("Enter your weapon...")
      if r == "Dagger":
        print("You kill the evil zombies with the dagger!")
        someclass.otherclass()
      elif r == "Sword":
        print("You die cause your sword isn't sharp...")
      elif r == "Axe":
        print("The axe cuts through the evil chicken creatures, all named John")



    print("John roundhouse kicks sensi in the face...")
    print("JOHN!!!!!")
    print("SMOKES CRACK")



  def otherclass():

    print("Welcome...to the undead world...")


    r = randint(1, 5)
    if r == 2:
      print("You will never leave")
    if r == 3:
      print("You are JOHNS SON")
    if r == 4:
      print("JOHN BE GONE!")
    if r == 1:
      print("JOHNN!!!!")



someclass.func()

    


