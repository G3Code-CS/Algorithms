#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache = None):
    cache = {}

    def eat_cookie(val):
        if (val == 0):
            return 1
        if (val < 0):
            return 0
        if (val not in cache):
            ways = eat_cookie(val-1) + eat_cookie(val-2) + eat_cookie(val-3)
            cache[val] = ways
        return cache[val]
    return eat_cookie(n)


# print(eating_cookies(10))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies."
#              .format(ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
