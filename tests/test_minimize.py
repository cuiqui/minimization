from minimization.dfa import DFA
from minimization.algorithms import minimize, equivalent


def test_minimize_figure_4_8():
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
    minimized_dfa = minimize(dfa)

    AE, C, G, BH, DF = (
        frozenset({'A', 'E'}),
        frozenset('C'),
        frozenset('G'),
        frozenset({'B', 'H'}),
        frozenset({'D', 'F'})
    )
    assert equivalent(dfa, minimized_dfa)
    assert minimized_dfa.start_state == AE
    assert minimized_dfa.states == {AE, C, G, BH, DF}
    assert minimized_dfa.transition == {
        (AE, '0'): BH,
        (AE, '1'): DF,
        (C, '0'): AE,
        (C, '1'): C,
        (G, '0'): G,
        (G, '1'): AE,
        (BH, '0'): G,
        (BH, '1'): C,
        (DF, '0'): C,
        (DF, '1'): G
    }
    assert minimized_dfa.accept_states == {C}


def test_minimize_figure_4_15():
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

    ADG, BEH, CFI = (
        frozenset({'A', 'D', 'G'}),
        frozenset({'B', 'E', 'H'}),
        frozenset({'C', 'F', 'I'})
    )
    assert equivalent(dfa, minimized_dfa)
    assert minimized_dfa.start_state == ADG
    assert minimized_dfa.states == {ADG, BEH, CFI}
    assert minimized_dfa.transition == {
        (CFI, '0'): ADG,
        (CFI, '1'): BEH,
        (ADG, '0'): BEH,
        (ADG, '1'): BEH,
        (BEH, '0'): CFI,
        (BEH, '1'): CFI
    }
    assert minimized_dfa.accept_states == {CFI}


def test_minimize_minimal_dfa():
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

    for _ in range(10):
        minimized_dfa = minimize(dfa)
        assert equivalent(minimized_dfa, dfa)
        assert len(minimized_dfa.states) == 3
        assert len(minimized_dfa.transition) == 6
        dfa = minimized_dfa
