# Matrix addition or subtraction.
def combine(resource: list, result: list, t=True):
    # If the matrices cannot be added or subtracted, throw an error.
    assert has_same_col_length(resource)
    assert has_same_col_length(result)
    assert (len(resource) == len(result) and len(resource[0]) == len(result[0]))
    for i, x in enumerate(resource):
        for j, y in enumerate(x):
            result[i][j] += y if t else -1 * y
    return result


# Matrix multiplication
def multiply(resource, father_result: list):
    # If the matrices cannot be multiplied, throw an error.
    assert has_same_col_length(father_result)
    assert (len(g) == len(father_result) for g in resource)
    # if the second matrix is an identity_matrix, the answer will be the same as first matrix.
    if is_unit_matrix(father_result):
        return resource
    ans = list()
    for i, x in enumerate(resource):
        tmp_slice = list()
        for n in transpose(father_result):
            tmp_num = list()
            for j, y in enumerate(x):
                tmp_num.append(y * n[j])
            tmp_slice.append(sum(tmp_num))
        ans.append(tmp_slice)
    return ans


def inverse(r):
    assert len(r) == 2  # not finished yet, it can only calculate two-by-two.
    assert has_same_col_length(r)
    rate = 1 / determinant(r)
    r[0][0], r[1][1] = r[1][1], r[0][0]
    r[0][1] *= -1
    r[1][0] *= -1
    return magnification_iteration(r, rate)


def transpose(resource: list):
    return list(map(list, zip(*resource)))


def is_unit_matrix(resource: list):
    for i, x in enumerate(resource):
        if not x[i] == 1:
            return False
    return True


def has_same_col_length(r):
    for p in range(len(r) - 1):
        if len(r[p]) != len(r[p + 1]):
            return False
    return True


def get_ans_range(ii, jj, resource: list):
    ans = list()
    for i, x in enumerate(resource):
        tmp_slice = list()
        for j, y in enumerate(x):
            if not (i == ii or j == jj):
                tmp_slice.append(y)
        if len(tmp_slice):
            ans.append(tmp_slice)
    return ans


def magnification_iteration(r: list, rate):
    for i, x in enumerate(r):
        for j, y in enumerate(x):
            r[i][j] *= rate
    return r


def determinant(r, result=list()):
    assert has_same_col_length(r)
    assert len(r) == len(r[0])
    if len(r) == 2:
        return r[0][0] * r[1][1] - r[0][1] * r[1][0]
    for i, x in enumerate(r):
        for j, y in enumerate(x):
            h = (-1 if i % 2 else 1) * (-1 if j % 2 else 1)
            result.append(determinant(magnification_iteration(get_ans_range(i, j, r), h * y), result))
    return (result)


def main():
    a = [[2, 5, 2], [3, 4, 2], [1, 1, 1]]
    b = [[5, 6], [7, 8]]
    print(determinant(a))


if __name__ == "__main__":
    main()
