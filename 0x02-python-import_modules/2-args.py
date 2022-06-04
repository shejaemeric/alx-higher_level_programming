#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    def printArgs(lis,num):
        for index in range(1, num+1):
            print("{:d}: {:s}".format(index,lis[index]))
    argv_count = len(argv)
    if argv_count == 1:
        print("{:d} arguments.".format(argv_count))
    elif argv_count == 2:
        print("{:d} argument:".format(argv_count))
        printArgs(sys.argv,argv_count)
    else:
        print("{:d} arguments:".format(argv_count))
        printArgs(sys.argv,argv_count)
