txt = "The quick brown fox jumps over the lazy dog."
t1 = "fox"
t2 = "cat"

###############################################################################
# DONE: 1. (6 pts)
#
#   Write each of the functions below (each that takes two parameters and uses
#   the appropriate operator from the reading) that simply returns the boolean
#   evaluation of those two parameters:
#
#   equal()
#   not_equal()
#   greater_than()
#   less_than()
#   greater_than_or_equal_to()
#   less_than_or_equal_to()
#
#   Now write a line of code for each one using numbers for the parameters that
#   would cause each function to return True. 
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def equal(a, b):
    print(bool(a == b))
    return equal

equal(3, 3)

def notequal(c, d):
    print(bool(c != d))
    return notequal

notequal(3, 7)

def greater_than(e, f):
    print(bool(e > f))
    return greater_than

greater_than(7, 3)

def less_than(g, h):
    print(bool(g < h))
    return less_than

less_than(3, 7)

def greater_than_or_equal_to(i, j):
    print(bool(i >= j))
    return greater_than_or_equal_to

greater_than_or_equal_to(7, 6)

def less_than_or_equal_to(k, l):
    print(bool(k <= l))
    return less_than_or_equal_to

less_than_or_equal_to(6, 7)

###############################################################################
# DONE: 1. (2 pts)
#
#   Write a line of code that returns True if the string
#       t1 (defined above)
#   is contained in the string
#       txt (also defined above)
#   and prints the result.
#
#   Write another line of code that returns True if the string
#       t2
#   is contained in the string
#       txt
#   and prints the result.
#
#   Run your code. Does it return what you expect?
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(txt)
print(t1 in txt)
print(t2 in txt)

###############################################################################
# DONE: 1. (1 pt)
#
#   Now, write a line of code that returns True if the string
#       t1
#   is *not* the same thing as
#       t2
#   and prints the result
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(t1 is not t2)