#!/usr/bin/python

import argparse


def find_max_profit(prices):
    k = [iprice-jprice for i, iprice in enumerate(prices[:0:-1]) for j, jprice in enumerate(prices[-(i+2)::-1])]
    k.sort()
    return k[-1]


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit: prices.')
    parser.add_argument('integers',
                        metavar='N',
                        type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))