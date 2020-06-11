# xmatrix MODULE IS CREATED BY MYSELF, VISIT THIS PAGE TO SEE README.
# https://pypi.org/project/xmatrix
# SOURCE CODE
# https://github.com/Xanonymous-GitHub/xmatrix
from xmatrix import xm, ixm, Matrix
# To calculate Complex Square Root, built-in module
from cmath import sqrt


# RUN THIS COMMAND TO INSTALL MODULE BEFORE YOU START : pip3 install xmatrix --upgrade

def define_matrices() -> list:
    s = xm('2,0;0,-5')
    t = xm('2,-12;1,-5')
    u = xm('5,2;2,3')
    v = xm('1,1;1,1')
    w = xm('2,1;0,2')
    x = xm('3,1;-1,1')
    y = xm('0,1;-1,0')
    z = xm('3,-5;1,1')
    return [s, t, u, v, w, x, y, z]


def get_solution_amount_and_judgement(original_matrix: Matrix) -> [int, float or complex]:
    source = original_matrix.raw
    a = source[0][0]
    b = source[0][1]
    c = source[1][0]
    d = source[1][1]
    judgement = ((a - d) ** 2) + 4 * b * c
    return [(0 if judgement < 0 else (1 if judgement == 0 else 2)), judgement]


def remove_unneeded_zeros(number: int or float) -> int or float:
    return int(number) if number == int(number) else number


def get_two_dim_eigenvalues(original_matrix: Matrix) -> list:
    solution_amount, judgement = get_solution_amount_and_judgement(original_matrix)
    source = original_matrix.raw
    result = list()
    part_answer = (source[0][0] + source[1][1])
    if solution_amount == 2:
        [result.append(remove_unneeded_zeros((part_answer + x * (judgement ** 0.5)) * 0.5)) for x in range(-1, 2, 2)]
    elif solution_amount == 1:
        [result.append(remove_unneeded_zeros(part_answer * 0.5)) for _ in range(2)]
    elif solution_amount == 0:
        [result.append((part_answer + x * sqrt(judgement)) * 0.5) for x in range(-1, 2, 2)]
    return result


def get_eigenvector_row_reduced_echelon_form(original_matrix: Matrix, two_dim_eigenvalues: list) -> list:
    result = list()
    [result.append((original_matrix - (two_dim_eigenvalues[x] * ixm(2))).rref) for x in range(2)]
    return result


def get_eigenvector(rref_list: list) -> Matrix or str:
    result = list()
    for x in range(2):
        if not sum(rref_list[x].raw[1]):
            if rref_list[x].raw[0][1] and rref_list[x].raw[0][0]:
                result.insert(0, [-1 * rref_list[x].raw[0][1], rref_list[x].raw[0][0]])
            elif rref_list[x].raw[0][0]:
                result.insert(0, [0, 1])
            elif rref_list[x].raw[0][1]:
                result.insert(0, [1, 0])
        else:
            result.insert(0, [0, 0])
    if result[1] == result[0]:
        result.pop()
    if len(result) == 1 and not result[0][0] and not result[0][1]:
        return 'No eigenvector'
    return Matrix(result).tp


def get_ans():
    problem_source_pack = define_matrices()
    eigenvalues = list()
    rref = list()
    for data in problem_source_pack:
        eigenvalues.append(get_two_dim_eigenvalues(data))
    for i, problem_matrix in enumerate(problem_source_pack):
        rref.append(get_eigenvector_row_reduced_echelon_form(problem_matrix, eigenvalues[i]))
    eigenvectors = list()
    for rref_result in rref:
        eigenvectors.append(get_eigenvector(rref_result))
    return eigenvalues, eigenvectors


def main():
    problems = define_matrices()
    eigenvalues, eigenvectors = get_ans()
    for index, problem in enumerate(problems):
        print('===> Problem', index + 1, ':')
        print(problem)
        print('eigenvalue :', (', '.join(map(str, eigenvalues[index]))).replace('j', 'i'))
        print('eigenvector :')
        print(eigenvectors[index])
        print()


if __name__ == '__main__':
    # pip3 install xmatrix --upgrade
    main()
