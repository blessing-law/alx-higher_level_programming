#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) - 1 == 0:
        print("0 arguments.")
    elif len(argv) - 1 == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        for i in range(len(argv)):
            print("{}: {}".format(i, argv[i]))
