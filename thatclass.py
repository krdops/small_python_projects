

class Dog(object):



    def override(self):


         self.x = 5



class smallDog(Dog):



    def override(self):

        print("YES")
        super(smallDog, self).override()
        print(self.x)




y = Dog()

y.override()
z = smallDog()

z.override()
