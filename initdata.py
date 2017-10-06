#records

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 25000, 'job': 'dev2'}
tom = {'name': 'Tomity Tom', 'age': 23, 'pay': 25670, 'job': 'dev3'}




# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


if __name__ == '__main__':

    for key in db:
      print(key, '=>\n ', db[key])

      
