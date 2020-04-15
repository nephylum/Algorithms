#!/usr/bin/python

import argparse

def find_max_profit(prices):
    #initialize a max
    max_profit = 0
    #iterate through prices
    for x in range(len(prices)):
        #iterate through following values
        for y in range(x + 1, len(prices)):
            #check if selling would be more profitable than previously recorded
            #and update max_profit if it is
            if prices[y] - prices[x] > max_profit:
                max_profit = prices[y] - prices[x]
    return max_profit

#for testing:
# print("find_max_profit([1050, 270, 1540, 3800, 2])  returns:")
# print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
