def power_of_two(x):
    i = 2
    if x==2 or x==1:
        return True
    if x%2!=0:
         return False
    while i<x:
        i=i*2
    return i == x 
  # your code here
