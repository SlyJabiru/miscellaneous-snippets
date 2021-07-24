import numpy as np


# If we consider all possible cases, firstly consider the first min/max operation!
# maximin: ui_ = max_{i} min_{-i} ui(ai, a{-i})  -> first consider  i's action
# minimax: ui^_ = min_{-i} max_{i} ui(ai, a{-i}) -> first consider -i's action


def zero_sum_maximin(arr):
    """
    Find the equilibrium in a discrete zero sum 2 player game using maximin method
    ui_ = max_{i} min_{-i} ui(ai, a{-i})
    Maximize the minimum payoff by other players.

    :param arr: A numpy array with 2 dimension. Only contains numbers in the perspective of the row player
    :param row_or_col:
    :return:
    """

    # In a discrete 2 player zero sum game

    # row player. U_row = max_{row} min_{col} u_row(a_row, a_col)
    # In the perspective of row player, let's put all possible action first
    # Then, for each action, minimum payoff can be calculated
    # Then among them list of min_per_action values, pick maximum!

    #      12  -1  0 |  -1
    #       5   2  3 |   2
    #     -16   0 -1 | -16

    # first, row player consider worst case per each action
    row_worst_case = np.min(arr, axis=1)
    row_max_among_mins = np.max(row_worst_case)
    row_best_strategy = np.argmax(row_worst_case)
    print(f'row_max_among_mins: {row_max_among_mins}')
    print(f'row_best_strategy: {row_best_strategy}')

    # column player's payoff matrix
    #    -12   1  0
    #     -5  -2 -3
    #     16   0  1
    # --------------
    #    -12  -2 -3
    col_worst_case = np.min(-arr, axis=0)
    col_max_among_mins = np.max(col_worst_case)
    col_best_strategy = np.argmax(col_worst_case)
    print(f'col_max_among_mins: {col_max_among_mins}')
    print(f'col_best_strategy: {col_best_strategy}')

    # Let's consider column player while not flipping the sign of original matrix
    #      12  -1  0
    #       5   2  3
    #     -16   0 -1
    # --------------
    #      12   2  3
    # The column player wants his lost should be small

    col_max_lost = np.max(arr, axis=0)
    col_min_among_max_lost = np.min(col_max_lost)
    col_best_strategy = np.argmin(col_max_lost)
    print(f'col_min_among_max_lost: {col_min_among_max_lost}')
    print(f'col_best_strategy: {col_best_strategy}')


def zero_sum_minimax(arr):
    """
    Find the equilibrium in a discrete zero sum 2 player game using maximin method
    ui^_ = min_{-i} max_{i} ui(ai, a{-i})

    :param arr: A numpy array with 2 dimension. Only contains numbers in the perspective of the row player
    :param row_or_col:
    :return:
    """

    # In a discrete 2 player zero sum game

    # row player. U_row = min_{col} max_{row} u_row(a_row, a_col)
    # Let's consider col player's action and consider that cases

    #      12  -1  0
    #       5   2  3
    #     -16   0 -1
    # --------------
    #      12   2  3; If col plays 1 -> row's max will be 12, and then so on.
    row_best_by_col_action = np.max(arr, axis=0)
    row_min_among_maxs = np.min(row_best_by_col_action)
    row_resulted_strategy = np.argmin(row_best_by_col_action)
    print(f'row_min_among_maxs: {row_min_among_maxs}')
    print(f'row_resulted_strategy: {row_resulted_strategy}')

    # col player. Let's put other player's action first.
    #     -12   1  0 |  1
    #      -5  -2 -3 | -2
    #      16   0  1 | 16
    # Column player plans the best action for each action of the other player (the row player)
    # However, the row player disturb this. Because he is adversary to the col player!
    col_best_by_row_action = np.max(-arr, axis=1)
    col_min_among_maxs = np.min(col_best_by_row_action)  # disturbed by other player
    col_resulted_strategy = np.argmin(col_best_by_row_action)
    print(f'col_min_among_maxs: {col_min_among_maxs}')
    print(f'col_resulted_strategy: {col_resulted_strategy}')

    # col player, but do not flip the sign
    #      12  -1  0 |  -1
    #       5   2  3 |   2
    #     -16   0 -1 | -16
    # Column player's best plan is, to minimize the lost for each action of the row player.
    col_best_by_row_action = np.min(arr, axis=1)
    col_max_among_min_losts = np.max(col_best_by_row_action)  # disturbed by other player
    col_resulted_strategy = np.argmax(col_best_by_row_action)
    print(f'col_max_among_min_losts: {col_max_among_min_losts}')
    print(f'col_resulted_strategy: {col_resulted_strategy}')


if __name__ == '__main__':
    arr = np.array(
        [[4, 3, 2, 5],
         [-10, 2, 0, -1],
         [7, 5, 1, 3],
         [0, 8, -4, 5]]
    )

    # arr = np.array([
    #     [12, -1, 0],
    #     [5, 2, 3],
    #     [-16, 0, -1]
    # ])
    zero_sum_maximin(arr)
    print()
    zero_sum_minimax(arr)
