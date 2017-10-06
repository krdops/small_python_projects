

cont = "yes";

while cont == "yes":

  user = input('Create username: ')
  password = input('Create Password: ')
  store_user = []
  store_pass = []
  dbdict = {}
  if user in store_user:
    print("USER EXISTS")
    

  elif user not in store_user:

    store_user.append(user)
    store_pass.append(password)
    
    for i in store_user:
        dbdict[i] = password
        
        
    #dbdict[user] = password
    print("CREATED SUCCESSFULLY")
    y =  input("Add another? (y/n): ")
    if y == "y":
      cont = "yes"
    elif y == "n":
      cont = "no"
    else:
      pass

  else:
    pass


  what_is = input("Want to see user/pass? (y/n)")
  if what_is == "y":
    print(dbdict)
  else:
    pass








