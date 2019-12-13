#!/usr/bin/python

# import sys


rps = ['rock', 'paper', 'scissors']


def rock_paper_scissors(n):
    if (n == 0):
        return [[]]
    if (n == 1):
        return [[r] for r in rps]
    if (n > 1):
        # return [[r] + x for r in rps for x in rock_paper_scissors(n-1)]
        total = []
        for r in rps:
            print(f'Value of r from rps is {r}')
            for x in rock_paper_scissors(n-1):
                print(f'Value of x from rock_paper_Scisssors is {x}')
                # print([r] + x)
                total.append([r]+x)
        return total


print(rock_paper_scissors(3))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
