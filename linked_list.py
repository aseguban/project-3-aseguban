# an AnyList is one of
# - None
# - a Pair
class Pair:
    def __init__(self, first, rest):
        self.first = first  # any value
        self.rest = rest  # a Pair
    
    def __eq__(self, other):
        return (type(other) == type(self)
                and self.first == other.first
                and self.rest == other.rest)
    
    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)


# -> AnyList
# This function takes no arguments and returns an empty list
def empty_list():
    return None


# AnyList int Any -> AnyList
# This function takes a list, an integer index, and another value (of any type)
#   as arguments and places the value at index position in the list
def add(anylist, index, value):
    if index < 0 or anylist is None and index > 0:
        raise IndexError()
    if index == 0:
        if anylist is None:
            return Pair(value, None)
        return Pair(value, Pair(anylist.first, anylist.rest))
    return Pair(anylist.first, add(anylist.rest, index - 1, value))


# AnyList -> int
# This function takes a list as an argument and returns the number of elements
#   currently in the list
def length(anylist):
    if anylist is None:
        return 0
    return 1 + length(anylist.rest)

# AnyList int -> Any
# This function takes a list and an integer index as arguments and returns the
#   value at the index position in the list
def get(anylist, index):
    if anylist is None or index < 0:
        raise IndexError()
    if index == 0:
        return anylist.first
    return get(anylist.rest, index - 1)


# AnyList int Any -> AnyList
# This function takes a list, an integer index, and another value (of any type)
#   as arguments and replaces the element at index position in the list with
#   the given value
def set(anylist, index, value):
    if index < 0 or anylist is None:
        raise IndexError()
    if index == 0:
        return Pair(value, anylist.rest)
    return Pair(anylist.first, set(anylist.rest, index - 1, value))


# AnyList int -> AnyList
# This function takes a list and an integer index as arguments and removes the
#   element at the index position from the list, returns the resulting list
def remove_helper(anylist, index):
    if index < 0 or anylist is None:
        raise IndexError()
    if index == 0:
        return anylist.rest
    return Pair(anylist.first, remove_helper(anylist.rest, index - 1))


# AnyList int -> Any AnyList
# This function takes a list and an integer index as arguments and removes the
#   element at the index position from the list, returns a tuple of the
#   removed element and the resulting list
def remove(anylist, index):
    return get(anylist, index), remove_helper(anylist, index)


# List function -> None
# applies the provided function to the value at each position in the List
def foreach(anylist, func):
    if anylist is None:
        return
    func(anylist.first)
    foreach(anylist.rest, func)

# List function -> List
# returns sorted list using comparator function
def sort(anylist, func):
    if anylist is None:
        return anylist
    c = 1
    newlist = add(None, 0, get(anylist, 0))
    anylist = anylist.rest
    while anylist is not None:
        for f in range(c + 1):
            if f == c:
                newlist = add(newlist, f, anylist.first)
                break
            elif func(anylist.first, get(newlist, f)):
                newlist = add(newlist, f, anylist.first)
                break
        anylist = anylist.rest
        c = c + 1
    
    return newlist

