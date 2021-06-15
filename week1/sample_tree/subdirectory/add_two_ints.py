# this is a python script that reads in two integers and prints their sum

# the 'sys' module contains functions for (among
# other things) reading command-line arguments
import sys

# first, check that we have two integers
n_args = len(sys.argv) - 1

# ^ why minus 1? because the first argument in sys.argv is the name
# of the script! (follows C++ argv convention)

# if we don't have the right number of arguments, print out instructions
# to the user and quit
if len(sys.argv) != 3:
    print("Usage: python add_two_ints.py int1 int2")
    exit(1)

# cast the (string) arguments as integers
int1 = int(sys.argv[1])
int2 = int(sys.argv[2])

# calculate the sum
result = int1 + int2

# print it out
print("{:d} + {:d} = {:d}".format(int1,int2,result))
