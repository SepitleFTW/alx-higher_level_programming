#!/usr/bin/pyhton3

"""Write a program that prints the result of the addition of all arguments"""
if __name__ == "__main__":
    import sys

    Total = 0
    for i in range(len(sys.argv) - 1):
        Total += int(sys.argv[i + 1])
    print("{}".format(Total))

