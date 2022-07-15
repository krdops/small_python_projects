# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', outputs an integer with the number of
# stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces





# input: string of words a-z and maybe spaces
# output: int of how many stickers of "facebook" will be needed.


# How do I account for how many of a specific letter I will need?


def getnum(data):



    
    f = 'tom'
    check = {}
    checklist = []
    count = 0
    stickers = 0

    t = 0
    o = 0
    m = 0

    for i in data:


        if i == 't':
            t += 1
        elif i == 'o':
            o += 1
        elif i == 'm':
            m += 1
        else:
            break
        

    
   ''' for i in data:
        
        check[i] = count
        count += 1
    for i in check:

        if i in f:

            checklist.append(i)
            
        else:
            pass
    
    'return checklist'''

   

    

data = 'chtomddtom'
print(getnum(data))
        
