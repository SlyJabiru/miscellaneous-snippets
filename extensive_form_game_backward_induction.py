import numpy as np


"""
Why Backward Induction?

When we convert an extensive form game (sequential game) to a normal form game,
the game would be represented as a matrix.

However, that matrix could make incredible threats, which pretend to be NEs, but impossible in fact.
Backward induction algorithm finds real and credible Nash Equilibrium in a sequential game.
And we call the credible NE as a Sub-game Perfect Nash Equilibrium, SPNE.

This Backward Induction code for extensive form game (sequential game) could not be general.
However, who cares?
"""


class Node:
    def __init__(self, _player, _children_list, _scores):
        self.player = _player
        self.children_list = _children_list
        self.scores = _scores

    def backward_induction(self, ancient_action):
        if not self.children_list:
            return self.scores

        # The node has children
        child_score_list = []  # This should be a list of lists.

        for action, ch in enumerate(self.children_list):
            child_scores = ch.backward_induction(action)
            child_score_list.append(child_scores)

        player_payoff_list = np.array([l[self.player] for l in child_score_list])

        # In fact, backward induction could make multiple NEs.
        # However, let's be simple here.
        action = np.argmax(player_payoff_list)
        scores = child_score_list[int(action)]
        if self.player == 1:
            print(f'Player {self.player} chose action {action} when player 0 does {ancient_action}')
        else:
            print(f'Player {self.player} chose action {action}')
        # print(f'Score: {scores}\n')
        return scores

    def append(self, node):
        self.children_list.append(node)


if __name__ == '__main__':
    n0 = Node(0, [], [])
    n1 = Node(1, [], [])
    n2 = Node(1, [], [])
    n3 = Node(None, [], [3, 1])
    n4 = Node(None, [], [1, 0])
    n5 = Node(None, [], [0, 0])
    n6 = Node(None, [], [2, 2])

    n1.append(n3)
    n1.append(n4)
    n2.append(n5)
    n2.append(n6)
    n0.append(n1)
    n0.append(n2)

    NE = n0.backward_induction(0)
    print(f'SPNE, Subgame Perfect Nash Equilibrium is {NE}')
    # P1's strategy: 0
    # P2's strategy: 01 (When player0 plays 0, he will play 0. When player0 plays 1, he will play 1)
