


def count(string):


    xs = 0
    os = 0


    for i in string:

        if i == 'x':
            xs += 1
        elif i == 'o':
            os += 1
        else:
            print('ufuckedup')
            break
    if xs == os:

        print("YES!!!!")

    else:

        print("FICGE!")



string = 'xxxxoooo'


count(string)



    
    
