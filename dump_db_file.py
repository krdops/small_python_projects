from shelveruner import loadDbbase

db = loadDbbase()

for key in db:
  print(key, '=>\n ', db[key])

print(db['sue']['name'])

