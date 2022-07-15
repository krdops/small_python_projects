


def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))






num = 3

    
print(factorial(num))




def towerOfHanoi(numrings, from_pole, to_pole, aux_pole):

    if numrings == 1:
        print("Move ring 1 from", from_pole, 'pole to', to_pole, 'pole')
        return
    towerOfHanoi(numrings - 1, from_pole, aux_pole, to_pole)
    print('move rings', numrings, 'from', from_pole, 'pole to', to_pole)
    towerOfHanoi(numrings - 1, aux_pole, to_pole, from_pole)

    

numrings = 2
towerOfHanoi(numrings, 'left', 'right', 'middle')



def power(num, topwr):

    if topwr == 0:
        return 1
    else:
        return num * power(num, topwr - 1)
    
