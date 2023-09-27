#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Sept/27/2023
# This program calculates the circumference of a circle using tau and a user's  input.
import constants


def main():
    # Getting user input for radius.
    radius = float(input("Enter the radius of the circle (cm): "))

    # Calculating the circumference using the user's input.
    circumference = constants.TAU * radius

    # Displaying the circumference back to the user.
    print("")
    print("The circumference = {:.2f} cm".format(circumference))


if __name__ == "__main__":
    main()
