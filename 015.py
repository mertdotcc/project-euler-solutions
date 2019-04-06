import scipy.special as sp
import time

def solve():
    start = time.time()

    # This problem can be treat as a simple combinatorics problem.
    # When we are given a N by N grid, we need to make N moves to the right
    # and N moves to the bottom. Since every move we are going to make,
    # i.e., either right or bottom, is indistinguishable, the problem
    # boils down to making N decisions from 2N possible cases.
    # Which is the binomial coefficient of 40 and 20 in this question.

    # Note that the SciPy package contains two functions that are eligible
    # to deal with this kind of a problem. binom() and comb()

    # In this case I am going to use the comb() function instead of the binom()
    # function because I want to use the exactness parameter that only the function
    # comb() has.

    print("Solution:", sp.comb(40, 20, exact=True))

    end = time.time() - start
    print("Runtime:", end)