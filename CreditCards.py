


def credit(cardnumber):
    x = []
    str1 = ""
    for i in range(0, len(cardnumber[:-4])):
        x.append('*')
    
    for i in cardnumber[-4:]:
        x.append(i)

    return (str1.join(x))  

c = '1893040322346'


print(credit(c))


    
