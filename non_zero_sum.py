import numpy as np


def non_zero_sum_minimax(matrix):
    """
    Apply minimax method to non zero sum payoff matrix
    
    :param matrix: 
    :return: 
    """
    # Example
    # Prisoner's Dilemma
    #  (3,3),  (10, 0)
    # (0, 10), (5,  5)

    # Player 1 can expect that player 2 should choose the strategy 0
    # Because the possible minimum payoff is larger for player 2 when she choose the strategy 0

    player2_worst = np.min(arr[1])
    player2_expected_strategy = np.argmax(player2_worst)

    player1_expected_array = arr[0][:, player2_expected_strategy]
    player1_best_payoff = np.max(player1_expected_array)
    player1_best_strategy = np.argmax(player1_expected_array)

    return player1_best_payoff, player1_best_strategy


if __name__ == '__main__':
    arr = np.array(
        [[[3, 10],
         [0, 5]],
        [[3, 0],
         [10, 5]]]
    )

    print(non_zero_sum_minimax(arr))
