"""
    Copyright (C) 2020 By Xanonymous All Rights Reserved, Do Not Copy this file for anyway.
    >>Note: Everything there you see is made by myself, does not use any matrix package (ex:numpy).
    Visit My GitHub:https://github.com/Xanonymous-GitHub
    This package is formatted by python official coding style linter (PEP8).
    More style details on:https://www.python.org/dev/peps/pep-0008
"""

# Some special math value is included in the question
import math


class Matrix:
    """Define the Matrix class"""

    def __init__(self, u):
        # object constructor
        assert self.__has_same_col_length(u), "invalid matrix."
        self.__storage = u

    def __str__(self):
        return self.__pretty(self.__storage)

    # Matrix addition or subtraction.
    def combine(self, resource, t=True):
        # If the matrices cannot be added or subtracted, throw an error.
        assert (self.__has_same_col_length(self.__storage) and self.__has_same_col_length(resource) and (
                len(self.__storage) == len(resource) and len(self.__storage[0]) == len(resource[0]))), "can't combine."
        for i, x in enumerate(resource):
            for j, y in enumerate(x):
                # the parameter T can control the method to plus or minus.
                self.__storage[i][j] += y if t else -1 * y

    # Matrix multiplication
    def multiply(self, result):
        if type(result) is int:
            # method accept single integer to be calculated.
            return self.__rate(self.__storage, result)
        # If the matrices cannot be multiplied, throw an error.
        assert self.__has_same_col_length(result), "can not multiply."
        for g in self.__storage:
            assert len(g) == len(result), "can't not multiply."
        # if the second matrix is an identity_matrix, the answer will be the same as first matrix.
        if self.is_unit_matrix(result):
            return self.__storage
        ans = list()
        for i, x in enumerate(self.__storage):
            tmp_slice = list()
            for n in self.__transpose(result):
                tmp_num = list()
                for j, y in enumerate(x):
                    tmp_num.append(y * n[j])
                tmp_slice.append(sum(tmp_num))
            ans.append(tmp_slice)
        self.__storage = ans

    def inverse(self):
        # we not accept the matrix of 3 by 3 or more to be inverse.
        assert len(self.__storage) == 2
        assert self.__has_same_col_length(self.__storage)
        determinant = self.__determinant(self.__storage)
        assert determinant, "can not inverse."
        self.__storage[0][0], self.__storage[1][1] = self.__storage[1][1], self.__storage[0][0]
        self.__storage[0][1] *= -1
        self.__storage[1][0] *= -1
        self.__storage = self.__rate(self.__storage, 1 / determinant)

    def transpose(self):
        self.__storage = self.__transpose(self.__storage)

    def __determinant(self, r):
        assert self.__has_same_col_length(r)
        assert len(r) == len(r[0])
        if len(r) == 2:
            return r[0][0] * r[1][1] - r[0][1] * r[1][0]
        result = list()
        for i, x in enumerate(r[0]):
            h = (-1 if i % 2 else 1)
            result.append(
                self.__determinant(self.__magnification_iteration(self.__get_ans_range(0, i, r), h * x)))
        return sum(result)

    @property
    def val(self):
        # get the real value of the object
        return self.__storage

    @staticmethod
    def __pretty(r) -> str:
        # Detect if the value can be an integer.
        for i, x in enumerate(r):
            for j, y in enumerate(x):
                if r[i][j] == int(r[i][j]):
                    r[i][j] = int(r[i][j])
        # format the value then return
        return '\n'.join(map(str, r))

    @staticmethod
    def __error_handler(msg) -> str:
        print(msg)
        return msg

    @staticmethod
    def __transpose(resource: list) -> list:
        return list(map(list, zip(*resource)))

    @staticmethod
    def is_unit_matrix(resource: list) -> bool:
        for i, x in enumerate(resource):
            if not x[i] == 1:
                return False
        return True

    @staticmethod
    def __has_same_col_length(r) -> bool:
        for p in range(len(r) - 1):
            if len(r[p]) != len(r[p + 1]):
                return False
        return True

    @staticmethod
    def __get_ans_range(ii, jj, resource: list) -> list:
        ans = list()
        for i, x in enumerate(resource):
            tmp_slice = list()
            for j, y in enumerate(x):
                if not (i == ii or j == jj):
                    tmp_slice.append(y)
            if len(tmp_slice):
                ans.append(tmp_slice)
        return ans

    @staticmethod
    def __rate(r, amount) -> list:
        for i, x in enumerate(r):
            for j, y in enumerate(x):
                r[i][j] *= amount
        return r

    @staticmethod
    def __magnification_iteration(r: list, rate) -> list:
        for i, x in enumerate(r):
            r[i][0] *= rate
        return r


class UnitMatrix(Matrix):
    def __init__(self):
        super().__init__([[1, 0], [0, 1]])

    def __str__(self):
        return super().__str__()


def defines():
    pi = math.pi
    a = Matrix([[-1, 2, 0], [2, 0, 3]])
    b = Matrix([[2, 0, -1], [1, -2, 0]])
    c = Matrix([[0, 2], [1, 0], [-1, 1]])
    e = Matrix([[2, -1], [round(pi, 2), round(math.log10(2), 4)], [-2, 6]])
    i = UnitMatrix()
    return a, b, c, e, i


def question_1():
    # get requirements.
    resources = defines()
    a, b, c, e = resources[:4]

    # A+2B
    b.multiply(2)
    b.combine(a.val[:].copy())
    ans_1 = b

    # C-E
    c.combine(e.val, False)
    ans_2 = c

    # transpose A
    a.transpose()
    ans_3 = a

    # transpose E
    e.transpose()
    ans_4 = e

    # return results
    result = list()
    result.append("--> A+2B <--")
    result.append(ans_1)
    result.append("--> C-E <--")
    result.append(ans_2)
    result.append("--> Transpose A <--")
    result.append(ans_3)
    result.append("--> Transpose E <--")
    result.append(ans_4)
    return '\n'.join(map(str, result))


def question_2():
    # get requirements.
    resources = defines()
    a = resources[0]
    c = resources[2]

    # F=AxC
    a.multiply(c.val)
    ans_1 = a

    # G=CxA
    del a
    a = defines()[0]
    c.multiply(a.val)
    ans_2 = c

    # return results
    result = list()
    result.append("--> F=A*C <--")
    result.append(ans_1)
    result.append("--> G=C*A <--")
    result.append(ans_2)
    return '\n'.join(map(str, result))


def question_3():
    # get requirements.
    resources = defines()
    a = resources[0]
    c = resources[2]
    i = resources[4]
    tmp = defines()[0]  # single call API

    # F=AxC
    a.multiply(c.val)
    f = Matrix(a.val)

    # inverse of F
    tmp.multiply(c.val)
    tmp.inverse()
    f_inverse = Matrix(tmp.val)
    ans_1 = f_inverse

    # FxF-1
    f_inverse2 = Matrix(tmp.val)
    f_inverse2.multiply(f.val[:])
    ans_2 = f_inverse2
    ans_3 = "Yes" if ans_2.val == i.val else "No"

    # return results
    result = list()
    result.append("--> inverse of F <--")
    result.append(ans_1)
    result.append("--> FxF-1 <--")
    result.append(ans_2)
    result.append("--> Is F*F-1 equal to I? <--")
    result.append(ans_3)
    return '\n'.join(map(str, result))


def main():
    print(question_1())
    print(question_2())
    print(question_3())


if __name__ == '__main__':
    main()
