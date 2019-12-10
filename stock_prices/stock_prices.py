#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # pt = tuple(prices)
    # prices.sort()
    # if (pt.index(prices[-1]) == 0):
    #     return (prices[-2] - prices[-1])
    # else:
    #     hv = [prices[-1] - pt[i] for i in range(pt.index(prices[-1]))]
    #     hv.sort()
    #     return hv[-1]
    # for i, iprice in enumerate(prices[:0:-1]):
    #     for j, jprice in enumerate(prices[-(i+2)::-1]):
    #         print(f'{i, iprice} - {j, jprice}')
    k = [iprice-jprice for i, iprice in enumerate(prices[:0:-1]) for j, jprice in enumerate(prices[-(i+2)::-1])]
    # print(k)
    k.sort()
    return k[-1]


# print(find_max_profit([10, 7, 5, 8, 11, 9]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))
# print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit: prices.')
    parser.add_argument('integers',
                        metavar='N',
                        type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))