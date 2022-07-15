



def Roman(string):


   romandict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

   sumrn = 0
   last = 'I'
   
   for i in range(len(string)-1, -1, -1):
        print(string[i])
        if int(romandict[string[i]]) < romandict[last]:
            sumrn -= romandict[string[i]]
        else:
            sumrn += romandict[string[i]]
            print(sumrn)
        last = string[i]
        
   return sumrn


string = "XMXVXMCCXMC"        
print(Roman(string))

    
