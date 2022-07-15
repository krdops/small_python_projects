'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        # what is problem asking? Given ARRAY of UNIQUE INTS -> ALL POSSIBLE PERMUTATIONS
        # What object type am I to return? -> ARRAY
        # Reminder: Permutations are possible combinations.
        
    numsdict = {}    
    for i, v in enumerate(nums):
        
'''



def perm(a, k=0):

    if k == len(a):
        print(a)
    else:

        for i in xrange(k, len(a)):
            a[0], a[i] = a[i], a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]

    
perm([1,2,3])
