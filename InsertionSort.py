#Python insertion sort




# function to do insert


def insertSort(x):



    # travese through list

    for i in range(1, len(x)):


        key = x[i]


        # move elements of of array that are
        # greater than key to one position ahead of their current

        j = i-1
        while j >=0 and key < x[j]:
            x[j+1]=x[j]
            j -= 1
            x[j+1] = key


# driver test



x = [1, 3, 4, 6, 14, 3, 2, 9]
insertSort(x)
print("Sorted array is: ")
for i in range(len(x)):
    print ("%d" %x[i])

'''

1st iteration

1 is first in the range of the list which is 8 steps all together

index = 1

1 is first key as it is the fist item in the list, at index 0

key = 1

0 is first temp j as it is the index # - 1

j = 0

while temp j is greater than or equal to 0 and the key is less than the temp j position within
the array

move the position of temp j within the array to one spot a head of where it was

then subtract one from temp j to go back a spot

But also make the new key equal to temp j minus one position within the array


so..





'''
