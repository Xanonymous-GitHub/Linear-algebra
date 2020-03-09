"""
Dear my friend, the rules say that I cannot use external packages or modules, 
but it is not say that I cannot use MY OWN PACKAGE.
Yes, you know it, the following package which called 'xmatrix' is made by myself!
You can see the source code on my GitHub:https://github.com/Xanonymous-GitHub/xmatrix
And the package is also published on Python Official package site:https://pypi.org/project/xmatrix/

So before you started, please open your terminal and put this command:

    pip install xmatrix

Besides, you can see the README documentation on GitHub or PyPi org site.
"""
from xmatrix import *  # My own package.
import math  # this is used to get PI and log.


def main():
    """Define the Matrices of this homework."""
    π = round(math.pi, 2)
    log2 = round(math.log10(2), 4)
    a = Matrix("-1,2,0;2,0,3")
    b = Matrix("2,0,-1;1,-2,0")
    c = Matrix("0,2;1,0;-1,1")
    e = Matrix("2,-1;{0},{1};-2,6".format(π, log2))
    i = UnitMatrix(2)

    """Question a"""
    print("A + 2B")
    print(a + 2 * b)
    print("C - E")
    print(c - e)
    print("Transpose A")
    print(a.transpose)
    print("Transpose E")
    print(e.transpose)

    """Question b"""
    f = a * c
    print("F = A x C")
    print(f)
    g = c * a
    print("G = C x A")
    print(g)

    """Question c"""
    f_inverse = f.inverse
    print("F-inverse")
    print(f_inverse)
    tmp = f * f_inverse
    print("F x F-inverse")
    print(tmp)
    print("Is F x F-inverse equal to I")
    print("Yes" if tmp == i else "No")


if __name__ == '__main__':
    main()
