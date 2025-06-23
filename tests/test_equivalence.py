from minimization.dfa import DFA
from minimization.algorithms import equivalent


def test_dfas_are_equivalent():
    # Testing equivalence of example from page 158.
    # Figure 4.10: Two equivalent DFA's.
    alphabet = {0, 1}
    dfa_1 = DFA(
        states={'A', 'B'},
        alphabet=alphabet,
        transition={
            ('A', 0): 'A',
            ('A', 1): 'B',
            ('B', 0): 'A',
            ('B', 1): 'B'
        },
        start_state='A',
        accept_states={'A'}
    )
    dfa_2 = DFA(
        states={'C', 'D', 'E'},
        alphabet=alphabet,
        transition={
            ('C', 0): 'D',
            ('C', 1): 'E',
            ('D', 0): 'D',
            ('D', 1): 'E',
            ('E', 0): 'C',
            ('E', 1): 'E'
        },
        start_state='C',
        accept_states={'C', 'D'}
    )

    assert equivalent(dfa_1, dfa_2)
