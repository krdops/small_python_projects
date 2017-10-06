from shelveruner import loadDbbase, storeDbase


db = loadDbbase()

db['sue']['pay'] *= 1.10

db['tom']['name'] = 'Tom Tom'
storeDbase(db)

