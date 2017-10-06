from math import *



def shor(num):

  width = math.ceil(math.log(num, 2))

  qmax = 2^width
  factor = 0
  
