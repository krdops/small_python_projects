

#initialze data to be stored in files, pickels and shelves


#records

bob = {'name': 'Bob Smitty', 'age': 32, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Sue Sue', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom',         'age': 50, 'pay': 50000, 'job': None}


db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


if __name__ == '__main__':

    for key in db:
        print(key, '=>\n ', db[key]['pay'])

    for key in db:
        print(db[key]['name'].split()[-1])
        db[key]['pay'] *= 1.10

    for record in db.values():

        print(record['pay'])


    x = [db[key]['name'] for key in db]
    print(x)
    db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
    print(db['tom'])

    print(db['tom']['name'])

    list(db.keys())

    len(db)

    print([rec['age'] for rec in db.values()])

    print([rec['name'] for rec in db.values() if rec['age'] >= 45])
    
    
          
            
