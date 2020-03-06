import math


class Matrix:

    def __init__(self, u):
        assert self.__has_same_col_length(u), "invalid matrix."
        self.__storage = u

    def __str__(self):
        self.__pretty(self.__storage)

    @staticmethod
    def __pretty(r):
        return '\n'.join(map(str, r))

    @property
    def show(self):
        return self.__pretty(self.__storage)

    @property
    def val(self):
        return self.__storage

    # Matrix addition or subtraction.
    def combine(self, result, t=True):
        # If the matrices cannot be added or subtracted, throw an error.
        assert (self.__has_same_col_length(self.__storage) and self.__has_same_col_length(result) and (
                len(self.__storage) == len(result) and len(self.__storage[0]) == len(result[0]))), "can't combine."
        for i, x in enumerate(self.__storage):
            for j, y in enumerate(x):
                result[i][j] += y if t else -1 * y
        return result

    # Matrix multiplication
    def multiply(self, result):
        if type(result) is int:
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
        return ans

    @property
    def inverse(self):
        assert len(self.__storage) == 2
        assert self.__has_same_col_length(self.__storage)
        determinant = self.__determinant(self.__storage)
        assert determinant, "can not inverse."
        self.__storage[0][0], self.__storage[1][1] = self.__storage[1][1], self.__storage[0][0]
        self.__storage[0][1] *= -1
        self.__storage[1][0] *= -1
        return self.__magnification_iteration(self.__storage, 1 / determinant)

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

    @staticmethod
    def __error_handler(msg):
        print(msg)
        return msg

    @staticmethod
    def __transpose(resource: list):
        return list(map(list, zip(*resource)))

    @staticmethod
    def is_unit_matrix(resource: list):
        for i, x in enumerate(resource):
            if not x[i] == 1:
                return False
        return True

    @staticmethod
    def __has_same_col_length(r):
        for p in range(len(r) - 1):
            if len(r[p]) != len(r[p + 1]):
                return False
        return True

    @staticmethod
    def __get_ans_range(ii, jj, resource: list):
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
    def __rate(r, amount):
        for i, x in enumerate(r):
            for j, y in enumerate(x):
                r[i][j] *= amount
        return r

    @staticmethod
    def __magnification_iteration(r: list, rate):
        for i, x in enumerate(r):
            r[i][0] *= rate
        return r


class UnitMatrix(Matrix):
    def __init__(self):
        super().__init__([[1, 0], [0, 1]])


def defines():
    pi = math.pi
    a = Matrix([[-1, 2, 0], [2, 0, 3]])
    b = Matrix([[2, 0, -1], [1, -2, 0]])
    c = Matrix([[0, 2], [1, 0], [-1, 1]])
    e = Matrix([[2, -1], [pi, math.log10(2)], [-2, 6]])
    i = UnitMatrix
    return a, b, c, e, i


def main():
    a, b, c, e, i = defines()
    result = Matrix
    # A+2B
    result = a.combine(b.multiply(2))
    print("A+2B")
    print(result.show)
    # C-E
    result = c.combine(e.val, False)
    print("C-E")
    print(result.show)
    # transpose A
    # result = a.transpose
    # print("transpose A")
    # print(result.show)


if __name__ == '__main__':
    main()
