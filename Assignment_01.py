class Matrix:

    def __init__(self, user_input):
        self.__storage = user_input

    def __str__(self):
        return str(self.__storage)

    # Matrix addition or subtraction.
    def combine(self, result: list, t=True):
        # If the matrices cannot be added or subtracted, throw an error.
        assert self.__has_same_col_length(self.__storage)
        assert self.__has_same_col_length(result)
        assert (len(self.__storage) == len(result) and len(self.__storage[0]) == len(result[0]))
        for i, x in enumerate(self.__storage):
            for j, y in enumerate(x):
                result[i][j] += y if t else -1 * y
        return result

    # Matrix multiplication
    def multiply(self, father_result: list):
        # If the matrices cannot be multiplied, throw an error.
        assert self.__has_same_col_length(father_result)
        assert (len(g) == len(father_result) for g in self.__storage)
        # if the second matrix is an identity_matrix, the answer will be the same as first matrix.
        if self.is_unit_matrix(father_result):
            return self.__storage
        ans = list()
        for i, x in enumerate(self.__storage):
            tmp_slice = list()
            for n in self.transpose(father_result):
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
        self.__storage[0][0], self.__storage[1][1] = self.__storage[1][1], self.__storage[0][0]
        self.__storage[0][1] *= -1
        self.__storage[1][0] *= -1
        return self.__magnification_iteration(self.__storage, 1 / self.__determinant(self.__storage))

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
    def transpose(resource: list):
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
    def __magnification_iteration(r: list, rate):
        for i, x in enumerate(r):
            r[i][0] *= rate
        return r


def main():
    a = [[-1, 2, 0], [2, 0, 3]]
    b = [[5, 6], [7, 8]]
    c = [[0, 2], [1, 0], [-1, 1]]
    # print(multiply(c, a))
    matrix = Matrix(b)
    print(matrix.multiply(a))


if __name__ == "__main__":
    main()
