#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if u got the right random number

import constants


def main():
    # this program checks if the random number is 5

    # input
    RANDOM_NUMBER = int(input("enter a number from 1 to 9:"))

    # process
    if RANDOM_NUMBER == constants.SET_NUMBER:

        # output
        print("")
        print("You guessed correctly")


if __name__ == "__main__":
    main()
