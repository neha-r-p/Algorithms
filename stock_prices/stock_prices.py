#!/usr/bin/python

import argparse

def find_max_profit(prices):
#start at index 1
    max_profit = prices[1]-prices[0]
    print(max_profit)
    for i in range(1, len(prices)):
        #counter for indices to compare
        for j in range(0, i):
            #compare prices of stocks at index to previous indices for profit calc
            if prices[i] - prices[j] > max_profit:
                #keep track of maximum profit in variable
                max_profit = prices[i] - prices[j]
                print("max", max_profit, "i:", i, "j:", j)

    return max_profit

print(find_max_profit([10, 7, 5, 8, 11, 9]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))