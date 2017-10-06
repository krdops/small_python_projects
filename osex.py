import os, sys



contents = os.listdir(".") # contents of current dir


files = []
directory = []

for i in contents:

  if os.path.isfile(i) == True:
       files.append(i)
  elif os.path.isdir(i) == True:
       directory.append(i)
  
#printing contents

for j in files:

    choice = input("Do you want to print file %s (y/n): " %j)
    if choice == 'y':

        print("***************************")
        print("Printing Files %s" %j)
        print("***************************")
        #fileobj = open(j, 'r')
        #contents = fileobj.readlines()
        #for k in contents:
            #sys.stderr.write(k)

    elif(choice == 'quit'):
        sys.exit()

    else: 
         pass

        
