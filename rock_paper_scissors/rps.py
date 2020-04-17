#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    poss_index = [0] * n
    rps = ['rock','paper','scissors']
    lol = [[rps[x] for x in poss_index]]

    done = False
    while done == False:
        poss_index[n-1] += 1

        for x in range(1, n+1):
            if poss_index[n-x] == 3:
                poss_index[n-x] = 0
                if n-x+1 >= 0:
                    poss_index[n-(x+1)] += 1
        list = [rps[x] for x in poss_index]
        lol.append(list)
        if all(x == 2 for x in poss_index):
            done = True




    return lol


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
