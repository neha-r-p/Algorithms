#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
    if n <= 1: 
        return 1
    elif n == 2: 
        return 2
    elif cache and cache[n] > 0: #if there is a cache and cache[n] is more than 0, return/stop the recursion
        return cache[n]
    else: #n > 2 and cache[n] == 0
        if not cache:
            cache = {i:0 for i in range(n+1)} #create cache of 0 for n numbers
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

print(eating_cookies(10))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')