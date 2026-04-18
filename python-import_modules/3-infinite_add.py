#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # sys.argv[0] proqramın adıdır, onu keçib 1-dən sona qədər hamısını toplayırıq
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print("{}".format(total))
