from collections import Counter







f = 'facebook'


z = 'faceafbfacceeebkkbokeefkccbo, ffoekk'
z = z.replace(',','')
z = z.replace(' ', '')





counter = dict(Counter(z))


print(counter)

tempv = min(counter.values())
tempc = counter['o'] // 2


templ = [k for k in counter if counter[k] == tempv]


if tempv >= counter['o']:

    print(counter['o'] // 2)


if (tempv % 2) == 0 and (tempv+tempc) == counter['o']:

    print(tempv)

elif counter['o'] == tempv and (tempv % 2) == 0:

    print(tempv 
    print(tempv)

    

    
