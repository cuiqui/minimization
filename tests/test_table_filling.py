from collections import Counter

from minimization.dfa import DFA
from minimization.algorithms import table_filling


def test_table_filling_figure_4_8():
    # Figure 4.8: An automaton with equivalent states
    dfa = DFA(
        states={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'},
        alphabet={'0', '1'},
        transition={
            ('A', '0'): 'B', ('A', '1'): 'F',
            ('B', '0'): 'G', ('B', '1'): 'C',
            ('C', '0'): 'A', ('C', '1'): 'C',
            ('D', '0'): 'C', ('D', '1'): 'G',
            ('E', '0'): 'H', ('E', '1'): 'F',
            ('F', '0'): 'C', ('F', '1'): 'G',
            ('G', '0'): 'G', ('G', '1'): 'E',
            ('H', '0'): 'G', ('H', '1'): 'C'
        },
        start_state='A',
        accept_states={'C'}
    )
    equivalent_states = {frozenset(pair) for pair in table_filling(dfa)}

    # Assert with Figure 4.9: Table of state inequivalences
    assert equivalent_states == {
        frozenset({'E', 'A'}),
        frozenset({'B', 'H'}),
        frozenset({'D', 'F'})
    }


def test_table_filling_figure_4_14():
    # Figure 4.14: A DFA to be minimize
    dfa = DFA(
        states={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'},
        alphabet={'0', '1'},
        transition={
            ('A', '0'): 'B', ('A', '1'): 'A',
            ('B', '0'): 'A', ('B', '1'): 'C',
            ('C', '0'): 'D', ('C', '1'): 'B',
            ('D', '0'): 'D', ('D', '1'): 'A',
            ('E', '0'): 'D', ('E', '1'): 'F',
            ('F', '0'): 'G', ('F', '1'): 'E',
            ('G', '0'): 'F', ('G', '1'): 'G',
            ('H', '0'): 'G', ('H', '1'): 'D',
        },
        start_state='A',
        accept_states={'D'}
    )
    equivalent_states = {frozenset(pair) for pair in table_filling(dfa)}

    assert equivalent_states == {
        frozenset({'B', 'F'}),
        frozenset({'G', 'A'}),
        frozenset({'C', 'E'})
    }


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
    equivalent_states = {frozenset(pair) for pair in table_filling(dfa)}

    assert equivalent_states == {
        frozenset(('B', 'E')),
        frozenset(('B', 'H')),
        frozenset(('I', 'C')),
        frozenset(('I', 'F')),
        frozenset(('G', 'A')),
        frozenset(('G', 'D')),
        frozenset(('C', 'F')),
        frozenset(('H', 'E')),
        frozenset(('A', 'D'))
    }
