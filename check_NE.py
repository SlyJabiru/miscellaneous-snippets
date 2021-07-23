import numpy as np


def zero_sum_check_ne(matrix, p1_strategy, p2_strategy):
    """
    Check if the entry is Nash Equilibrium by definition.
    \forall i,  u_i(s^*_i, s^*_{\neg i}) \geq u_i(s_i, s^*_{\neg i})

    :param matrix: 2 player zero sum matrix. 2 dimension
    :return: True if strategies are NE, False if not
    """

    shape = np.shape(matrix)

    # define return variable
    ret = True

    # check p1.
    p1_payoff_vector = matrix[:, p2_strategy]
    p1_best_strategy = np.argmax(p1_payoff_vector)
    ret = (p1_strategy == p1_best_strategy) & ret

    # check p2.
    p2_payoff_vector = matrix[p1_strategy, :]
    p2_best_strategy = np.argmin(p2_payoff_vector)
    ret = (p2_strategy == p2_best_strategy) & ret

    return ret


if __name__ == '__main__':

    arr = np.array(
        [[12, -1, 0],
         [5, 2, 3],
         [-16, 0, -1]]
    )
    print(zero_sum_check_ne(arr, 1, 1))

    arr = np.array(
        [[4, 3, 2, 5],
         [-10, 2, 0, -1],
         [7, 5, 1, 3],
         [0, 8, -4, 5]]
    )
    print(zero_sum_check_ne(arr, 0, 2))
