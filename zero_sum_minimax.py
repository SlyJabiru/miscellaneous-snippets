import numpy as np


def zero_sum_minimax(arr):
    """
    Find the equilibrium in a discrete zero sum 2 player game using minimax method

    :param arr: A numpy array with 2 dimension. Only contains numbers in the perspective of the player 1
    :return: An index of strategy the player 1 choose, utility / payoff the player 1 gets
    """

    # In a discrete 2 player zero sum game
    # player 1's strategy

    # Player 1 can consider that
    # Player 2 will choose the strategy
    # that makes the least loss in the worst case

    #      12  -1  0
    #       5   2  3
    #     -16   0 -1
    # --------------
    #      12   2  3  will be the worst case in the perspective of player 2,
    #                 if player 2 selects A B C respectively.
    #                 Then player 1 can assume that player 2 will choose the strategy B
    player_2_worst = np.max(arr, axis=0)
    player_2_predicted_strategy = np.argmin(player_2_worst)
    player_2_predicted_payoff_arr = arr[:, player_2_predicted_strategy]

    # Then player 1 maximize its utility / payoff
    player_1_strategy = np.argmax(player_2_predicted_payoff_arr)
    player_1_value = player_2_predicted_payoff_arr[player_1_strategy]

    return player_1_strategy, player_1_value


def zero_sum_maximin(arr):
    """
    Find the equilibrium in a discrete zero sum 2 player game using maximin method

    :param arr: A numpy array with 2 dimension. Only contains numbers in the perspective of the player 1
    :return: An index of strategy the player 2 choose, utility / payoff the player 2 gets
    """

    #      12  -1  0 |  -1
    #       5   2  3 |   2
    #     -16   0 -1 | -16

    #                 will be the worst case in the perspective of player 1,
    #                 if player 1 selects A B C respectively.
    #                 Then player 2 can assume that player 1 will choose the strategy B
    player_1_worst = np.min(arr, axis=1)
    player_1_predicted_strategy = np.argmax(player_1_worst)
    player_1_predicted_payoff_arr = arr[player_1_predicted_strategy]

    # Then player 2 minimize the opponent's utility / payoff
    player_2_strategy = np.argmin(player_1_predicted_payoff_arr)
    player_2_value = player_1_predicted_payoff_arr[player_2_strategy]

    return player_2_strategy, player_2_value


if __name__ == '__main__':
    arr = np.array(
        [[4, 3, 2, 5],
         [-10, 2, 0, -1],
         [7, 5, 1, 3],
         [0, 8, -4, 5]]
    )
    player_1_strategy, player_1_value = zero_sum_minimax(arr)
    player_2_strategy, player_2_value = zero_sum_maximin(arr)

    print(player_1_strategy, player_1_value)
    print(player_2_strategy, player_2_value)
