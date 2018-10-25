# Wherever possible, try to write functions so that they only use local variables and parameters.
# Only access global and non-local variables when it is absolutely necessary
# Always use comments in situations like this.


def spam1():

    def spam2():

        def spam3():
            z = "even"
            z += y  # when we use a nonlocal variable, python adds it to the local scope for faster processing.
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more " + x  # y must exist before spam3 is called
        y += spam3()  # do not combine these assignments
        print("In spam2, locals are {}".format(locals()))
        return y

    x = " spam "  # x must exist before spam2 is called.
    x += spam2()  # do not combine these assigments.
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
# in the module scope locals and globals are the same
print(locals())
print(globals())
# dir(): Without arguments, return the list of names in the current local scope. With an argument, attempt to return a
#    list of valid attributes for that object.Without arguments, return the list of names in the current local scope.
#    With an argument, attempt to return a list of valid attributes for that object.
dir()

# python scoping:
#     local - global - built-in
