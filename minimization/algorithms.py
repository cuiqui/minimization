from itertools import combinations
from collections.abc import Hashable
from collections import deque, defaultdict

from minimization.dfa import DFA
from minimization.dsu import DSU


def table_filling(dfa: DFA) -> list[tuple[Hashable, Hashable]]:
    dependency_graph = defaultdict(list)
    distinguishable = defaultdict(bool)
    to_check = deque()

    # Initialization step
    for p, q in combinations(dfa.states, 2):
        dependent = frozenset({p, q})

        for a in dfa.alphabet:
            r, s = dfa.delta(p, a), dfa.delta(q, a)

            if r is not None and s is not None:
                dependency = frozenset({r, s})
                dependency_graph[dependency].append(dependent)

        if (p in dfa.accept_states) != (q in dfa.accept_states):
            distinguishable[dependent] = True
            to_check.append(dependent)

    # Propagation step
    while to_check:
        dependency = to_check.popleft()
        for dependent in dependency_graph[dependency]:
            if not distinguishable[dependent]:
                distinguishable[dependent] = True
                to_check.append(dependent)

    # Return list of equivalent pairs
    equivalent = []
    for p, q in combinations(dfa.states, 2):
        key = frozenset({p, q})
        if not distinguishable[key]:
            equivalent.append((p, q))

    return equivalent


def equivalent(dfa_1: DFA, dfa_2: DFA) -> bool:
    dfa = dfa_1 | dfa_2
    equivalent_states = table_filling(dfa)

    for p, q in equivalent_states:
        if {p, q} == {dfa_1.start_state, dfa_2.start_state}:
            return True
    return False


def minimize(dfa: DFA) -> DFA:

    equivalent_states = table_filling(dfa)

    dsu = DSU()
    for p, q in equivalent_states:
        dsu.union(p, q)
    
    # Minimized DFA
    transitions = {}
    accept_states = set()
    start_state = None

    partitions = {frozenset(p) for p in dsu.subsets()}
    for partition in partitions:
        for a in dfa.alphabet:
            # We take one representative of each partition
            p = next(iter(partition))
            q = dfa.delta(p, a)
            transitions[partition, a] = frozenset(dsu[q])

        for accept_state in dfa.accept_states:
            if accept_state in partition:
                accept_states.add(partition)
    
        if dfa.start_state in partition:
            start_state = partition

    return DFA(
        states=partitions,
        alphabet=dfa.alphabet,
        transition=transitions,
        start_state=start_state,
        accept_states=accept_states
    )
