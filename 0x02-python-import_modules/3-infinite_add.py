#!/usr/bin/python3
if __name__ == "__main__ ":
    from sys import argv

    for i in range(len(argv) - 1):
        print("{}".format(int(argv[i + 1])))
