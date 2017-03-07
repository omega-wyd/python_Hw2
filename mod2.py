#!/usr/bin/env python3
import sys

def modify(k):
    """
    Modify the content of a list of items
    ARGS:
        k -> a list of items
    Returns:
        None
    """
    # Everything is a reference
    k.append(39)
    print("k=",k)


def replace(g):
    """
    Replace content of the list
    ARGS:
        g-. a list of items
    Returns:
        None
    """
    g = [17,23,45,90]
    print("g = ", g)
    

def replace_content(g):
    """
    Replace content of the list
    ARGS:
        g -> a list of items
    Returns:
        None
    """
    g[0] = 99
    g[1] = 88
    g[2] = 77
    print("g = ", g)

# Main function
def main():
    """
    Test Funciton
    """
    m = [9,13,15]
    print("Original ", m)
    modify(m)
    print("after modify", m)
    replace(m)
    print("After replace", m)


if __name__=="__main__":
    # Call Main
    main()

    exit(0)
