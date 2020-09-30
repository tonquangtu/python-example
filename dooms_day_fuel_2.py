from fractions import Fraction


def find_gcd(numerator, denominator):
    def find_gcd_internal(x, y):
        if y == 0:
            return x
        return find_gcd_internal(y, x % y)

    return find_gcd_internal(abs(numerator), abs(denominator))


def find_lcm(numerator, denominator):
    return int(numerator * denominator / find_gcd(numerator, denominator))


def frac(numerator, denominator):
    g = find_gcd(numerator, denominator)
    return Fraction(int(numerator / g), int(denominator / g))


def convert_to_probabilities_mat(mat):
    row_sums = [sum(row) for row in mat]
    stable_indices = set([i for i, row_sum in enumerate(row_sums) if row_sum == 0])

    prob_mat = []
    for i in range(len(mat)):
        if i not in stable_indices:
            prob_mat.append([frac(x, row_sums[i]) for x in mat[i]])

    for i in range(len(mat)):
        if i in stable_indices:
            prob_mat.append([Fraction(0, 1) for x in mat[i]])

    transformed_prob_mat = []
    for i in range(len(prob_mat)):
        transformed_prob_mat.append([])
        stable_mat = []
        for j in range(len(prob_mat)):
            if j not in stable_indices:
                transformed_prob_mat[i].append(prob_mat[i][j])
            else:
                stable_mat.append(prob_mat[i][j])
        transformed_prob_mat[i].extend(stable_mat)

    return [transformed_prob_mat, len(stable_indices), len(transformed_prob_mat) - len(stable_indices)]


def copy_mat(mat):
    new_mat = []
    for i in range(len(mat)):
        new_mat.append([Fraction(mat[i][j].numerator, mat[i][j].denominator) for j in range(len(mat))])
    return new_mat


def find_inverse_mat(input_mat):
    mat = copy_mat(input_mat)
    inverse = []
    for i in range(len(mat)):
        inverse.append([Fraction(int(i == j), 1) for j in range(len(mat))])

    for i in range(len(mat)):
        apply_row_operator(mat, inverse, i)

    return inverse


def apply_row_operator(mat, inverse, index):
    if mat[index][index].numerator != mat[index][index].denominator:
        ratio = 1 / mat[index][index]
        for i in range(len(mat)):
            mat[index][i] = ratio * mat[index][i]
            inverse[index][i] = ratio * inverse[index][i]

    for i in range(len(mat)):
        if i != index and mat[i][index].numerator != 0:
            ratio = -mat[i][index] / mat[index][index]
            for j in range(len(mat)):
                mat[i][j] += ratio * mat[index][j]
                inverse[i][j] += ratio * inverse[index][j]


def multiply_mat(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res


def solution(m):
    prob_mat, stable_len, transient_len = convert_to_probabilities_mat(m)
    if transient_len == 0:
        return [1, 1]

    transient_transient_mat = [[1 - prob_mat[i][j] if i == j else 0 - prob_mat[i][j] for j in range(transient_len)]
                               for i in range(transient_len)]
    transient_stable_mat = [[prob_mat[i][j + transient_len] for j in range(stable_len)] for i in range(transient_len)]

    inverse_transient_transient_mat = find_inverse_mat(transient_transient_mat)

    stable_prob_mat = multiply_mat(inverse_transient_transient_mat, transient_stable_mat)

    lcm_denominator = 1
    for item in stable_prob_mat[0]:
        lcm_denominator = find_lcm(lcm_denominator, item.denominator)

    res = [lcm_denominator * item.numerator / item.denominator for item in stable_prob_mat[0]]
    res.append(lcm_denominator)

    # print res
    return res


def print_mat(mat):
    for i in range(len(mat)):
        print mat[i]
    print "---------------------------"

# solution([[0, 1, 0, 0, 0, 1],
#           [4, 0, 0, 3, 2, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0]])

solution([[0, 2, 1, 0, 0],
          [0, 0, 0, 3, 4],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0,0],
          [0, 0, 0, 0, 0]])


# inv = find_inverse_mat([[Fraction(1, 1), Fraction(1, 3), Fraction(-1, 2)],
#                 [Fraction(1, 1), Fraction(-1, 2), Fraction(1, 4)],
#                 [Fraction(1, 2), Fraction(1, 2), Fraction(1, 1)]])
# print_mat(inv)