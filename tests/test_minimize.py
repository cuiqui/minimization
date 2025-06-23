from minimization.dfa import DFA
from minimization.algorithms import minimize, equivalent


def test_table_filling_figure_4_15():
    # Figure 4.15: Another DFA to minimize
    dfa = DFA(
        states={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'},
        alphabet={'0', '1'},
        transition={
            ('A', '0'): 'B', ('A', '1'): 'E',
            ('B', '0'): 'C', ('B', '1'): 'F',
            ('C', '0'): 'D', ('C', '1'): 'H',
            ('D', '0'): 'E', ('D', '1'): 'H',
            ('E', '0'): 'F', ('E', '1'): 'I',
            ('F', '0'): 'G', ('F', '1'): 'B',
            ('G', '0'): 'H', ('G', '1'): 'B',
            ('H', '0'): 'I', ('H', '1'): 'C',
            ('I', '0'): 'A', ('I', '1'): 'E',
        },
        start_state='A',
        accept_states={'C', 'F', 'I'}
    )

    minimized_dfa = minimize(dfa)

    assert equivalent(dfa, minimized_dfa)
    assert minimized_dfa.start_state == frozenset({'A', 'D', 'G'})
    assert minimized_dfa.states == {
        frozenset({'A', 'D', 'G'}),
        frozenset({'B', 'E', 'H'}),
        frozenset({'C', 'F', 'I'})
    }
    assert minimized_dfa.transition == {
        (frozenset({'F', 'I', 'C'}), '0'): frozenset({'G', 'D', 'A'}),
        (frozenset({'F', 'I', 'C'}), '1'): frozenset({'B', 'H', 'E'}),
        (frozenset({'G', 'D', 'A'}), '0'): frozenset({'B', 'H', 'E'}),
        (frozenset({'G', 'D', 'A'}), '1'): frozenset({'B', 'H', 'E'}),
        (frozenset({'B', 'H', 'E'}), '0'): frozenset({'F', 'I', 'C'}),
        (frozenset({'B', 'H', 'E'}), '1'): frozenset({'F', 'I', 'C'})
    }
    assert minimized_dfa.accept_states == {frozenset({'C', 'F', 'I'})}
