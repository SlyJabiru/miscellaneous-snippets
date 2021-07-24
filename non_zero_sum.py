import numpy as np


def non_zero_sum_maximin(matrix):
    """
    Apply maximin method to non zero sum payoff matrix.
    ui_ = max_{i} min_{-i} ui(a{i}, a{-i})

    :param matrix: payoff matrix with shape (2, _, _)
    :return:
    """

    # Example
    # Prisoner's Dilemma
    #  (5, 5),  (0, 10)
    # (10, 0), (3,  3)

    # First, consider player0's payoff
    #   5, 0 | 0
    #  10, 3 | 3
    u0 = matrix[0]
    u0_min_by_1 = np.min(u0, axis=1)  # min_{-0} u0(a{0}, a{-0})
    u0_max_among_mins = np.max(u0_min_by_1)
    u0_best_strategy = np.argmax(u0_min_by_1)
    print(f'u0_max_among_mins: {u0_max_among_mins}')
    print(f'u0_best_strategy: {u0_best_strategy}')

    # Let's consider player1's payoff
    # 5, 10
    # 0,  3
    # -----
    # 0,  3
    u1 = matrix[1]
    u1_min_by_0 = np.min(u1, axis=0)  # min_{-1} u1(a{1}, a{-1})
    u1_max_among_mins = np.max(u1_min_by_0)
    u1_best_strategy = np.argmax(u1_min_by_0)
    print(f'u1_max_among_mins: {u1_max_among_mins}')
    print(f'u1_best_strategy: {u1_best_strategy}')


def non_zero_sum_minimax(matrix):
    """
    Apply minimax method to non zero sum payoff matrix
    ui^_ = min_{-i} max_{i} ui(a{i}, a{-i})
    
    :param matrix: 
    :return: 
    """
    # Example
    # Prisoner's Dilemma
    #  (5, 5),  (0, 10)
    # (10, 0), (3,  3)

    # First, consider player0's payoff
    #   5, 0
    #  10, 3
    # ------
    #  10, 3
    u0 = matrix[0]
    u0_max_by_1 = np.max(u0, axis=0)
    u0_min_among_maxs = np.min(u0_max_by_1)  # 0 was disturbed by other players
    u0_resulted_strategy = np.argmin(u0_max_by_1)
    print(f'u0_min_among_maxs: {u0_min_among_maxs}')
    print(f'u0_resulted_strategy: {u0_resulted_strategy}')

    # First, consider player0's payoff
    #  5, 10 | 10
    #  0,  3 | 3
    u1 = matrix[1]
    u1_max_by_0 = np.max(u1, axis=1)
    u1_min_among_maxs = np.min(u1_max_by_0)
    u1_resulted_strategy = np.argmin(u1_max_by_0)
    print(f'u1_min_among_maxs: {u1_min_among_maxs}')
    print(f'u1_resulted_strategy: {u1_resulted_strategy}')


if __name__ == '__main__':
    arr = np.array([
        [[5, 0],
         [10, 3]],
        [[5, 10],
         [0, 3]]
    ])

    non_zero_sum_maximin(arr)
    non_zero_sum_minimax(arr)
