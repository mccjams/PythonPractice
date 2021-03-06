# Functions do three things
# They take arguments the way your scripts take argv.
# Using #1 and #2 they let you make your own "mini-scripts" or "tiny-commands"
# You can create a function by using the word "def" in Python.

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this.
def print_two_again (arg1, arg2):
    print "arg1: %r, arg2 %r" % (arg1, arg2)

# this just takes one arguments
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
